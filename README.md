# Principles of Earned Autonomy - Skills Suite

## Give your AI Intent, Reasoning & Memory.

These skills will immediately solve:

- **Intent decay** — starts on your goal, drifts to a different one.
- **Directionless autonomy** — Implements exactly what you wrote, misses the obvious point.
- **Session amnesia** — every chat starts from zero.
- **Groundhog Day** — twenty messages in, and it's still making the mistake you corrected in message two.
- **Lost reasoning** — decisions survive, the why doesn't.
- **Confident confabulation** — plausible stories hide unfinished work.
- **Self-grading blind spots** — the agent that erred declares itself correct.
- **Quietly wasted effort** — sensible edits that move nothing that matters.
- **No honest stop** — the loop invents work to keep running.

This suite gives an agent a durable destination, memory of what happened, and a disciplined way to examine, improve, verify, and learn from its work. It interprets what you mean before acting, keeps the work anchored to the purpose, preserves decisions across sessions and model swaps, and stops when independent attempts find nothing material left to change.

**Try it:** run `Improve` on a real, bounded task. The agent chooses the route; you keep the destination and the consequential decisions.

The suite is the reference implementation of [Agent Context Memory (ACM)](https://github.com/ntholm86/agent-context-memory) and the implementation repo for the [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy). It is compatible with Claude (skills / Agent SDK), GitHub Copilot (custom skills), and any LLM agent that can read markdown and append to a file.

![The full architecture illustrated as a Storm P-style Rube Goldberg machine: Operator's Intent feeds the Improve loop, the audit trail runs as a conveyor belt through the whole machine, Orient reads the arc and feeds learning back in, and the machine converges to silence.](./stormpInspired.png)

## One skill to rule them all: IMPROVE

Run **Improve** on a real, bounded task. It invokes Intent before acting and Trail after substantive work, and schedules Destination or Orient when the accumulated evidence makes either service useful. You do not orchestrate the other operational skills; **Probe** is separate, optional research instrumentation.

```text
/improve create a professional knitting webshop in vanilla HTML, CSS, and JavaScript
```

| Component | Role | What it does | PEA principle | ACM artifact |
| :--- | :--- | :--- | :--- | :--- |
| **[Improve](./improve/SKILL.md)** | **Start here** | Makes one highest-leverage change per run. |  | reads all three |
| **[Intent](./intent/SKILL.md)** | **Automatic** | States what the agent believes you mean before acting. | Operator's Intent |  |
| **[Trail](./trail/SKILL.md)** | **Automatic** | Writes every run to an append-only audit trail. | Observable Autonomy | .acm/audit-trail.md |
| **[Destination](./destination/SKILL.md)** | **Automatic** | Consolidates accepted mandates into durable direction. |  | .acm/destination.md |
| **[Orient](./orient/SKILL.md)** | **Automatic** | Reflects on past runs to spot recurring mistakes and dead ends. |  | .acm/orientation.md |
| **[Probe](./probe/SKILL.md)** | **Research** | Measures Autonomous Reasoning Fidelity. | Autonomous Reasoning Fidelity |  |
| **Convergence to silence** | **Automatic** | Stops when independent evaluators find nothing left to change. | Convergence Is Silence |  |

The operator remembers one command: `/improve`. The rest is automatic under Improve's control.

## How The Model Works

Point Improve at a task. Each run reads your destination, the current map, and the trail; examines the target; makes one highest-leverage change; verifies it against a prediction recorded in advance; and writes the whole thing to an append-only ledger before finishing. When accumulated runs expose an unclear direction, Improve pauses to ask you; when the trail contradicts the map, it re-reads the whole arc and refreshes the map; and every lesson feeds the next run, so the suite gets smarter across sessions and model swaps. It stops when independent evaluators from different model families find nothing left to change.

### Destination — Where are we going?

Each narrated Intent gives Improve a mandate for the current prompt. When accepted mandates accumulate, conflict, or expose an unresolved priority, Improve triggers Destination to consolidate them into durable cross-run direction. Destination asks one sourced question at a time and never turns an unconfirmed agent inference into operator-held direction.

> "No-one knows exactly what they want."
>
> — David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)

### Improve — Move toward the destination

Improve is the workhorse and the single normal entry point. Point it at a target and run it. Each run applies Intent, explains its interpretation, examines what is there, challenges the first read, chooses the highest-leverage move, acts, verifies, records through Trail, and explains any automatic Destination or Orient handoff when the evidence triggers one.

> "Invest in the design of the system every day."
>
> — Kent Beck, [Extreme Programming Explained](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

### Orientation — The architecture keeps its map current

After many locally sensible runs, the overall arc can still drift. When triggered, Orient reads the accumulated history as one document and refreshes the current orientation: what the target is becoming, where attention has gone, and whether that is where the real weight lies. Destination schedules it after material direction changes; Improve schedules it when the evidence forms a meaningful arc, contradicts the current map, or approaches convergence. A raw iteration count alone does not trigger it.

> "Life can only be understood backwards; but it must be lived forwards."
>
> — Søren Kierkegaard, Journals (1843)

Intent and Trail operate automatically around the work. Destination and Orient activate automatically when their evidence-based triggers fire. Probe sits outside normal operation as optional ARF research instrumentation.

## The Suite Improved Itself — [314 self-improvement iterations](./.acm/ITERATION-COUNT.md)

**314 runs improved the suite itself** — its skills, reasoning, memory, or architecture — out of **377 self-targeted runs** in the public trail; the rest were consistency, evidence, and onboarding work, recorded the same way. The earliest 30 rely on bulk or reconstructed provenance; runs 31 onward have per-run GENBA or Trail records preserved in git, though one commit can contain multiple runs. The full provenance breakdown — including git SHAs, verification commands, the classification rule behind the 314, and an honest account of what is independently verifiable — is in [ITERATION-COUNT.md](./.acm/ITERATION-COUNT.md).

Convergence was declared only when **three independent evaluators from distinct model families** (Claude, Gpt, Gemini) each ran the loop and found nothing left to change.

> "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction."
>
> — Jie Huang et al., [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) (ICLR 2024)

If the loop can't improve itself, the claim that it improves anything else is empty. It can.

## Confidential Professional Field Evidence

This skillset has also been used successfully in professional enterprise delivery on a confidential production system with high complexity and scale: multi-tenant cloud architecture, domain-driven service boundaries, multiple collaborating microservices, cross-platform delivery requirements, and fully automated CI/CD.

In that deployment, a scope estimated internally as a large T-shirt-size effort was completed in 3 days.

The full trail exists, but it cannot be published in this repository because it is employer-owned professional work product and covered by intellectual property and confidentiality obligations. Treat this as high-signal private field evidence: a strong indication of practical leverage, but not public, independently reproducible proof.

## Agent Context Memory (ACM)

Each skill externalizes what normally only lives inside a single model session — the goal, the destination, the decisions, the arc. Together they implement Agent Context Memory: a persistent memory layer that no model reset can erase.

This memory structure is formally specified by the [Agent Context Memory (ACM)](https://github.com/ntholm86/agent-context-memory) standard. ACM defines three tiers organized by trust level: Intent (`destination.md`, principal-authored), Trace (`audit-trail.md`, `orientation.md`, agent append-only), and Evidence (harness-captured session records). This suite implements the Intent and Trace tiers; the Evidence tier requires a separate harness.

The files (`.acm/audit-trail.md`, `.acm/destination.md`, `.acm/orientation.md`) provide the literal storage, but the interaction of the skills with those files creates **contextual awareness**.

Memory alone is just retrieval; awareness is orientation. Because `Orient` reads the arc, `Destination` uncovers where you're heading, and `Intent` aligns the goal, the suite uses that memory to understand where it is and where it is going.

When you swap from Claude to Gpt to Gemini, the next model picks up this exact orientation. That accumulation is what makes the suite get smarter over time.

## Workflow

1. **Run:** Invoke `improve` with a concrete prompt. Without explicit delegation, Intent asks you to confirm its interpretation and Improve asks you to approve its proposed change. Each accepts Stop or Specify instead.
2. **Keep going:** Invoke `improve` again when there is more work. Improve automatically schedules Destination when broader direction needs confirmation and Orient when accumulated evidence makes the current orientation stale.

The user remembers one command: `/improve`. `/destination` and `/orient` remain manual overrides, not routine responsibilities.

After trust is earned, explicitly delegate either routine gate for one prompt or in Destination. Delegation preserves visible narration and the final change summary; it never answers Destination questions or bypasses operator-declared consequential gates. A host-wide autopilot setting does not replace this boundary.

## Quickstart (First Successful Run)

Want a copy-pasteable, 10-minute path? See [QUICKSTART.md](./QUICKSTART.md).

1. Install with one command:
   - macOS / Linux: `bash install.sh`
   - Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1`
   - ARF researchers only: add `--research` on macOS/Linux or `-Research` on Windows to include Probe.
2. In your target repo, run Improve on one concrete, verifiable task:
   - `/improve review the checkout module for waste and overburden`
3. Confirm the run produced evidence:
   - `.acm/audit-trail.md` has a new entry with outcome and delta.
4. Optional but recommended: install the pre-commit hook from the cloned suite's `harness/tools/` directory (see [QUICKSTART.md](./QUICKSTART.md)) to enforce trail discipline structurally.

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

**The deeper limitation — protocol, not structure:** The five mitigations above assume the agent follows the protocol. Skills are markdown instructions interpreted by an LLM. There is no structural guarantee that the agent writes the trail at the right moment, issues the pre-commit prediction before acting, or runs any step at all. The suite is only as reliable as the model reading it. Structural enforcement — intercepting every LLM call at the API layer, writing the ledger before the response is released to the agent, fail-closed — is the responsibility of [`llm-harness-proxy`](https://github.com/ntholm86/llm-harness-proxy) and [`ai-steward`](https://github.com/ntholm86/ai-steward). This skills suite is the behavioural scaffolding and the experiment that generated the requirement for that structural layer.

## Reference

- Convergence criterion: three independent model families report no further actionable change.
- Principles source: [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy).
- Benchmark set and replication protocol: [harness/BENCHMARKS.md](./harness/BENCHMARKS.md).

## Citation and License

MIT License.
[CITATION.cff](./CITATION.cff) | Zenodo: [10.5281/zenodo.19842994](https://doi.org/10.5281/zenodo.19842994)
