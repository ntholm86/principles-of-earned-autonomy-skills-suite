# orientation.md — autonomous-agent-skills

_Last updated: 2026-08-01 (run: orient-how-close-to-destination)_

## Scope of this read

The arc from entry `orient-post-bom-cleanup-and-efficiency-check` (the last orient run) through entry `systematic-verifypy-audit-closes-stale-path-docs-gap` (current tail) — 12 new entries in the same session: `route-batching-tension-to-operator-then-fix-three-skillmd-boms`, `orient-step3b-argyris-double-loop-check`, `resolve-sessions-fingerprint-blind-spot-and-fix-six-boms`, `fix-orientation-and-audit-trail-boms-closes-cleanup-arc`, `fix-lens-count-miscount-three-vs-four`, `fix-real-mojibake-corruption-and-extend-check-no-mojibake`, `trail-condensed-entry-format-for-non-decision-fixes`, `citation-cff-currency-fix-surfaces-git-tag-drift`, `clarify-history-learning-optional-per-acm-spec-conformance`, `destination-note-skillsuite-as-acm-development-site`, `implement-scale-gap-in-acm-spec-repo`, `systematic-verifypy-audit-closes-stale-path-docs-gap`.

Arc-question, driven directly by the operator's own framing this run ("I'm trying to decide how close we are to the destination"): read this window, and the destination.md it should be measured against, honestly enough to answer that question in bounded terms — not "are we done" (destination.md itself says convergence on a skill is not convergence on the question), but which of the destination's named success conditions have real evidence behind them after this window, and which remain exactly as untested as before.

**Freshness check (run evidence):**
- `python harness/tools/record.py history --write` -> 188 entries.
- `python harness/tools/record.py learning --write` -> 60 recent + 274 archived markers.
- `python verify.py` -> OK, trail integrity checks pass.
- Gate: PASS (arc-claims allowed).

---

## Current claims

**1. This window closed the entire systemic BOM cleanup arc and, in the same window, resolved the "one change per run vs. efficiency" tension the prior orient run identified but did not act on.**
All twelve remaining files (three `SKILL.md` files, six session files, `orientation.md`, `audit-trail.md`) were fixed, the last two with deliberately designed safeguards given `audit-trail.md`'s corruption history. The delegated-autonomy entry (operator unavailable, standing instruction to decide) chose a middle path — grouped entries, per-file verification preserved — which is now precedent. This is the first entry in this repo's history where a prior orient run's own named tension was picked up and resolved by a subsequent window, rather than named again.
**Falsifiable by:** a future BOM-class fix reverting to strict one-per-entry without a stated reason, which would suggest the grouping precedent didn't actually stick.

**2. The Argyris double-loop mechanism is now present in both `improve/SKILL.md` (step 6b) and `orient/SKILL.md` (step 3b) — closing a gap the operator asked about directly, and doing so by codifying a pattern the loop had already used informally twice before, not by inventing new behavior.**
Both prior informal uses (`orient-post-argyris-window`, and this window's own claim 5 from the prior orientation.md) are now retroactively explainable as evidence the codification was warranted rather than premature.
**Falsifiable by:** step 3b, once actually exercised in a future orient run, producing a lower-quality or more mechanical governing-variable judgment than the informal uses did.

**3. Destination note item 3 (efficiency) received sustained, direct attention this window — a genuine change from the prior window, where it got one entry then was dropped for four.**
This window: the condensed trail-entry format (directly efficiency-motivated, explicitly reasoned through rather than assumed), and — the more significant instance — the ACM Scale-gap contribution, which is an efficiency *pattern* (bounded trace-tier windowing) generalized and pushed to a different repo's formal specification. Two distinct, substantive efficiency-lens entries in one window, versus one in six last time.
**Falsifiable by:** a future window reverting to zero efficiency-lens entries across several consecutive iterations.

**4. The systematic `verify.py` audit — the item named as the highest-confidence candidate across at least four prior entries — was finally executed as a deliberate, single pass rather than continuing to arrive by accident, and it closed with a smaller yield than the accumulated concern about it implied.**
11 of 12 checks were correctly scoped; one dormant gap (`STALE_PATH_DOCS` missing two files) was found and fixed. The recurring-finding-class trigger that fired four separate times across unrelated subject areas (file lists, encoding, version metadata, git tags) is now closed as a standing concern, with an honest record that the pattern's *recurrence* was more informative than any individual instance.
**Falsifiable by:** a fifth instance of the same "check coverage narrower than stated" pattern surfacing in a part of the repo this audit didn't examine (it covered `verify.py` only, not e.g. `record.py` or the skill files themselves).

**5. This window produced the first evidenced instance of a genuinely new category: a finding that belongs to a different repository's own governing specification, not to this repo's internal consistency — and the full cycle (recognition → draft → operator authorization → implementation → push) completed within a single conversation.**
The destination gained a note naming this repo as the site where ACM's own development is discovered, not only implemented (citing §6.6 of `agent-context-memory`'s SPEC.md, which states the implementation predates and informed the specification). The same conversation immediately produced a concrete instance: the Scale gap in that spec's own comparator table, closed using this repo's `learning.md`/`learning-archive.md` pattern, pushed to the public spec repo as v0.4.0. This is the most direct evidence this repo's trail has yet produced for destination.md's "research success" condition — it is evidence about the memory-model design question, not just about this implementation.
**Falsifiable by:** the pattern failing to recur without an unusually explicit, operator-led conversation walking through each step — which is exactly what happened this time, and is named as an open question below, not yet resolved in the loop's favor.

**Carried forward, unchanged by this arc window (no contrary evidence found):**

- Whether a target-agnostic formulation of "self-targeting should surface reasoning-capability gaps" is coherent — still deliberately not attempted, correctly, per the standing guidance not to rush it.
- The suite's older backlog items not touched this window: B1 cross-family replication, mtime-based freshness on a fresh clone, whole-suite ACM mandate-gate conformance (operator-deferred).
- The duplicate "Section 5" numbering defect found in `agent-context-memory/SPEC.md` — that repo's own decision, not this repo's to make.

---

## Direct answer to this run's arc-question: how close is this repo to its destination?

Destination.md's own words rule out a single number: "convergence on a particular skill is not convergence on the question." The honest, bounded answer splits by named success condition:

- **Research success** ("the experiment produces evidence about what trustworthy delegation actually requires") — **genuinely advancing, with this window's strongest evidence yet.** The cross-repo ACM contribution (claim 5) is qualitatively different from mechanical self-consistency work: it is evidence about the memory-model design question itself, independently checkable by anyone reading `agent-context-memory`'s own SPEC.md and trail. The double-loop mechanism now exists in both loop-facing skills. This condition has real, accumulating, citable evidence behind it.

- **Adoption success** ("developers read the skills and start using them... without help from the author") — **untested this entire session, and the least-examined condition in this repo's whole trail.** Nothing in today's twelve entries (or, on this reading, in the arc before it) produces or gathers evidence of independent, non-operator-assisted adoption. This is not a new gap — it has been named before — but it is worth stating plainly here: it is the harder half of "how close are we," and today's real progress was almost entirely on the research-success side.

- **The "hard problem" (autonomous orientation.md derivation from the trail alone)** — **partially evidenced, with an honest caveat.** Most of today's twelve entries were self-directed from agent-generated candidate lists once given a bare "continue" — genuine autonomous prioritization within a session. But the *deepest* version of the hard problem — the loop independently deciding an arc-level Orient pass was warranted — did not happen until the operator asked "how close are we to the destination" directly. This orient run exists because the operator asked, not because the loop noticed twelve entries had accumulated and decided on its own that a fresh arc-read was due.

- **Learning** (destination.md's own "most underdeveloped" dimension) — **the most improved dimension this session, arc-wide, not just this window.** The precedent-check requirement, the bounded `learning.md` window, and today's systematic-audit entry are all concrete instances of the loop acting on accumulated learning rather than re-discovering it. This is real progress on a dimension destination.md itself flagged as the most important gap.

**Bounded overall claim:** this repo is closer to demonstrating *that* the architecture can produce trustworthy delegation evidence (research success, learning) than it is to demonstrating *that anyone besides the operator trusts it enough to use it* (adoption success). Today's session did not touch the second condition at all. If "how close to the destination" means the whole destination, the honest answer is: further along on the half this loop can generate evidence for on its own, no closer on the half that requires someone else to pick this up.

---

## What the next runs should test

1. **Adoption success has had zero dedicated attention across this entire session** (twelve entries, all internal or cross-repo-with-the-same-operator) — this is the single most under-served destination condition and the most honest answer to "what should happen next" if research-side momentum is judged sufficient for now.
2. **Whether the loop can initiate an Orient-level arc-read on its own**, without an operator directly asking "how are we doing" — today's evidence is that it did not, across twelve accumulated entries. A future test: let a comparable number of entries accumulate and see whether a self-directed run ever proposes running Orient itself.
3. **Exercise the new Orient step 3b in a genuinely live, not-retrospectively-justified run** — this orient run itself did not encounter a recurring pattern requiring the double-loop question, so step 3b remains formally added but still not exercised in anger.
4. **Whether the skillsuite → ACM contribution pattern recurs without this session's unusually explicit, multi-turn operator scaffolding** (pointing out lineage, confirming intent, drafting, authorizing) — untested in the other direction.
5. **The suite's older backlog** — B1 cross-family replication, mtime-based freshness, whole-suite ACM mandate-gate conformance (operator-deferred, do not act without direction).

---

## Active operational rules

- **The BOM cleanup's grouped-entry-with-per-file-verification precedent held through to the end of the arc** — confirmed in practice, not just decided in principle. Available as precedent for any future class of uniform, low-risk, multi-file fixes.
- **The condensed trail-entry format (no genuine judgment call → shortened entry, four-trigger evaluation never dropped) has been exercised once and held up** — including passing `verify.py`'s existing mechanical checks with no changes needed, confirming the format was designed correctly the first time.
- **PowerShell 5.1's `Out-File`/`Add-Content -Encoding utf8`/`UTF8` always writes a BOM on fresh-file creation; `create_file` and explicit `UTF8Encoding(false)` writes do not.** Still holds, now fully applied — no live file in this repo carries a BOM as of this window's close.
- **`history.md`, `learning.md`, and `learning-archive.md` are optional per the ACM spec's own conformance criteria — not a canonical minimum.** New this window. Adopt them once a trail is large enough to justify the token cost, not as a default starting configuration.
- **This repo is expected to recognize when a finding is about the memory model's own properties, not just this implementation, and surface it as a candidate upstream contribution.** New this window (destination note). Exercised once, successfully, in the same window it was named.
- **When the recurring-finding-class trigger fires with no new diagnosis beyond a specific prior entry, a lighter-weight macro-Hansei pointer is legitimate.** Held through the rest of the BOM arc; not yet tested outside that specific sequence.
- **`verify.py`'s trigger-evaluation check requires `- *Label:* content` and a literal `**Across-trail macro-Hansei` heading whenever any trigger fires.** Still the most common formatting trip-up; still caught before commit every time it occurred this window.
- **Destination.md content is exempt from the "Generic first" constraint that governs skill files.** Unchanged.

---

## Loop-effectiveness notes

**Quality bar tested this window: does the loop, across a long accumulation of entries, ever initiate an arc-level check on itself — or does that only happen when the operator asks?** Result: it only happened when the operator asked. Twelve entries accumulated, including several that explicitly discussed process ceremony, recurring patterns, and governing-variable-level tensions — any of which could have been a legitimate trigger for a self-initiated Orient run — and none produced one. This orient run exists because the operator's own question ("how close are we to the destination") is precisely the kind of question Orient is built to answer, and the operator asked it directly rather than the loop surfacing the need for it.

**Operator-gate effectiveness:** exercised in more distinct forms this window than any prior window — ranked-candidate selection, delegated autonomy under an explicit standing instruction, direct operator-initiated diagnostic questions, full delegation of an architectural-format decision, and now a direct arc-level "how are we doing" question answered by an actual Orient run rather than a conversational guess. Five distinct shapes of the same gate, all functioning, none indistinguishable from each other.

[!REALIZATION] The clearest, most falsifiable finding this window's full arc-read produces is the asymmetry between research success and adoption success. Every entry this session — without exception — was either internal self-consistency work or, in the single most exciting case, a contribution to a repo the same operator also controls. Nothing gathered or produced evidence of use by anyone who is not the operator. Destination.md names both conditions as necessary; this session, for all its real velocity, advanced only one of them. That is not a criticism of today's work — the work done was genuine and well-evidenced — it is a bounded, honest answer to the question that was actually asked: how close to the destination, not how much was done today.