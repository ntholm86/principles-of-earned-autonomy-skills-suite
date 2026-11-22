# Session 2026-05-23 — verify-encoding-guard-required-files

- date: 2026-05-23
- target: autonomous-agent-skills
- operator: user
- agent: GitHub Copilot (Anthropic Claude family)
- skill: improve

fidelity: reconstructed

## Summary

`check_required_markdown_docs` now wraps `path.read_text(encoding="utf-8")` in `try/except UnicodeDecodeError`. A non-UTF-8 REQUIRED file skips H1/link analysis and lets `check_no_mojibake` (check #5) report the clean failure message. Smoke-tested with `[byte]0xFF` injected into `BENCHMARKS.md`: verifier produced one clean `FAIL` line, no crash. The check #5 docstring was expanded to explicitly say it covers `REQUIRED_FILES`.

## Reversal

[!REVERSAL] The initial `multi_replace_string_in_file` call produced a broken block (`text = path.read_text(...)\nexcept UnicodeDecodeError:`) missing the `try:` keyword and losing the `analysis_text =` assignment. Required two follow-up repairs. Root cause: the old-string context in the replacement included the line that should follow the `except` block, not the line that belongs inside the `try` body.

## Realization

[!REALIZATION] The gap was never missing detection — `check_no_mojibake` already detected non-UTF-8 bytes. The gap was detection that fails silently when it matters most. A verifier that crashes on the exact file it should flag is worse than no check at all.
