# orientation.md — autonomous-agent-skills

_Last updated: 2026-08-01 (run: orient-post-genericity-reversal)_

## Scope of this read

The arc from entry `orient-zero-new-arc` (2026-08-01, the last orient run) through entry `reversal-self-targeting-branch-violates-genericity` (2026-08-01) — 3 new entries in the same session, plus a new destination note added between them.

Arc-question: what happened in the window since the last orient run, given it contains both a well-reasoned architectural correction (trail's sessions/ mandate) and a self-correction cycle (a change proposed, then reverted for violating this suite's own "Generic first" constraint)? What does the reversal actually reveal about the loop's current reasoning capability, versus what the reverted change merely claimed to add?

**Freshness check (run evidence):**
- `python harness/tools/record.py history --write` -> 168 entries.
- `python harness/tools/record.py learning --write` -> 274 markers.
- `python verify.py` -> OK, trail integrity checks pass.
- Gate: PASS (arc-claims allowed).

---

## Current claims

**1. Trail's `.acm/sessions/` mandate removal (`trail/SKILL.md` 1.19.0 -> 2.0.0) is a genuine, well-reasoned architectural correction, not a reversal candidate.**
The operator's two stated reasons were independently verified before acting: `llm-harness-proxy`'s README was read directly (confirmed it's an MITM proxy capturing verbatim JSONL, but only for sessions explicitly routed through it — applies to harness-driven runs like ai-steward, not to this kind of interactive session); and the host-product session-history claim was verified indirectly via this workspace's own `chronicle`/`session_store_sql` tooling already depending on it. The change correctly kept `.acm/audit-trail.md` as the sole mandatory artifact and reframed the Fidelity section around independent capture rather than deleting the fidelity-marking concept outright.
**Falsifiable by:** a future entry finding that some downstream tooling silently depended on fresh `.acm/sessions/` files being written and broke when they stopped appearing.

**2. Destination gained a new note (2026-08-01) naming three gaps — genericity as an explicit self-claim, self-targeting deriving reasoning-capability improvement as a necessary instrument, and token/resource efficiency as a real constraint — and the very first attempt to act on gap 2 failed this suite's own oldest genericity constraint.**
The reverted addition to `improve/SKILL.md`'s Self-targeting section explicitly named "this suite" and a dated destination note inside a skill file that must work generically across any target repo — a direct violation of destination.md's "Generic first" constraint (architectural constraint #1, present since this file's earliest version).
**Falsifiable by:** a future re-reading of the reverted diff finding it was actually target-agnostic after all (it was not — checked directly against the "substitute an arbitrary target name" test).

**3. The genericity violation was not a novel mistake — the exact failure mode was already recorded in `.acm/learning.md`, read at the start of the same session, and the loop did not re-consult it before writing the contradicting edit.**
The `reflect-step-hansei-rewrite` entry (an earlier session) explicitly rejected a self-targeting branch for the same reason and left a named test for catching it ("remain target-agnostic enough that the self-targeting case falls out without special-casing"). This is the single most concrete, falsifiable piece of evidence this repo's own trail has produced yet on the suite's oldest open question: does the loop reliably carry prior learning forward, or does it re-derive (or in this case, repeat) mistakes learning.md already recorded? This window's answer is: not reliably, at least not just from a single read at session start.
**Falsifiable by:** a future session that proposes a change, checks it against a specific learning.md precedent before writing it, and names the precedent explicitly in its own reasoning (not just cites learning.md generically as "read").

**4. The operator-gate caught what the loop's own process did not, and did so immediately — this is the human gate functioning exactly as destination.md describes it ("the irreducible human gate is: what to implement"), except this instance was about catching a bad *implementation* of an agreed destination-level concern, not choosing between candidate next moves.**
The distinction matters: prior operator-gate evidence in this repo's history has mostly been about *which* next move to pick from a ranked list. This is the first clear instance in recent memory of the gate catching an already-implemented, already-committed change as wrong on architectural-constraint grounds, within the same session it was made.
**Falsifiable by:** a future window where the loop's own step 3 (Challenge the first read) or step 6b independently catches a similar constraint violation before the operator has to.

**5. Destination note item 3 (token/resource efficiency) remains entirely unaddressed as its own topic.**
The trail-sessions-mandate removal (claim 1) was efficiency-motivated, but it happened *before* the destination note that later named efficiency as a standing concern — it was operator-directed in the moment, not derived from the newly-written destination text. No entry in this window treats efficiency as its own dedicated examination.
**Falsifiable by:** a future entry that examines token/resource cost as its primary lens, independent of an unrelated operator instruction that happens to also save tokens.

**Carried forward, unchanged by this arc window (no contrary evidence found):**

- ACM §4 traversal arc — still closed and self-enforcing (verify.py check 15).
- `verify.py`'s trigger-line/macro-Hansei formatting rule — still holds; both new entries in this window passed on the first attempt.
- The suite's older backlog (CITATION.cff/`.zenodo.json` currency, B1 cross-family replication, mtime-based freshness, whole-suite ACM mandate gate) — still untouched, still available.

---

## What the next runs should test

1. **Whether a genuinely target-agnostic formulation of "self-targeting should surface reasoning-capability gaps" is even coherent.** Per the reversal entry's own reasoning: the distinction between "the agent's own reasoning" and "the target's structure" may only make sense when the target IS itself an AI's reasoning instructions (this suite, or a similar prompt/skill-authoring repo) — not for an arbitrary external target. Do not attempt a quick rewrite of the reverted paragraph without first settling this question honestly.

2. **Whether learning.md needs a re-trigger point, not just a single step-1 read.** Claim 3 above is the concrete evidence: a single read at session start was insufficient to prevent a same-session contradiction. A candidate (not yet decided, not yet actioned): require a learning.md check specifically before any SKILL.md edit is proposed, not only once per session.

3. **Audit this session's other changes (ACM §4 additions, the trail sessions-mandate removal) against learning.md for the same unconsulted-precedent pattern.** Named as a blind spot in the reversal entry itself; not yet done.

4. **Token/resource efficiency as its own dedicated examination (destination note item 3).** Still untouched as a topic in its own right.

5. **The suite's older backlog** — CITATION.cff/`.zenodo.json` currency (smallest, most mechanical item), B1 cross-family replication, mtime-based freshness on a fresh clone, whole-suite ACM mandate-gate conformance (operator-explicitly-deferred — do not act without direction).

---

## Active operational rules

- **A single read of `learning.md` at the start of a session is not sufficient insurance against contradicting a recorded precedent later in the same session.** New this window, and the most important addition — re-check `learning.md` specifically before proposing any SKILL.md edit, not only at step 1 of a fresh session. Confirmed by direct failure: the loop read learning.md this session, then minutes later wrote an edit that repeated a mistake learning.md had already named.

- **"Generic first" violations can look like reasonable-sounding prose right up until the substitution test is applied.** Before adding any instruction to a skill file, substitute an arbitrary unrelated target name into the sentence (a driving school's operations manual, a different codebase entirely) and confirm it still makes sense. If a reference to "this suite," a dated note, or a specific file only found in this repo survives the substitution, the wording has smuggled in a repo-specific assumption.

- **Every spec change must be paired with enforcement in the same session.** Still holds; unchanged this window (no spec changes requiring new enforcement occurred).

- **When a mechanical check exists because of a specific historical defect, periodically re-verify the check's file-scope still actually includes the file the defect happened in.** Still holds, from the ACM §4/PRINCIPLES.md arc.

- **The step-6b double-loop question should be answered honestly per instance, including "no."** Still holds; not exercised in this specific window (the recurring-finding-class trigger did not fire in either of this window's two entries).

- **Mark `[!REVERSAL]` when the iteration backs out of a planned step, not only when reversing prior runs.** Reinforced directly this window — the reversal entry is itself a same-session, cross-entry reversal, correctly marked.

- **`verify.py`'s trigger-evaluation check requires `- *Label:* content` (single-asterisk italics) and a literal `**Across-trail macro-Hansei` line/heading whenever any trigger fires.** Still holds; both entries in this window passed on the first attempt.

- **Destination.md content is exempt from the "Generic first" constraint that governs skill files.** New clarification this window: destination.md is explicitly this repo's own operator-held content and is expected to be repo-specific (its 2026-08-01 note about this suite is entirely appropriate there). The constraint applies to translating a destination-level concern into a *skill-file instruction* meant to be portable across targets — that translation step is where genericity must be actively re-checked, not assumed to carry over automatically from a legitimate repo-specific observation.

---

## Loop-effectiveness notes

**Quality bar tested this window: does the loop honor its own already-recorded architectural constraints (genericity) when making new additions, without operator intervention?** Result: no, not on the first attempt. The addition was made, committed, and only reverted after the operator caught it. This is a new, more demanding quality bar than this repo's trail has explicitly tested before — prior windows tested text-consistency and mechanical-enforcement-completeness (both passed reliably); this window tested self-consistency against a *named prior lesson already in the loop's own memory layer*, and the loop failed it once.

**Operator-gate effectiveness:** strongly validated this window, in a new way. Prior operator-gate evidence in this repo has mostly been about steering *which* next move to pick. This window shows the gate catching an already-committed *implementation* as architecturally wrong, immediately, in the same session. The gate is not just steering direction — it is also the current backstop for constraint violations the loop's own process did not catch.

[!REALIZATION] The most valuable evidence this window produced was not the reverted paragraph — it was the demonstration that a destination note naming "improve the agent's own reasoning" as an explicit goal does not, by itself, make the agent apply its own recorded learning more carefully. If anything, the excitement of a new framing (reasoning-capability gaps) appears to have distracted from a more mundane, already-known check (re-read learning.md before proposing this specific kind of change). Any future attempt to operationalize the destination's reasoning-capability concern should treat this arc — not the reverted text — as the primary evidence about where the suite's actual reasoning-capability gap currently sits: not in a missing self-check paragraph, but in how reliably a single early read of the memory layer survives contact with a new idea introduced later in the same session.