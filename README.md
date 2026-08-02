# Principles of Earned Autonomy - Skills Suite

AI agents forget everything between sessions — and many things within a session. No memory of what was tried. No memory of why a decision was made. No memory of where you were heading. Forgets what it already created.

The suite fixes that with two deliberate actions: set the **Destination** and **Run** Improve. The architecture maintains **Orientation** passively — refreshing its map of where the work is when direction changes or enough evidence accumulates. A persistent memory layer survives session resets and model swaps underneath that workflow.

These are the skills I use daily as a software engineer to safely delegate complex goals to AI agents. When an agent runs without constraints, it creates massive technical debt. These skills force it to stay on track, double-check its assumptions, and leave a clear record of why it made each change.

Implementation repo for [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy). The manifesto defines the principles; this suite enacts them.

The memory structure this suite uses is formally specified in [Agent Context Memory (ACM)](https://github.com/ntholm86/agent-context-memory) — the governance-first specification for AI agent context memory. This suite is the reference implementation of ACM.

Compatible with Claude (skills / Agent SDK), GitHub Copilot (custom skills), and any LLM agent that can read markdown and append to a file.

![The full architecture illustrated as a Storm P-style Rube Goldberg machine: Operator's Intent feeds the Improve loop, the audit trail runs as a conveyor belt through the whole machine, Orient reads the arc and feeds learning back in, and the machine converges to silence.](./stormpInspired.png)

## The Suite Improved Itself — [286 verified iterations](./.acm/ITERATION-COUNT.md)

The suite ran on itself **286 times** across four eras and two complete rewrites. Each self-targeted iteration is documented in the [evidence trail](./.acm/audit-trail.md), with 256 individually backed by git commits and the remaining 30 by a bulk initial commit. The full provenance breakdown — including git SHAs, verification commands, and an honest account of what is independently verifiable — is in [ITERATION-COUNT.md](./.acm/ITERATION-COUNT.md).

Convergence was declared only when **three independent evaluators from distinct model families** (Claude, Gpt, Gemini) each ran the loop and found nothing left to change.

> "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction."
>
> — Jie Huang et al., [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) (ICLR 2024)

If the loop can't improve itself, the claim that it improves anything else is empty. It can.

## Confidential Professional Field Evidence

This skillset has also been used successfully in professional enterprise delivery on a confidential production system with high complexity and scale: multi-tenant cloud architecture, domain-driven service boundaries, multiple collaborating microservices, cross-platform delivery requirements, and fully automated CI/CD.

In that deployment, a scope estimated internally as a large T-shirt-size effort was completed in 3 days.

The full trail exists, but it cannot be published in this repository because it is employer-owned professional work product and covered by intellectual property and confidentiality obligations. Treat this as high-signal private field evidence: a strong indication of practical leverage, but not public, independently reproducible proof.

## The Skills

Every skill belongs to one roster. What differs is how it activates:

- **Active** skills are deliberately invoked by the operator.
- **Passive** skills apply automatically around every substantive action.
- **Triggered** skills activate automatically when their conditions are met.

| Skill | Activation | What it does | Command or trigger |
| :--- | :--- | :--- | :--- |
| ![Destination icon](./assets/skills/destination.svg) **[Destination](./destination/SKILL.md)** | **Active** | Establishes where the work is going and what success means. | `/destination` when work begins or direction changes |
| ![Improve icon](./assets/skills/improve.svg) **[Improve](./improve/SKILL.md)** | **Active** | Examines, changes, verifies, and learns toward the Destination. | `/improve` repeatedly to move the work forward |
| ![Intent icon](./assets/skills/intent.svg) **[Intent](./intent/SKILL.md)** | **Passive** | States what the agent believes the operator means before acting. | Always applies before substantive work |
| ![Trail icon](./assets/skills/trail.svg) **[Trail](./trail/SKILL.md)** | **Passive** | Preserves decisions, findings, actions, and reflections across sessions. | Always applies after substantive work |
| ![Orient icon](./assets/skills/orient.svg) **[Orient](./orient/SKILL.md)** | **Triggered** | Refreshes where the work is now by reading the accumulated arc. | Destination changes or Improve finds Orientation stale; `/orient` is an override |
| ![Probe icon](./assets/skills/probe.svg) **[Probe](./probe/SKILL.md)** | **Active** *(research only)* | Tests reasoning with controlled cases and measures [Autonomous Reasoning Fidelity](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/PRINCIPLES.md#autonomous-reasoning-fidelity-operational-definition). | `/probe` during controlled ARF research |

In normal development, the operator activates Destination and Improve. Intent and Trail are always present, while Orient waits for evidence that its map needs refreshing. Probe sits outside normal operation as optional research instrumentation.

## Agent Context Memory (ACM)

Each skill externalizes what normally only lives inside a single model session — the goal, the destination, the decisions, the arc. Together they implement Agent Context Memory: a persistent memory layer that no model reset can erase.

This memory structure is formally specified by the [Agent Context Memory (ACM)](https://github.com/ntholm86/agent-context-memory) standard. ACM defines three tiers organized by trust level: Intent (`destination.md`, principal-authored), Trace (`audit-trail.md`, `orientation.md`, agent append-only), and Evidence (harness-captured session records). This suite implements the Intent and Trace tiers; the Evidence tier requires a separate harness.

The files (`.acm/audit-trail.md`, `.acm/destination.md`, `.acm/orientation.md`) provide the literal storage, but the interaction of the skills with those files creates **contextual awareness**.

Memory alone is just retrieval; awareness is orientation. Because `Orient` reads the arc, `Destination` uncovers where you're heading, and `Intent` aligns the goal, the suite uses that memory to understand where it is and where it is going.

When you swap from Claude to Gpt to Gemini, the next model picks up this exact orientation. That accumulation is what makes the suite get smarter over time.

## How The Model Works

### Destination — Where are we going?

During a long autonomous run, the agent can lose the plot and optimize whatever is easiest to see. Destination surfaces the direction held by the operator so the work has an explicit purpose to advance.

> "No-one knows exactly what they want."
>
> — David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)

### Orientation — The architecture keeps its map current

After many locally sensible runs, the overall arc can still drift. Orient passively reads the accumulated history as one document and refreshes the current orientation: what the target is becoming, where attention has gone, and whether that is where the real weight lies. Destination schedules it after material direction changes; Improve schedules it when the evidence forms a meaningful arc, contradicts the current map, or approaches convergence. A raw iteration count alone does not trigger it.

> "Life can only be understood backwards; but it must be lived forwards."
>
> — Søren Kierkegaard, Journals (1843)

### Run — Move toward the destination

Improve is the workhorse. Point it at a target and run it repeatedly. Each run examines what is there, challenges the first read, chooses the highest-leverage move, acts, verifies, and reflects against the current Destination and Orientation.

> "Invest in the design of the system every day."
>
> — Kent Beck, [Extreme Programming Explained](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

Intent and Trail operate automatically around the work, and Orient maintains Orientation automatically when its evidence-based triggers fire. Probe sits outside normal operation as optional ARF research instrumentation.

## Workflow

1. **Set direction:** Run `destination` when work begins and whenever the destination materially changes. A material change automatically refreshes Orientation.
2. **Run:** Invoke `improve` repeatedly. Intent aligns each request, Trail records each result, and Improve automatically schedules Orient when accumulated evidence makes the current orientation stale.

The user remembers two commands: `/destination` and `/improve`. `/orient` remains a manual override for an explicit arc-read, not a routine responsibility.

## Quickstart (First Successful Run)

Want a copy-pasteable, 10-minute path? See [QUICKSTART.md](./QUICKSTART.md).

1. Install with one command:
   - macOS / Linux: `bash install.sh`
   - Windows: `pwsh install.ps1`
   - ARF researchers only: add `--research` on macOS/Linux or `-Research` on Windows to include Probe.
2. In your target repo, run Destination first to set direction:
   - `/destination capture the destination for this repo and write .acm/destination.md`
3. Run Improve on one concrete, verifiable task:
   - `/improve review the checkout module for waste and overburden`
4. Confirm the run produced evidence:
   - `.acm/audit-trail.md` has a new entry with outcome and delta.
5. Optional but recommended: install the pre-commit hook from the cloned suite's `harness/tools/` directory (see [QUICKSTART.md](./QUICKSTART.md)) to enforce trail discipline structurally.

## Known Limitation: Stated Reasoning ≠ True Reasoning

Trail logs what the agent *says* it decided. Research shows this is not always the same as what actually drove the decision.

> "CoT explanations can be plausible yet misleading, which risks increasing our trust in LLMs without guaranteeing their safety."
>
> — Miles Turpin et al., [Language Models Don't Always Say What They Think](https://arxiv.org/abs/2305.04388) (NeurIPS 2023)

> "CoT monitoring is a promising way of noticing undesired behaviors during training and evaluations, but that it is not sufficient to rule them out."
>
> — Yanda Chen et al., [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) (2025)

**How this suite mitigates it:** To prevent LLMs from generating post-hoc justifications to fit decisions already made, the suite enforces structural constraints:
1. **Pre-commit prediction (Improve, Trail):** The agent must record a falsifiable prediction of what a change will and will not achieve *before* acting or observing the actual outcome.
2. **Outcome anchoring (Orient):** Subsequent arc-reads systematically evaluate actual outcomes against those prior predictions to expose localized confabulation.
3. **Reversal density (Trail, Orient):** A uniform, unbroken trail of "successes" is actively flagged as suspect rationalization. True reasoning leaves a trail of reversals, dead ends, and tested predictions.
4. **Adversarial audit (Orient):** A dedicated lens to actively hunt for outcome mismatch and logical discontinuities across the trail history.
5. **Separating writer and decider (Improve, Trail):** In maximum-trust sequences (High-Fidelity Mode), the agent making the change is procedurally forbidden from writing the final trail entry, handing off to a second independent evaluator.

Together, these force the agent to lock its reasoning *before* acquiring evidence, and introduce explicit adversarial structures to break the post-hoc rationalization loop.

**The deeper limitation — protocol, not structure:** The five mitigations above assume the agent follows the protocol. Skills are markdown instructions interpreted by an LLM. There is no structural guarantee that the agent writes the trail at the right moment, issues the pre-commit prediction before acting, or runs any step at all. The suite is only as reliable as the model reading it. Structural enforcement — intercepting every LLM call at the API layer, writing the ledger before the response is released to the agent, fail-closed — is the responsibility of [`harness-protocol`](https://github.com/ntholm86/harness-protocol) and [`ai-steward`](https://github.com/ntholm86/ai-steward). This skills suite is the behavioural scaffolding and the experiment that generated the requirement for that structural layer.

## Reference

- Convergence criterion: three independent model families report no further actionable change.
- Principles source: [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy).
- Benchmark set and replication protocol: [harness/BENCHMARKS.md](./harness/BENCHMARKS.md).

## Citation and License

MIT License.
[CITATION.cff](./CITATION.cff) | Zenodo: [10.5281/zenodo.19842994](https://doi.org/10.5281/zenodo.19842994)
