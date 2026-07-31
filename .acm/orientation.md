# orientation.md — autonomous-agent-skills

_Last updated: 2026-07-31 (run: orient-post-argyris-window)_

_Renamed from `retrospect.md` on 2026-06-23 alongside the Retrospect->Orient skill rename. The prior version of this file (last updated 2026-06-21) still called itself `retrospect.md` and referred to "Retrospect" throughout — stale terminology this run corrects, two days after the rename it postdated only slightly._

## Scope of this read

The arc from entry 152 (`2026-06-21 acm-scope-stop-conditions-propagated`, the last entry covered by the prior orient run) through entry 158 (`2026-07-31 improve-argyris-double-loop-6b-integration`) — 6 new entries across a 40-day span (2026-06-21 to 2026-07-31), including a 29-day gap (2026-07-02 to 2026-07-31) with no activity recorded in this repo's own trail.

Arc-question: What has this repo's own trail shown since the last orient run, and is the loop's attention landing on what the named candidate-next-moves and the destination actually call for — or is it drifting to easier, more visible work?

**Freshness check (run evidence):**
- `python harness/tools/record.py history --write` -> 158 entries.
- `python harness/tools/record.py learning --write` -> 240 markers.
- `python verify.py` -> OK, trail integrity checks pass.
- Gate: PASS (arc-claims allowed).

---

## Current claims

**1. Since the last orient run, this repo's own attention has gone almost entirely to terminology and ACM-conformance surfaces, not to capability gaps — even where capability gaps were explicitly named as the top candidate next move.**
Of the 6 entries in this window, 5 are rename/positioning/consistency work: ACM scope-stop-conditions (152), the trail-skill mandate-gate gap-note (unfixed), ACM §4 parent-scope-traversal propagation (added to improve and orient only), the Retrospect->Orient rename, and two Commander's-Intent/mission->destination sweeps. Only the final entry (158, this session) adds new reasoning capability. Two gaps named as candidate next moves in this exact window — the trail skill's missing ACM Mandate Gate enforcement, and intent/SKILL.md's missing ACM §4 parent-scope traversal — were not picked up by any of the 5 entries that followed them.
**Falsifiable by:** finding a post-152 entry (other than this orient run) that fixes either named gap.

**2. `intent/SKILL.md` is the one primary skill that still lacks the ACM §4 parent-scope-traversal instruction, over five weeks after it was named the top candidate next move.**
Entry `acm-parent-scope-traversal-propagated` (2026-06-22) added the traversal paragraph to `improve/SKILL.md` and `orient/SKILL.md` (then `retrospect/SKILL.md`) and explicitly ranked "check intent/SKILL.md for the same gap" as candidate #1. Direct grep of `intent/SKILL.md` for "ACM §4", "parent-scope", and "traversal" returns zero hits as of this run (2026-07-31). An agent running Intent on a repo nested under a workspace-level destination (such as this one, under `c:\git\pea\.acm-root`) will not read the workspace mandate before interpreting a prompt — the same gap improve and orient already closed.
**Falsifiable by:** finding the traversal paragraph in a future version of `intent/SKILL.md`.

**3. The prior orientation.md (replaced by this run) had drifted from the artifact it describes: it called itself `retrospect.md` and referred to "Retrospect" throughout, two days after the skill was renamed to Orient — and it carried an open item referencing `de-ai/SKILL.md`, a skill that does not exist anywhere in the current live tree (confirmed by file search, 0 results).**
Neither drift was self-correcting; both required this orient run to notice and fix. This is a small but genuine instance of the same failure class the loop has repeatedly found in prose (stale path tokens, stale skill names) — orientation.md itself is not immune to the drift it exists to catch in other files.
**Falsifiable by:** a future orient run finding orientation.md still references "Retrospect" or `de-ai/SKILL.md`.

**4. The trail-skill ACM Mandate Gate gap (2026-06-21) was a unilateral agent deferral, not an operator instruction — a different category of "open" than the suite's other operator-deferred items.**
The gap-note entry explicitly reasons "the operator is always present... risk is low in practice. Fix when the skill suite is next revised" — that is the agent choosing not to act, not the operator declining the work. This should not be conflated with genuinely operator-gated items like whole-suite ACM mandate-gate conformance or CITATION.cff alignment, which are deferred by explicit operator signal. Carrying an agent's own low-priority judgment forward under the same "operator-deferred" label as an actual operator decision risks the loop treating its own avoidance as if it had been authorized.
**Falsifiable by:** finding an operator statement (trail entry or session note) that explicitly deferred the trail-skill mandate-gate fix, rather than the agent's own reasoning.

**5. This session's Argyris double-loop addition (entry 158) is explicitly self-described as untested, and it is structurally the same kind of untested claim as the suite's oldest open question (cross-session learning acted-on).**
Both are "the mechanism exists on paper; it has not been observed to fire in a real run." The learning.md-citation claim has been open since at least the prior orient run (carried forward below); the double-loop step-6b question is now open in the same shape, one entry old.
**Falsifiable by:** a future entry citing a `learning.md` entry by date+slug in step 1 narration, or a future entry where the recurring-finding-class trigger fires and the agent names a governing variable and routes it to Destination.

**Carried forward, unchanged by this arc window (no contrary evidence found):**

- Named-boundary discipline across Destination -> Improve -> Orient (renamed from the prior claim about "Improve -> Retrospect"; substance unchanged — silence claims still require a named quality bar).
- Suite positioned as an ACM implementation, not the definition of the memory model (README/`.zenodo.json`, entry 150) — unchanged.
- `.trail/` -> `.acm/` rename complete across prescriptive surfaces (entry 151) — unchanged; this window's new files (`improve/SKILL.md`, `CHANGELOG.md`) use `.acm/` consistently.
- June-02 ARF restriction-reasoning silence — still held; no post-June-02 entry (including this window) reopens it.
- Suite does not yet implement the ACM mandate gate at the whole-suite level — still true, still operator-deferred at that level (distinct from claim 4 above, which is about the narrower trail-skill instance).

---

## What the next runs should test

1. **`intent/SKILL.md`'s missing ACM §4 parent-scope traversal (claim 2, now over five weeks overdue).** This is the smallest, most concretely-specified open item in the suite right now — the exact paragraph already exists in two other files to copy the pattern from.

2. **Cross-session learning acted-on, and its new sibling: does the step-6b double-loop question ever fire (claim 5, carried and extended).** Run Improve in a fresh session on an external target or on this repo's next recurring-finding-class trigger. Does the agent cite a `learning.md` entry by date+slug, and separately, does a recurring pattern ever produce a named governing-variable escalation to Destination? Neither has behavioral evidence yet.

3. **Mandate gate conformance at the whole-suite level (operator-explicitly-deferred — do not act without direction).** Unchanged from the prior orient run: no hard mandate gate, no session-validity binary check. Do not open this work without explicit operator signal. Keep this separate from claim 4's narrower trail-skill instance, which was an agent deferral and may warrant lower-ceremony action if the operator simply confirms it.

4. **CITATION.cff and `.zenodo.json` alignment (operator-deferred).** `CITATION.cff` is at 3.19.0; `CHANGELOG.md` is now at v4.3.0 after this window — the gap has widened, not narrowed, since the prior orient run.

5. **B1 replication in a fresh session by a non-Claude evaluator family (BENCHMARKS gap).** Unchanged — still Pending for GPT/Gemini families.

6. **mtime-based freshness on a fresh clone (named blind spot, still unresolved).** Unchanged.

7. **Retired this run:** the prior "de-ai/SKILL.md and trail/SKILL.md stopping-signal question" item is dropped — `de-ai/SKILL.md` does not exist in the current tree (claim 3). If a de-ai-equivalent skill is reintroduced later, re-open the stopping-signal question then; do not carry a reference to a nonexistent file forward indefinitely.

---

## Active operational rules

- **Every spec change must be paired with enforcement in the same session.** Still holds.

- **Mark `[!REVERSAL]` when the iteration backs out of a planned step, not only when reversing prior runs.** Still holds.

- **When writing non-ASCII content to disk in PowerShell, use explicit UTF-8 encoding.** `[System.IO.File]::WriteAllText` or pipe through `Out-File -Encoding utf8`. `Set-Content` defaults to Windows-1252 on PS5.

- **Enforcement softenings must be published as explicit policy with a named era boundary.** Do not quietly weaken a spec or verifier constraint.

- **When running Orient, regenerate derived artifacts before forming arc-claims.** Freshness guard enforces this at commit time.

- **ACM §4.2 scope traversal stop conditions: filesystem root, `.acm-root` marker, 4-level ceiling.** Every skill with scope-traversal instructions must use these three conditions. As of this run, `improve/SKILL.md` and `orient/SKILL.md` have the traversal instruction; `intent/SKILL.md` still does not (claim 2) — do not assume all three are in sync without checking.

- **Trail entries are required for SKILL.md changes.** Any change to a SKILL.md that modifies agent-visible instructions must have a corresponding trail entry, even if committed with `--no-verify` and backfilled afterward. This happened twice more in this window (the stormp-illustration entry, the parent-scope-traversal entry) — it is a recurring near-miss, not a one-off.

- **PEA-vocabulary vs. cited-doctrine-name split.** Before any bulk rename of PEA's own coined terminology (e.g. "Commander's Intent", "mission"), check whether the same string also names a real external doctrine cited by the framework (e.g. Auftragstaktik / "Mission Command"). Rename the former, leave the latter as a historically-accurate citation. Established across two consecutive rename passes (2026-07-02).

- **A single bulk find-and-replace over natural-language prose is never exhaustive.** Follow every rename pass with an unfiltered recursive grep for the bare term across the whole tree, then manually triage hits (lowercase generic usage, YAML-escaped strings, and asset-generation prompts are the classes that reliably survive a first pass). Confirmed three times independently in this repo's history (PRINCIPLES.md, CHANGELOG.md, trail/README.md splices; then the Commander's-Intent sweep needing a second recursive-grep pass).

- **PowerShell's `Copy-Item` can introduce a BOM into shell scripts, breaking the shebang line.** Re-install hooks from `harness/tools/hooks/pre-commit` by reading and re-writing content explicitly (or strip the BOM afterward) rather than relying on `Copy-Item` alone.

- **`verify.py`'s trigger-evaluation check has a stricter format than the trail's prose examples suggest.** Trigger lines must be `- *Label:* content` (single-asterisk italics around the label, not plain text or bold). Any entry where at least one trigger is marked `FIRED` must also contain a line starting with `**Across-trail macro-Hansei` (bold) or a `#`-heading of that name — a bare `[!REALIZATION]` without that heading fails the check. This session needed three corrective passes against `verify.py` before it passed; future entries should format trigger lines and the macro-Hansei heading correctly on the first attempt rather than iterating against the verifier.

---

## Loop-effectiveness notes

**Which quality bars has this window tested, and which has it never touched?** Internal text-layer consistency was tested repeatedly and thoroughly — three rename/consistency passes, with the recurring-finding-class trigger explicitly firing twice and converging on a real, now-recorded operational rule (the bulk-replace-is-never-exhaustive rule above). Comparative defensibility under hostile external review, comparator coverage, empirical replication, and operational deployability were **not tested at all** in this 40-day window. No silence or convergence claims were made in this window (every entry's outcome was a change), so there is nothing to check against the named-boundary rule here — but the absence of any convergence attempt is itself notable after a window this long.

**Did the operator-gate follow the agent's own top-ranked candidate next moves?** Weakly, no. Two consecutive entries (the 2026-06-21 gap-note and the 2026-06-22 parent-scope-traversal entry) named "check `intent/SKILL.md` for the same gap" as the top candidate. Neither of the next 5 entries picked it up — attention went to the Retrospect->Orient rename, an illustration placement, and two terminology sweeps, before landing on the Argyris double-loop work (an operator-initiated topic, not a candidate the loop itself had surfaced). This is not necessarily wrong — the operator is entitled to redirect — but it is worth naming plainly: the loop's own candidate-ranking has had weak predictive value for what actually happens next, across this window.

[!REALIZATION] The clearest, cheapest, most overdue piece of work visible in this repo right now is not a new idea — it is finishing something the loop already started and named five weeks ago (`intent/SKILL.md`'s ACM §4 gap). A loop that keeps generating new findings while a small, previously-identified, well-specified gap sits untouched is exhibiting exactly the single-loop-without-follow-through pattern the destination's own Learning section flags as underdeveloped — except here the miss is not "no realization was recorded," it is "a realization was recorded and then not acted on across five subsequent entries." That is worth the next Improve iteration's attention before anything else.