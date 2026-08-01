# orientation.md — autonomous-agent-skills

_Last updated: 2026-08-01 (run: orient-post-acm4-closure)_

## Scope of this read

The arc from entry `orient-post-argyris-window` (2026-07-31, the last orient run) through entry `verify-overburden-audit-principles-h1-gap-fix` (2026-08-01) — 4 new entries in under 24 hours: `improve-intent-acm4-traversal-fix`, `improve-destination-acm4-traversal-fix`, `acm4-sweep-complete-plus-consistency-enforcement`, `verify-overburden-audit-principles-h1-gap-fix`.

Arc-question: did the ACM §4 traversal gap-closing arc (the prior orient run's own top-ranked finding) actually get closed, and what did the loop do once it was? Is the loop still avoiding the suite's older backlog, or has that changed?

**Freshness check (run evidence):**
- `python harness/tools/record.py history --write` -> 163 entries.
- `python harness/tools/record.py learning --write` -> 256 markers.
- `python verify.py` -> OK, trail integrity checks pass.
- Gate: PASS (arc-claims allowed).

Step 0 (destination, all scopes): re-read the workspace-level destination at `c:\git\pea\.acm\destination.md` (via the `.acm-root` marker one level up). No changes since the prior orient run; no conflict with this repo's destination notes.

---

## Current claims

**1. The ACM §4 parent-scope-traversal gap-closing arc — first opened 2026-06-22, reopened as the top finding of the prior orient run — is now closed and, more importantly, self-enforcing.**
`intent/SKILL.md` and `destination/SKILL.md` both received the traversal paragraph (2026-07-31). `orient/SKILL.md`'s own copy was found to have already drifted from the other three (stale "operator ceiling" wording, missing the "(implementation ceiling)" label) and was harmonized (2026-08-01). A new `verify.py` check (#15, `check_acm_scope_traversal_consistency`) now fails automatically if any of the four files' stop-condition clause diverges again. This is qualitatively different from the prior three "silence" claims in this repo's history (ARF restriction-reasoning, named-boundary discipline, `.acm` rename) — those held because no one touched the surface again; this one holds because a mechanical check would catch a re-drift even if no one is reading the four files side by side.
**Falsifiable by:** a future edit to any of the four files' stop-condition wording that `verify.py` fails to flag.

**2. The step-6b double-loop question (added 2026-07-31) has now been exercised three times in four days with genuinely different, non-templated outcomes — it is functioning as a real discriminator, not ceremony.**
Run 1 (`improve-intent-acm4-traversal-fix`) concluded no governing-variable escalation was warranted (ordinary operator-gated backlog work). Run 2 (`improve-destination-acm4-traversal-fix`) concluded escalation *was* warranted — the original 2026-06-22 scan's selection criterion was implicit and incomplete — and surfaced it as an operator-facing question rather than resolving it unilaterally. Run 3 (`acm4-sweep-complete-plus-consistency-enforcement`) answered that question in practice (re-derived the criterion, applied it exhaustively, confirmed the concern was correct) and closed it structurally. Run 4 did not fire the trigger at all (distinct finding-class). Three fired, one didn't, and the three that fired produced three different conclusions. That variance is itself the evidence the mechanism is discriminating rather than defaulting to one answer.
**Falsifiable by:** a future run where the question fires but the entry does not show genuine reasoning distinct from the templated shape above (e.g. it always concludes "escalate" or always concludes "no action").

**3. A second instance of the same underlying failure class was found and closed this window: a mechanical check silently stopped covering the exact file its own history says it exists for.**
`PRINCIPLES.md` — the file that suffered a real duplicate-H1 splice defect on 2026-04-23 — had been excluded from `verify.py`'s duplicate-H1 check via dead code (an exclusion clause referencing a list `PRINCIPLES.md` was never part of). Found and fixed 2026-08-01, in the same session as the ACM §4 enforcement work. Two instances of "a recorded historical realization's mechanical protection had silently regressed or never fully applied" in the same two-day window is now a named pattern, not a one-off.
**Falsifiable by:** finding a third instance of a check that exists because of a specific past defect but no longer covers the file that defect happened in.

**4. Across this entire 4-entry window, every candidate-next-move list named the suite's older backlog (CITATION.cff/`.zenodo.json` currency, B1 cross-family replication, mtime-based freshness, whole-suite ACM mandate-gate conformance) as an available redirect, and none of the 4 entries picked any of them up.**
This is not the same pattern the prior orient run flagged (weak follow-through on the loop's *own* candidates) — this window's loop was actually quite disciplined about following its own immediately-prior candidate each time (claim 2 above is evidence of that). What has not moved is the *older*, pre-existing backlog, which is now stale relative to when it was first named (CITATION.cff was already stale at the prior orient run; the gap has only widened as CHANGELOG advanced to v4.7.0).
**Falsifiable by:** a future entry that acts on any of the four named older-backlog items.

**5. `verify.py`'s own file-scoping constants (`STALE_PATH_DOCS`, `ACM_SCOPE_TRAVERSAL_FILES`) have not been systematically audited for the same silent-exclusion pattern just found in `REQUIRED_FILES`' consumer (claim 3).** Named explicitly as an open candidate in the most recent entry; not yet examined.

**Carried forward, unchanged by this arc window (no contrary evidence found):**

- Named-boundary discipline across Destination -> Improve -> Orient — unchanged.
- Suite positioned as an ACM implementation, not the definition of the memory model — unchanged.
- `.trail/` -> `.acm/` rename complete across prescriptive surfaces — unchanged.
- June-02 ARF restriction-reasoning silence — still held.
- Whole-suite ACM mandate gate — still not implemented, still operator-deferred.
- Cross-session learning acted-on (citing `learning.md` by date+slug in a fresh session) — still the oldest untested claim in this repo's history; not exercised this window either.

---

## What the next runs should test

1. **The older backlog, if the operator wants to redirect.** CITATION.cff (3.19.0) vs. CHANGELOG.md (now v4.7.0) — the gap has only widened since it was first flagged. B1 cross-family replication, mtime-based freshness on a fresh clone, and whole-suite ACM mandate-gate conformance are all unchanged and all still available. This is now the single most useful thing to surface plainly: the loop has been effective at closing what it finds, but has not initiated any of these on its own across at least 6 weeks of entries.

2. **Systematic audit of `STALE_PATH_DOCS` and `ACM_SCOPE_TRAVERSAL_FILES` for the silent-exclusion pattern (claim 5).** The cheapest, most concretely-scoped item the loop itself has already named.

3. **Cross-session learning acted-on.** Unchanged, still the oldest open behavioral question in this repo — run Improve in a genuinely fresh session (not a continuation of this conversation) on an external target and see whether it cites `learning.md` by date+slug unprompted.

4. **`verify.py`'s docstring-numbering vs. `main()`'s call-order mismatch.** Cosmetic, low priority, named but not fixed (`verify-overburden-audit-principles-h1-gap-fix`, candidate #1).

5. **Whole-suite ACM mandate-gate conformance (operator-explicitly-deferred — do not act without direction).** Unchanged.

6. **B1 replication in a fresh session by a non-Claude evaluator family; mtime-based freshness on a fresh clone.** Unchanged, both still open.

---

## Active operational rules

- **Every spec change must be paired with enforcement in the same session.** Reinforced twice more this window (ACM §4 wording fix + new verify.py check together; PRINCIPLES.md gap fix + positive/negative sanity test together, run before committing rather than only trusting `verify.py`'s own pass).

- **When a mechanical check exists because of a specific historical defect, periodically re-verify the check's file-scope still actually includes the file the defect happened in.** New this window. Dead-code exclusions (a list comprehension excluding a name that was never in the source list) can silently disable the exact protection a check was built for, without `verify.py` itself ever failing to alert anyone — confirmed twice in one session (the ACM §4 wording drift in `orient/SKILL.md`, and `PRINCIPLES.md`'s H1-check exclusion).

- **The step-6b double-loop question should be answered honestly per instance, including "no."** Three worked examples now exist in this repo's own trail with three different outcomes (no escalation / escalate, surfaced not resolved / escalate, resolved structurally) — do not let repeated firing turn it into a templated "always escalate" or "always dismiss" response.

- **Mark `[!REVERSAL]` when the iteration backs out of a planned step, not only when reversing prior runs.** Still holds; exercised again this window (the destination-fix entry's own within-run correction on the duplication question).

- **When writing non-ASCII content to disk in PowerShell, use explicit UTF-8 encoding.** `Set-Content` defaults to Windows-1252 on PS5; use `Add-Content -Encoding UTF8` or `[System.IO.File]::WriteAllText`.

- **ACM §4.2 scope traversal stop conditions: filesystem root, `.acm-root` marker, 4-level ceiling.** Now mechanically enforced across `improve/SKILL.md`, `orient/SKILL.md`, `intent/SKILL.md`, and `destination/SKILL.md` by `verify.py` check 15 — this is no longer only a manual reminder for whoever edits one of the four files; a mismatch fails the build.

- **`verify.py`'s trigger-evaluation check requires `- *Label:* content` (single-asterisk italics) and a literal `**Across-trail macro-Hansei` line/heading whenever any trigger fires.** Still holds; every entry this window passed on the first or near-first attempt, consistent with this being applied correctly from the start now.

- **Trail entries are required for SKILL.md changes.** Still holds; no gap found this window.

- **PEA-vocabulary vs. cited-doctrine-name split; bulk-replace-is-never-exhaustive; PowerShell `Copy-Item` BOM hazard.** Unchanged, not exercised this window, still valid from the prior orient run.

---

## Loop-effectiveness notes

**Quality bars tested this window:** internal text-layer consistency (again) and, newly, mechanical-enforcement completeness (does a check that exists because of a named historical defect still cover the file that defect happened in). Comparative defensibility, comparator coverage, empirical replication, and operational deployability remain untouched — now unchanged across two consecutive orient windows.

**Candidate-next-move follow-through, updated:** the prior orient run found this weak (top-ranked candidates sat unpicked for 5 entries). This window is the opposite: every one of the 4 entries directly built on the immediately-prior entry's own candidate list. The loop's short-horizon self-referential follow-through is now demonstrably strong. What remains weak is follow-through on the *older*, pre-existing backlog (claim 4) — the loop is good at finishing threads it just started, and has not yet shown it will reach back for threads that predate the current session's focus.

[!REALIZATION] The suite now has a working, repeatedly-exercised example of exactly the capability the destination's own Learning section named as underdeveloped ("what to do differently next time... The skillset does not currently produce this reliably"): the ACM §4 arc shows a realization (2026-06-22) being rediscovered as still-open (2026-07-31 orient), acted on across two entries, cross-checked against its own duplication risk, and finally converted into a mechanical guarantee rather than a hope that a future run reads the trail correctly. That is the shape "learning acted on" was supposed to have. It happened here on a narrow, mechanical topic (file-consistency wording) — the open question (item 3 above) is whether the same discipline transfers to a harder, less mechanical topic like the suite's older, more substantive backlog items.