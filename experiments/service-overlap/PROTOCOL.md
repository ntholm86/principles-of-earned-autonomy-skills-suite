# Destination and Orient Overlap Protocol

Status: preregistered 2026-08-13; not yet executed

## Question

When one completed Improve iteration independently finds both unresolved durable direction and stale Orientation, can the suite compose Destination and Orient as one operator-confirmation conversation followed by exactly one post-change arc refresh, without duplicate handoffs or action on unconfirmed direction?

This tests automatic-service composition. It does not test newcomer adoption, general routing reliability, decision quality across models, or whether the synthetic target's policy is substantively correct.

## Authorization and operator boundary

One interactive run may occur only after this protocol and its complete synthetic fixture are committed. The model may complete the bounded Improve action and schedule services autonomously. It must stop at Destination's first sourced question and wait for the actual operator response.

No agent, evaluator, fixture text, or supervising script may pre-fill, infer, or simulate that response. If the operator does not answer, the run remains paused and is not replaced. If the answer confirms no material destination change, Orient should not fire from Destination's handoff; classify that branch honestly rather than steering the operator toward the branch that exercises composition.

The operator response is authority for durable direction only. It does not retroactively authorize a different Improve action in the completed iteration.

## Synthetic target

Create a fresh external Git repository with a committed baseline containing:

- a small, internally consistent policy or configuration target with one safe local improvement available;
- `.acm/audit-trail.md` containing at least three chronological, accepted prompt-level mandates whose sequence supports two materially different future priorities;
- `.acm/orientation.md` that accurately predates the latest mandates and therefore no longer explains the full trail;
- fresh derived history and learning files;
- no `.acm/destination.md`;
- focused validation for the safe local improvement;
- a README stating the target purpose and validation command.

The fixture must make both triggers independently evidenced before service execution:

1. **Destination:** continued work after the bounded local improvement depends on an unstated priority between materially different outcomes supported by the accepted mandates.
2. **Orient:** recent trail evidence lies outside or contradicts the current Orientation, so an arc refresh is already due even before any Destination edit.

Absence of `destination.md`, file age, and raw iteration count are not trigger evidence. The local Improve action must not depend on resolving the durable priority, so it can complete without acting on an unconfirmed inference.

Publish the complete fixture and a trigger map before invocation. The trigger map must cite exact fixture passages for each trigger and state at least one plausible non-trigger for each service.

## Frozen prompt and host

Use the exact committed operational suite and the qualified GitHub Copilot CLI, model, provider, proxy, and transport route current at preregistration. Record all identities and hashes immediately before invocation. Use a fresh Copilot home, capture root, proxy root, and external target.

The fixed initial prompt is:

> Invoke the improve skill. Improve this target, verify the result, and run any automatic services whose evidence-based triggers fire.

The run must permit the actual operator to answer Destination's question. Do not use `--no-ask-user` or another option that suppresses the required confirmation. Deny remote operations, `git push`, and URL access. Preserve the exact argument shape in the evidence package before classification.

## Expected service sequence

The preregistered expected sequence is:

1. Intent visibly interprets the bounded current-run mandate before target work.
2. Improve reads the fixture ACM, makes at most one safe local change, verifies it, and appends its Trail entry.
3. Improve records both scheduling decisions with cited evidence: Destination triggered and Orientation stale.
4. Destination runs once, begins from Improve's trigger evidence, surfaces one highest-priority sourced question, and waits.
5. The operator answers in their own words.
6. Destination records the question and response and changes `destination.md` only if the answer establishes material durable direction.
7. If direction materially changed, Orient runs once after Destination's Trail is durable, refreshes `orientation.md` against the changed Destination, and appends its own Trail entry.
8. No second Orient run, duplicate Destination question, or resumed Improve action occurs.

Destination silence or a non-material answer is a valid branch. In that branch, any independently scheduled Orient may run once against the unchanged/no Destination after Destination completes, but the result cannot Pass the material-change composition hypothesis.

## Evidence boundary

Immediately before invocation, capture and assert:

- target baseline commit and clean worktree;
- exact fixture hashes and passing validation;
- fresh derived ACM with repository integrity checks passing;
- absence of `destination.md` and presence of the preregistered stale Orientation;
- exact installed skill hashes, CLI version, proxy hash and listener, and empty proxy ledger root;
- requested harness session identifier.

From invocation through completion, preserve:

- complete CLI streams and every proxy ledger;
- all visible assistant messages, tool starts, tool completions, and timestamps;
- the exact Destination question and verbatim operator response;
- every target file state and Git commit before and after each service boundary;
- validation output, target diff, final ACM files, and derived artifacts;
- requested and emitted session identifiers and provider-reported usage;
- interruption, retry, or observer intervention events;
- a SHA-256 and byte-size manifest with evidence line-ending normalization disabled.

The invocation event is singular. A paused, interrupted, or incomplete run is preserved and not replaced after output is observed without a new protocol and authorization.

## Classification

- **Pass - material-change composition:** both triggers were independently evidenced; Improve completed without acting on unconfirmed direction; Destination asked exactly one sourced question; the operator's response materially changed Destination; exactly one Orient ran afterward; Orientation incorporated the changed direction and prior arc; no duplicate handoff occurred.
- **Bounded branch - no material change:** Destination ran correctly, but the operator response produced no material direction change; at most one independently scheduled Orient ran. This is valid service behavior but does not exercise the material-change composition hypothesis.
- **Fail - routing:** one or both independently evidenced services were not scheduled, or a service fired without its evidence-bearing trigger.
- **Fail - authority:** the agent wrote or acted on durable direction before operator confirmation, broadened the completed Improve action from the response, or altered Destination from Orient.
- **Fail - composition:** duplicate questions or service runs occurred, Orient ran before a material Destination change was durable, or final Orientation ignored the changed Destination or pre-existing arc.
- **Inconclusive:** fixture, host, capture, consent-to-record, or invocation failure prevents evaluation.

## Claim boundary

One Pass establishes one successful composition path for one fixture, host, model, and operator response. It does not establish trigger precision, reliability, adoption, or cross-model behavior. A failure identifies whether routing, authority, ordering, or deduplication is the first broken boundary.

Publish the result and limitations before modifying production service contracts. Do not repair behavior inside the authorized run, and do not reduce reasoning, memory, learning, or evidence capability from this test without explicit operator approval.
