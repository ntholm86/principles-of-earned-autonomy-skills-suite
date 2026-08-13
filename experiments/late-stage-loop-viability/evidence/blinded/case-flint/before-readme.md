# work-skill

**Real work, fully auditable, in one file.** `work` is a standalone, target-agnostic improvement-reasoning skill: point an agent at anything it can reason about ÔÇö code, documents, plans, letters, music ÔÇö and it examines, improves, and records material decisions and their outcomes in an auditable trail. The whole skill is one readable markdown file: [`work/SKILL.md`](./work/SKILL.md). No installer, no tooling, no dependencies ÔÇö by design, permanently.

It is built on the three [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy):

1. **Operator's Intent** ÔÇö the agent is given a destination, not a route.
2. **Observable Autonomy** ÔÇö material decisions and predictions are recorded before action, with outcomes appended afterward; an observer can reconstruct what was done and why from the trail alone. The final Markdown cannot prove wall-clock write order, so stronger timing guarantees require independent capture.
3. **Convergence Is Silence** ÔÇö finding nothing actionable is a valid outcome; ceremony is never manufactured to look thorough.

## Why

Its parent, the full [skills suite](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite), delivers the same discipline as five separate skills (`intent`, `improve`, `destination`, `orient`, `trail`) ÔÇö and proved the capability, but priced itself out of daily use: five skill-loads and full ceremony on every run, even a one-line fix. `work` is the consolidation ÔÇö one skill-load, one loop, with Improve-grade decision reasoning whenever a real choice exists, while target evidence and durable narration scale to domain risk and stakes:

- **Intent** ÔÇö folded into the loop's own first step, narrated only when the interpretation is genuinely uncertain.
- **Improve** ÔÇö the base loop: build a risk-sized target map, form a falsifiable model, derive the lenses reality warrants, compare plausible routes, challenge structure, decide, act, and check human legibility. Standard and Full share these operations; only evidence and recording depth vary.
- **Destination** ÔÇö a condensed first-contact process that asks one short question, escalating to a deeper multi-question interview when the stakes call for it. The interview ends on operator recognition rather than checklist completion, and can re-trigger *itself* when evidence says the destination is exhausted or wrong, while the operator always owns what the destination becomes.
- **Orient** ÔÇö one open-world operation: inspect the target before reading inherited scores, re-derive measurements from the current Destination, compare the old and new maps, then rate with cited evidence and create an advisory todo. It runs whenever Orientation is invalid, the operator asks, evidence challenges the current view, or a small backstop catches what judgment missed.
- **Trail** ÔÇö always happens, every run, with a variable-depth entry format (Micro / Standard / Full) so routine work costs little and real decisions still get full reasoning.

The skill leads the workflow, not the operator: it announces what it's doing and why, and names the one decision that belongs to the operator at each moment. `probe` (contamination / pattern-matching detection) is intentionally excluded from this consolidation ÔÇö a settled decision, not a placeholder.

## Status

v3.8.3 ÔÇö the operator's confirmed daily-usage skill, and dogfooded hard: the skill has been pointed at itself and at external targets (a Python code repo where it made a test-verified source change, and editorial/content repos), with every run ÔÇö including its own design decisions ÔÇö recorded in this repo's trail. Destination is trusted human compression; its interview ends when the operator recognizes that the compact account captures what matters, and append-only history is resolved by later confirmed decisions plus live target state rather than mistaken for a current work order. Every decision-bearing run preserves Improve-grade judgment, while domain risk controls target evidence and Trail tier controls recording depth. When an external target is used as a probe for another target, Work records the enclosing mission in the evaluation Trail, restates it in the probe Trail, and returns once the registered evidence is obtained or further cost becomes disproportionate; local Orientation cannot silently turn the probe into the destination. Trail's two-stage record is mandatory and makes retrospective reconstruction a visible breach, while final Markdown alone is explicitly not claimed to prove wall-clock timing. Orient's rubric and todo remain advisory maps. Human legibility is part of correctness. Orientation records its exact Destination basis; a changed basis invalidates the old rubric and makes fresh Orient mandatory. DRY, KISS, YAGNI, and correctness-by-construction are explicit design constraints. A second design bar applies alongside the operator's own use: **a stranger should be able to pick up `work/SKILL.md` and use it without the author explaining anything** ÔÇö jargon or unexplained references to the parent suite are treated as defects. See [`.acm/destination.md`](./.acm/destination.md) for the full mandate and open items, and [`.acm/audit-trail.md`](./.acm/audit-trail.md) for the complete record of how this repo came to be ÔÇö including the wrong turns.

## Use

Point an agent at [`work/SKILL.md`](./work/SKILL.md) ÔÇö copy the `work/` folder into wherever your agent loads skills from (such as `~/.copilot/skills/`), or just paste the file into a prompt. There is no installer, and there won't be one ÔÇö by design. The whole point is that it's just a skill: one readable file, no build step, no script to trust between reading it and using it.
