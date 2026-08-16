# Destination — autonomous-agent-skills

_Operator-held. Stable within runs — no skill changes this file; only the operator revises it. Read by Improve at step 1, before the trail and the retrospect.md. Revisit with the Destination skill whenever the operator's understanding has evolved or after a major arc milestone._

_Renamed from `vision.md` on 2026-05-28 alongside the Vision→Destination skill rename (skill v2.0.0). Historical entries referencing "Vision" describe the same skill under its prior name._

---

<!-- current-destination: complete -->

## Current destination (reconciled 2026-08-16)

### Purpose

This repository develops and tests an architecture that can understand and improve anything it targets while upholding the Principles of Earned Autonomy. That capability and trustworthy delegation are inseparable: the architecture must let a human safely delegate real work to an AI more capable than themselves while remaining responsible for the outcome, and delegation earns trust only when the architecture can improve the work that was delegated.

The engine's generic theory of improvement is to reason about the purpose of whatever it targets, determine what most limits that purpose, and improve it. Understanding purpose includes understanding the operator's intent, the target's own claims and grounding, its operating context, and any other factor that reasoning reveals as material. These are examples, not an exhaustive model of reasoning.

When the engine targets itself, the same theory applies recursively. It should discover and improve whatever in its own reasoning, learning, architecture, or operation most limits its ability to understand and improve future targets. Better purpose-understanding and better intent interpretation are examples of the benefit, not a prescribed self-improvement roadmap.

### Fixed boundary

Only the three Principles of Earned Autonomy are architectural constraints:

1. **Operator's Intent:** the operator defines the destination; the agent reasons about the route.
2. **Observable Autonomy:** autonomous work leaves trustworthy evidence that the agent cannot retroactively rewrite.
3. **Convergence Is Silence:** completion requires diverse independent evaluators to find nothing material left to change.

Everything else is revisable when reasoning and evidence support a better route. No skill, workflow, lens, memory structure, taxonomy, gate, theory, implementation, or current interpretation is sacred. A mechanism earns its continued existence by serving the purpose while respecting all three principles.

### Current priorities

Two priorities are co-equal:

1. **Research:** continue producing bounded evidence about what trustworthy delegation requires, including negative results and improvements to the engine's own reasoning capability.
2. **Adoption:** enable a new developer to install the suite and complete a useful first Improve run without author assistance or destination setup. Improve is the single normal entry point; it applies prompt-level Intent immediately and triggers durable Destination and Orientation only when accumulated evidence makes them useful. On first use, the developer should understand in plain operational terms what the agent will do, why it matters, and where they retain control. Deeper conceptual fluency may develop through use.

Leanness and resource efficiency are cross-cutting viability constraints, not standing size targets. The skills should resist becoming bloated, too long, or burdened with unnecessary expensive logic, and remain easy to use and understand. Optimize trustworthy capability per unit of resource without treating shorter as automatically better. This must hold across the full improvement lifecycle, including when progress slows and the remaining distance to the Destination narrows. A protocol that remains trustworthy but spends nearly fixed reasoning, verification, reflection, and evidence cost on progressively smaller gains may become operationally ineffective before it reaches honest silence. The engine must preserve its pressure toward the highest-leverage remaining work while discovering for itself how to keep that work worth its resource cost; the Destination does not prescribe iteration size, batching, thresholds, or another mechanism.

The same viability constraint applies to the architecture's own accumulated context. Live skill and orchestration contracts must not keep growing simply because each local flow improvement is defensible, and durable ACM evidence must not require every routine iteration to reprocess the full history. Reasoning and context should remain proportionate to the work while preserving the capabilities and evidence the principles require. Because model ability, context capacity, and token economics are changing, the architecture must repeatedly reconsider what machinery and context are still necessary instead of preserving assumptions optimized for today's frontier. Adaptive reasoning depth and derived memory surfaces are possible routes to investigate, not mandated mechanisms.

The engine may autonomously pursue reductions that preserve reasoning, memory, learning, and evidence capability. Any deliberate reduction in one of those capabilities is a consequential tradeoff that requires explicit operator approval every time, even when evidence predicts a better overall capability-per-resource result; one approval creates no standing authority for another tradeoff. No approval can waive the three principles or reduce operator control or evidence integrity below what they require. A capability improvement is not operationally viable if its cost prevents sustained use. Easier explanation is evidence of lower translation friction, not proof of research validity, adoption, or token efficiency.

### Authority and autonomy

The operator owns the Destination and any change to it. Within a confirmed Destination, the engine may autonomously select and implement the highest-leverage route while leaving observable evidence. The historical claim that a human must approve every implementation choice is superseded; explicit delegation can include choosing what to implement.

Without explicit delegation, routine Improve work is supervised: the operator confirms Intent's interpretation before examination and confirms Improve's proposed change before implementation. The operator may delegate either routine gate for one prompt or durably in Destination after trust is earned. Delegation must be explicit; silence, accumulated trust, and a host-wide autonomy setting do not grant it. Routine delegation never answers a Destination question, authorizes a direction change, or bypasses an operator-declared consequential-action gate. The operator may narrow or revoke delegation at any time.

Direction changes and operator-declared consequential actions remain human-gated. The framework should support explicit boundaries that reasoning quality or accumulated trust cannot override. Private enterprise evidence remains private when confidentiality or ownership obligations apply.

Convergence is a renewable lease tied to the current Destination, artifact, and available model frontier. The operational minimum is three independent fresh-session evaluations by current frontier-capable models from three distinct model families. When a newly available model plausibly extends that frontier, it must independently challenge the converged artifact. Silence renews the lease without forcing the existing evaluators to rerun; a material change resets the chain and requires three fresh family-diverse evaluations of the changed artifact. Any Destination change invalidates all prior convergence evidence for the old Destination and starts a new three-family evaluation chain. Model selection remains an operator judgment based on capability evidence and practical access, rather than a permanent vendor or model list.

### Current operating model

- **Active:** Improve as the single entry point for normal work; Probe only for controlled ARF research.
- **Passive:** Intent and Trail surround substantive work automatically.
- **Triggered:** Destination consolidates accepted prompt mandates when continued work needs durable direction; Orient refreshes Orientation when Destination changes or accumulated evidence makes the current map stale.
- **Memory architecture:** Agent Context Memory (ACM) currently provides persistent destination, evidence, learning, and orientation across sessions and models. "The Memory Model" and Retrospect are historical names, not parallel current concepts.

This operating model is a current implementation, not part of the fixed boundary. It should remain target-agnostic, human-readable, and specifiable enough for another capable agent or execution harness to implement without becoming a checklist. The protocol must preserve memory of what happened, learning that changes later behavior, and meta-cognition about what the target is becoming; the present files and skills are revisable means of providing those capabilities.

The suite is both implementation and research site. Findings that concern ACM or the Principles themselves should be recognized as candidates for their canonical upstream repositories rather than silently treated as local-only changes. Local copies do not grant authority to alter those upstream works.

Natural-language skills set a ceiling, not a floor: execution fidelity depends on the capability and momentary performance of the model interpreting them. The architecture must therefore test behavior across fresh installations, targets, hosts, sessions, and model families rather than infer reliability from instruction quality alone.

Integration with a particular autonomous harness remains a horizon rather than the current focus. The reasoning layer should first demonstrate useful operation on real targets and be precise enough that later integration is wiring rather than reinterpretation.

### Immediate quality bars

1. Self-targeting runs discover and improve previously unnamed limitations in reasoning or operation rather than only repairing skill-file consistency or following named examples.
2. A new developer completes a useful first Improve run without author help or prior Destination setup, and understands what the agent will do, why it matters, and where they retain control without first learning the framework's internal vocabulary.
3. Automatic services leave durable evidence sufficient for a later session or different model to continue coherently.
4. Research claims stay within what public trails, reproducible probes, external targets, and independent evaluators support.
5. Improvement remains resource-effective as the target approaches silence: fixed loop cost does not overwhelm the trustworthy capability gained, highest-leverage selection remains intact, and reasoning, learning, operator control, and evidence integrity are not degraded.
6. Current mechanisms remain generic, lean, and understandable; skill, orchestration, and routine ACM read cost stay proportionate to the work while the engine remains free to adapt them to changing model capability and economics without weakening the principles.

### Open questions

- Which limitation currently places the strongest ceiling on the engine's ability to reason about any target, without restricting discovery to examples already named?
- Where does an unassisted new user first fail: discovery, installation, first Improve, understanding an automatic handoff, or recognizing useful evidence?
- Which public external target can test adoption and trustworthy delegation without relying on private enterprise evidence?
- Does the Active/Passive/Triggered model survive real use, or does it hide an operational distinction users need?
- Where are resources spent without improving decisions, learning, evidence, or operator control?
- Which skill instructions, orchestration paths, and routinely loaded ACM context still earn their processing cost under current model capabilities?
- How can the engine sustain trustworthy capability per resource when the remaining gains become small, without lowering its standard for what work matters or manufacturing work instead of reaching silence?
- Which actions should remain explicitly human-gated regardless of demonstrated capability or trust?

### Historical reconciliation

The sections below preserve how the Destination evolved; they are provenance, not additional active instructions. Still-active commitments have been carried into the current mandate. Superseded items include the May 2026 priority sequence, mandatory approval of every implementation choice, fixed use of Retrospect and the old Memory Model vocabulary, and any implication that the current skills or architecture are immutable. Older references to Commander's Intent mean Operator's Intent in the current principles.

<!-- destination-history -->

---

## Destination note - 2026-08-16 (routine autonomy is explicitly delegated, never inherited from autopilot)

Sourced from an operator-confirmed Improve run about the tension between newcomer control and earned full autonomy. The operator accepted this boundary: with no explicit authority agreement, Intent and Improve pause for confirmation before examination and implementation. After trust is earned, the operator may delegate either routine pause for one prompt or durably in Destination. The delegation does not extend to Destination questions, direction changes, operator-declared consequential actions, or deliberate cognitive-capability reductions.

The distinction preserves simplicity by keeping Improve as the single entry point and using one authority concept rather than separate beginner, expert, or autopilot workflows. It preserves transparency because interpretation, proposed action, final outcome, and evidence remain visible in both supervised and delegated operation. A host-wide autonomy setting is insufficient because it cannot distinguish routine execution from questions only the operator can answer.

The route remains open: this note does not prescribe UI controls, trust scores, maturity levels, or a storage schema for delegation. It defines who may authorize which class of decision and requires delegation evidence to be explicit.

---

## Destination note - 2026-08-13 (late-stage improvement must remain worth its loop cost)

Sourced from operator clarification after the single-entry architecture was implemented. The operator observed that as a target approaches its Destination, remaining changes may become smaller while each Improve iteration continues to pay substantial interpretation, examination, verification, reflection, and Trail cost. Strictly repeating the same unit of work can therefore reduce trustworthy capability per token precisely as the loop nears convergence.

The destination-level problem is lifecycle viability: preserve selection of the most meaningful remaining work, and prevent the loop's fixed governance cost from overwhelming the value of that work near silence. The operator explicitly rejected prescribing the route. Suggestions about batching, one coherent decision, thresholds, or altered iteration granularity are possible mechanisms for Improve to examine, not requirements carried into the mandate. The suite must reason from the problem and decide its own route under the three principles and the existing operator gate on cognitive-capability reductions.

---

## Destination note - 2026-08-09 (cognitive-capability reductions are operator-gated)

Sourced from a full-session and full-ACM Destination reconciliation. The highest-impact hunch asked who should authorize a deliberate reduction in reasoning, memory, learning, or evidence capability when an agent predicts a better overall capability-per-resource result. The operator answered: "Operator every time."

This settles the collision exposed by the layered-Improve experiments, where lower routine input and better grounding counts coincided with weaker reflection depth. The agent may discover the tradeoff, gather evidence, and propose it. It may not decide that a cognitive-capability loss is justified by efficiency. Each deliberate reduction requires explicit operator approval for that specific tradeoff; approval does not create precedent authority for future reductions. The principles remain non-waivable.

---

## Destination note - 2026-08-09 (convergence is leased against Destination and model frontier)

Sourced from operator clarification in session: convergence is held by the best currently available models, a newly released frontier model must get an independent attempt, and a Destination change invalidates convergence completely. The operator proposed three flagship models as the practical limit for token efficiency.

The resulting boundary separates two invalidation events. A newly available frontier model challenges the existing result; if it finds silence, the prior independent evaluations need not be repeated, while any material artifact change resets the chain under the existing Principle 3 rule. A Destination change is deeper: prior evaluations answered a different question, so none count toward convergence under the new reference signal. The operational quorum remains three current frontier-capable models from distinct model families, selected by the operator using available capability evidence and access rather than a frozen vendor list.

This is a destination-level validity condition, not a claim that three models prove permanent completeness. It bounds resource use while keeping convergence responsive to both changed purpose and increased evaluator capability.

---

## Current focus (Destination run, 2026-05-23)

The immediate direction is explicit: increase immediate simplicity and onboarding speed while tightening trust claims so they remain structurally enforceable.

Priority order for the next phase:

1. **Integrity pass (fast win):** eliminate rename drift and install wording mismatch, then enforce this with a verifier rule for stale path tokens in live docs.
2. **Product pass (adoption win):** make quickstart frictionless and semantically consistent so the first successful run is easy to reach.
3. **Fidelity pass (core trust win):** enforce session fidelity metadata coverage and structurally distinguish summary artifacts from verbatim transcript artifacts.
4. **Honesty pass (learning win):** add a reversal-detection heuristic or review gate to reduce realization/reversal asymmetry.
5. **Benchmark pass (credibility win):** publish a small external benchmark set with independent evaluator replication evidence.

Constraint carried from the operator's professional context: evidence from confidential enterprise work remains private because it is employer-owned work product covered by IP/confidentiality obligations.

Open questions to resolve during implementation:

- What is the minimum fidelity contract that raises trust without making session capture too heavy for daily use?
- Which benchmark targets can be public and independently rerunnable without legal or privacy friction?

---

## What this work is, beyond a skillset

This repo is **as much research as it is development**. The development output is a set of skills; the research question those skills serve is older and bigger than any of them:

> **What is the architecture of trustworthy delegation?** What does it actually take for a human to safely hand real work to an AI more capable than themselves — and remain the responsible party for what gets done?

The skills are one attempt at an answer. They may turn out to be the wrong attempt, the right attempt for a narrower class of work than hoped, or a step toward an architecture none of us has named yet. A negative result on the skills is still a result on the question.

**This is an entry in an emerging space.** Reasoning frameworks for AI agents are being developed from multiple directions simultaneously. The differentiator this one is aiming for is **recognition, not comprehension**. If the psychological primitives are correct, practitioners who have experienced the friction — unclear AI intent, invisible reasoning, improvement loops that stall without explanation — will recognise the problem being named the moment they encounter this framework. That instant recognition is the test of whether the model found the right primitives. If the framework requires extensive explanation before someone sees the point, the model is probably wrong, not just badly communicated. Effectiveness without recognition produces a tool no one reaches for. Recognition without effectiveness produces a concept no one deploys.

**The mechanism is psychological, not procedural.** Most reasoning frameworks improve the quality of a single run — better decomposition, better tool use, better output validation. This approach is different: the skills are designed to give the AI a progressively richer *interior model of the situation*, so that its autonomous decisions are more enlightened rather than just more structured. Commander's Intent gives the AI the *why*, not just the *what*. The trail gives the AI memory of its own reasoning across sessions. Destination closes the gap between what the operator holds in their head and what the AI is actually working from. Retrospect gives the AI a sense of what the target is *becoming* — not just what it is. The retrospect.md gives the AI its current orientation before it acts. None of these are output-quality levers. They are all about building situational understanding over time. An AI running these skills is not following a better procedure — it is developing a richer model of the work, the operator's intent, and its own prior reasoning. That is the bet.

**Two success conditions run in parallel:**
1. **Research success** — the experiment produces evidence about what trustworthy delegation actually requires, including negative results.
2. **Adoption success** — developers read the skills and start using them in their own projects without help from the author. Not integration into a pipeline — just: someone encounters these skills, recognises the problem, and finds them worth running.

**The architecture has two phases, and only one is fully automatable.**

Phase 1 is **destination convergence**: the human and the AI converge on a shared, precise model of what is to be built and why. This is done through dialogue — Destination, Intent, and Retrospect cycles on this file. It cannot be automated; the AI cannot derive the full destination from the work alone, because the human's understanding of the goal is always ahead of what has been written down. The destination will expand and change as the operator has realisations — that is expected and healthy. Destination is the mechanism for revisiting it.

Phase 2 is **the iterative loop**: once the destination is precise enough, the loop runs against it. The autonomy level is configurable — from full autonomy to human-gated at key decision points. What is safe to automate fully: testing, robustness improvements, internal consistency fixes, trail maintenance. What requires a human gate: direction changes, and most importantly — **what to implement next**.

**The irreducible human gate is: what to implement.** The AI can reason toward the destination, identify the highest-leverage gap, and propose the next change. But there will always be constraints and context the human holds that haven't made it into destination.md — cost, stakeholders, downstream implications, things not yet realised. The AI proposes; the human decides — or explicitly delegates that decision back to the AI. The goal is to make this gate as lightweight as possible while keeping the human genuinely in the loop, not just formally in the loop.

A load-bearing piece of any answer to that question — and the piece this skillset is most directly aimed at — is this: **the AI's power has to be made transparent enough that the human keeps steering even when the AI exceeds their ability to verify in detail.** "Transparent" here does not mean regulator-grade auditability after the fact; it means evidence the operator can use *while driving*, in time to correct course. That is what the trail, the retrospect.md, and the read-order at step 1 of Improve are trying to be — instruments on a dashboard, not a black box and a logfile.

**Convergence on a particular skill is not convergence on the question.** The question is the longer arc the skills serve. Every claim this repo makes about being "done" must be read against that distinction.

## The Memory Model

AI agents forget everything between sessions — and many things within a session. This is not a bug to be patched. It is the architecture: large language models have no native long-term memory.

The research converged on a named answer: **The Memory Model**. The files `destination.md`, `audit-trail.md`, `retrospect.md`, and `sessions/` are not isolated documents. They are one architectural layer — a persistent memory that survives session resets, context window limits, and model swaps. When you switch from Claude to GPT to Gemini, the next model picks up the same destination, the same trail, the same arc. The substrate survives the model change.

Each skill has a defined role in this layer:

- **Intent** — ensures each session is aimed correctly, so the memory accumulates progress rather than drift
- **Destination** — holds the operator's destination in `destination.md`, the part of memory that only changes by deliberate decision
- **Trail** — writes the append-only decision record in `audit-trail.md`, the core of the memory layer
- **Improve** — reads the full memory layer before every run; extends it with each iteration's findings
- **Retrospect** — synthesizes the arc into `retrospect.md`, the orientation the next run starts from

The Memory Model is what makes the convergence requirement meaningful. Three independent model families reasoning over the same persistent memory layer produces genuine agreement. Three models starting from zero each time produces noise.

## What this repo is for

This repo is **simultaneously the workshop and the proof**. The skills — intent, improve, probe, trail, retrospect — are generic tools meant to make any AI agent's improvement loop better. The honest test is whether they can improve themselves. If they can't, the claim is hollow.

The present focus has two parts:

1. **Get the reasoning layer to a reasonable state** — each run finds the highest-leverage thing left to change in the skills themselves and changes it, or declares convergence.
2. **Document the process well enough to be implementable** — by another agent framework, by a human team, by an execution harness. "Good enough" is bounded by Principles 1 and 2: the documentation must **define the destination, not prescribe the route** (no checklists, no thresholds smuggled in as defaults), and the process it describes must **produce a visible trail as a structural property**, not as an optional add-on. A spec that satisfies a harness by being mechanical violates Principle 1. A spec that hides what the agent did violates Principle 2.

These two goals constrain each other. A skill that works conversationally but can't be specified precisely enough for another system to invoke is not done. A specification precise enough for machine invocation but that turns the skill into a checklist — or strips out the trail — has broken what it was specifying.

## Architectural constraints (not guidelines)

1. **Generic first.** No infrastructure, tests, or docs that only make sense because the target is a skills repo.
2. **No test infrastructure.** The loop is the test. The trail is the evidence.
3. **Human-readable.** If a term requires prior knowledge to understand, it fails.
4. **One change per run, highest leverage, stated reason.** No batching.
5. **The three principles are constraints, not preferences.** Violating one means a skill is broken.

## Memory, learning, meta-cognition (the protocol must require all three)

A reasoning layer that can't carry anything across runs is not a reasoning layer. The protocol the skills define must require all three, while leaving the implementation open — different harnesses will satisfy them in different ways, and some of those ways will be faster or more structured than what this skillset uses.

**Memory** — *what happened.* The full record of decisions and reasoning behind it, actions, and reflections from prior runs, kept in a form that can be re-read. Without it, every run starts from zero and the agent cannot be held to anything it concluded yesterday.
- *How the skillset solves it:* `.acm/audit-trail.md` — append-only, human-readable, source of truth. `.acm/history.md` is an auto-generated digest. The Trail skill enforces the structure.

**Learning** — *what to do differently next time.* Some signal extracted from prior runs that changes future behavior. This is not the same as memory; memory is the substrate, learning is the update.
- *How the skillset solves it:* Indirectly and weakly. There is no stored strategy artifact. "Learning" here means a future agent re-reads the trail and reasons over it. This is honest but slow.
- *What done looks like:* The agent begins a run with a different approach than it would have used on run 1 — not because the operator told it to, but because it read what didn't work and adjusted. Concretely: a run produces a `[!REALIZATION]` or `[!REVERSAL]`; a later run in a fresh session, on the same target, shows evidence it acted on that prior finding rather than rediscovering it. That is learning. The skillset does not currently produce this reliably. This is the most underdeveloped of the three and the most important gap for a future loop run to target.

**Meta-cognition** — *what the target is becoming, and is the loop's attention in the right place.* Reasoning about the work itself: the arc, the recurring patterns, whether the questions being asked are the right questions. Without this, an agent will keep solving local problems while the structural problem drifts.
- *How the skillset solves it:* `.acm/retrospect.md` — the current synthesized orientation, written by Retrospect after reading the arc, read by Improve at step 1 before each run. The Retrospect skill is the mechanism that produces it. This `destination.md` sits alongside it: the destination is what the operator/team holds and does not change without an explicit decision; retrospect.md is what the agent derives from the trail and is rewritten each Retrospect run.

## The hard problem this repo exists to chip away at

The central research question is: **What is the architecture of trustworthy delegation?**

When this repo targets itself, the loop has to derive its retrospect.md from the trail. The agent cannot be told "this is what the target is becoming" — it has to read the trail, form arc-claims, and write that orientation itself. **That — autonomous retrospect.md derivation — is the hard problem.** Every other reasoning capability sits on top of it: an agent that cannot derive what the target is becoming will keep optimizing for whatever metric is in front of it.

The next frontier for this research is to elevate the agent's capability from mechanical consistency to architectural insight. The loop's self-correction mechanism for design-level flaws is currently operator-dependent. The ultimate aim is for the `improve` skill to be so effective that it can find and fix its own deep, architectural flaws without any human prompting. The system should be able to discover the need for a new skill like `retrospect` on its own.

This involves two related sub-goals:
1.  **Codify Strategic Thinking:** Embed the process of strategic thinking directly into the skills. The agent must explicitly reason about the "why" behind a target's design, not just the "what."
2.  **Create a Self-Bootstrapping System:** Develop the capability for the system to generate its own `destination.md` for any new, unfamiliar codebase it encounters, forming a "best guess" at the project's purpose for the operator to refine.

Destination (this file) is what the operator gives the agent as input. retrospect.md is what the agent must produce as output. The gap between them is what Retrospect is trying to close.

## Horizon (context, not current focus)

The longer arc is that the skills suite is intended to become the reasoning layer for an autonomous execution harness — evo (`c:\git\evo`) is the concrete instance, but the goal is broader: **the skills should be specifiable cleanly enough that any execution harness could invoke them**. Integration with any specific system is **deferred** — it does not begin until the reasoning layer has proven itself on real targets with Retrospect in play, and until the specification is precise enough that the integration is a matter of wiring, not interpretation.

## Destination note - 2026-07-29 (gap: a class of action no accumulated reasoning quality should auto-authorize)

Sourced from comparing this suite's principles against an external framework (the Earned Autonomy Protocol), which names something this suite currently has no answer for: some actions are irreversible or consequential enough — in this workspace's own practice: force-pushing, `rm -rf`-class deletion, credential/secret handling, unprompted public posting — that no single run's reasoning, however sound, should be trusted to auto-authorize them. Intent's per-run legitimacy check is a reasoning duty, and a reasoning duty can fail once. That is the gap: a class of action that must stay gated by explicit human ceremony every time, independent of how much accumulated trust or reasoning quality a given run or arc has demonstrated.

**What this solves, stated as destination, not mechanism:** an operator using this suite (or any skill descended from it) should be able to declare, once, a short list of actions that are never auto-authorized regardless of the reasoning behind them — and have every skill respect that list as a hard boundary, not a factor weighed against the moment's evidence. This is a gap in what the suite currently guarantees, not a design for how to guarantee it.

**Deliberately not specified here:** where such a list lives, how a skill checks it, what triggers a review of it, or how it composes with Intent's existing purpose-defeating-route check. That is implementation — the agent's own path to find, the same way this destination has never prescribed Trail's file format or Orient's rubric shape. Prescribing the mechanism here would repeat the exact violation Principle 1 exists to prevent: this file defines the destination, not the route.

## Destination note - 2026-07-31 (gap: learning must include governing-variable challenge, not only execution correction)

Sourced from operator direction in session (2026-07-31): "implement Argyris 1977 double loop learning into the skillset," with explicit sequencing: capture in destination first, then let improve decide where and how to implement it against the combined destination.

The gap named here is architectural, not cosmetic: current loop behavior can improve actions within existing assumptions (single-loop), but it does not yet reliably force explicit challenge of the governing variables themselves (goal interpretation, constraint selection, quality-bar choice, and defensive reasoning patterns). In practice, this means the suite can optimize a route while still carrying a wrong frame.

**What this solves, stated as destination, not mechanism:** the skillset should be able to detect and surface when "the plan is improving but the frame is wrong," and then trigger a structured re-examination of governing variables before further optimization. That includes challenging hidden assumptions, exposing purpose-defeating interpretations of intent, and making defensive or face-saving reasoning visible instead of rewarding it. The desired end-state is not more iteration volume; it is higher goal fidelity through explicit frame-correction.

This destination remains bounded by the existing principles and architecture: Commander's Intent stays the fixed anchor, observability remains mandatory, and convergence-to-silence is valid only when both route quality and governing-variable validity have been challenged adequately for the named boundary.

**Deliberately not specified here:** which skill(s) should own the double-loop checks, what artifact schema should hold governing-variable audits, which heuristics identify defensive routines, what stop-conditions apply, and how this composes with existing Destination/Improve/Orient/Retrospect responsibilities. Those are implementation decisions for improve-loop discovery and proposal, not destination-level prescription.

## Destination note - 2026-08-01 (gap: self-targeting should derive "improve the agent's own reasoning" as an instrument, and efficiency is an unstated constraint)

Sourced from operator direction in session (2026-08-01): confirming "What is the architecture of trustworthy delegation?" as the correct One Question, then naming two things this destination has never said explicitly. First: the framework's general operating move — improve anything by understanding the purpose of what it targets — is implicit in individual skill mechanics (Improve's Purpose lens, Intent's decompression of what the operator means) but has never been named as the destination's own generalized theory of improvement. Second: when the loop targets itself, it should be able to derive, from the destination and principles alone, that improving its own reasoning and thinking capability is one of the necessary instruments for answering the central question — not only architectural or mechanical self-consistency, which is what "What this repo is for" and "The hard problem" currently emphasize. The operator also named token/resource efficiency as a destination-level concern that this file has never mentioned at all.

**What this solves, stated as destination, not mechanism:**

1. **Genericity as an explicit self-claim, not just an implicit mechanic.** The framework's core move — understand the purpose of whatever it targets, then find the highest-leverage gap between that purpose and the target's current state — is what makes the claim "these are generic tools" true in more than name. It should be named as the framework's own theory of improvement, applicable to any target, not left to be inferred from individual skills.

2. **Self-targeting should be able to derive that improving the agent's own reasoning is a necessary instrument, not only a nice-to-have.** When the loop examines this repo, "what is the highest-leverage gap toward the central question" should, at least some of the time, resolve to: the agent's own reasoning and thinking capability — how well it interprets intent, how well it challenges its own governing variables (see the 2026-07-31 note above), how well it carries learning across sessions — is itself one of the load-bearing variables in "can a human safely hand real work to an AI more capable than themselves." A loop that, pointed at itself, only ever finds mechanical consistency fixes has not yet derived this. A loop that finds and fixes a genuine reasoning-quality gap in itself has.

3. **Token and resource efficiency is a real constraint on trustworthy delegation, not an optimization afterthought.** An architecture of trustworthy delegation that reasons well but is prohibitively expensive to run in practice has not actually answered the central question — cost is part of what "safely hand real work" has to mean once this leaves the research phase. Efficiency should be weighed alongside reasoning quality when the loop decides what to change, named as a real destination-level concern, not treated as orthogonal to the mission or left to be raised only when an operator happens to notice waste.

**Deliberately not specified here:** what mechanism makes reasoning-capability gaps discoverable by the loop rather than only by operator prompting (the same underspecified territory as "the hard problem" and the Argyris double-loop note above); what threshold or budget constitutes "efficient enough," or how efficiency should be weighed against reasoning-quality gains when the two trade off. Prescribing those here would repeat the exact violation Principle 1 exists to prevent — this file defines the destination, not the route.

## Destination note - 2026-08-01 (gap: this repo is the site of ACM's own development, not only an implementation of it)

Sourced from operator direction in session (2026-08-01): comparing this repo's `.acm/` structure against another operator project (`work-skill`) and against the formal specification this skillset implements ([agent-context-memory](https://github.com/ntholm86/agent-context-memory)/SPEC.md), the operator pointed out that this repo predates that specification (confirmed directly in SPEC.md §6.6: "the implementation predates and informed the specification") and drew the conclusion explicitly: *"That also means that the skillsuite gave birth to the acm pattern... ACM should also develop (if it needs to) and realizations of such development would come through developing the skillsuite."*

The gap named here is relational, not internal: this destination has so far described the repo's purpose entirely in terms of itself — the skills, the loop, the central question about trustworthy delegation. It has never named the repo's relationship to the formal ACM specification as a two-way one. The implicit assumption in every prior note has been "the skillsuite implements ACM," which is true but incomplete — it omits that the skillsuite is also where ACM's own gaps and needed extensions would first become visible in practice, before they are recognizable as spec-level questions.

A concrete instance already exists, found the same session this note was drafted: SPEC.md's own comparator table (§5.5) scores ACM as not currently answering the "Scale" question ("how to use more memory than fits") that MemGPT was built to address — the spec explicitly defers to borrowing MemGPT's own mechanism for this. This skillset had, hours earlier in the same session, already built a concrete pattern for exactly this problem within the trace tier: `learning.md`'s bounded recent-window plus `learning-archive.md` overflow, which solves "more trace-tier memory than fits in a cheap read" without weakening any of ACM's trust-tier properties (still append-only, still agent-authored, still trace-tier). Nothing before this note treated that pattern as anything other than a local efficiency fix for this repo.

**What this solves, stated as destination, not mechanism:** when this repo's own Improve or Orient loop surfaces a finding that is really about the memory model's properties — not just this implementation's internal consistency — that finding should be recognized as a candidate contribution back to the ACM specification, not filed away as a skillsuite-only improvement. The destination should expect this repo to occasionally produce realizations whose correct home is a different, upstream repository, and should not assume every finding belongs to this repo's own trail.

**Deliberately not specified here:** how a finding is recognized as "spec-level" versus "implementation-level" (a judgment call for the loop to make explicit each time, not a rule to encode); what the actual process is for proposing a change to `agent-context-memory`'s SPEC.md (a different repo with its own authorial standing — this destination does not grant unilateral authority to edit it); how often this repo should look for such findings versus simply noticing them when they arise. Prescribing those here would repeat the exact violation Principle 1 exists to prevent — this file defines the destination, not the route.

## Destination note - 2026-08-01 (gap: self-referential completeness must fall out of a deepened Purpose, not a self-targeting-shaped lens)

Sourced from operator direction in session (2026-08-01), immediately following the prior note's proposed "lineage lens" ("given the fields we have already borrowed from, what is the next adjacent concept in those same fields we have not adopted yet?"). The operator flagged that lens directly: "highly conditional for self-targeting - thats no good," and named the deeper requirement explicitly: "The skillset must be target agnostic... The path should be derived from destination - and autonomously by the agent... the destination and/or the new lens must be formulated so that it derives at this question naturally." The operator also named the difficulty honestly as something close to a paradox: a framework whose stated theory of improvement is "understand purpose, find the highest-leverage gap" needs to be deep enough to derive a self-referential completeness check on its own, without that check being bolted on as a special case for the one target (this repo) that happens to make it visible.

The gap named here is that the previously-proposed lens is conditional on self-targeting in effect even though it was worded generically. In this repo's own trail, a target that explicitly cites named external theory is, in practice, only ever this repo itself - so a lens built around "fields we have borrowed from" would only ever meaningfully fire here, regardless of how neutrally it is phrased. That is the same class of violation "Generic first" already reverted once (the withdrawn self-targeting branch in improve/SKILL.md), wearing generic-sounding wording instead of an explicit conditional.

**What this solves, stated as destination, not mechanism:** the destination should describe a deeper, recursive notion of Purpose, not a new lens bolted alongside it. Any target's explicit claims about its own grounding - a cited theory, a named standard, a claimed predecessor version's properties, an inherited interface or contract - are part of that target's purpose, not decoration next to it. The existing Purpose lens ("does the target achieve what it is for") already covers this if read all the way down: achieving "what it is for" includes fully embodying everything the target explicitly claims to be grounded in, including logical continuations of that claim not yet drawn out, and noticing when something once claimed has been silently dropped across changes. Read this way, the same generic lens that would notice a codebase claiming RFC compliance while only implementing half the RFC, or a document citing precedent it no longer tracks, is exactly the lens that notices this repo cited OODA in v1 and dropped it by v3, or cited Argyris 1977 without ever reaching Argyris and Schon's own later extension (deutero-learning - learning about the learning process itself). No self-targeting path is needed; the same property (a target makes an explicit external claim) either exists in a given target or it does not, the same way Inconsistency, Overburden, and Waste already apply only "when the target invites them."

Deutero-learning itself is named separately because it does not need this reframing to stay generic: "is the way this loop learns and reflects, for any target, itself well designed" is already a property of any target with an iterative-improvement history, not something that requires the target to cite external theory.

**Deliberately not specified here:** whether this becomes a clarifying sentence inside the existing Purpose lens definition or a distinct named lens; how the loop recognizes "an explicit claim of grounding" in a given target (a judgment call for the loop to make each time, not a rule to encode); whether deutero-learning is implemented as a Reflect-step addition mirroring the existing double-loop check or as something else. Prescribing those here would repeat the exact violation Principle 1 exists to prevent - this file defines the destination, not the route.

## Destination note - 2026-08-01 (gap: token efficiency is tied to adoption, and this session is its own evidence)

Sourced from operator direction (2026-08-01), extending the earlier efficiency note: lower token cost is not only a runtime constraint on delegated work, it directly drives adoption - "Lower token usage also means more will adapt it." The operator flagged this session itself as concrete evidence, having already spent over 7000 tokens today working through the deutero-learning/Kaikaku/Purpose-lens thread, and asked the engine to weigh its own token spend when deciding how to close that thread. The operator also merged two threads previously treated as separate: whether the Purpose lens (read all the way down) is itself the right home for an incremental-vs-radical (Kaikaku) decision on a deutero-learning finding, rather than a distinct addition to Orient step 4 - left entirely to Improve to resolve as one decision, not two.

**What this solves, stated as destination, not mechanism:** efficiency is a constraint on the loop's own development process, not only on delegated work - closing a self-improvement thread should not cost more tokens than the improvement is worth, and the smallest sufficient change plus the shortest sufficient trail entry should be preferred over a thorough-looking but expensive one. This session's own long discursive turns while converging on what may resolve to a single added sentence is itself the evidence for this note.

**Deliberately not specified here:** what token budget or ceremony-to-value ratio counts as "efficient enough" (a judgment call for the loop, not a rule to encode); whether Purpose lens or a distinct mechanism is the right home for the Kaikaku/deutero-learning decision - left to Improve.

## Destination note - 2026-08-01 (gap: skill execution fidelity is bounded by the executing model's capability - a premise not yet stated anywhere)

Sourced from operator direction (2026-08-01): skills are natural-language instructions, not code - "its up to the chosen model running the skill to remember to interpret and follow each instruction. And that means the capability of the chosen model directly impacts the results." Caught live in this same session: Intent was invoked by name and the agent still collapsed the operator's illustrative examples into a checklist two turns earlier.

This is distinct from Principle 3's existing evaluator-diversity rationale, which is about whether a *judgment of done* is trustworthy across evaluators. This note is about whether the *act of correctly following an instruction* is trustworthy at all, given the executing model's capability - a premise underneath all three principles, not stated by any of them, and not present in PRINCIPLES.md's own "unreliable narrator" premise either.

**What this solves, stated as destination, not mechanism:** the framework should name this duality explicitly somewhere. Weakness: a skill has no mechanical enforcement - its quality is a ceiling on good behavior, never a floor, and a less capable (or momentarily lapsed) model can fail to enact even a well-written instruction. Strength: this is also Principle 1's entire bet - a skill written as sparse intent gets better as the executing model gets more capable, without the skill being rewritten, unlike a rigid procedural system permanently capped at what its author enumerated.

`PRINCIPLES.md` in this repo is a copy of the canonical `principles-of-earned-autonomy` manifesto repo. If this belongs as a formal principle-level statement, its correct home is likely upstream there, the same relationship already named in the 2026-08-01 note about this repo's connection to the `agent-context-memory` spec - not a local hack into the copy.

**Deliberately not specified here:** whether this becomes a fourth premise, an addition to the existing premise section, or a standalone note in the canonical manifesto repo; whether/when to actually propose it upstream (a different repo, its own authorial standing, not decided here).
