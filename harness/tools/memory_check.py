#!/usr/bin/env python3
"""memory_check.py: check a memory repository against the reference layout and mandate rules.

Usage
  python harness/tools/memory_check.py <memory-root> [--history]

With `--history` (a git memory repository), also fail for each accepted record that a commit modified,
deleted or renamed (R-05: accepted records are create-only). A later record that names the commit in an
`- overrides: <commit>[, <commit>]` line acknowledges it, which is how an administrative override is recorded.
This detects after the fact; it does not prevent a writer who can rewrite the repository.

Failures (exit code 1):
  - the memory root has no `.acm-root` marker;
  - a hidden `.acm/` folder inside the memory (a scope is a folder, not a hidden folder);
  - a retired file name in a scope (`orientation.md`, `history.md`, `learning-archive.md`, `destination.md`: now `learning.md` and `mission.md`);
  - a `mission.md` whose `<!-- current-mission: complete -->` and `<!-- mission-history -->`
    lines are not both present and in that order, or whose current mandate has no (or an empty) `## Human gate`
    section (the Mission skill: a mission that does not state its human gate is incomplete);
  - a `repositories/<id>/repository.json` that is not valid, whose `id` differs from its folder, whose
    `root_commits` are not a non-empty list of 40-hex commits, or that shares a root commit with another
    binding (an ambiguous binding);
  - a file in `records/` whose name is not `<yyyyMMddTHHmmssZ>-<slug>.md`, or whose `- record:` line
    differs from its file name, or whose `- format:` line names a format this tool does not know (a record
    without a `format` line is format 1);
  - a symbolic link anywhere in the memory (a link can leave the memory or hide a scope: R-15).
Warnings (do not fail): an ordinary record without the attribution fields of R-16 (record, time, scope,
agent, authority, session, mandate), a record whose header still holds an unfilled `TODO` stub field, a
`learning.md` that is not labelled a derived view or whose named source record is older than a newer record of
its scope (R-19: a stale view is not used), and a tracked file under a `generated/` folder (disposable reading
aids are not committed).
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

RETIRED = ("orientation.md", "history.md", "learning-archive.md", "destination.md")
STRUCTURAL = {"records", "tasks", "paths", "evidence", "generated"}
SCOPE_FILES = ("mission.md", "learning.md", "audit-trail.md")
KNOWN_FORMATS = {"1"}
RECORD_NAME = re.compile(r"^\d{8}T\d{6}Z-[a-z0-9][a-z0-9-]*\.md$")
FIELD = re.compile(r"^-\s+([a-z-]+):\s*(.*)$", re.M)
ATTRIBUTION = ("record", "time", "scope", "agent", "authority", "session", "mandate")
PLACEHOLDER = re.compile(r"^-\s+(operator|agent|authority|session|outcome|delta):\s*TODO\b", re.M)
OPEN = re.compile(r"^<!-- current-mission: complete -->\s*$", re.M)
CLOSE = re.compile(r"^<!-- mission-history -->\s*$", re.M)


def is_scope(path: Path) -> bool:
    return path.is_dir() and (any((path / name).is_file() for name in SCOPE_FILES) or (path / "records").is_dir())


def scopes(root: Path) -> list[Path]:
    found: list[Path] = []

    def visit(scope: Path) -> None:
        found.append(scope)
        tasks = scope / "tasks"
        if tasks.is_dir():
            for task in sorted(tasks.iterdir()):
                if task.is_dir():
                    visit(task)
        paths = scope / "paths"
        if paths.is_dir():
            walk_paths(paths)

    def walk_paths(folder: Path) -> None:
        for child in sorted(folder.iterdir()):
            if not child.is_dir() or child.name in STRUCTURAL:
                continue
            if is_scope(child) or (child / "tasks").is_dir():
                visit(child)
            walk_paths(child)

    visit(root)
    repositories = root / "repositories"
    if repositories.is_dir():
        for repo in sorted(repositories.iterdir()):
            if repo.is_dir():
                visit(repo)
    return found


def check_mission(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    opened = OPEN.search(text)
    closed = CLOSE.search(text, opened.end()) if opened else None
    if bool(OPEN.search(text)) != bool(CLOSE.search(text)) or (opened and not closed):
        return ["the current-mission and mission-history lines must both be present, in that order"]
    current = text[opened.end():closed.start()] if opened and closed else text
    gate = re.search(r"^## Human gate\s*$(.*?)(?=^## |\Z)", current, re.M | re.S)
    if not gate:
        return ["the current mandate has no '## Human gate' section"]
    if not gate.group(1).strip():
        return ["the '## Human gate' section is empty (a mission states where its human gate is)"]
    return []


def check_bindings(root: Path) -> list[str]:
    problems: list[str] = []
    seen: dict[str, str] = {}
    repositories = root / "repositories"
    if not repositories.is_dir():
        return problems
    for repo in sorted(p for p in repositories.iterdir() if p.is_dir()):
        binding = repo / "repository.json"
        if not binding.is_file():
            continue
        where = binding.relative_to(root).as_posix()
        try:
            data = json.loads(binding.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as exc:
            problems.append(f"{where}: not valid JSON ({exc})")
            continue
        if data.get("id") != repo.name:
            problems.append(f"{where}: id {data.get('id')!r} differs from the folder name {repo.name!r}")
        commits = data.get("root_commits")
        if not isinstance(commits, list) or not commits or not all(isinstance(c, str) and re.fullmatch(r"[0-9a-f]{40}", c) for c in commits):
            problems.append(f"{where}: root_commits must be a non-empty list of 40-hex commits")
            continue
        for commit in commits:
            if commit in seen:
                problems.append(f"{where}: root commit {commit[:12]} is also bound by {seen[commit]} (ambiguous binding)")
            seen[commit] = where
    return problems


def check_records(scope: Path, root: Path) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings: list[str] = []
    records = scope / "records"
    if not records.is_dir():
        return failures, warnings
    for record in sorted(records.glob("*.md")):
        where = record.relative_to(root).as_posix()
        if not RECORD_NAME.match(record.name):
            failures.append(f"{where}: the name is not <yyyyMMddTHHmmssZ>-<slug>.md")
            continue
        text = record.read_text(encoding="utf-8", errors="replace")
        fields = dict(FIELD.findall(text.split("\n###", 1)[0]))
        if "record" in fields and fields["record"].strip() != record.stem:
            failures.append(f"{where}: '- record: {fields['record'].strip()}' differs from the file name")
        if fields.get("format", "1").strip() not in KNOWN_FORMATS:
            failures.append(f"{where}: '- format: {fields['format'].strip()}' is not a record format this tool knows")
        missing = [name for name in ATTRIBUTION if name not in fields]
        if missing:
            warnings.append(f"{where}: no {', '.join(missing)} (R-16 attribution)")
        unfilled = sorted({m.group(1) for m in PLACEHOLDER.finditer(text.split("\n###", 1)[0])})
        if unfilled:
            warnings.append(f"{where}: unfilled stub field(s): {', '.join(unfilled)}")
    return failures, warnings


def acknowledged_overrides(root: Path) -> set[str]:
    found: set[str] = set()
    for record in root.rglob("records/*.md"):
        if ".git" in record.relative_to(root).parts:
            continue
        head = record.read_text(encoding="utf-8", errors="replace").split("\n###", 1)[0]
        for value in re.findall(r"^-\s+overrides:\s*(.*)$", head, re.M):
            found.update(c.lower() for c in re.findall(r"[0-9a-fA-F]{7,40}", value))
    return found


def history_failures(root: Path) -> list[str]:
    if not (root / ".git").exists():
        return []
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "log", "--diff-filter=MDR", "--name-status", "--format=@%H", "--", ":(glob)**/records/*.md"],
            capture_output=True, text=True, check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return []
    acknowledged = acknowledged_overrides(root)
    failures: list[str] = []
    commit = ""
    for line in out.splitlines():
        if line.startswith("@"):
            commit = line[1:]
        elif line.strip() and commit and not any(commit.startswith(a) for a in acknowledged):
            status, *paths = line.split("\t")
            verb = {"M": "modified", "D": "deleted"}.get(status[:1], "renamed")
            failures.append(f"{paths[0]}: an accepted record was {verb} in commit {commit[:7]} (R-05); acknowledge it with an '- overrides: {commit[:7]}' line in a new record")
    return failures


LEARNING_SOURCE = re.compile(r"\b(\d{8}T\d{6}Z-[a-z0-9][a-z0-9-]*)\b")


def check_learning(scope: Path, root: Path) -> list[str]:
    learning = scope / "learning.md"
    if not learning.is_file():
        return []
    where = learning.relative_to(root).as_posix()
    head = "\n".join(learning.read_text(encoding="utf-8", errors="replace").splitlines()[:6])
    warnings: list[str] = []
    if not re.search(r"derived view", head, re.I):
        warnings.append(f"{where}: not labelled a derived view (R-19)")
    named = LEARNING_SOURCE.findall(head)
    records = scope / "records"
    if named and records.is_dir():
        newest = max((r.stem for r in records.glob("*.md") if RECORD_NAME.match(r.name)), default="")
        if newest and newest > max(named):
            warnings.append(f"{where}: derived from {max(named)}, but the scope has a newer record {newest}; the view is stale (R-19)")
    return warnings


def tracked_generated(root: Path) -> list[str]:
    try:
        out = subprocess.run(["git", "-C", str(root), "ls-files"], capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return []
    return [f"{line}: a tracked file under generated/ (disposable reading aids are not committed)"
            for line in out.splitlines() if "/generated/" in "/" + line]


def symlinks(root: Path) -> list[Path]:
    found: list[Path] = []
    for folder, names, files in os.walk(root):
        names[:] = [n for n in names if n != ".git"]
        found += [Path(folder, n) for n in names + files if Path(folder, n).is_symlink() or getattr(os.path, "isjunction", lambda p: False)(Path(folder, n))]
    return sorted(found)


def check(root: Path) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings: list[str] = []
    if not (root / ".acm-root").is_file():
        failures.append("no .acm-root marker at the memory root")
    for hidden in sorted(root.rglob(".acm")):
        if ".git" not in hidden.relative_to(root).parts and hidden.is_dir():
            failures.append(f"{hidden.relative_to(root).as_posix()}: a hidden .acm/ folder inside the memory (a scope is a folder)")
    for link in symlinks(root):
        failures.append(f"{link.relative_to(root).as_posix()}: a symbolic link inside the memory (R-15: a link can leave the memory)")
    for scope in scopes(root):
        where = scope.relative_to(root).as_posix() or "."
        for name in RETIRED:
            if (scope / name).exists():
                failures.append(f"{where}/{name}: retired file name")
        mission = scope / "mission.md"
        if mission.is_file():
            failures += [f"{mission.relative_to(root).as_posix()}: {m}" for m in check_mission(mission)]
        record_failures, record_warnings = check_records(scope, root)
        failures += record_failures
        warnings += record_warnings
        warnings += check_learning(scope, root)
    failures += check_bindings(root)
    warnings += tracked_generated(root)
    return failures, warnings


def main(argv: list[str]) -> int:
    history = "--history" in argv
    argv = [a for a in argv if a != "--history"]
    if len(argv) != 2 or argv[1] in {"-h", "--help"}:
        print(__doc__)
        return 2
    root = Path(argv[1]).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    failures, warnings = check(root)
    if history:
        failures += history_failures(root)
    for message in warnings:
        print(f"WARN  {message}")
    for message in failures:
        print(f"FAIL  {message}")
    count = len(scopes(root)) if root.is_dir() else 0
    print(f"{'FAIL' if failures else 'PASS'}: {count} scope(s) checked, {len(failures)} failure(s), {len(warnings)} warning(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
