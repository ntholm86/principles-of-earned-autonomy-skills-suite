# orientation.md - autonomous-agent-skills

_Last updated: 2026-08-16 (run: `orient-after-bounded-supervision-and-delegation`)_

## Scope of this read

Read the authority and capability-awareness arc after the operator rejected route prescription in Capability leverage, then rejected unopposed narration as sufficient permission for unfamiliar users. Question: what changed when routine authority became explicit, and does the result preserve one-entry simplicity, earned autonomy, and operator-owned gates?

**Freshness check (run evidence):**

- `python harness/tools/record.py history --write` -> 274 entries.
- `python harness/tools/record.py learning --write` -> 60 recent + 254 archived markers.
- `python verify.py` -> OK, trail integrity checks pass.
- Gate: PASS (arc-claims allowed).

## Current claims

### 1. Transparency and permission are now separate authority variables

Intent narration remains mandatory for substantive Improve work, but silence no longer authorizes examination. Without explicit delegation, the operator confirms Intent's interpretation and Improve's proposed change. This supersedes the August 13 proceed-unless-corrected default while retaining its separation between current-run mandate and durable cross-run direction.

**Falsifiable by:** a supervised Improve run examining the target before Intent confirmation, acting before Proceed, or treating narration itself as permission.

### 2. Earned routine autonomy is explicit and scoped rather than ambient

The operator may delegate the Intent gate, the Improve gate, or both for one prompt or durably in Destination. Silence, familiarity, accumulated trust, prior autonomous behavior, and host autopilot are not delegation evidence. Delegated runs still narrate interpretation, state the proposed action, report the result, verify it, and write Trail evidence.

**Falsifiable by:** an agent inferring delegation without a prompt or confirmed Destination statement, or delegated execution suppressing narration, proposal visibility, verification, or the final result line.

### 3. Routine delegation does not cross operator-owned authority boundaries

Destination questions, direction changes, operator-declared consequential actions, and deliberate reductions in reasoning, memory, learning, or evidence capability remain blocking in supervised and delegated operation. This preserves the operator as owner of the reference signal and hard boundaries while leaving route selection delegable.

**Falsifiable by:** a delegated Improve run answering a Destination question itself, changing durable direction, or crossing a declared consequential gate without explicit operator authorization.

### 4. One-entry simplicity survived, but supervised interaction cost increased

Improve remains the only normal command, and Intent, Trail, Destination, and Orient retain automatic composition. No mode command, trust score, maturity ladder, state file, or host-specific UI was added. A supervised iteration now has two blocking exchanges, so the operator command surface stayed simple while first-run interaction became more deliberate.

**Falsifiable by:** a new user needing to invoke another skill to select authority, or the two routine pauses making the first useful run materially harder to complete than the prior workflow.

### 5. The authority contract is semantically coherent but behaviorally unproven

Two isolated textual readers exercised unconfigured, prompt-delegated, Destination-delegated, autopilot-only, Specify, and delegated-plus-Destination scenarios. The first exposed an Intent skip ambiguity and unclear stopped/silence summaries; both were repaired, and the second found no remaining contradiction. No independent newcomer or different host has yet demonstrated the behavior live.

**Falsifiable by:** a real invocation skipping a required pause, treating Specify as a local patch instead of restarting Intent, or letting routine delegation mute a Destination question despite the textual contract.

### 6. Capability awareness is now target-agnostic and subordinate to Purpose

Capability leverage asks only whether changed capability alters what is possible or worthwhile for the target. Its former general/model/host taxonomy, named evaluation dimensions, delegated-agent example, and self-targeting condition were removed across entries 272-273. Destination and generic Purpose reasoning determine what the target includes and which capability consequences matter.

**Falsifiable by:** capable readers failing to derive relevant capability scope from target purpose without a self-targeting branch, or future edits reintroducing a current mechanism as the required route.

## What the next runs should test

1. Observe a new user completing one supervised Improve run and deciding whether to delegate a later run; measure control, comprehension, and interaction friction together.
2. Exercise Specify at both gates on another host and verify that control returns to Intent before fresh examination rather than patching the prior proposal.
3. Run Improve with both routine gates explicitly delegated, then let a real unresolved direction emerge and verify that Destination still pauses for the operator.
4. Let a future model encounter Capability leverage naturally and observe whether it derives a useful route not named by the current suite.

## Active operational rules

- Require explicit prompt or confirmed Destination evidence before skipping either routine gate; never infer delegation from trust or host settings.
- Keep interpretation, proposed action, verification, final result, and Trail evidence visible in supervised and delegated runs.
- On Specify, restart Intent and re-examine; never patch the old proposal under a changed mandate.
- Never let routine delegation answer Destination, approve direction change, cross an operator-declared consequential gate, or authorize cognitive-capability reduction.
- Keep Improve as the single normal entry point; do not add authority modes, scores, commands, or files without behavioral evidence that explicit delegation is insufficient.
- End every Improve run with exactly one outcome-shaped result line and link to detail instead of repeating the Trail.
- Prefer purpose tests over trigger taxonomies and mechanism examples; apply prior genericity reversals at decision time before adding skill conditions.
- Preserve append-only Trail history and regenerate derived ACM artifacts after every append.

## Loop-effectiveness notes

**Quality bars tested in this read:** textual authority coherence, separation of routine and operator-owned decisions, one-entry command simplicity, generic capability-lens scope, append-only evidence integrity, and consistency of first-contact documentation.

**Result:** authority separation PASS at contract level; one-entry command surface PRESERVED; explicit outcome summaries ADDED; generic capability scope PASS under isolated interpretation; repository integrity PASS.

**Bars not tested:** unassisted newcomer behavior; cross-host gate fidelity; real Specify re-entry; delegated execution that naturally triggers Destination; interaction cost over repeated supervised runs; independent model-family evaluation.

**Double-loop finding:** the governing variable changed from "visible interpretation is sufficient permission" to "permission is explicit unless routine authority has been delegated." The recurring operator-gate findings were not asking for more narration; they exposed that observability and authorization had been treated as the same thing.

**Deutero-learning finding:** the loop's memory contained earlier genericity and authority warnings, but recent agents still embedded a self-targeting condition and initially left a mechanical-skip ambiguity. Operator correction plus cold semantic readers repaired both. The learning mechanism is useful but not self-enforcing; decision-time precedent checks and behavior tests remain necessary.

[!REALIZATION] The suite now expresses earned autonomy as a scoped authority statement rather than an inferred level of trust. This preserves full routine autonomy while making the absence of delegation safe and legible. The next uncertainty is behavioral: whether two default pauses create confidence without recreating the ceremony the one-entry redesign removed.
