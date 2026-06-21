# Session 2026-05-23 — harness-boundary-soften-and-benchmark-matrix

- date: 2026-05-23
- target: autonomous-agent-skills
- operator: user
- agent: GitHub Copilot (Anthropic Claude family)
- skill: improve

fidelity: reconstructed

## Summary

Applied five user-greenlit improvements in one Improve iteration:

1. **trail/SKILL.md 1.18.0 → 1.19.0.** Removed the "Harness Boundary Constraint" mandate that required raw JSONL `reasoningText` extraction from VS Code workspaceStorage. Replaced with: reasoning capture is required; verbatim harness extraction is optional/highest-tier when available. Added an explicit Anti-rationalization discipline list (predict before action, mark `[!REVERSAL]`, name a rejected alternative, prefer literal quotes, mark fidelity honestly). Updated the content-minimum template to model agent-authored reasoning with an Outcome-vs-prediction section.
2. **.trail/vision.md canonical path drift fixed.** ".trail/log.md" → ".trail/audit-trail.md" (single-token surgical correction; vision remains append/layered per operator-held rule).
3. **verify.py historical-era policy made explicit.** Added a comment block above `SESSION_FIDELITY_CONTRACT_DATE` naming the "pre-contract era", explaining the forward-only enforcement, and pointing to BENCHMARKS.md for the public framing.
4. **BENCHMARKS.md rewritten around a Results Matrix v0.1.** Added Historical-Era Policy section. Replaced the single Status column with explicit per-evaluator-family columns (Claude, GPT, Gemini) and a four-state legend (Seed / In progress / Replicated / Pending). B1–B3 marked Seed in Claude column with Pending in GPT and Gemini; B4 marked Replicated across all three under the existing convergence chain. No fabricated evaluator outcomes.
5. **QUICKSTART.md added.** New 10-minute first-successful-run checklist (prereqs → install → vision → one improve iteration → confirm evidence → optional hook). Linked from README.md Quickstart section.

## Reversals

[!REVERSAL] First write of BENCHMARKS.md used `Set-Content` (Windows-1252 default on PS5) which corrupted em-dashes and broke verify.py's UTF-8 read. Re-encoded via `System.IO.File.WriteAllText` with `UTF8Encoding(false)` and re-verified green.

[!REVERSAL] First audit-trail append used `session-file: .trail/audit-trail.md` and omitted the four trigger-evaluation lines required by the v3.8.0 reflection contract for in-era entries. Corrected before commit by creating this sessions file and amending the appended entry's metadata + reflection block.

## Realizations

[!REALIZATION] The "harness boundary constraint" was an instance of letting an unimplementable ideal mask a working substrate. Agent-authored reasoning under explicit anti-rationalization discipline is not a downgrade from verbatim JSONL; it is the substrate that always exists, and verbatim is the bonus tier when a harness happens to expose it. Specifying the bonus as the floor blocks adoption on every harness that does not.

[!REALIZATION] Encoding defaults on Windows are a silent trail-integrity risk. Set-Content on PowerShell 5 writes Windows-1252 by default while the verifier reads UTF-8 strictly. Any future protocol that mandates non-ASCII characters (em-dashes, smart quotes) must pin writer encoding or risk a verifier failure that looks like a content bug.

## Outcome vs prediction

All four pre-commit predictions held: verifier green after encoding fix; no historical session files modified; spec replaced JSONL mandate with reasoning + anti-rationalization discipline while preserving the verbatim tier; benchmark matrix shipped with two Pending evaluator-family columns per B1–B3 and zero fabricated cells.
