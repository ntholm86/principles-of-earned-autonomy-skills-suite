# Destination — work-skill

_Operator: Nils Holmager | Initialised: 2026-07-03_

> Repo-level destination. Governs work specific to this repo. The workspace destination (`../.acm/destination.md`, i.e. `pea/.acm/destination.md`) governs cross-repo coordination and wins on any conflict — see ACM §4 Scoped Memory. Read that file first when reasoning about how this repo fits the wider research program; this file governs what happens *inside* work-skill (renamed from `pea-skills-lite`, then `think-it-through-skill`, then `auditonomy-skill` — see "Destination run — 2026-07-04 (rename)", "Destination run — 2026-07-04 (second rename)", and "Destination run — 2026-07-05 (third rename)" below).

---

## The One Question

> What does a **standalone, target-agnostic improvement-reasoning architecture with full auditability** look like — one that can reason about and improve *anything* the model it runs on can reason about, adhering to PEA principles, **and cheap enough to actually use every day without losing quality**?

*(Cost is not a side constraint on this question — it is half of it. The full suite already proved the capability; what killed its daily use was cost. See "Destination run — 2026-07-04 (cost is co-equal)" below.)*

*(Superseded framing, kept for the record: "What does the accountability-architecture skill suite look like once the binding constraint is cost-per-unit-of-reasoning-quality, not reasoning quality alone?" — that was the question during this repo's birth as a fork; see "Destination run — 2026-07-04 (standalone reframing)" below for why it no longer leads.)*

## Why this repo exists

**[Reframed 2026-07-04, operator-confirmed — see "Destination run — 2026-07-04 (standalone reframing)" below.]** `work` is a **standalone skill**: an autonomous improvement-reasoning architecture with full auditability that is *target-agnostic* — it can work on anything the model it runs on can reason about: code, music, letters, books, plans, whatever. Its lineage (below) is a fork of the full suite, but lineage is not identity: the suite comparison was scaffolding during its birth, not its purpose. When this skill is pointed at itself, the thing being improved is **that general capability** — the ability to understand and improve anything — not fidelity to its parent suite.

*Lineage, kept for the record:* The full skills suite (`pea/skills`: intent, improve, destination, orient, trail, probe) was built during what the operator calls the **"token bonanza"** — a period before 2026-07 where token cost was not the binding constraint. In practice, the operator found they mostly invoked two of those six skills — Intent and Improve — for almost everything, and was **"running out of tokens too fast"** using the full multi-skill-invocation discipline. This repo began as a deliberate cost-optimized fork: the same governing principles, delivered as **one consolidated skill** instead of chaining several, so a session pays for one skill-load and one reasoning pass instead of many. That cost discipline remains a real constraint — it just isn't the destination anymore.

**[Confirmed 2026-07-03, second Destination pass]** This is not a side experiment — the operator has confirmed this skill (originally named `pea-lite`, renamed `think-it-through`, then `auditonomy`, then `work` on 2026-07-05) is meant to become their actual daily-usage skill, superseding day-to-day reliance on the full `pea/skills` suite. The full suite remains untouched and available for whatever still warrants its depth (this repo does not delete or deprecate it), but the default reach-for is now `work`.

## Operator's direct mandate

Source: operator's message, 2026-07-03 (quoted in full in this repo's `.acm/audit-trail.md`, first entry). Verbatim requirements:

1. **One skill, not six.** Improve becomes the base loop; it always applies Intent internally — no separate invocation.
2. **Trail always happens.** Every run appends to `.acm/audit-trail.md` in the target repo. No exceptions, no opt-out.
3. **Mini-Destination.** If `.acm/destination.md` doesn't exist yet in the *target* repo being worked on, ask the operator a short question or two and write it. If it exists, just read it.
4. **Mini-Orient.** Every 5th iteration, do a condensed arc-read (not the full freshness-guard / derived-artifact machinery of real Orient) and note what's changing.
5. **The explicit trade-off:** lower token cost per session, *without* silently lowering reasoning quality at the moments quality actually matters (real decisions). If a cost/quality trade-off is unavoidable, it must be visible and justified in the trail entry, never silently absorbed.
6. **[Confirmed 2026-07-04]** Between the two axes this fork trades on, **reasoning quality outranks mechanism completeness.** Operator's words, verbatim: "capability is one of the most important things for pea-lite... mechanisms are less important... Similar Quality with much less cost is the goal." Concretely: whether `think-it-through` (then named `pea-lite`) carries the full suite's harder tooling (freshness guards on derived artifacts, writer-splitting, ARF/Probe, session-transcript capture) matters far less than whether its three core reasoning moments are *as good* as the suite's — not merely structurally present. The operator named those three moments directly: **Intent** ("understand what and why, not how"), **Improve's examination** ("surroundings" — reading the target's actual context before deciding), and **Orient** ("meta" — arc-level reasoning about the work itself). And explicitly general-purpose: this reasoning quality is what makes the skill work on *any* kind of target, not just software.

## Sourced inferences (not literally stated — offered for confirmation, not blocking)

- **[Confirmed 2026-07-03]** Probe (the 6th original skill — contamination / pattern-matching detection) is intentionally *not* part of the lite consolidation. *Source:* the operator's message names Intent, Improve, mini-Orient, mini-Destination, and Trail explicitly, and never mentions Probe. Operator confirmed directly: "I dont think the probe skill is needed in pea-skills-lite." Probe stays a separate, occasionally-invoked skill outside `think-it-through`, not folded in — settled, not just assumed.
- **[Corrected 2026-07-03]** No installer — permanently, by design, not a temporary v1 scope cut. Operator's own words: "I dont want an installer, its should be so easy its just a skill that ppl can use." Ease-of-adoption is itself part of what "lite" means here: a single self-contained `SKILL.md` a person can read, drop into wherever their agent loads skills from, or paste straight into a prompt — no build step, no script to trust, no packaging ceremony between the file and using it. This supersedes the earlier unconfirmed inference, which had incorrectly framed the lack of an installer as "not yet" rather than "not ever."

## Constraints carried over from the workspace destination

- Higher scope wins on coordination matters (ACM §4) — `pea/.acm/destination.md` governs if this repo's direction ever conflicts with cross-repo coordination.
- Append-only memory — corrections happen by appending, never rewriting.
- The three principles — **Operator's Intent, Observable Autonomy, Convergence Is Silence** — are constraints, not preferences, even in the lite version. Cost is optimized *around* them, never at their expense. This is the design tension the `work/SKILL.md` file exists to resolve.

## What "done" looks like for this repo

Not a fixed release. Working-in-use signal: the operator actually reaches for `work` instead of chaining Intent → Improve manually, session token cost visibly drops, and reasoning quality at real decision points is not perceptibly worse — the operator would notice a regression and say so.

**[Confirmed 2026-07-03, second Destination pass]** A second, independent bar now applies alongside the operator's own daily use: **a stranger could pick up `work/SKILL.md` and use it without the operator explaining anything.** This is a real design constraint, not aspirational framing — it means jargon, unexplained references to the original five-skill suite, or assumptions about shared context with the operator are defects, not just stylistic choices.

## Open items (not blocking, revisit when the operator has a moment)

_(none currently open from the original two bootstrap inferences — both settled. See "Destination run — 2026-07-03 (second pass)" below for what's open now.)_

Both sourced inferences from the initial bootstrap are now settled: Probe stays excluded, and no installer will be built. Ease-of-use (a single readable file, no packaging step) is now a confirmed design constraint on `work/SKILL.md`, not just a scope cut.

---

## Destination run — 2026-07-03 (second pass)

Operator asked to run the full Destination skill again (not the mini version). Signal gathered: this file, `.acm/audit-trail.md`'s 4 entries, and the pattern across the two prior corrections this session.

### Sourced inferences

1. **[Direction, unconfirmed]** The operator wants `pea-lite` to become their actual day-to-day default, not a parallel experiment. *Source:* the original bootstrap message ("I find myself mostly using Intent and improve"), plus both corrections since bootstrap pushing toward permanence rather than provisional framing ("not ever," not "not yet").
2. **[Priority, unconfirmed]** The operator wants this repo's files kept lean — no speculative "decide later" open items invented unprompted. *Source:* twice now (Probe exclusion, no-installer) the operator corrected an open item or hedge that was added without being asked for.
3. **[Question being asked, resolved this run]** The one open item left (whether to list this repo in the workspace layer table) was itself something added unprompted, not requested.
4. **[Quality bar, unconfirmed]** "ppl that can use it" may signal the actual bar is "a stranger could pick this up," not just "works for the operator."

### Questions asked

All four inferences above were surfaced as direct questions. **The operator was not available to respond** ("Work autonomously and make good decisions").

### What I now believe (confirmed 2026-07-03 by the operator, except where noted)

- **Confirmed.** `pea-lite` is the operator's new daily-usage skill. "Yes i want pea skills lite to become my new daily usage skill." This is now stated in "Why this repo exists" above, not just this section.
- **Confirmed.** Keep this repo's files clean — no speculative open items added unprompted. "yes i want the repo files kept clean." Adopted as an ongoing practice, not just a one-time correction.
- **Deferred by the operator, not dropped.** The workspace-layer-table question confused as asked ("im not sure what you mean abotu question 3 i will decide later"). Clarifying it here for whenever it's picked back up: `pea/.acm/destination.md` (the workspace-level file, one directory up, operator-held) has a table listing the research program's repos by role (Theory, Construct, Runtime, Reasoning, etc.) — `pea/skills` is currently listed there as "Reasoning." The open question was whether `pea-skills-lite` should also get a row in that table, or stay unlisted since it's a fork of an already-listed repo. This is a real open item now, explicitly operator-owned and deferred — not one I invented and should trim per the lean-files practice above.
- **Confirmed.** "ppl that can use it" was literal, not just phrasing: "Yes it should also be that a stranger could pick up the skill." This is now reflected as an explicit second success bar in "What 'done' looks like" above.

### What's still open

- The workspace-layer-table question (see above) — operator-deferred, revisit when they want to decide.

---

## Destination run — 2026-07-04 (third pass)

Operator corrected the priority ordering implicit in the prior day's comparative-rating work. That rating had weighted mechanism-completeness (freshness guards, writer-splitting, ARF/Probe, session/transcript capture) as a significant gap against the full suite. The operator's correction: those mechanisms matter comparatively little; what must hold up is **reasoning quality**, specifically in the three moments that carry the actual thinking — interpreting the ask (Intent), examining the target and its surroundings (Improve's step 2), and arc-level meta-reasoning about the work itself (Orient). This is now folded into the confirmed mandate above as point 6, verbatim-sourced.

### What this changes going forward

- Future comparative ratings of `pea-lite` against the full suite should weight **interpretive depth, examination depth, and meta/arc-reasoning depth** as the primary axis — not mechanism parity.
- A legitimate open question this creates, not yet answered: is `pea-lite`'s current step 1 (Intent-fused), step 2 (Work/examine), and step 4 (mini-Orient) text actually *as rigorous* as the full suite's `intent`, `improve` step 2, and `orient` — or only structurally analogous? That assessment has not yet been done under this corrected priority and is the natural next piece of work.

### What's still open

- The workspace-layer-table question — operator-deferred, revisit when they want to decide.
- **New:** the reasoning-quality depth assessment named above — not yet run.

---

## Destination run — 2026-07-04 (rename)

Operator judged the name `pea-lite` a defect in its own right: it tells an outsider nothing about what the skill does, and fails the same stranger-pickup bar this file already holds as a confirmed design constraint. Three rounds of candidate names were proposed and rejected on the operator's own explicit criteria — round 1 rejected for not "sounding useful" on sight, round 2 (`show-your-work`) rejected for not capturing the reasoning-and-generality dimension, round 3 confirmed: **`think-it-through`**. The repo itself was renamed too (operator's explicit choice): `pea-skills-lite` → `think-it-through-skill`, avoiding a redundant nested `think-it-through/think-it-through/SKILL.md` by keeping the skill subfolder as `think-it-through/`.

**What changed:** `pea-lite/` → `think-it-through/` (git mv, history preserved), repo folder `pea-skills-lite` → `think-it-through-skill`, frontmatter `name:` field, the `# think-it-through` H1, the one in-body mention, README.md, and this file's forward-facing prose (mandate, current-state, "what done looks like" sections). Version bumped 2.2.0 → 2.3.0 (a structural/identity change, not a prose polish).

**What was deliberately left alone:** every verbatim operator quote naming `pea-lite` or `pea-skills-lite` (e.g. "capability is one of the most important things for pea-lite...", "I dont think the probe skill is needed in pea-skills-lite", "Yes i want pea skills lite to become my new daily usage skill") — quotes are a historical record of what was literally said and are not rewritten. The two dated "Destination run" sections above (2026-07-03 second pass, 2026-07-04 third pass) are likewise left using the old name throughout, by the same logic applied to `.acm/audit-trail.md`'s append-only rule: they are historical log entries describing what was true and what things were called at that point in time, not living/forward-facing prose.

### What's still open

- The workspace-layer-table question — operator-deferred, if it's ever revisited it should now reference `auditonomy-skill`.
- The reasoning-quality depth assessment (named 2026-07-04, third pass) — still not yet run.
- The real empirical with/without-skill test — still the single most-repeated unresolved item across this whole arc.

---

## Destination run — 2026-07-04 (second rename)

Operator judged `think-it-through` itself not quite right either: it reads as a generic reasoning-discipline slogan, not a name tied to what the skill actually enforces. The correction came in two steps — first toward a made-up word blending Improve/audit/reasoning/autonomy (`Reckonomy`, rejected: too close to the unrelated word "reckoning"), then the operator's own realization: the right word was already named in this skill's own three principles — **Principle 2, Observable Autonomy**. `auditonomy` is a portmanteau of *audit* (the always-on Trail step — what makes the autonomy observable) and *autonomy* itself, naming the skill after the one governing principle that most defines its mechanism, not an arbitrary blend of adjacent themes.

**Action.** OS-level rename of the repo folder (`think-it-through-skill` → `auditonomy-skill`) and the inner skill folder (`think-it-through/` → `auditonomy/`); updated frontmatter `name:`, the H1, and the one in-body mention in SKILL.md; updated README.md throughout; updated this file's forward-facing prose (title, mandate, current-state, "what done looks like" sections). Version 2.3.0 → 2.4.0.

**Operational complication, disclosed.** The folder rename did not go cleanly: a `cmd /c move` failed silently (exit code 1, no message), and a follow-up `Move-Item` failed partway with a permission error deleting `.git`'s read-only pack objects from the source — but only *after* it had already copied `.git`, `.acm/`, and `README.md` to the new destination. This left the repo split across two paths: the intact `.git` (with the working index correctly showing a staged `think-it-through/SKILL.md` → `auditonomy/SKILL.md` rename) in the new `auditonomy-skill/` folder, but the actual `SKILL.md` file itself still physically sitting in the old `think-it-through-skill/auditonomy/` path. Diagnosed via `git status` (showed the rename staged but the destination file "deleted" in the working tree — the tell that the file hadn't actually moved), fixed by moving the one straggler file into place, verified with a clean `git status`, then deleted the confirmed-empty leftover shell. No data was lost; the near-miss is disclosed here rather than smoothed over, per this skill's own Trail discipline.

**Deliberately not touched:** every verbatim quote and every historical dated section above containing the old names `pea-lite`, `pea-skills-lite`, or `think-it-through` — preserved as historical record, same convention as the first rename. `audit-trail.md`'s own historical entries are likewise untouched; a new entry was appended instead.

### What's still open

- The workspace-layer-table question — operator-deferred, if it's ever revisited it should now reference `auditonomy-skill`.
- The reasoning-quality depth assessment (named 2026-07-04, third pass) — still not yet run.
- The real empirical with/without-skill test — still the single most-repeated unresolved item across this whole arc.

---

## Destination run — 2026-07-04 (standalone reframing)

Operator corrected the repo's core identity, prompted by reading the baseline 10-metric scorecard: the measurements ("reasoning-depth parity **vs. full suite**", "mechanism integrity") revealed the working destination had drifted into *"make an economical copy of this other skillset"* — a derivative identity. Operator's correction, near-verbatim: it should be **"standalone"** — *"an autonomous skill with improve reasoning and full auditability that is target-agnostic — can work on anything the model you use can reason about: code, music, letters, books, whatever, anything."* One overall destination point is unchanged from the skillset era: something with the ability to reason about and improve **anything**, adhering to PEA principles.

The self-targeting arc (24+ trail entries of this skill auditing and improving itself) is not self-polish — *"we just happen to point it at itself"*, and what's actually being improved in those runs is the **general improvement-reasoning capability itself**, exactly as was done with the skillset before it. The skill must know this overall purpose when it reasons about itself.

**What this changes:**

- "The One Question" and "Why this repo exists" above — rewritten to lead with standalone identity; the fork framing demoted to lineage-for-the-record.
- **Future scorecards:** measurements must weight *target-agnostic improvement capability* — how well this skill understands and improves arbitrary targets — as the primary axis. Suite-parity metrics are lineage diagnostics at best; a scorecard dominated by them is measuring the scaffolding, not the building. (The baseline scorecard in `orientation.md` stands as an honest record of the plateau *as it was framed then* — per the plateau rule, this destination shift voids it; the next rating starts from this reframed axis.)
- **The external-target test rises further in priority:** under the old framing it was one open item among several; under this one it is the *only* direct test of the actual destination — a target-agnostic improver that has almost never left its own repo is unproven at precisely the thing it is for.

**What this does not change:** the three PEA principles (constraints, not preferences), the cost discipline (real constraint, just not the identity), the no-installer rule, Probe's exclusion, the stranger-pickup bar, lean files. All confirmed constraints, all still binding.

### What's still open

- The workspace-layer-table question — operator-deferred.
- **The external-target test — now the top item by an even wider margin** (see above): point this skill at something that isn't itself and isn't software — a letter, a plan, a piece of writing — and see whether the improvement reasoning holds.
- The reasoning-quality depth assessment — subsumed into the above: the external test *is* that assessment under the corrected framing.

---

## Destination run — 2026-07-04 (cost is co-equal)

Same-day correction to the standalone reframing above, operator-initiated. That reframing over-rotated: it demoted cost to "a real constraint, just not the identity." The operator's correction, paraphrased per their instruction to capture intent rather than exact words: **cost is half the identity.** This repo is about creating the target-agnostic improvement-reasoning architecture *in a way that makes it cheap to use without losing quality* — because cost, not capability or effectiveness, is what became the problem with the full skillset. The suite already proved the capability; it priced itself out of daily use.

**What this means operationally:**

- The destination is a single product with two inseparable halves: **capability** (target-agnostic improvement reasoning, full auditability) × **affordability** (cheap enough to reach for by default, every session). An improvement to one that regresses the other is not an improvement — it is the failure mode that killed the suite, or a lobotomy that saves tokens by cutting judgment.
- **Future scorecards** must carry both axes: alongside the target-agnostic capability metrics (per the reframing above), at least one or two measurements must track cost-per-run / ceremony-weight — and a capability gain that shows up with a cost regression should be scored as the trade-off it is, not celebrated on the capability axis alone.
- Self-targeting runs improve *the capability-at-a-price*, not capability in the abstract.

**Unchanged:** everything else in the standalone reframing — target-agnosticism, the demotion of *suite-parity* (not cost) to lineage, the external-target test as top open item.

### What's still open

- Same three items as the reframing above — this correction changes the weighting of future work, not the open list.

---

## Destination run — 2026-07-04 (self-triggered destination)

Operator directive, this session: the skill should be able to trigger its destination step **itself** when its own evidence says it's necessary — plateau exhausted, etc. The operator explicitly delegated the design decision ("Based on my destination and your own belief — make the decision. Think carefully."), instructing intent-reading over literal wording.

**The decision, made under that delegation.** Intent read: "trigger its destination itself" means the skill owns **detection and initiation** — it must not sit passively on an exhausted plateau waiting for the operator to notice, and it must not silently keep polishing a destination its own evidence says is served. It does **not** mean the skill authors its own mandate: an agent that can rewrite its own destination unsupervised is the post-hoc-rationalization failure this research program exists to prevent — the destination is the alignment anchor the whole trail is audited against, and an anchor the anchored thing can move is not an anchor. The boundary chosen: **self-trigger the process, never self-settle the content.**

Concretely, in SKILL.md v2.9.0:

- Step 0.5 gains a third legitimate re-run trigger alongside explicit invocation and operator signal: **the loop's own evidence** — a plateaued scorecard whose destination-vs-measurements coverage diff comes back empty, or observed reality contradicting this file's claims. "Never merely because time passed" stays.
- A self-triggered destination run may ask and propose; its output enters this file only as an appended, dated proposal **marked unconfirmed** until the operator rules. The pre-commit read-back rule applies in full.
- The scoring clause gains the plateau-exit protocol: flat scores → first distrust the plateau (coarse metrics vs. exhausted territory) → coverage-diff destination against measurements → uncovered obligations become work or new measurements → an empty diff is the self-trigger. New metrics are *derived* from uncovered obligations, never invented to have something to score.

This widens the previous step 0.5 rule ("never re-run automatically") by the operator's own instruction — the old rule guarded against re-bootstrapping churn; the new one keeps that guard ("never merely because time passed") while removing the passivity it accidentally mandated at a genuine plateau.

**Read-back note:** the active operational rule says destination-layer edits are read back before commit. This session the operator explicitly delegated the decision in the same turn; that delegation is treated as the required confirmation, and this section is itself the read-back — if any part of this misreads the intent, the correction happens by appended section, per convention.

### What's still open

- The three standing items (workspace-layer table, non-software artifact test, second fresh multi-writer trail) — unchanged.
- **New:** the self-trigger has never fired — it becomes real the first time a plateaued scorecard's empty coverage diff actually initiates a destination question. Until then it is text, like every rule before its first conversion.

---

## Destination run — 2026-07-04 (need-triggered orient; the skill leads the workflow)

Operator, same session, confirming the v2.9.0 boundary ("Yes, the operator owns the destination") and extending the principle:

1. **The "every 5th" orient cadence was arbitrary, by the operator's own account** — "just a value I tossed out," not a principled rule. The mandate's original point 4 ("Mini-Orient. Every 5th iteration...") is hereby corrected at the trigger level: the *logic* to run orient must live in the flow — the skill triggers it when the work signals a need — exactly the detection-ownership principle v2.9.0 established for destination. (The condensed arc-read itself, versus full Orient machinery, is unchanged.)
2. **New confirmed constraint — the skill leads the workflow.** Operator verbatim: the operator "will be new to the skill... they must be guided and hand-held through the workflow." This extends the stranger-pickup bar from *reading* the file to *operating* it: the operator never needs to remember to invoke a step; the loop announces what's due, why, and names the one decision that belongs to the operator at that moment.

**Design judgment exercised (delegation pattern of this session, read back here):** the arbitrary counter was not deleted — it was **demoted to a backstop** behind four need-signals (arc contradicts itself; operator pushback; a stretch closes; orientation.md reads stale). Rationale: the run that most needs an arc-read is often the one least able to notice it — a rationalizing run won't feel its own need-signal — and the append-time due-check is the one mechanism in this repo with *behaviorally converted* evidence (self-fired at entries 33 and 38). Deleting the only mechanically checkable tripwire in favor of pure judgment would trade a proven mechanism for an unfalsifiable one. Need-signals lead; the counter catches what judgment misses. If the operator meant the counter should go entirely, this is the paragraph to push back on.

**Version note:** 2.9.0 → 3.0.0, and the frontmatter description changed for the first time since the scoring convention ("a mini-Orient every 5th entry" → "a self-triggered mini-Orient when the arc needs one") — the description would otherwise have stated a rule the file no longer contains.

### What's still open

- Everything above, unchanged — plus: the need-signals are text-only until one fires as the *primary* trigger (every firing to date was the counter). First conversion event: a mini-orient that runs off a need-signal before the backstop count is reached.

---

## Destination run — 2026-07-05 (third rename)

Operator judged `auditonomy` a defect too, on different grounds than the first two renames: not wrong or unclear, but an invented word — and it doesn't actually name the whole of what the skill does. Operator's own words, verbatim: *"'Work' SKILL captures exactly what its for - its for real work. The Work skill - the only skill you need."* Confirmed: **`work`** — a real, plain word, chosen specifically *because* it is not a portmanteau or a coinage, describing the skill's actual domain (any real task the operator points it at) rather than one mechanism inside it (as `auditonomy` did, naming only the Trail/audit half).

**Action.** OS-level rename of the repo folder (`auditonomy-skill` → `work-skill`, clean `Rename-Item`, no complications this time) and `git mv` of the inner skill folder (`auditonomy/` → `work/`, history preserved); updated frontmatter `name:`, the H1, and the two in-body mentions in SKILL.md; updated README.md throughout, including the tagline ("Auditable autonomy in one file" → "Real work, fully auditable, in one file" — the auditability claim is preserved, not dropped, just no longer load-bearing in the name itself); updated this file's forward-facing prose (title, blockquote naming chain, "why this repo exists", mandate constraints, "what done looks like"); updated `orientation.md`'s title line. Version 3.0.0 → 3.1.0.

**Deliberately not touched:** every verbatim quote and every historical dated section above containing the old names (`pea-lite`, `pea-skills-lite`, `think-it-through`, `auditonomy`) — preserved as historical record, same convention as the first two renames. `audit-trail.md`'s own historical entries are untouched; a new entry was appended instead. Other repos in this workspace (`ai-steward`, `vectorium`) that recorded past runs of this skill under the name `auditonomy` in their own trail files were also left untouched — those are accurate historical records of what the skill was called at the time the work happened, not references that should track the current name.

**Operator not consulted on GitHub rename mechanics this run** — operator was unavailable mid-task ("Work autonomously and make good decisions"); proceeded to rename the GitHub remote (`ntholm86/auditonomy-skill` → `ntholm86/work-skill`) via `gh repo rename`, on the judgment that this is what "make a proper rename... also the repo" most plausibly meant, and that GitHub's automatic redirect from the old URL makes this a low-risk, easily-visible action rather than a silently destructive one.

Blind spot: same as both prior renames — the new name has not been cold-read-tested against the stranger-pickup bar by a fresh reader, only judged by the operator directly. A generic word like `work` also carries a namespacing risk the coined names didn't (collision with other tools/skills literally named "work") — not yet weighed by the operator, worth flagging if it comes up. Next: the still-pending real empirical with/without-skill test remains the single highest-value open item, older and larger than any of the three renames.
Cost: moderate — roughly 20 tool ops across 4 files plus a GitHub API rename, no subagent.

### What's still open

- The workspace-layer-table question — operator-deferred, if it's ever revisited it should now reference `work-skill`.
- The reasoning-quality depth assessment — still not yet run.
- The real empirical with/without-skill test — still the single most-repeated unresolved item across this whole arc.
- **New:** whether a bare, generic word (`work`) creates any real confusion in practice (tool names, search collisions, verbal ambiguity in conversation) — not yet observed, worth a note if the operator hits it.

---

## Destination run — 2026-07-26 (one universal path: destination → orient-with-rubric → loop-until-silence)

Operator ran the full Destination skill (not the mini version) to capture a conversation that started from a question about whether an independent-evaluator's convergence-log rules belonged in the general skill. Signal gathered: that conversation itself, this file, and the current `.acm/orientation.md` / `.acm/audit-trail.md` state. Operator's own framing: **"the overall destination remains the same but this is for accuracy"** — this is a refinement of mechanism-shape, not a redirection of "The One Question" above.

### Sourced inferences

1. **[Direction, confirmed this run]** There should be exactly one workflow shape, with no fork between self-targeting and external-targeting runs — the loop should look identical either way. *Source, verbatim:* "In my mind the flow is obvious. THere should be only one path - always, self targetting run or not - and it should end with silence against a certain destination."
2. **[Mechanism, confirmed this run]** Orient must run once, immediately after destination is established, **even on a target with zero trail history** — producing a measurement rubric and a todo list as a structural output of orient-bootstrap itself, not as something gated behind an explicit "rate it" request. *Source, verbatim:* "then orient (yes even without history) - so that the measurement rubric created (not triggered on 'rate it' just as a mechanism of the mini-orient) and the todo list is created."
3. **[Constraint, confirmed this run]** This whole bootstrap apparatus (destination.md, orientation.md-with-rubric) must be skippable for genuinely small tasks — it would be overkill to demand both files exist for a trivial ask. *Source, verbatim:* "Orientation and destination and rubric should exist before it begins - but be skippable if the task is small enough - and it would be overkill demand destination.md and orientation.md just for a small task."
4. **[Priority, confirmed this run]** The loop must self-detect, without operator prompting, both (a) when an arc-read is due and (b) when destination itself needs redefining because progress has visibly slowed. *Source, verbatim:* "the work skill should be aware of when to trigger the orient skill - or when to redefine destination because the speed is slowing down." (Note: (b) already exists mechanically as step 0.5's third re-trigger, added in "Destination run — 2026-07-04 (self-triggered destination)" above — this run confirms that mechanism rather than introducing it.)
5. **[Constraint / meta-stance, confirmed this run]** Corrections to how the skill should behave should route through destination-setting, not through piecemeal mechanism bolt-ons reacting to one observed rule at a time — and the fact that independent model families have already converged on the current path/workflow is itself part of the architecture's evidentiary strength, worth protecting from ad hoc bloat. *Source, verbatim:* "i dont want to add unnessecary bloat to the skill and part of the strong arguements of the skills architecture is that several models converged on the path and the workflow - which is what i am now defining when i really need to only define the destination."

### Questions surfaced and operator responses

All five inferences above were read back to the operator in full (this repo's `.acm/audit-trail.md`, prior turn) before this file was touched, per the destination-layer read-back rule. The operator's instruction to "run destination skill to capture this talk" — after confirming "the overall destination remains the same but this is for accuracy" — is treated as confirmation of all five.

### What I now believe

- **Confirmed.** The loop's mechanical shape (steps 0-4) must never special-case self-targeting vs. external targets — already true of the current text; this run makes it an explicit, checkable constraint rather than an incidental property.
- **Confirmed.** Orient needs a first-contact mode (paired with step 0's Destination bootstrap) that fires once on encountering a target with no history, producing a rubric and a todo list unconditionally — **not yet in `work/SKILL.md`**. Today's step 4 is entirely arc-based (reads "the last ~5-10 entries," fires on need-signals or a backstop count) and structurally cannot fire on a target with zero entries. This is a real, confirmed mechanism gap, not yet closed.
- **Confirmed.** Step 0's condensed Destination process needs a depth-escalation path that references the full `destination` skill's interview methodology (this file's own governing skill, `pea/skills/destination/SKILL.md`) when the condensed "1-3 guesses → one question" shape is too shallow for what's being decided — not yet in `work/SKILL.md`.
- **Confirmed.** The whole bootstrap-plus-orient-bootstrap apparatus needs an explicit small-task skip clause, consistent with the existing Tier system's cost discipline — not yet in `work/SKILL.md`.
- **Not yet ruled on by the operator — left open, not assumed:**
  1. What an orient-bootstrap rubric rests on when a target has zero prior entries to cite as evidence (the scoring clause's own rule is "a score with no cited evidence is a guess wearing a number"). Two readings were offered — provisional/unscored axes first vs. scoring directly against live inspection of the fresh target — neither confirmed.
  2. Whether the literal **Cross-model convergence log** table format needs to become a general SKILL.md concept every target keeps, or whether only the underlying *behavior* (independent runs eventually converging to silence) needs to generalize while the table itself stays this repo's own bookkeeping choice, the same status as a target-specific rubric or todo list.

### What this changes going forward

This section is a destination-level confirmation only — it does **not** yet change `work/SKILL.md`. The corresponding mechanism deltas (Orient bootstrap sub-step, unconditional rubric-and-todo generation, destination-interview depth escalation, task-size skip clause) are named above as confirmed obligations this destination now imposes on the skill text, but implementing them is a separate, explicitly deferred decision — the operator has not yet chosen between capturing this as policy-only (done, this run) versus also drafting the SKILL.md deltas for review.

### What's still open

- The workspace-layer-table question — still operator-deferred, unchanged.
- The real empirical with/without-skill test — still the single most-repeated unresolved item across this whole arc.
- **New:** the two unconfirmed sub-questions above (rubric-with-zero-evidence handling; convergence-log-as-general-mechanism vs. target-specific artifact).
- **New:** whether and how to draft the `work/SKILL.md` mechanism deltas this destination run now obligates (Orient bootstrap, rubric/todo unconditional on bootstrap, destination-interview escalation, task-size skip) — confirmed as owed, not yet scheduled.

---

## Destination run — 2026-07-26 (one Orient, destination-derived ratings, correctness by construction)

Operator corrected the v3.4.3 design after asking how Mini-Orient worked: "The orient bootstrap should be the same as the mini-orient (but it should be just be called Orient - no 'mini' anywhere)" and "we already had some kind of rubric measurement rating mechanism - i thought it was tied to the orient/mini-orient." This is a correction to the mechanism interpretation captured in the preceding 2026-07-26 run, not a change to the repo's overall destination.

### Sourced inferences

1. **[Architecture, confirmed]** There is one Orient operation, invoked both on first contact and later need-signals. Bootstrap and later arc-read are call conditions, not separate implementations or names. *Source:* operator's quoted correction above; the live v3.4.3 file instead has separate step 0.5 "Orient bootstrap" and step 4 "Mini-Orient" procedures.
2. **[Mechanism, confirmed by question]** Every Orient creates or refreshes a destination-derived rubric and evidence-backed ratings. First contact uses current target evidence; later Orient runs combine current target state with Trail evidence. Rating is not a separate operator-triggered Work feature. *Source:* operator's statement that the existing rubric/measurement/rating mechanism was expected to be tied to Orient. Asked directly: "Should every Orient produce or refresh evidence-backed ratings for its destination-derived rubric, including first contact using live target evidence?" Operator selected "Yes, every Orient rates."
3. **[Constraints, explicit]** DRY, KISS, and YAGNI govern the design: one definition of Orient, the smallest flow that expresses the invariant, and no speculative branches or machinery. *Source:* operator: "We need to apply simple principles to the destination: DRY, KISS, YAGNI."
4. **[Quality bar, confirmed by question]** Prefer constructions in which invalid paths cannot be represented; where a Markdown skill can only prescribe behavior, disclose that enforcement boundary instead of claiming a structural guarantee. *Source:* operator: "I believe that the best design is one that makes bugs impossible." Asked directly whether Work should prefer one construction that makes invalid paths unrepresentable and disclose procedural-only boundaries; operator selected "Yes, construction first."
5. **[Usability, explicit]** The complete flow, including ordinary cases and edge cases, must be describable and visualizable as one coherent system. *Source:* operator asked for the "entire skillset flow with all cases and edge-cases," reinforcing the existing stranger-pickup and skill-leads-workflow bars.

### What I now believe

- **Orient owns measurement.** It derives the rubric from the confirmed destination, rates each axis from cited evidence, forms falsifiable current claims, identifies the next candidate moves, checks cost/loop effectiveness where evidence exists, and bounds silence.
- **Invocation changes evidence breadth, not procedure identity.** On first contact there may be no Trail history, so Orient rates from direct inspection of the target and marks unavailable historical evidence explicitly. On later triggers it reads recent Trail evidence as well. The same output contract applies in both cases.
- **The current split is a design defect.** v3.4.3 duplicates Orient across steps 0.5 and 4 while keeping ratings in step 2 behind "when the operator asks." That violates DRY, permits the two paths to drift, and caused the operator's correction.
- **Correctness by construction outranks reminder text.** The live skill should define Orient once and make both first-contact and later triggers route to it. Trail-before-action remains a procedural guarantee because a Markdown instruction cannot mechanically enforce write ordering; that bound must remain honest.

### Rejected or superseded

- Superseded: bootstrap Orient may leave ratings blank when no Trail exists. Direct target inspection is evidence; every Orient rates, while honestly marking axes whose evidence is unavailable.
- Superseded: rating is a distinct Work behavior triggered only by "rate this." An explicit rating request triggers Orient; it does not invoke a separate scoring implementation.
- Superseded terminology in live guidance: "mini-Destination" and "Mini-Orient." Historical quotations and dated records retain the words as evidence of what the design used to call them; they are not current architecture.

### Still open

- No destination question remains open for this redesign. Behavioral conversion on a genuinely fresh target remains an evidence task after the mechanism is changed, not a destination ambiguity.

---

## Destination refinement — 2026-07-26 (rubrics visualize progress but must not become the field of vision)

Operator confirmed the intended loop in direct form: **Destination → Orient measures and creates the todo list → iterate until silence; when Destination changes, Orient creates a fresh rubric.** The measurements are retained because their visible deltas are satisfying and useful to the operator, despite the autonomy cost that caused the full PEA suite to abandon rubric-led improvement.

### Confirmed tradeoff and constraints

1. **Rubrics are an operator-facing visualization, not the agent's search space.** They show a useful projection of progress; they do not define everything worth seeing. *Source:* operator: measurements were dropped by the PEA suite because they limited autonomy, but the visualization tradeoff is worth retaining in Work.
2. **The skill must actively mitigate rubric blindness.** Merely saying scores are temporary addresses Goodhart persistence but not attentional anchoring during the current plateau. The agent must look beyond inherited measurements before using them.
3. **Destination is the sole rubric source.** Orient derives measurements from the current confirmed destination. A materially changed destination invalidates the entire prior rubric, ratings, deltas, and todo; the next non-Micro operation is a fresh Orient.
4. **The flow should be expressed as invariants, not an expanding edge-case catalogue.** Apply KISS, YAGNI, DRY, Simplicity, Clarity, Transparency, and Solve by Design. Prefer one state rule that absorbs many cases over another branch explaining one symptom.
5. **Scores do not determine convergence.** The visible delta is progress telemetry. Silence across independent destination-reading evaluators remains the stopping condition.

### Design consequence

Orient must examine the target openly **before consulting inherited rubric scores**, re-derive candidate measurements from Destination, and compare that derivation with the inherited rubric. Anything important found outside the rubric, or any divergence in re-derivation, is a first-class finding. Only then may Orient score and produce the todo. This preserves the operator-facing visualization while preventing the inherited rubric from becoming the ceiling by construction of the reading order.

---

## Destination refinement — 2026-07-26 (trusted compression and Improve-grade judgment)

The operator identified a deeper boundary behind rubric blindness: Work cannot afford to read an entire solution on every run, so Destination must serve as **trusted compression of the human meaning**. That compression saves tokens only when the interview captures the destination accurately enough that the operator recognizes their own intent in it. Even an accurate Destination cannot prescribe every useful way of thinking; Work must retain enough reasoning capability to discover principles, structural simplifications, and target-specific lenses that the operator did not know to name.

### Confirmed responsibilities

1. **Destination compresses the human model.** It holds the ends, durable constraints, recurring principles, quality bars, and rejected trade-offs that later work should not have to reconstruct by reading the whole solution or replaying the conversation.
2. **Operator recognition is the stopping bar for the interview.** Purpose, audience, quality bar, constraints, and unacceptable trade-offs are useful prompts, not a completion checklist. Destination is sufficiently accurate when the operator recognizes that it captures what matters and would let a human judge the result.
3. **Recurring principles may be named defaults, never a closed reasoning set.** DRY, KISS, YAGNI, simplicity, clarity, transparency, and solve-by-design may remain explicit constraints because the operator repeatedly values them. Their presence does not excuse Work from independently deriving other lenses the target and domain require.
4. **Every decision-bearing run retains Improve-grade reasoning.** Standard and Full may differ in recording depth and evidence breadth, but both must form a model of the target, derive target-specific lenses, consider competing interpretations or routes, test whether structural redesign dominates another local patch, and challenge the resulting model. Micro remains genuinely cheap.
5. **Map before local reasoning is the default, scaled by domain risk.** Work should first establish a compact view of the target's major parts, controlling relationships, and important unknowns. The agent decides how broad that map must be from the target domain's risk and reversibility; low-risk work may stop early, while high-risk work earns broader evidence. No universal read count or token quota substitutes for judgment.
6. **Orient's rubric and todo are advisory maps.** Every Work iteration may retain or displace the suggested top item when its current target model reveals more important work. The reason for displacement becomes evidence for the next Orient; following the list is never a substitute for examining reality.
7. **Human legibility is universal.** Work must leave the target, the reasoning that changed it, and why the result serves Destination intelligible to the operator, with explanation depth scaled to the target and stakes. A technically functioning result that humans cannot understand or judge has not fully served the destination.

### Why this refinement was needed

The recent self-improvement sequence required repeated operator prompts to add DRY, KISS, YAGNI, simplicity, and flow verification before Work recognized that its growing edge-case catalogue needed one invariant. Part of that miss came from an incomplete Destination. The remaining part came from Work's compressed reasoning implementation: it copied Improve's named lenses and challenge questions but did not reliably preserve Improve's stronger operations of building a target model, inventing lenses from the domain, comparing plausible routes, ranking structural alternatives, and reflecting on where the target's real weight sits. Improving Destination alone would hide that capability gap rather than solve it.

### Consequence for the next Work run

The current v3.6.0 Orientation is void as current guidance because its Destination basis predates this refinement. The next non-Micro Work run must perform a fresh Orient against this exact basis before mechanism changes. That Orient should derive measurements capable of testing trusted compression, Improve-grade decision reasoning, risk-sized mapping, advisory todo behavior, and human legibility without turning those measurements into a new closed checklist.

### Still open

- How to encode Improve-grade reasoning compactly enough to preserve the daily-use cost goal without reducing it to another checklist.
- What minimum evidence demonstrates a sufficient risk-sized map in different target domains; the agent owns the judgment, and the Trail must make the chosen breadth inspectable.
