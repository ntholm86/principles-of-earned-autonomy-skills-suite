# work-skill

**Real work, fully auditable, in one file.** `work` is a standalone, target-agnostic improvement-reasoning skill: point an agent at anything it can reason about — code, documents, plans, letters, music — and it examines, improves, and records material decisions and their outcomes in an auditable trail. The whole skill is one readable markdown file: [`work/SKILL.md`](./work/SKILL.md). No installer, no tooling, no dependencies — by design, permanently.

It is built on the three [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy):

1. **Operator's Intent** — the agent is given a destination, not a route.
2. **Observable Autonomy** — material decisions and predictions are recorded before action, with outcomes appended afterward; an observer can reconstruct what was done and why from the trail alone.
3. **Convergence Is Silence** — finding nothing actionable is a valid outcome; ceremony is never manufactured to look thorough.

## Why

Its parent, the full [skills suite](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite), delivers the same discipline as five separate skills (`intent`, `improve`, `destination`, `orient`, `trail`) — and proved the capability, but priced itself out of daily use: five skill-loads and full ceremony on every run, even a one-line fix. `work` is the consolidation — one skill-load, one loop, with reasoning depth scaled to the stakes of the moment instead of a fixed template:

- **Intent** — folded into the loop's own first step, narrated only when the interpretation is genuinely uncertain.
- **Improve** — the base loop (examine → challenge → decide → act → reflect), depth-scaled to the stakes of the change.
- **Destination** — a condensed first-contact process that asks one short question, escalating to a deeper multi-question interview when the stakes call for it — and can re-trigger *itself* when evidence says the destination is exhausted or wrong, while the operator always owns what the destination becomes.
- **Orient** — one open-world operation: inspect the target before reading inherited scores, re-derive measurements from the current Destination, compare the old and new maps, then rate with cited evidence and create the todo. It runs whenever Orientation is invalid, the operator asks, evidence challenges the current view, or a small backstop catches what judgment missed.
- **Trail** — always happens, every run, with a variable-depth entry format (Micro / Standard / Full) so routine work costs little and real decisions still get full reasoning.

The skill leads the workflow, not the operator: it announces what it's doing and why, and names the one decision that belongs to the operator at each moment. `probe` (contamination / pattern-matching detection) is intentionally excluded from this consolidation — a settled decision, not a placeholder.

## Status

v3.7.0 — the operator's confirmed daily-usage skill, and dogfooded hard: the skill has been pointed at itself and at external targets (a Python code repo where it made a test-verified source change, and editorial/content repos), with every run — including its own design decisions — recorded in this repo's trail. Every decision-bearing run performs Improve-grade reasoning (examination, challenge, model-building); Standard and Full tiers differ in recording depth, not reasoning depth. Orient owns the destination-derived rubric and evidence-cited rating path, but performs an open-world examination and independently re-derives the measurement scheme before reading inherited scores. Orientation records its exact Destination basis; a changed basis invalidates the old rubric and makes fresh Orient mandatory. DRY, KISS, YAGNI, and correctness-by-construction are explicit design constraints. A second design bar applies alongside the operator's own use: **a stranger should be able to pick up `work/SKILL.md` and use it without the author explaining anything** — jargon or unexplained references to the parent suite are treated as defects. See [`.acm/destination.md`](./.acm/destination.md) for the full mandate and open items, and [`.acm/audit-trail.md`](./.acm/audit-trail.md) for the complete record of how this repo came to be — including the wrong turns.

## Use

Point an agent at [`work/SKILL.md`](./work/SKILL.md) — copy the `work/` folder into wherever your agent loads skills from (such as `~/.copilot/skills/`), or just paste the file into a prompt. There is no installer, and there won't be one — by design. The whole point is that it's just a skill: one readable file, no build step, no script to trust between reading it and using it.
