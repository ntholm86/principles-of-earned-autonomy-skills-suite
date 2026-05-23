#!/usr/bin/env python3
"""verify.py — mechanical integrity check for the trail.

Replaces verify-suite.ps1 from v2. Pure-Python, zero dependencies, runs on
Windows / macOS / Linux.

Checks:
1. .trail/audit-trail.md exists and is non-empty.
2. Every entry heading matches `## YYYY-MM-DD — <slug>`.
3. Entries are in non-decreasing date order.
4. Every entry contains the mandatory metadata fields: target, agent, skill, outcome.
5. No U+FFFD replacement characters (mojibake) or non-UTF-8 bytes anywhere in
    the live tree, including every REQUIRED_FILE
    (excludes archive/ and local virtual environments).
6. Live repo files that current docs depend on exist.
7. Required markdown docs do not contain duplicate H1 headings, and their local
    markdown links resolve.
8. Every `session-file:` reference in audit-trail.md points to an existing file.
9. Entries written under the v3.8.0 reflection contract (from
    `improve-step6b-trigger-observability` onward) record an explicit
    four-trigger evaluation — bare "N/A"/"TODO" rejected — and include a
    macro-Hansei subsection when any trigger fired.
10. `.trail/history.md` and `.trail/learning.md` are not older than
    `.trail/audit-trail.md` (staleness check using file mtime).
11. Live docs do not contain stale trail path tokens (`trail/log.md` or
    `.trail/log.md`); canonical path is `.trail/audit-trail.md`.
12. Entries on or after the session-fidelity contract date use structurally
    correct session artifacts (`.trail/sessions/` summaries,
    `.trail/transcripts/` verbatim exports) with explicit fidelity metadata.
13. Transcript-file references point to existing files.
14. Entries under the reversal honesty contract do not narrate reversal cues
    without a `[!REVERSAL]` marker.

Exit code: 0 if all checks pass, 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOG = ROOT / ".trail" / "audit-trail.md"

REQUIRED_FILES = [
    "README.md",
    "CHANGELOG.md",
    "INSTALLING.md",
    "harness/BENCHMARKS.md",
    "harness/benchmark-b5-target/main.py",
    "improve/SKILL.md",
    "probe/SKILL.md",
    "intent/SKILL.md",
    "trail/SKILL.md",
    "vision/SKILL.md",
    "retrospect/SKILL.md",
    ".trail/audit-trail.md",
]

ENTRY_HEADING = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s+[\u2014-]\s+(.+?)\s*$")
META_FIELD = re.compile(r"^-\s+(target|agent|skill|outcome)\s*:", re.MULTILINE)
SESSION_FILE_META = re.compile(r"^-\s+session-file:\s+(.+?)\s*$", re.MULTILINE)
TRANSCRIPT_FILE_META = re.compile(r"^-\s+transcript-file:\s+(.+?)\s*$", re.MULTILINE)
H1_HEADING = re.compile(r"^#\s+.+$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EXTERNAL_LINK = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)

STALE_TRAIL_PATH_PATTERNS = [
    re.compile(r"\.trail/log\.md"),
    re.compile(r"(?<!\.)trail/log\.md"),
]

STALE_PATH_DOCS = [
    "README.md",
    "INSTALLING.md",
    "POSITION.md",
    "PRINCIPLES.md",
    "intent/SKILL.md",
    "vision/SKILL.md",
    "improve/SKILL.md",
    "trail/SKILL.md",
    "retrospect/SKILL.md",
    "probe/SKILL.md",
]

FIDELITY_TEXT = re.compile(
    r"(?im)^\s*(?:\*\*fidelity:\*\*|fidelity:)\s*(.+?)\s*$"
)
SUMMARY_FIDELITY_VALUES = {"reconstructed", "mixed", "split-writer"}
TRANSCRIPT_FIDELITY_VALUES = {"verbatim", "verbatim-structural"}

# Forward-only enforcement contract: entries dated on or after this date must
# meet the structural fidelity rules (see check_session_fidelity_structure).
# Entries strictly before this date belong to the "pre-contract era" and are
# grandfathered in place — they are kept unmodified as historical evidence,
# not retroactively rewritten. See BENCHMARKS.md for how the era boundary is
# treated when computing replication evidence.
SESSION_FIDELITY_CONTRACT_DATE = "2026-05-23"

REVERSAL_HONESTY_CONTRACT_SLUG = "vision-sourced-inference-reframe"
REVERSAL_CUE = re.compile(
    r"\b(backed out|rolled back|reverted|undo(?:ne)?|undid|attempted[^\n]{0,120}then removed|removed it after|abandon(?:ed|ing)?)\b",
    re.IGNORECASE,
)


def _strip_fenced_code_blocks(text: str) -> str:
    lines: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append(line)
    return "\n".join(lines)


def check_required_files() -> list[str]:
    failures: list[str] = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            failures.append(f"missing required file: {rel}")
    return failures


def check_log_format() -> list[str]:
    failures: list[str] = []
    if not LOG.exists():
        return [".trail/audit-trail.md does not exist"]
    text = LOG.read_text(encoding="utf-8")
    if not text.strip():
        return [".trail/audit-trail.md is empty"]

    entries: list[tuple[str, str, str]] = []
    current_date: str | None = None
    current_slug: str | None = None
    current_body: list[str] = []
    malformed_heading = re.compile(r"^#{1,3}\s*\d{4}-\d{2}-\d{2}")
    for line in text.splitlines():
        m = ENTRY_HEADING.match(line)
        if m:
            if current_date is not None:
                entries.append((current_date, current_slug or "", "\n".join(current_body)))
            current_date, current_slug = m.group(1), m.group(2)
            current_body = []
        elif malformed_heading.match(line):
            failures.append(f"malformed entry heading in .trail/audit-trail.md: {line}")
        elif current_date is not None:
            current_body.append(line)
    if current_date is not None:
        entries.append((current_date, current_slug or "", "\n".join(current_body)))

    if not entries:
        failures.append(".trail/audit-trail.md contains no entries matching '## YYYY-MM-DD — slug'")
        return failures

    prev_date: str | None = None
    for date, slug, body in entries:
        if prev_date is not None and date < prev_date:
            failures.append(f"entries out of chronological order: {date} after {prev_date}")
        prev_date = date

        meta_fields = set(META_FIELD.findall(body))
        for required in ("target", "agent", "skill", "outcome"):
            if required not in meta_fields:
                failures.append(f"entry '{date} {slug}' missing required metadata field: {required}")
    return failures


def check_no_mojibake() -> list[str]:
    failures: list[str] = []
    skip_dirs = {"archive", ".git", ".venv", "venv", "__pycache__"}
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in skip_dirs for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() not in {".md", ".txt", ".py", ".yml", ".yaml", ".cff", ".json"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            failures.append(f"non-UTF-8 file: {path.relative_to(ROOT)}")
            continue
        if "\ufffd" in text:
            failures.append(f"replacement character (mojibake) in {path.relative_to(ROOT)}")
    return failures


def check_required_markdown_docs() -> list[str]:
    failures: list[str] = []
    # PRINCIPLES.md is a verbatim external copy; its relative links point to its home repo
    markdown_files = [rel for rel in REQUIRED_FILES if rel.endswith(".md") and rel not in (".trail/audit-trail.md", "PRINCIPLES.md")]
    for rel in markdown_files:
        path = ROOT / rel
        if not path.exists():
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # Non-UTF-8 encoding; check_no_mojibake() will report this as a
            # clean failure (check #5). Skip H1/link analysis here so a bad
            # encoding produces one actionable error, not a crash.
            continue
        analysis_text = _strip_fenced_code_blocks(text)
        if len(H1_HEADING.findall(analysis_text)) > 1:
            failures.append(f"multiple H1 headings in {rel}")

        for raw_target in MARKDOWN_LINK.findall(analysis_text):
            target = raw_target.strip()
            if not target or target.startswith("#") or EXTERNAL_LINK.match(target):
                continue

            link_path = target.split("#", 1)[0]
            if not link_path:
                continue

            resolved = (path.parent / link_path).resolve()
            if not resolved.exists():
                failures.append(f"broken local markdown link in {rel}: {target}")

    return failures


def _line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def check_stale_path_tokens() -> list[str]:
    """Fail when live docs contain old trail path tokens."""
    failures: list[str] = []
    for rel in STALE_PATH_DOCS:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in STALE_TRAIL_PATH_PATTERNS:
            for match in pattern.finditer(text):
                line = _line_number(text, match.start())
                failures.append(
                    f"stale trail path token in {rel}:{line}: '{match.group(0)}' — use .trail/audit-trail.md"
                )
    return failures


def _extract_fidelity_value(text: str) -> str | None:
    m = FIDELITY_TEXT.search(text)
    if not m:
        return None
    raw = m.group(1).strip().lower()
    # Preserve canonical hyphenated values while tolerating legacy notes like
    # "full — arc-read completed ..." by extracting the first token.
    token = re.split(r"\s+[—-]\s+|\s+", raw, maxsplit=1)[0]
    return token


def check_session_fidelity_structure() -> list[str]:
    failures: list[str] = []
    if not LOG.exists():
        return failures

    entries = _parse_entries(LOG.read_text(encoding="utf-8"))
    for date, slug, body in entries:
        if date < SESSION_FIDELITY_CONTRACT_DATE:
            continue

        for m in SESSION_FILE_META.finditer(body):
            rel_path = m.group(1).strip()
            path = ROOT / rel_path
            if not path.exists():
                # Existence is validated separately by check_session_files.
                continue
            rel_parts = Path(rel_path).parts
            if len(rel_parts) < 2 or rel_parts[0] != ".trail":
                failures.append(
                    f"entry '{date} {slug}' uses non-trail session-file path: {rel_path}"
                )
                continue

            text = path.read_text(encoding="utf-8")
            fidelity = _extract_fidelity_value(text)
            if fidelity is None:
                failures.append(
                    f"entry '{date} {slug}' session summary missing fidelity metadata: {rel_path}"
                )
                continue

            if rel_parts[1] == "sessions":
                if fidelity in TRANSCRIPT_FIDELITY_VALUES:
                    failures.append(
                        f"entry '{date} {slug}' summary file uses verbatim fidelity ({fidelity}): {rel_path}"
                    )
                elif fidelity not in SUMMARY_FIDELITY_VALUES:
                    failures.append(
                        f"entry '{date} {slug}' has invalid summary fidelity value ({fidelity}): {rel_path}"
                    )
            elif rel_parts[1] == "transcripts":
                if fidelity not in TRANSCRIPT_FIDELITY_VALUES:
                    failures.append(
                        f"entry '{date} {slug}' transcript file has invalid fidelity ({fidelity}): {rel_path}"
                    )
            else:
                failures.append(
                    f"entry '{date} {slug}' session-file must live in .trail/sessions/ or .trail/transcripts/: {rel_path}"
                )

        for m in TRANSCRIPT_FILE_META.finditer(body):
            rel_path = m.group(1).strip()
            path = ROOT / rel_path
            if not path.exists():
                # Existence is validated separately by check_transcript_references.
                continue
            rel_parts = Path(rel_path).parts
            if len(rel_parts) < 2 or rel_parts[0] != ".trail" or rel_parts[1] != "transcripts":
                failures.append(
                    f"entry '{date} {slug}' transcript-file must live in .trail/transcripts/: {rel_path}"
                )
                continue
            text = path.read_text(encoding="utf-8")
            fidelity = _extract_fidelity_value(text)
            if fidelity is None:
                failures.append(
                    f"entry '{date} {slug}' transcript missing fidelity metadata: {rel_path}"
                )
            elif fidelity not in TRANSCRIPT_FIDELITY_VALUES:
                failures.append(
                    f"entry '{date} {slug}' transcript has invalid fidelity ({fidelity}): {rel_path}"
                )

    return failures


def check_transcript_references() -> list[str]:
    """Check that every transcript-file reference in audit-trail.md points to an existing file."""
    failures: list[str] = []
    if not LOG.exists():
        return failures
    for date, slug, body in _parse_entries(LOG.read_text(encoding="utf-8")):
        for m in TRANSCRIPT_FILE_META.finditer(body):
            rel_path = m.group(1).strip()
            if not (ROOT / rel_path).exists():
                failures.append(
                    f"entry '{date} {slug}' references missing transcript file: {rel_path}"
                )
    return failures


# Slug at and after which the v3.8.0 reflection contract applies.
# Entries strictly before this slug (in file order) are grandfathered.
TRIGGER_CONTRACT_SLUG = "improve-step6b-trigger-observability"

TRIGGER_KEYWORDS = ("recurring", "silence", "contradict", "operator")
MACRO_HANSEI_HEADING = re.compile(
    r"^\*\*Across-trail macro-Hansei", re.MULTILINE
)
TRIGGER_LINE = re.compile(
    r"^-\s+\*([^*]*?)\*\s*(.*)$",
    re.MULTILINE,
)
BARE_PLACEHOLDER = re.compile(r"^\s*(?:n/?a|todo)\s*\.?\s*$", re.IGNORECASE)
FIRED_NOT_NEGATED = re.compile(r"(?<!not\s)\bfired\b", re.IGNORECASE)


def _parse_entries(text: str) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    current_date: str | None = None
    current_slug: str | None = None
    current_body: list[str] = []
    for line in text.splitlines():
        m = ENTRY_HEADING.match(line)
        if m:
            if current_date is not None:
                entries.append((current_date, current_slug or "", "\n".join(current_body)))
            current_date, current_slug = m.group(1), m.group(2)
            current_body = []
        elif current_date is not None:
            current_body.append(line)
    if current_date is not None:
        entries.append((current_date, current_slug or "", "\n".join(current_body)))
    return entries


def check_trigger_evaluation() -> list[str]:
    """Enforce the v3.8.0 reflection contract for entries from the contract slug onward."""
    failures: list[str] = []
    if not LOG.exists():
        return failures
    entries = _parse_entries(LOG.read_text(encoding="utf-8"))

    contract_index: int | None = None
    for i, (_, slug, _) in enumerate(entries):
        if slug == TRIGGER_CONTRACT_SLUG:
            contract_index = i
            break
    if contract_index is None:
        return failures  # contract entry not yet present; nothing to enforce

    for date, slug, body in entries[contract_index:]:
        matches = TRIGGER_LINE.findall(body)
        # Map keyword -> content for trigger lines (label may include trailing ':').
        trigger_content: dict[str, str] = {}
        for label, content in matches:
            label_lc = label.lower()
            for kw in TRIGGER_KEYWORDS:
                if kw in label_lc:
                    trigger_content.setdefault(kw, content)
                    break
        for required in TRIGGER_KEYWORDS:
            if required not in trigger_content:
                failures.append(
                    f"entry '{date} {slug}' missing trigger evaluation line for: {required}"
                )

        any_fired = False
        for kw, content in trigger_content.items():
            placeholder_text = content.strip().strip("*").strip()
            if BARE_PLACEHOLDER.match(placeholder_text):
                failures.append(
                    f"entry '{date} {slug}' trigger '{kw}' uses bare placeholder"
                )
                continue
            if FIRED_NOT_NEGATED.search(content):
                any_fired = True

        if any_fired and not MACRO_HANSEI_HEADING.search(body):
            failures.append(
                f"entry '{date} {slug}' has a fired trigger but no 'Across-trail macro-Hansei' subsection"
            )

    return failures


def check_derived_artifact_freshness() -> list[str]:
    """Fail when history.md or learning.md is older than audit-trail.md.

    Uses file mtime. After a git checkout both files have the same checkout
    timestamp and the check correctly passes. The check catches the primary
    failure mode: agent appended to audit-trail.md but forgot to regenerate the
    derived artifacts before committing.
    """
    failures: list[str] = []
    if not LOG.exists():
        return failures
    log_mtime = LOG.stat().st_mtime
    for artifact_name in ("history.md", "learning.md"):
        artifact = ROOT / ".trail" / artifact_name
        subcommand = artifact_name.replace(".md", "")
        if not artifact.exists():
            failures.append(
                f"missing derived artifact .trail/{artifact_name} — "
                f"run: python tools/record.py {subcommand} --write"
            )
        elif artifact.stat().st_mtime < log_mtime:
            failures.append(
                f"stale derived artifact .trail/{artifact_name} is older than .trail/audit-trail.md — "
                f"run: python tools/record.py {subcommand} --write"
            )
    return failures


def check_reversal_honesty_gate() -> list[str]:
    """Fail when entries under contract narrate reversal cues without [!REVERSAL]."""
    failures: list[str] = []
    if not LOG.exists():
        return failures
    entries = _parse_entries(LOG.read_text(encoding="utf-8"))

    contract_index: int | None = None
    for i, (_, slug, _) in enumerate(entries):
        if slug == REVERSAL_HONESTY_CONTRACT_SLUG:
            contract_index = i
            break
    if contract_index is None:
        return failures

    for date, slug, body in entries[contract_index:]:
        if "[!REVERSAL]" in body:
            continue
        cue = REVERSAL_CUE.search(body)
        if cue:
            failures.append(
                f"entry '{date} {slug}' contains reversal cue '{cue.group(0)}' without [!REVERSAL] marker"
            )
    return failures


def check_session_files() -> list[str]:
    """Check that every session-file: reference in audit-trail.md points to an existing file."""
    failures: list[str] = []
    if not LOG.exists():
        return failures
    for date, slug, body in _parse_entries(LOG.read_text(encoding="utf-8")):
        for m in SESSION_FILE_META.finditer(body):
            rel_path = m.group(1).strip()
            if not (ROOT / rel_path).exists():
                failures.append(
                    f"entry '{date} {slug}' references missing session file: {rel_path}"
                )
    return failures


def main() -> int:
    all_failures: list[str] = []
    all_failures.extend(check_required_files())
    all_failures.extend(check_log_format())
    all_failures.extend(check_no_mojibake())
    all_failures.extend(check_required_markdown_docs())
    all_failures.extend(check_stale_path_tokens())
    all_failures.extend(check_session_files())
    all_failures.extend(check_transcript_references())
    all_failures.extend(check_session_fidelity_structure())
    all_failures.extend(check_trigger_evaluation())
    all_failures.extend(check_reversal_honesty_gate())
    all_failures.extend(check_derived_artifact_freshness())

    if all_failures:
        print(f"FAIL — {len(all_failures)} issue(s):")
        for f in all_failures:
            print(f"  - {f}")
        return 1
    print("OK — trail integrity checks pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
