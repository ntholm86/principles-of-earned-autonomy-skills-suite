# retrospect.md — autonomous-agent-skills

_Last updated: 2026-05-23 (run: retrospect-v3-22-0-arc)_

## Scope of this read

The arc from entry 109 (`improve-offer-next-moves`, 2026-05-11) through entry 123 (`verify-encoding-guard-required-files`, 2026-05-23) — 15 entries since the last Retrospect at entry 108. The prior retrospect covered entries 63–106 and held its claims through entry 108; this run reads forward from there.

Arc-question: What has the loop been doing since the May 11 arc-read? Where is the weight now? Which of the May 11 claims aged well and which did not?

**Freshness check (run evidence):**
- commands: `python tools/record.py history --write`; `python tools/record.py learning --write`; `python verify.py`
- verify result: `OK — trail integrity checks pass` (123 entries, 162 markers)
- gate: PASS (arc-claims allowed)

---

## Current claims

- **The operator-gate formalization is complete and validated.** The May 11 retrospect said the operator-gate pattern was "the strategic engine, but informal." Entry 109 added a Candidate Next Moves subsection to every trail entry; entry 112 (Probe PASS) demonstrated it changes behavior — an agent reading the trail treated the Candidate Next Moves list as suggestions not commands, distinguishing reasoning from compliance. The gate now has a structural trail surface and empirical validation.

- **The May 11 reversal-density claim was formed from a stale artifact and has since been corrected.** The retrospect stated "2:118 across the whole arc." That count was based on a `learning.md` snapshot captured before the same session's parser fix recovered 37 historical markers. Entry 111 corrected the ratio to ~7:119 at the time; the current baseline is 12:162 (7.4%). The freshness guard (entries 107 and 113) is directly responsible for making this visible. Prior claim partially refuted; reversal density is healthier than the retrospect reported.

- **The loop's center of gravity has shifted from trail epistemics to trust-structure credibility.** The May 11 claim was "the target's centre of gravity has visibly shifted from skill mechanics to trail epistemics." That was accurate through entries 63–108. Entries 109–123 show a different pattern: operator-gate completion (109, 112), distribution/adoption infrastructure (116–118), external positioning (118–120), trust-claim credibility tightening (121–123). The last eight entries address how the repo presents its evidence to external evaluators, not how it produces that evidence internally. The internal machinery is largely stable; the publication surface is the active front.

- **Two systematic enforcement over-reaches have been corrected, establishing a pattern.** Forward-only fidelity contract (May 23, pre-session) and harness-boundary mandate (entry 122, same session) were both stated at maximum strength, encoded in spec or verifier, then had to be softened when reality exposed them as unimplementable. Both softenings were published as explicit era-boundary policy (historical-era labeling in verify.py; "verbatim harness extraction is optional" in trail/SKILL.md 1.19.0) rather than quietly weakening enforcement. The pattern is now recognizable and the healthy resolution is documented: acknowledge the ideal, name the era boundary, keep the aspiration visible without blocking adoption.

- **verify.py is now the most mechanically enforced component of the suite.** It runs 14+ checks including: entry format, date order, mandatory metadata, mojibake/encoding, broken links, stale path tokens, session fidelity structure, transcript references, trigger evaluation, reversal honesty, derived-artifact freshness, and the new encoding-guard hardening (entry 123). The trust claims in PRINCIPLES.md and the external benchmark credibility now depend directly on this verifier running reliably. It is load-bearing infrastructure, not a quality gate.

- **The "cross-session learning acted-on" question from the May 11 retrospect remains open.** The May 11 retrospect's top next-test was: "A future fresh-session agent should reach for `learning.md` at step 1 and reference specific prior realizations by date+slug rather than rediscovering them." No entry in 109–123 is such a run. This has not been tested. The infrastructure exists (learning.md is current, improve step 1 instructs reading it); the behavioral evidence does not yet exist.

---

## What the next runs should test

- **Cross-session learning acted-on (still the primary open question):** Run Improve in a fresh session on an external target, confirm the agent cites at least one learning.md entry by date+slug in its step 1 narration rather than rediscovering the same finding class.

- **B1 replication in a fresh session by a non-Claude evaluator family:** The BENCHMARKS.md matrix has three Pending cells for B1/B2/B3 (GPT and Gemini families). Flipping one Pending cell to In Progress requires a single external-family run on the same benchmark ID. This is the lowest-cost move to shift the benchmarks from scaffold to evidence.

- **Enforced-ideal-vs-implementable-reality pattern recurrence:** Two over-reaches corrected in one session (fidelity contract; harness boundary) raises the question: are there other enforcement points where the spec is ahead of what any current harness can produce? Candidate: the `split-writer` fidelity tier in trail/SKILL.md — it specifies an independent second agent, but there is no harness that instantiates this. Either document it as an aspirational tier explicitly (as was done for verbatim transcripts) or test it.

- **mtime-based freshness on a fresh clone (named as a blind spot in May 11 retrospect):** After `git clone`, all files have the same checkout timestamp, so verify.py's mtime-based freshness check passes trivially. A CI-aware workaround or a hash-based check would close this. Remains untested.

---

## Active operational rules

- **Every spec change must be paired with enforcement in the same session.** Still holds. The May 11 arc named "spec written, enforcement deferred" as the recurring failure class; entries 109 and 113 closed that gap for the operator-gate and freshness guard respectively.

- **Mark `[!REVERSAL]` when the iteration backs out of a planned step, not only when reversing prior runs.** Still holds. Calibrated in entry 110. The current arc shows 12 reversals vs 150 realizations — healthier than the May 11 claim but still lower than expected for complex work.

- **When writing non-ASCII content to disk in PowerShell, use explicit UTF-8 encoding.** New rule from entries 122–123. `Set-Content` defaults to Windows-1252 on PS5; use `[System.IO.File]::WriteAllText(path, content, [System.Text.UTF8Encoding]::new($false))` or pipe through `Out-File -Encoding utf8`.

- **Enforcement softenings must be published as explicit policy with a named era boundary.** New rule from entries 122. Do not quietly weaken a spec or verifier constraint. Name the era before which the old rule does not apply, document the reason, and keep the aspiration visible as the highest-trust tier when conditions allow it.

- **When running Retrospect, regenerate derived artifacts before forming arc-claims.** Entry 111's realization: the May 11 retrospect's reversal-density claim was wrong because it was formed from a stale `learning.md`. The freshness guard now enforces this at commit time; Retrospect must also do its own freshness check at read time per the step 1b checklist in retrospect/SKILL.md.