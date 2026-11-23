#!/usr/bin/env python3
"""record.py — write and read records for the resolved memory scope.

Replaces the kiroku-*.ps1 family from v2. Pure-Python, zero dependencies.

The scope is resolved as record/SKILL.md "Where memory lives" defines: the work
repository (cwd or $RECORD_ROOT) is bound by its git root commits to exactly one
`repositories/<id>/repository.json` in the memory repositories listed in
~/.acm/memories ($ACM_MEMORIES_FILE overrides the registry path). A bound scope
uses create-only records in `records/`. An unbound repository that already has an
in-repo `.acm/` is legacy memory and keeps its single `audit-trail.md`.

Subcommands:
  resolve
      Print the bound scope path, or the unbound/ambiguous/unavailable reason
      on stderr with exit code 2/3/4.

  new --slug=<slug> [--target=<target>] [--skill=<skill>] [--body-file=<path>]
      Bound scope: create the record records/<UTC yyyyMMddTHHmmssZ>-<slug>.md
      (create-only; an identical resubmission is a no-op, a different record
      with the same identifier is an error). With --body-file the tool adds the
      header lines it knows (record, format, time, scope, repository, mandate)
      that the body lacks, and refuses a body whose `- record:` line names another
      identifier. Legacy scope: append a stub to audit-trail.md and
      print its line range.

  summary
      Print the most recent entry. Suitable for a 60-second observer view.

  index [--target=<target>]
      Print a per-iteration timeline: date, slug, outcome, and decisions.
      Shows convergence direction at a glance. Optionally filter by target.
      Print only; nothing is written.

  markers [--write]
      Print (or write to generated/trail-markers.md and, once the recent
      window is full, generated/trail-markers-archive.md) a compact
      chronological extract of every [!REALIZATION] and [!REVERSAL] marker
      from the trail. Generated, disposable, never required reading.

index, markers and summary read a legacy audit-trail.md first, then the
records/ records in filename order.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple


def _resolve_root() -> Path:
    """Resolve the target repo root.

    Order: $RECORD_ROOT env var, else current working directory.
    record.py lives in the skills install (read-only); it always writes
    into the target repo, never into its own folder.
    """
    env = os.environ.get("RECORD_ROOT")
    if env:
        return Path(env).resolve()
    return Path.cwd().resolve()


ROOT = _resolve_root()


def _resolve_log(scope: str | None) -> Path:
    """Locate audit-trail.md for the repo scope or a named task scope (.acm/<scope>/)."""
    acm_dir = ROOT / ".acm"
    if scope:
        acm_dir = acm_dir / scope
    return acm_dir / "audit-trail.md"


LOG = _resolve_log(os.environ.get("ACM_SCOPE"))


class Resolution(NamedTuple):
    status: str  # bound | unbound | ambiguous | unavailable
    reason: str
    scope: Path | None = None
    memory: Path | None = None
    repo_id: str = ""
    root_commit: str = ""


EXIT_CODES = {"bound": 0, "unbound": 2, "ambiguous": 3, "unavailable": 4}


def _registry_path() -> Path:
    env = os.environ.get("ACM_MEMORIES_FILE")
    return Path(env).expanduser() if env else Path.home() / ".acm" / "memories"


def _git(cwd: Path, *arguments: str) -> str | None:
    try:
        result = subprocess.run(["git", "-C", str(cwd), *arguments], capture_output=True, text=True)
    except OSError:
        return None
    return result.stdout if result.returncode == 0 else None


def _memory_revision(memory: Path) -> str:
    """HEAD of the memory repository itself, never of a repository enclosing it."""
    top = (_git(memory, "rev-parse", "--show-toplevel") or "").strip()
    if not top or Path(top).resolve() != memory.resolve():
        return ""
    return (_git(memory, "rev-parse", "HEAD") or "").strip()


def _root_commits(root: Path) -> set[str]:
    out = _git(root, "rev-list", "--max-parents=0", "HEAD") or ""
    return {line.strip().lower() for line in out.splitlines() if line.strip()}


def _remote_urls(root: Path) -> set[str]:
    out = _git(root, "config", "--get-regexp", r"^remote\..*\.url$") or ""
    return {_normal_url(line.split(None, 1)[1]) for line in out.splitlines() if " " in line}


def _normal_url(url: str) -> str:
    return url.strip().lower().rstrip("/").removesuffix(".git")


def resolve_binding(root: Path) -> Resolution:
    """Bind the work repository to one memory scope by root commit, never by name."""
    commits = _root_commits(root)
    if not commits:
        return Resolution("unbound", f"{root} has no git root commit, so it has no repository identity")
    if (_git(root, "rev-parse", "--is-shallow-repository") or "").strip() == "true":
        return Resolution("unavailable", f"{root} is a shallow clone, so its root commit is not the repository's identity; fetch the full history first (git fetch --unshallow)")
    registry = _registry_path()
    if not registry.exists():
        return Resolution("unbound", f"no memory registry at {registry}")
    try:
        entries = registry.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeDecodeError) as exc:
        return Resolution("unavailable", f"memory registry {registry} is unreadable: {exc}")

    seen: set[Path] = set()
    matches: list[Resolution] = []
    for raw in entries:
        entry = raw.strip()
        if not entry or entry.startswith("#"):
            continue
        memory = Path(entry).expanduser()
        if not memory.is_absolute():
            return Resolution("unavailable", f"registry entry is not an absolute path: {entry}")
        if not (memory / ".acm-root").is_file():
            return Resolution("unavailable", f"registered memory repository {memory} is missing or has no .acm-root")
        real = memory.resolve()
        if real in seen:
            continue
        seen.add(real)
        for binding in sorted((memory / "repositories").glob("*/repository.json")):
            try:
                data = json.loads(binding.read_text(encoding="utf-8-sig"))
                bound = data["root_commits"]
                if not isinstance(bound, list):
                    raise TypeError("root_commits is not a list")
            except (OSError, ValueError, KeyError, TypeError) as exc:
                return Resolution("unavailable", f"binding {binding} is unreadable: {exc}")
            shared = sorted(commits.intersection(str(c).strip().lower() for c in bound))
            if not shared:
                continue
            locators = {_normal_url(str(u)) for u in data.get("locators") or []}
            if locators and not locators & _remote_urls(root):
                return Resolution(
                    "ambiguous",
                    f"{root} shares root commit {shared[0][:12]} with {binding}, but none of its remotes matches the binding's locators; "
                    "it may be a fork or a copy (R-13). Add this clone's URL to the locators with the operator's confirmation, or leave it unbound",
                )
            scope = binding.parent
            if not scope.resolve().is_relative_to(real):
                return Resolution("unavailable", f"scope {scope} resolves outside its memory repository {memory}")
            repo_id = str(data.get("id") or binding.parent.name)
            matches.append(Resolution("bound", f"bound by {binding}", scope, memory, repo_id, shared[0]))

    if not matches:
        listed = ", ".join(sorted(commits))
        return Resolution("unbound", f"no repository.json in the memory repositories listed in {registry} has root commit {listed}")
    if len(matches) > 1:
        sources = "; ".join(m.reason.removeprefix("bound by ") for m in matches)
        return Resolution("ambiguous", f"{len(matches)} bindings match this repository: {sources}")
    return matches[0]


class Target(NamedTuple):
    acm: Path  # the active scope directory
    records: bool  # True: create-only records/ records; False: legacy single file
    resolution: Resolution
    task: str | None


_RESERVED = {"records", "tasks", "evidence", "generated"}


def _escape_component(name: str) -> str:
    """A code folder named like a scope entry gets one extra leading underscore, so a path can never be read as a scope entry."""
    return "_" + name if name.lower() in _RESERVED or name.lower().endswith(".md") or name.startswith("_") else name


def _select_target(task: str | None, code_path: str | None = None) -> tuple[Target | None, Resolution]:
    if task and (task in {".", ".."} or re.search(r"[\\/:]", task)):
        return None, Resolution("unavailable", f"invalid task scope name: {task!r}")
    parts = [p for p in re.split(r"[\\/]", code_path or "") if p]
    if code_path and (not parts or any(p in {".", ".."} or ":" in p for p in parts)):
        return None, Resolution("unavailable", f"invalid path scope: {code_path!r}")
    res = resolve_binding(ROOT)
    if res.status == "bound":
        assert res.scope is not None and res.memory is not None
        acm = res.scope.joinpath("paths", *[_escape_component(p) for p in parts]) if parts else res.scope
        acm = acm / "tasks" / task if task else acm
        if not acm.resolve().is_relative_to(res.memory.resolve()):
            return None, Resolution("unavailable", f"scope {acm} resolves outside its memory repository {res.memory}")
        return Target(acm, True, res, task), res
    if res.status == "unbound" and parts and (ROOT / ".acm").is_dir():
        return None, Resolution("unavailable", "path scopes need a shared ACM; legacy in-repo memory has none")
    if res.status == "unbound" and (ROOT / ".acm").is_dir():
        acm = ROOT / ".acm" / task if task else ROOT / ".acm"
        return Target(acm, False, res, task), res
    return None, res


def _report_unresolved(res: Resolution) -> int:
    print(f"{res.status}: {res.reason}", file=sys.stderr)
    if res.status == "unbound":
        print(
            "no memory read or written and no .acm/ created in the work repository; "
            "to bind it, add repositories/<id>/repository.json with its root commit to a registered "
            "memory repository, with the operator's confirmation",
            file=sys.stderr,
        )
    return EXIT_CODES[res.status]


def _note_legacy(target: Target) -> None:
    if not target.records:
        print(
            f"legacy in-repo memory at {target.acm} ({target.resolution.reason}); "
            "recording in its existing single-file format; migration to a memory repository is recommended",
            file=sys.stderr,
        )


TARGET: Target | None = None

ENTRY_HEADING = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s+[\u2014-]\s+(.+?)\s*$")
# Any level-2 heading is an entry boundary, canonical or not. Recognising only
# the canonical form meant a drifted heading matched nothing and its body was
# appended to the PREVIOUS entry -- silently reattributing that entry's markers
# and decisions to a different run. Boundaries must be structural; format
# compliance is checked separately (and loudly) by verify.py.
ANY_HEADING = re.compile(r"^##\s+(.+?)\s*$")
# Tolerant salvage for drifted headings: leading ISO date with any separator,
# or a bare "Entry: <slug>" label.
LOOSE_DATED_HEADING = re.compile(r"^(\d{4}-\d{2}-\d{2})\s*\W+\s*(.+?)\s*$")
ENTRY_LABEL_HEADING = re.compile(r"^Entry:\s*(.+?)\s*$")
# Date carried in the entry body when the heading itself lacks one.
BODY_DATE = re.compile(r"^-\s+(?:\*\*)?[Dd]ate(?:\*\*)?:\s*(\d{4}-\d{2}-\d{2})")
META_FIELD = re.compile(r"^-\s+(target|outcome|delta):\s*(.+)$")
MARKER = re.compile(
    r"(?:^\s*(?:[-*]\s+|\d+\.\s+)?|[.!?][ \t]+)"
    r"(?:\*\*`?)?\[!(DECISION|REVERSAL|REALIZATION)\](?:`?\*\*)?[ \t]+(.+?)\s*$"
)

# generated/trail-markers.md is read at the start of every run (improve/learn/intent step 1).
# Without a bound, it grows by every [!REALIZATION]/[!REVERSAL] marker forever,
# making that mandatory read progressively more expensive with no ceiling.
# Keep only the most recent N markers in the live file; older ones move to
# generated/trail-markers-archive.md, read only when the recent window doesn't cover what's
# needed. Mirrors the CHANGELOG.md / archive/v2 split already used in this repo.
MARKERS_RECENT_COUNT = 60

LEGACY_HEADER = """\

## {date} \u2014 {slug}

- target: {target}
- operator: TODO
- agent: TODO (model family and version, e.g. Claude Fable 5.1; mark operator-stated identity as such - the host product alone is not a family)
- skill: {skill}
- outcome: TODO
- delta: TODO
"""

# A bound-scope record carries the attribution record/SKILL.md requires (ACM R-16); a record without a `format` line is format 1.
RECORD_HEADER = """\
## {date} \u2014 {slug}

- record: {record_id}
- format: 1
- time: {time}
- scope: {scope}
- repository: {repo_id} @ {root_commit}
- target: {target}
- operator: TODO
- agent: TODO (model family and version as the host exposes or the operator states; "unknown" if neither, never invented)
- authority: TODO (the prompt, goal or delegation this work acts under)
- session: TODO (the host's session or run identifier; "unknown" when not exposed)
- mandate: {mandate}
- skill: {skill}
- outcome: TODO
- delta: TODO
"""

STUB_BODY = """\

### Interpretation of the ask

TODO

### Examination

TODO

### Decision

[!DECISION] TODO

### Prediction

TODO — state a falsifiable prediction of what this change will achieve and what will not happen, before taking action.

### Action

TODO — detail what was done, and explicitly compare the actual outcome to the prediction above.

### Reflection

**Falsifiable claim about the target's current state:**

TODO — a specific, disprovable statement about what is true of the target right now.

**Named blind spot:**

TODO — what this examination likely missed, and why.

**Imagined-reader pushback:**

TODO — the strongest objection from someone who knows the target better.

**Across-trail trigger evaluation** *(every entry — one line per trigger, with brief evidence from the trail; bare "N/A" is not allowed)*:

- *Recurring finding-class:* TODO (FIRED / not fired — evidence from last N entries)
- *About to declare silence:* TODO
- *Contradicts prior [!REALIZATION]:* TODO
- *Operator explicitly asked:* TODO

**Across-trail macro-Hansei** *(only if a trigger above fired; otherwise omit this subsection)*:

TODO

### Candidate Next Moves

*(One ranked list of candidate moves visible from this iteration. Operator may pick, redirect, or ignore. Omit if convergence was declared.)*

1. TODO
"""


def _read_text(path: Path) -> str:
    """Read a trail file, gracefully falling back if utf-8 strict decoding fails."""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # Fallback for Windows-1252 / ANSI encoded files containing em-dashes etc.
        return path.read_text(encoding="utf-8", errors="replace")


def _safe_read_log() -> str:
    return _read_text(LOG)


def _record_files() -> list[Path]:
    records_dir = LOG.parent / "records"
    return sorted(records_dir.glob("*.md")) if TARGET is not None and TARGET.records and records_dir.is_dir() else []


def _sources_exist() -> bool:
    return LOG.exists() or bool(_record_files())


def _read_sources() -> str:
    """Legacy audit-trail.md first, then the records/ files in filename (UTC) order."""
    parts = [_safe_read_log()] if LOG.exists() else []
    parts.extend(_read_text(p) for p in _record_files())
    return "\n".join(part if part.endswith("\n") else part + "\n" for part in parts)


def _source_label() -> str:
    if TARGET is None or not TARGET.records:
        return "`.acm/audit-trail.md`"
    count = len(_record_files())
    legacy = "the legacy `audit-trail.md` and " if LOG.exists() else ""
    memory = TARGET.resolution.memory
    revision = _memory_revision(memory) if memory else ""
    return (
        f"{legacy}{count} `records/` record(s) at memory revision {revision or 'unknown'} "
        "(derived view: generate locally on demand or in the Learn step; ordinary writers do not commit it)"
    )


def _missing_sources() -> int:
    print(f"ERROR: no trail in {LOG.parent} ({LOG.name} or records/ records).", file=sys.stderr)
    return 1


def _slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "record"


def _create_record(trail: Path, stamp: str, slug: str, render) -> tuple[Path, bool]:
    """Create-only acceptance: identical resubmission is a no-op; a different record with the same identifier fails."""
    trail.mkdir(parents=True, exist_ok=True)
    record_id = f"{stamp}-{slug}"
    path = trail / f"{record_id}.md"
    content = render(record_id)
    try:
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        return path, True
    except FileExistsError:
        if _read_text(path) == content:
            return path, False
        raise RuntimeError(f"record {record_id} already exists with different content; nothing was written (run again for a new timestamp)")


def _mandate_hash(scope: Path, memory: Path) -> str:
    """sha256 of the narrowest governing goal.md (the scope's, else the next broader one), or 'none'."""
    folder = scope.resolve()
    top = memory.resolve()
    while True:
        goal = folder / "goal.md"
        if goal.is_file():
            return "sha256:" + hashlib.sha256(goal.read_bytes()).hexdigest()[:12]
        if folder == top or top not in folder.parents:
            return "none"
        folder = folder.parent


MACHINE_FIELDS = ("record", "format", "time", "scope", "repository", "mandate")


def _with_machine_fields(body: str, values: dict[str, str]) -> str:
    """Add the header lines the tool knows that a finished body lacks; refuse a body that names another identifier."""
    lines = body.replace("\r\n", "\n").split("\n")
    heading = next((i for i, line in enumerate(lines) if line.startswith("## ")), -1)
    start = heading + 1
    if start < len(lines) and not lines[start].strip():
        start += 1
    end = start
    while end < len(lines) and lines[end].startswith("- "):
        end += 1
    present = {m.group(1): m.group(2).strip() for m in map(re.compile(r"^-\s+([a-z-]+):\s*(.*)$").match, lines[start:end]) if m}
    if "record" in present and present["record"] != values["record"]:
        raise RuntimeError(f"the body's '- record: {present['record']}' names another identifier than {values['record']}; omit the line and the tool adds it")
    added = [f"- {name}: {values[name]}" for name in MACHINE_FIELDS if name not in present]
    if not added:
        return "\n".join(lines)
    if end == start:
        added.append("")
    return "\n".join(lines[:start] + added + lines[start:])


def _new_record(args: argparse.Namespace) -> int:
    assert TARGET is not None
    res = TARGET.resolution
    assert res.memory is not None
    now = _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0)
    slug = _slugify(args.slug)
    body = None
    if args.body_file:
        body = sys.stdin.read() if args.body_file == "-" else _read_text(Path(args.body_file))
    mandate = _mandate_hash(TARGET.acm, res.memory)
    scope = TARGET.acm.relative_to(res.memory).as_posix()
    if not (TARGET.acm / "records").resolve().is_relative_to(res.memory.resolve()):
        print(f"ERROR: {TARGET.acm / 'records'} resolves outside its memory repository {res.memory}; nothing was written", file=sys.stderr)
        return 1

    def render(record_id: str) -> str:
        if body is not None:
            return _with_machine_fields(body, {
                "record": record_id, "format": "1", "time": now.isoformat().replace("+00:00", "Z"), "scope": scope,
                "repository": f"{res.repo_id} @ {res.root_commit}", "mandate": mandate,
            })
        return RECORD_HEADER.format(
            date=now.date().isoformat(), slug=slug, record_id=record_id,
            time=now.isoformat().replace("+00:00", "Z"), scope=scope,
            repo_id=res.repo_id, root_commit=res.root_commit, target=args.target or "TODO",
            mandate=mandate, skill=args.skill or "improve",
        ) + STUB_BODY

    try:
        path, created = _create_record(TARGET.acm / "records", now.strftime("%Y%m%dT%H%M%SZ"), slug, render)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    verb = "created record" if created else "identical record already accepted"
    print(f"{verb}: {path}")
    return 0


def cmd_new(args: argparse.Namespace) -> int:
    if TARGET is not None and TARGET.records:
        return _new_record(args)
    if not LOG.exists():
        print(f"ERROR: {LOG} does not exist. Create it first (it should already be in the repo).", file=sys.stderr)
        return 1
    date = _dt.date.today().isoformat()
    stub = LEGACY_HEADER.format(
        date=date,
        slug=args.slug,
        target=args.target or "TODO",
        skill=args.skill or "improve",
    ) + STUB_BODY
    if args.body_file:
        print("ERROR: --body-file applies to create-only records; legacy entries are appended as stubs.", file=sys.stderr)
        return 1
    existing = _safe_read_log()
    if not existing.endswith("\n"):
        existing += "\n"
    new_text = existing + stub
    LOG.write_text(new_text, encoding="utf-8")

    # Compute and print the line range of the new entry.
    start_line = existing.count("\n") + 1
    end_line = new_text.count("\n")
    print(f"appended stub: {LOG.relative_to(ROOT).as_posix()} lines {start_line}-{end_line}")
    print(f"  date: {date}")
    print(f"  slug: {args.slug}")
    return 0


def _new_entry(date: str, slug: str, dated: bool) -> dict:
    return {
        "date": date,
        "slug": slug,
        "target": "",
        "outcome": "",
        "delta": "",
        "decisions": [],
        "reversals": [],
        "realizations": [],
        "dated": dated,
    }


def _heading_to_entry(heading_text: str, prev_date: str) -> dict:
    """Derive an entry from any level-2 heading, canonical or drifted.

    A drifted heading still opens a new entry so its content is never
    reattributed to the preceding run. When the heading carries no date, the
    previous entry's date is used provisionally and corrected if the body
    supplies an explicit one.
    """
    loose = LOOSE_DATED_HEADING.match(heading_text)
    if loose:
        return _new_entry(loose.group(1), loose.group(2), True)
    label = ENTRY_LABEL_HEADING.match(heading_text)
    slug = label.group(1) if label else heading_text
    return _new_entry(prev_date, slug, False)


def _parse_entries(text: str) -> list[dict]:
    """Parse .acm/audit-trail.md into a list of entry dicts."""
    lines = text.splitlines()
    entries: list[dict] = []
    current: dict | None = None
    last_date = ""

    for line in lines:
        heading = ANY_HEADING.match(line)
        if heading:
            if current is not None:
                entries.append(current)
            m = ENTRY_HEADING.match(line)
            if m:
                current = _new_entry(m.group(1), m.group(2), True)
            else:
                current = _heading_to_entry(heading.group(1), last_date)
            last_date = current["date"] or last_date
            continue

        if current is None:
            continue

        if not current["dated"]:
            body_date = BODY_DATE.match(line)
            if body_date:
                current["date"] = body_date.group(1)
                current["dated"] = True
                last_date = body_date.group(1)

        meta = META_FIELD.match(line)
        if meta:
            current[meta.group(1)] = meta.group(2).strip()
            continue

        marker = MARKER.search(line)
        if marker and line[: marker.start()].count('"') % 2 == 0:
            kind = marker.group(1).lower() + "s"
            current[kind].append(marker.group(2).strip())

    if current is not None:
        entries.append(current)
    return entries


def _render_index(entries: list[dict]) -> str:
    """Render entries as a terminal timeline."""
    lines: list[str] = []

    for i, e in enumerate(entries, 1):
        icon = "·" if "silence" in e["outcome"].lower() else "▸"
        lines.append(f"{icon} Run {i:>2}  {e['date']}  {e['slug']}")
        if e["outcome"]:
            lines.append(f"         outcome:  {e['outcome']}")
        if e["delta"] and e["delta"].upper() != "TODO":
            lines.append(f"         delta:    {e['delta']}")
        for d in e["decisions"]:
            truncated = d if len(d) <= 80 else d[:77] + "..."
            lines.append(f"         decided:  {truncated}")
        for r in e["reversals"]:
            truncated = r if len(r) <= 80 else r[:77] + "..."
            lines.append(f"         REVERSAL: {truncated}")
        lines.append("")
    silence_count = sum(1 for e in entries if "silence" in e["outcome"].lower())
    change_count = len(entries) - silence_count
    lines.append(f"  {len(entries)} runs total — {change_count} with changes, {silence_count} silence")
    return "\n".join(lines)


def cmd_index(args: argparse.Namespace) -> int:
    if not _sources_exist():
        return _missing_sources()

    text = _read_sources()
    entries = _parse_entries(text)

    if not entries:
        print("(no entries in .acm/audit-trail.md)")
        return 0

    target_filter: str | None = getattr(args, "target", None)
    if target_filter:
        entries = [e for e in entries if target_filter.lower() in e["target"].lower()]
        if not entries:
            print(f"(no entries matching target '{target_filter}')")
            return 0

    print(_render_index(entries))
    return 0


def _render_markers_page(items: list[tuple[str, str, str, str]], *, archived_count: int, is_archive: bool) -> str:
    """Render one markdown page (recent window or archive) of trail markers."""
    lines: list[str] = []
    banner = f"GENERATED from {_source_label()} by `record.py markers --write`. Do not edit. Safe to delete. Not required reading."
    if is_archive:
        lines.append("# Trail markers (archive)")
        lines.append("")
        lines.append(banner)
        lines.append("")
        lines.append("Markers older than the recent window kept in `trail-markers.md`. Read this only when the recent window doesn't cover what you're looking for — most runs will never need it.")
    else:
        lines.append("# Trail markers")
        lines.append("")
        lines.append(banner)
        lines.append("")
        lines.append("Compact chronological extract of the most recent `[!REALIZATION]` and `[!REVERSAL]` markers: what the loop has concluded across runs. Read this before reading the trail in full; reach for the trail only when an item here needs its surrounding context.")
        if archived_count:
            lines.append("")
            lines.append(f"Showing the most recent {len(items)} markers. {archived_count} older marker(s) are in `trail-markers-archive.md` — check there if the recent window doesn't cover what you're looking for.")
    lines.append("")
    if not items:
        lines.append("_(no markers found)_")
        return "\n".join(lines) + "\n"
    for date, slug, kind, content in items:
        lines.append(f"## {date} — {slug}")
        lines.append("")
        lines.append(f"**[!{kind}]** {content}")
        lines.append("")
    lines.append("---")
    lines.append("")
    realisation_count = sum(1 for it in items if it[2] == "REALIZATION")
    reversal_count = len(items) - realisation_count
    lines.append(f"**{len(items)} markers — {realisation_count} realisations, {reversal_count} reversals**")
    return "\n".join(lines) + "\n"


def _render_markers(entries: list[dict], markdown: bool) -> str:
    """Render the [!REALIZATION] / [!REVERSAL] markers across all entries.

    The compact marker extract — what the loop has concluded across runs.
    Each item carries its date+slug context so the source entry is locatable
    in log.md.
    """
    items: list[tuple[str, str, str, str]] = []  # (date, slug, kind, content)
    for e in entries:
        for r in e["realizations"]:
            items.append((e["date"], e["slug"], "REALIZATION", r))
        for r in e["reversals"]:
            items.append((e["date"], e["slug"], "REVERSAL", r))

    if markdown:
        recent = items[-MARKERS_RECENT_COUNT:] if len(items) > MARKERS_RECENT_COUNT else items
        archived_count = len(items) - len(recent)
        return _render_markers_page(recent, archived_count=archived_count, is_archive=False)

    # Terminal format — full dump, not windowed (ad-hoc viewing, not the committed artifact).
    lines = []
    if not items:
        lines.append("(no [!REALIZATION] or [!REVERSAL] markers found)")
        return "\n".join(lines)
    for date, slug, kind, content in items:
        truncated = content if len(content) <= 100 else content[:97] + "..."
        lines.append(f"{date}  {slug}")
        lines.append(f"  [!{kind}] {truncated}")
        lines.append("")
    realisation_count = sum(1 for it in items if it[2] == "REALIZATION")
    reversal_count = len(items) - realisation_count
    lines.append(f"  {len(items)} markers — {realisation_count} realisations, {reversal_count} reversals")
    return "\n".join(lines)


def cmd_markers(args: argparse.Namespace) -> int:
    if not _sources_exist():
        return _missing_sources()
    text = _read_sources()
    entries = _parse_entries(text)
    write = getattr(args, "write", False)
    if write:
        items: list[tuple[str, str, str, str]] = []
        for e in entries:
            for r in e["realizations"]:
                items.append((e["date"], e["slug"], "REALIZATION", r))
            for r in e["reversals"]:
                items.append((e["date"], e["slug"], "REVERSAL", r))
        recent = items[-MARKERS_RECENT_COUNT:] if len(items) > MARKERS_RECENT_COUNT else items
        archived = items[:-MARKERS_RECENT_COUNT] if len(items) > MARKERS_RECENT_COUNT else []

        generated = LOG.parent / "generated"
        generated.mkdir(parents=True, exist_ok=True)
        markers_out = generated / "trail-markers.md"
        markers_out.write_text(_render_markers_page(recent, archived_count=len(archived), is_archive=False), encoding="utf-8")

        archive_out = generated / "trail-markers-archive.md"
        if archived:
            archive_out.write_text(_render_markers_page(archived, archived_count=0, is_archive=True), encoding="utf-8")
            print(f"wrote {markers_out} ({len(recent)} recent markers) and {archive_out} ({len(archived)} archived markers) from {len(entries)} entries")
        else:
            print(f"wrote {markers_out} ({len(recent)} markers, none archived yet) from {len(entries)} entries")
    else:
        output = _render_markers(entries, markdown=False)
        print(output)
    return 0


def cmd_summary(_args: argparse.Namespace) -> int:
    if not _sources_exist():
        return _missing_sources()
    text = _read_sources()
    lines = text.splitlines()

    # Find the last entry heading. Any level-2 heading counts, so a drifted
    # heading still surfaces the newest entry rather than an older canonical one.
    last_idx: int | None = None
    for i, line in enumerate(lines):
        if ANY_HEADING.match(line):
            last_idx = i
    if last_idx is None:
        print("(no entries in .acm/audit-trail.md)")
        return 0

    # Print from the last heading to EOF, but cap at 80 lines for digest size.
    body = lines[last_idx:]
    if len(body) > 80:
        body = body[:80] + ["", f"... ({len(lines) - last_idx - 80} more lines; see .acm/audit-trail.md)"]
    print("\n".join(body))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="record.py", description="Write and read Record records for the resolved memory scope.")
    p.add_argument("--scope", default=None, help="Named task scope (bound: tasks/<scope>/; legacy: .acm/<scope>/). Overrides $ACM_SCOPE.")
    p.add_argument("--path", default=None, help="Path scope for a sub-project, relative to the repository (bound only: paths/<path>/). Combines with --scope.")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_res = sub.add_parser("resolve", help="Print the bound scope path, or why there is none (exit 2 unbound, 3 ambiguous, 4 unavailable).")
    p_res.set_defaults(func=None)

    p_new = sub.add_parser("new", help="Create a record in records/ (bound scope) or append a stub to audit-trail.md (legacy).")
    p_new.add_argument("--slug", required=True, help="Short slug for the entry (e.g. 'v3-redesign').")
    p_new.add_argument("--target", default=None, help="What is being operated on.")
    p_new.add_argument("--skill", default=None, help="Which skill is running (improve | probe).")
    p_new.add_argument("--body-file", default=None, help="Complete record content to accept create-only ('-' reads stdin); bound scopes only.")
    p_new.set_defaults(func=cmd_new)

    p_sum = sub.add_parser("summary", help="Print the most recent entry as a 60-second digest.")
    p_sum.set_defaults(func=cmd_summary)

    p_hist = sub.add_parser("index", help="Print a per-iteration timeline of all trail entries.")
    p_hist.add_argument("--target", default=None, help="Filter entries by target name (substring match).")
    p_hist.set_defaults(func=cmd_index)

    p_learn = sub.add_parser("markers", help="Extract every [!REALIZATION]/[!REVERSAL] marker — the compact marker extract.")
    p_learn.add_argument("--write", action="store_true", help="Write generated/trail-markers.md (and the archive) instead of printing.")
    p_learn.set_defaults(func=cmd_markers)

    return p


def main(argv: list[str] | None = None) -> int:
    # Ensure UTF-8 output on platforms where the default encoding is not UTF-8
    # (e.g. Windows cp1252 terminals). records contain em-dashes, arrows,
    # and other Unicode characters that cp1252 cannot encode.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args(argv)
    global LOG, TARGET
    TARGET, res = _select_target(args.scope or os.environ.get("ACM_SCOPE"), args.path)
    if args.func is None:
        if res.status != "bound" or TARGET is None:
            if TARGET is not None:
                _note_legacy(TARGET)
                print(f"{res.status}: {res.reason}", file=sys.stderr)
                return EXIT_CODES.get(res.status, 2)
            return _report_unresolved(res)
        print(TARGET.acm)
        return 0
    if TARGET is None:
        return _report_unresolved(res)
    LOG = TARGET.acm / "audit-trail.md"
    _note_legacy(TARGET)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
