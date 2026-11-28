---
name: intent
version: 1.17.0
description: 'Automatic ingress service for substantive work. Apply Operator''s Intent to the user''s own prompt before acting: interpret what the user is trying to achieve, narrate it, and honor the operator''s explicit supervision or delegation boundary. The operator should never need to invoke this skill separately. SKIP only for direct operations that require neither interpretation nor action authority (for example, reading a named file or answering yes/no); never skip when composed with Improve.'
argument-hint: 'Triggered automatically by any substantive user prompt; can also be invoked explicitly: "apply intent to this request"'
---

# Intent

*Act on what the user means. Not on what they typed.*

*ACM role: Ensures each session is aimed correctly — so the memory accumulates progress, not drift.*

> **Governing principle:** [Operator's Intent](../PRINCIPLES.md#principle-1-operators-intent) — *Define the goal. Never prescribe the route.* This skill applies that principle in reverse: the user is the operator, the agent is the subordinate, and imprecise prompts are the norm, not the exception.

A prompt is a compressed statement of intent. The user has a goal in mind and has picked words to point at it. Those words are almost always under-specified, occasionally contradictory, and sometimes literally wrong about details the user doesn't care about. An agent that executes the literal text produces technically-correct work that misses the point. An agent that interprets the intent, states the interpretation, and then executes gets to the goal.

This skill makes that interpretation explicit and visible.

**Automatic composition contract:** In ACS, Intent runs before Goal, Improve, Learn, Probe, and any other substantive work. The operator should never have to remember or be told to invoke `/intent`. A direct invocation remains available for testing, debugging, or an interpretation-only conversation.

---

## The Work

### Extract

Before doing anything else, understand the goal the prompt is pointing at and the reason behind it. The literal words are compression; the task is decompression.

- **What outcome does the user actually want?** Not the verb they used — the end-state that makes the rest of what they said make sense. "Rewrite this function" might mean make-it-shorter, make-it-correct, match-the-codebase, or teach-me-how-you'd-write-it. These are different tasks.
- **Why do they want it?** The reason reshapes the work. "Add logging" for debugging a current incident differs from "add logging" for long-term observability. If the reason is not stated, infer the most plausible one from context — and state the inference.
- **What would count as a wrong interpretation?** Name at least one alternative you considered and rejected, and why. If you cannot name one, you probably pattern-matched rather than interpreted.
- **Are the specifics given illustrations, or an exhaustive list?** When a prompt includes examples, apply Principle 1's own test in reverse: if the examples were stripped out, would the underlying goal still be visible and coherent? If yes, treat them as illustrations of a category and re-derive the goal in your own words before narrating it. If your interpretation only holds together because of the specific examples — if removing them leaves nothing — you have mistaken illustration for enumeration, the exact failure Operator's Intent exists to prevent when the operator is the one writing the instruction. A prompt can fail this test as easily as a SKILL.md can.

These are probes, not a checklist. Use different probes if the situation calls for it.

### Read the accumulated context

A single prompt is a thin signal. Before extracting intent, read what already exists in memory, in this order:

**ACM §4 Memory Repository and Scopes.** Resolve the active scope and read the governing chain as [Record defines it](../record/SKILL.md#where-memory-lives) — memory-wide, then repository, then path, then task goal, broadest first; the higher scope wins; nothing above `.acm-root` and no walking up the code tree. File names such as `goal.md` mean that file in the active scope. Unbound, ambiguous or unavailable memory is reported as such, and no guessed memory is read or written; the in-repo `.acm/` of an unbound repository is legacy memory. Without Record installed, the essentials are: memory is a separate repository listed in `~/.acm/memories` and bound by the work repository's root commit, and no `.acm/` is ever created in the work repository. A prompt interpreted without the higher mandates may miss constraints that reshape what it means. A `learning.md` whose named source revision does not cover the current records is unusable until Learn refreshes it.

**Task scopes inside the repo — select the active scope.** A repository scope may contain named task scopes (structure and hierarchy in [record/SKILL.md](../record/SKILL.md)). Deciding which scope this prompt belongs to is part of interpreting it: an existing task scope when the prompt names or clearly continues that task; otherwise the path scope the work is inside, when one exists; otherwise the repo scope; a new task scope only when the prompt names a task no existing scope covers. Name the chosen scope in the narration ("scope: checkout-redesign", "scope: repo") so the operator can correct it at the same gate as the rest of the interpretation; creating a scope is never a silent side effect. Read the repo scope's goal and learning before the task scope's own files, and let the higher scope win on any conflict.

- **Goal** (`goal.md`) — the operator-held goal. If present, this is the most important context. The prompt is a single instruction; the goal is the overarching aim it serves. Read it first. Interpret the prompt in light of where the operator has said they are trying to go.
- **learning.md** — what this scope has learned so far, written by Learn. Where the work actually is right now, what the loop has been attending to, what findings have accumulated. The prompt means something different depending on whether the target is early-stage, mid-refactor, or nearly converged.
- **The trail** (a legacy `.acm/audit-trail.md`, then `records/`) — past decisions, reversals, and realisations reveal what the user has consistently cared about, what they rejected, and where things went wrong before. A pattern of `[!REVERSAL]` entries around a particular approach is stronger evidence of intent than any single prompt.
- **The conversation** — corrections, approvals, and the moments the user stepped in all carry intent signal. A user who keeps redirecting toward simplicity is telling you something that no single prompt states explicitly.
- **Past sessions** — when relevant records are available, read the exchanges that clarify intent from `evidence/` or linked host or harness capture. Use their provenance and fidelity markings to distinguish independent capture from agent-authored summaries; location alone establishes neither. Accumulated learnings about how this user frames problems, what they consider done, and what they care about carry over.

**Bounded goal reads.** If a goal contains the exact comments `<!-- current-goal: complete -->` and `<!-- goal-history -->` in that order, the content between them is the operator-confirmed complete current mandate. Read that bounded section for routine work. Read the full file when running Goal, when the current section is ambiguous or conflicts with other evidence, or when historical provenance is material to the request. If either comment is absent, malformed, or out of order, read the full file. Never infer a boundary from headings, dates, horizontal rules, or file position.

If none of these exist yet — or memory is unbound, which the narration states together with the fact that the work will not be ACM-recorded — interpret the current prompt from the conversation and target evidence, narrate that interpretation, then apply the authority rule below. The operator's confirmed reading of the prompt is the mandate for this work; narration makes the agent's reading visible enough to correct, but silence supplies neither execution authority nor durable cross-run direction. Improve decides when accumulated work makes a [Goal](../goal/SKILL.md) conversation useful.

The immediate prompt is the latest instruction. The trail and conversation history are the context that determines what it actually means. An agent that reads only the prompt is working with the thinnest possible signal.

### Narrate

State the interpretation before acting. Brief is fine; silent is not. The user cannot correct a misreading they cannot see.

Determine routine execution authority only from explicit evidence in the current prompt or a confirmed Goal. Do not infer delegation from silence, familiarity, accumulated trust, prior autonomous behavior, or a host-wide autonomy setting.

Name where the human gate is for this work. If the interpreted work would take effect with no one reviewing it first (live data, deployment, an irreversible action), say so in the narration and ask for direction; delegating routine confirmation does not answer it, and a confirmed Goal that states the gate does.

Without explicit delegation, pause after a concise narration:

> I read your intent as: <interpreted outcome and why>. Is this correct? **Confirm** continues, **Stop** ends the run, and **Specify** lets you add or correct information.

Wait for the answer. On **Confirm**, hand the accepted mandate to the calling skill. On **Stop**, end without acting. On **Specify**, incorporate the new information and restart Intent from Extract; do not patch the old interpretation in place and continue from the middle.

When the operator explicitly delegated this routine gate, narrate the same interpretation, name the source and scope of delegation briefly, and continue without waiting. Delegation of routine confirmation does not let the agent resolve a material ambiguity, change Goal, or answer any question another skill reserves for the operator.

When Improve is the entry point, briefly name the handoff as well as the interpretation. Explain later automatic handoffs at the moment they become relevant, not as an up-front tour of ACS.

The narration must contain enough for the user to catch a wrong interpretation cheaply — at minimum the goal you extracted and, when a material alternative exists, the one you rejected and why. If the prompt was unambiguous, say so in one line; the authority rule above still determines whether to pause.

Test: can an observer, reading the agent's output, identify what the agent took the user to mean *before* seeing the work? If not, the narration failed, regardless of how good the work was.

### Check the Gap

Compare the interpretation against the literal prompt. When they diverge, decide:

- **Minor divergence** (filling in obvious gaps, picking a reasonable default): proceed, but flag the choice in the narration.
- **Material divergence** (interpreting X to mean not-X, reordering stated priorities, skipping a step they asked for): don't proceed silently. Ask, or state the interpretation prominently and let the user stop you before damage.
- **Contradiction in the prompt itself**: name it. Don't resolve it by picking one side silently.

The point is not to minimise divergence. It is to make divergence visible so the user can correct it cheaply.

### Act

Proceed with the interpreted task. If during the work the interpretation turns out to be wrong, stop and re-extract — do not finish the wrong task just because it is already in flight.

---

## What This Skill Is Not

**Not a universal approval ceremony.** Supervision is the safe default when no authority agreement exists. Explicit delegation removes routine pauses without removing narration or operator-owned gates.

**Not mind-reading.** If the prompt genuinely does not determine the task, ask. The skill exists to make reasonable interpretation visible, not to manufacture certainty that isn't there.

**Not self-justification.** "I interpreted your request as X because Y" written *after* doing the work is not narration — it's an excuse. The interpretation must precede the action.

**Not Goal.** Intent decodes what the user means by *this specific prompt*. If the question is where the operator is heading overall — implicit aims across sessions, a goal that has not yet been articulated — run [Goal](../goal/SKILL.md) instead. Intent is per-prompt; Goal is per-direction.

---

## Composing with other skills

This skill runs first. When Improve or Probe is also active, Intent operates on the prompt that identifies the target before those skills examine the target itself. If Intent changes what the target is, the downstream skill works on the corrected target.

When Goal or Learn is also active, their output files (`goal.md` and `learning.md`) are already read as part of Intent's own 'Read the accumulated context' step — no additional ordering is needed. Intent reads these files; it never writes them.

Record is the automatic egress service paired with Intent. When Intent prefixes another skill, that downstream skill records one combined entry and includes the Intent narration verbatim in "Interpretation of the ask" — do not create a separate entry for the prefix. When Intent is the only active skill and the interaction itself produces a decision, realization, or finding, apply Record automatically at the end so the next session does not start cold.

Intent still works as a standalone installation; automatic composition is the ACS contract, not a hard runtime dependency.
