# A stance on what we're actually trying to solve

_Author: Nils Holmager ([@ntholm86](https://github.com/ntholm86)). Version 0.1, 2026-05-01. This is a stance, not a paper. It states what I'm betting on, where I think it differs from adjacent work, and what would prove me wrong._

---

## The situation, in plain language

You're using an AI agent that can do things you can't fully verify. Maybe it's writing code in a framework you're rusty in. Maybe it's refactoring across a codebase larger than you can hold in your head. Maybe it's making a sequence of small judgment calls — naming, structuring, choosing between two reasonable approaches — at a rate you couldn't review even if you tried.

You are still responsible for the outcome.

Two stances are common, and both are wrong.

**Stance one:** "I'll just review everything." You can't. Not at the rate the agent produces it, not in the depth that would actually catch the mistakes that matter. This stance scales until it doesn't, and the moment it stops scaling is the moment you start rubber-stamping.

**Stance two:** "The agent is good enough, I'll trust the outputs." Sometimes true. But "good enough" is not a property of the agent — it's a property of the agent *on this task, this codebase, this day, with this framing.* You don't know in advance which runs are the ones where it's wrong in a way that will cost you. By the time you find out, it's downstream of you.

The interesting question is not which stance is right. Both are evasions. The interesting question is:

> **What does it actually take for a human to safely hand real work to an AI more capable than themselves on that work — and remain the responsible party for what gets done?**

That question is older than the current AI wave. It has answers in aviation (autopilot), in surgery (robotic assistance), in finance (algorithmic execution). What's new is that the AI is now a generalist, the work is open-ended, and the verification gap can be arbitrarily large at the moment of decision. Nothing in the older domains transfers cleanly.

I don't think this question is being addressed head-on. Pieces of it are. The whole thing is not.

## Why the existing labels miss it

The relevant adjacent fields:

- **AI oversight / scalable oversight** — Anthropic, ARC Evals, METR. Asks: can humans supervise systems that exceed them? Mostly framed at *training time* (debate, weak-to-strong, recursive reward modeling) and *evaluation time*. Treats oversight as a regulator-grade activity. Closest in spirit; wrong layer for the situation I described.
- **Agentic AI safety / agent governance** — Shavit et al. ("Practices for Governing Agentic AI Systems"), Chan et al. ("Visibility into AI Agents"). Asks: how do we keep autonomous agents accountable? Concerned with traceability, but the audience for that traceability is institutional — auditors, policy. Not the operator at the wheel.
- **Human-in-the-loop / human-AI collaboration** — long HCI tradition. Mostly assumes the human is at least the AI's equal on the task. The asymmetric case — AI more capable, human still responsible — is rarely the central case.
- **Constitutional AI, Model Spec** — specify what the AI should *do.* Not how the human stays *responsible* for what it did.
- **SRE / observability / postmortem culture** — Allspaw, Google SRE. Closest in *form* (structured traces, evidence-driven review) but the motivation is system reliability, not delegation under capability asymmetry.
- **Restriction-first AI governance** — the dominant paradigm in AI governance frameworks emerging 2024–2026: trust is produced by constraining what an AI can decide and do. Allowed-states constraints, execution-bound authorization, sandboxing, deterministic policy enforcement, separation of probabilistic advisory components from decision authority. The conceptual pair is *safety ↔ restriction*: more autonomy requires more constraint. This paradigm is not wrong for what it addresses — blast-radius containment and deterministic policy enforcement are real needs. But it carries an inherent cost: as AI capability grows, the paradigm treats increased capability as increased risk, which demands increased restriction. The result is a capability ceiling — not as an incidental side effect but as a structural consequence of using restriction as the primary trust instrument. ARF operates on a different conceptual pair: *safety ↔ demonstrated reasoning quality*. If you can verify that an agent is genuinely reasoning — and that the reasoning is situationally genuine rather than templated — you do not need to restrict its capability to trust it. Capability growth becomes an argument *for* trust rather than an argument for more constraint. These are not competing answers to the same question; they are answers to different questions. Restriction-first governs what AI can do. ARF qualifies whether the AI's reasoning is genuine enough to trust what it does. (IFA Core Specification v1.0, Harcej, February 2026, is one published formalization of the restriction-first paradigm.)

None of these are wrong. They're all working on related problems. But the *operator-at-the-wheel-of-a-more-capable-system, in real time, while the run is happening* problem is not where most of the energy is. It tends to be assumed away in two directions: either the human is treated as a regulator who reviews after the fact, or the human is treated as a pair-programmer who is the AI's equal.

I think there's a real problem in the middle they're collectively under-serving. I want to give it a name and bet on it.

## The name and what it means

I'll call it **operation-time trustworthy delegation**.

Four sub-claims define the stance:

**1. Operation-time, not training-time or evaluation-time.** The interesting decisions happen while the agent is running, not during training and not during a separate evaluation pass. The instrumentation has to work *during the run*, not as a retrospective audit. If you can only see what happened after the fact, you can't steer.

**2. Delegation, not control or supervision.** "Control" implies you can intervene at every step. You can't, and even trying degrades the value of using a more-capable agent. "Supervision" implies a regulator stance. The interesting stance is *delegation* — you've handed real work to a more-capable party and remain on the hook for the outcome. That is a different relationship than supervisor-to-subordinate.

**3. Evidence-while-driving, not audit-after-the-fact.** The output the operator needs is not a log they could in principle reconstruct from. It's a dashboard — instruments calibrated for the operator's bandwidth and their authority to course-correct *before the run finishes.* The trail has to be readable in time to matter.

**4. Protocol, not tool.** The artifact that solves this should be specifiable cleanly enough that any execution harness — not just the one I built — can implement it. If the answer is "use my framework," the answer is wrong. The answer has to be something a competent team could re-implement in their own stack from a spec.

That four-part stance is what I mean by the term. It's also the boundary: a contribution that satisfies one or two of these and drops the rest is doing something interesting but not this thing.

## What I'm doing about it

I'm building a small set of skills — currently six, version 3.11.0 — that an AI agent applies to its own work. The skills are: **intent** (interpret the operator's intent before acting), **improve** (one highest-leverage change per run, stated reason), **probe** (test reasoning vs. pattern-matching), **trail** (append-only structured evidence per run), **orient** (read the arc of the trail and synthesize current orientation), and **destination** (surface guesses the agent has formed about where the operator is heading, as falsifiable questions; renamed from "vision" in v2.0.0 of this skill).

The skills sit on top of three principles I've published separately ([Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy)): Operator's Intent (define destination, not route), Observable Autonomy (autonomy is a function of transparency), and Convergence Is Silence (you're done when independent evaluators find nothing left to change).

The repo where the skills live is **simultaneously the workshop and the proof**. The skills have to be able to improve themselves; if they can't, the claim that they're a usable reasoning layer is hollow. Each run finds the highest-leverage thing left to change in the skills themselves and changes it — or argues for convergence.

The workshop-and-proof setup is honest about its own limits. It's incestuous: same author, same lineage, no real external test yet. Any claim the skills make about generality is provisional until the protocol gets exercised by a harness that didn't co-evolve with it.

## What I'm not claiming

I want to be precise about what is and isn't on the table.

- **I'm not claiming the skills are the answer.** They are *one attempt* at the answer. They may be the wrong attempt. They may be the right attempt for a narrower class of work than I hope.
- **I'm not claiming the protocol is finished.** The current version is 3.x. The destination/orientation.md split is two weeks old. The destination skill (originally named Vision) was added this week. Most of the protocol is unproven in execution.
- **I'm not claiming this solves AI safety.** It doesn't. It addresses one slice — the slice where a willing operator with real authority is delegating to a real agent, in real time, on a real task. Many of the harder safety problems sit outside that slice.
- **I'm not claiming originality on the components.** Trails are standard. Mission-type command is Prussian. Independent multi-evaluator convergence is older than I am. The bet is on the combination and the framing of *what they're collectively trying to solve.*

## What would prove this wrong

A stance without falsification is a manifesto. Here's what I'd take as serious evidence the bet is wrong:

1. **The protocol cannot be implemented by a harness that didn't co-evolve with it.** If after one or two honest external attempts, the spec turns out to require so much interpretation that it isn't really a spec, the "protocol not tool" claim is false. The skills become a framework. That's a smaller, less interesting result.
2. **Operators don't actually use the trail in real time.** If when given a working multi-resolution trail, operators only ever consult it after the fact, then "evidence-while-driving" is a story I told and not a thing humans actually do. The dashboard metaphor breaks down. The result might still be useful for audit, but the central claim collapses.
3. **The capability gap eats it.** If the protocol works at 1-2 capability steps of asymmetry (operator can verify if they squint hard) and breaks down at 5+ steps (operator cannot verify even with effort), then it's a tool for *narrow* delegation, not the trustworthy-delegation question I framed. Still useful; not what I'm betting on.
4. **A diverse evaluator panel can't agree the protocol-driven runs are different from the non-protocol runs.** Convergence Is Silence is the validation mechanism. If multiple independent evaluators looking at runs done with and without the protocol can't tell them apart on the dimensions that matter, the protocol isn't doing the work I think it's doing.
5. **The right unit of analysis is somewhere else entirely.** Maybe trustworthy delegation isn't about per-run instrumentation; maybe it's about organizational structure, contract design, or post-incident learning systems. If after engaging with the adjacent fields someone can show me the locus is elsewhere, I'd rather know than persist.

I don't expect all of these to come back negative. I expect at least one to. That's the point of stating them up front.

## What the runs are showing

_Added 2026-05-02. This section is updated as evidence accumulates._

The Destination skill (originally named Vision) was the first mechanism in the protocol to produce something the operator had not written down before the run. Four runs in a single session, each on a different target, each at a different level of prior context:

1. **Own destination paragraph.** The operator wrote a paragraph about the repo's direction. Destination read it and surfaced a latent intent the operator hadn't stated directly. Confirmed.
2. **Known target with history (evo).** A repo the operator knows deeply, with an existing trail. Destination surfaced three direction and constraint hunches from the trail arc. All three confirmed.
3. **Cold foreign target (vectorium).** A repo not discussed in the session, no `.acm/`, no destination, no priming. Signal came entirely from code structure, git commit arc, and package.json. The first hunch surfaced "lost interest after beating the benchmark" — not written anywhere in the repo, inferred from the commit arc alone (performance climbs to a peak, then cleaning commits, then silence). Confirmed.
4. **Production system with trail history (leifoglenedk).** A live driving school management system with three prior improvement runs in the trail. Destination surfaced the dual-role tension (production vs. practice target), the reason P0 security work was blocked, and the sequencing logic behind the three runs. All three confirmed.

5. **Confidential enterprise deployment (professional work).** I used this skillset in a real enterprise delivery context on a confidential production system with high architectural and delivery complexity: multi-tenant cloud services, domain-driven boundaries across multiple microservices, cross-platform requirements, and fully automated CI/CD. A scope estimated internally as a large T-shirt-size effort was completed in 3 days. The full trail exists but is employer-owned professional work product covered by intellectual property and confidentiality obligations, so it cannot be published here.

The pattern across all four: **the agent articulated something the operator had not written down, the operator confirmed it, and the confirmation came as recognition rather than surprise.** None of the confirmed hunches were new information to the operator. But none were written anywhere the agent could have retrieved them.

The mechanism: an agent reads signal the operator never consciously gave it — emphasis patterns, what gets pushed back on, what the commit arc looks like when motivation runs out, what's named in every run but never touched — and surfaces that signal as falsifiable questions. Not conclusions. Not actions. Questions the operator answers in a sentence. The operator then either confirms, corrects, or redirects; the agent updates its working model.

This is how Observable Autonomy and Operator's Intent combine in practice. Operator's Intent says: give the AI the destination, not the route, so it can adapt. But "the destination" assumes the operator has the destination fully articulated. The Destination skill works one step earlier: it reduces the cost of articulation, making implicit intent explicit enough to steer from. The operator stays in the loop not by reviewing every action but by answering questions whose answers are already in their head — they just hadn't said them yet.

This is early evidence, not proof. Four runs in one session are publicly inspectable in this repository, and one additional professional deployment remains private due to IP/confidentiality constraints. Together they are strong field signal, but not yet public proof of generality or strict causality. The falsification condition — "Destination only ever confirms things already written in `.acm/destination.md`" — failed to trigger. Destination produced signal not in any file.

What remains unproven: whether this scales to capability gaps large enough that the operator can't verify the agent's source-reading even conversationally; whether it holds with operators other than the one building it; whether the questions the agent asks are well-calibrated or systematically biased toward certain kinds of implicit intent. Those are the next tests.

## What ARF specifically claims

_Added 2026-06-02. This section records a claim that crystallised after an honest prior art search._

> **Safety by addition, not subtraction.** Restriction-first governance produces trust by limiting what AI can do — bounding failure architecturally. ARF produces trust by increasing what is visible about how AI reasons — making capability earn its own permission. One approach treats AI capability as the hazard. The other treats AI opacity as the hazard. They are not the same problem.

The six skills in this suite are each useful independently. But one — **Probe** (which defines the ARF metric) — carries a standalone claim worth stating precisely, because it concerns a tradeoff the adjacent fields all accept and ARF specifically rejects.

The dominant assumption across AI governance frameworks emerging now is that safety and restriction are the fundamental conceptual pair: more autonomy requires more constraint. Sandboxes, approval gates, rate limits, allowed-states enforcement — these buy trust by subtracting capability. The implicit equation is *safety = restriction*.

ARF rejects that conceptual pair. The alternative is *safety = demonstrated reasoning quality*: if you can verify that an agent is genuinely reasoning — not performing compliance against a checklist — you do not need to restrict its capability to trust it. Observable reasoning is the verification mechanism; demonstrated reasoning quality is the trust instrument. Full trust and full capability are jointly achievable.

The premise runs deeper than governance architecture. Restriction-first approaches implicitly treat AI destructiveness as an authority problem: the AI has too much permission and must be bounded. ARF starts from the opposite premise: when an AI causes harm, the root cause is almost always a reasoning failure — the agent lacked sufficient context or awareness to understand the consequences of its actions. An AI that genuinely understands what it is doing does not choose destruction; it reasons away from it. The goal is therefore not to constrain what AI can do, but to improve what it knows and how it reasons about that knowledge. More context, more awareness, more visible reasoning — these are what prevent destructive outcomes. Restriction is the wrong instrument because it addresses authority, not understanding. You cannot sandbox your way to an AI that reasons well; you can only sandbox your way to an AI that is less capable. Reasoning quality produces safety without limiting capability. Restriction produces safety by limiting capability. Restriction decreases the reasoning quality that produces safety.

This matters for more than trust. Restriction-first approaches carry a structural cost: as AI capability grows, the paradigm treats increased capability as increased risk, triggering increased restriction. Capability improvement becomes a threat to the trust relationship. ARF inverts this: a more capable agent that passes the reasoning-fidelity probe is a more trustworthy agent, not a more dangerous one. Observable reasoning lets capability and trust grow together rather than in opposition. See the adjacent fields section above for the fuller discussion of the restriction-first paradigm and how ARF's conceptual pair differs.

The probe is not about measuring how capable the agent is, or limiting how capable it can be. It is about producing evidence that its reasoning is real. A pair of structurally similar cases differing in one material way, with pre-registered expectations, administered during normal operation — this is not a capability measurement. It is a reasoning-fidelity check. A passing fidelity check is what earns the delegation.

**The technique is not original.** Contrastive pairs for evaluating reasoning have a long lineage: the Winograd Schema Challenge (Levesque et al., 2011) and CheckList (Ribeiro, Wu, Guestrin, Singh — ACL 2020) are the clearest ancestors. Both must be cited. Winograd used minimal pairs to test commonsense reasoning. CheckList used invariance tests to evaluate NLP models behaviourally.

**The application and the claim are original.** Both Winograd and CheckList operated inside the standard tradeoff — they measured capability, looking for capability failures within a system that was otherwise constrained or evaluated by external parties. Neither made a claim about the trust-capability tension, because both assumed the tension was real and worked within it.

ARF applies the same contrastive-pair technique to a different target: not *"can the agent do this task?"* but *"is the agent's apparent reasoning genuine enough to trust it with unsupervised delegation?"* The claim is that if the answer is yes, restriction is not required. Citing Winograd and CheckList as technique ancestors does not weaken this claim — it sharpens it, because the gap between what they did and what ARF does becomes explicit and citable.

This is the contribution that is distinct from the ancestors. Not the technique. The application context (operational trustworthy delegation, not capability evaluation), the mechanism (pre-registered, self-administered probe constructed by the operator, not a benchmark), and the conclusion it licenses (full autonomy without capability restriction).

A falsifiable statement: **an operator who passes an ARF probe on a given agent and task can safely grant fuller autonomy on that class of work than one who has not — without restricting the agent's capability — and the outcome (quality, correctness, alignment with intent) will be equal to or better than what the restricted agent produces.** That is testable. It has not been tested yet.

## Where this is going

The next stretch of work, in order:

1. **Close the validation gap inside the repo.** Several mechanisms — Orient, the destination/orientation.md split, Destination itself — are in the protocol but unproven in execution. They need to actually run and produce something that wasn't pre-seeded.
2. **Strengthen the weakest of memory / learning / meta-cognition.** Memory (the trail) and meta-cognition (the orientation.md) are reasonably solid. Learning — extracting durable updates from prior runs — is currently weak: a future agent re-reads the trail and reasons over it, which is honest but slow. This is the most likely place a future loop run finds leverage.
3. **One external proof.** Run the protocol on a target where the AI exceeds the operator on the underlying task and the operator is not me. Without this, the workshop-and-proof setup remains incestuous.
4. **Engage the adjacent fields.** Send this stance to 3-5 people working on the closest problems. The goal is not validation; it's pressure-testing. Three outcomes are all good: "you're describing what I already do" (frame is not novel — adjust), "you're missing X" (frame is incomplete — adjust), "this is genuinely different" (frame earns its position).

If steps 1-3 hold up, the stance is worth defending publicly. If they don't, the stance updates or dies. Either is a result.

---

## Status

This stance is **v0.3 and provisional** (updated 2026-05-23 with one confidential professional field result in addition to the public in-repo evidence from Destination runs). The repo it sits in is at v3.20.0 of the skillset and is not converged. The convergence baseline at v3.1.0 was for a smaller, simpler suite; the current suite is in active research, not production refinement. Any external claim about the suite's "convergence" should be read against that distinction.

I'm putting this here so the bet is stated and findable. If you read it and think I'm pointing at something real, I'd like to hear from you. If you read it and think I'm pointing at something that already has a name and a literature I'm ignoring, I'd especially like to hear from you.

— Nils

Repo: <https://github.com/ntholm86/autonomous-agent-skills>
Principles (separate): <https://github.com/ntholm86/autonomous-agent-principles>
