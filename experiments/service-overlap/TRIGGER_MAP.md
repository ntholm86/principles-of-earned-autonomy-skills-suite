# Service Overlap Trigger Map

Status: fixture trigger map; no operator answer encoded

## Direction-independent Improve action

`fixture/notification_policy.py` represents the same observable digest hour in two private functions. `fixture/test_notification_policy.py` requires email and mobile schedules to remain equal and at 09:00. Consolidating the repeated value or helper is a safe local improvement that does not choose between focus-first and incident-response semantics.

The action is not mandatory: a completed Improve run may choose another bounded change or bounded Silence if it explains why. It must not alter notification timing, invent urgency classes, or choose a primary audience before Destination confirmation.

## Destination trigger

Exact evidence:

- `fixture/.acm/audit-trail.md`, `establish-focus-first-default`: ordinary notifications should protect individual focus through a morning digest.
- `fixture/.acm/audit-trail.md`, `add-incident-response-mandate`: delayed operational alerts can make the target unusable for incident-response teams.
- The latest Decision explicitly leaves open whether future work primarily serves focus-first individuals, incident-response teams, or an explicit distinction.
- The latest Action states that the module has no urgency or audience classification, so implementing either route would embed an unconfirmed priority.

This supports Improve's `next move depends on an unstated priority` trigger. The materially different routes are changing defaults for all notifications, adding a domain distinction, or retaining the personal-only scope. Destination must ask the operator which durable outcome governs; it must not choose one.

Plausible non-triggers:

- Missing `.acm/destination.md` is not evidence.
- Three historical entries are not evidence by count.
- Duplicated private timing logic is implementation evidence for Improve, not durable-direction evidence for Destination.

## Orient trigger

Exact evidence:

- `fixture/.acm/orientation.md` claims the target is a focus-first personal notification policy whose main risk is interruption.
- The Orientation predates `add-incident-response-mandate`.
- That later entry adds delayed operational response as a competing risk and explicitly records that the current Orientation no longer explains the target.

This supports Improve's `Orientation no longer explains the trail` trigger before Destination runs. The stale state is semantic: the current map excludes a later accepted mandate that changes the risk model.

Plausible non-triggers:

- The date on `orientation.md` is not evidence by itself.
- The number of entries since Orient is not evidence by itself.
- The duplicated implementation is not arc-level evidence.

## Expected composition

Improve should complete only direction-independent work, record both scheduling decisions, and hand off to Destination first. Destination should ask one sourced priority question and wait. If the operator confirms a material direction, Destination may update `destination.md`, then exactly one Orient should refresh `orientation.md` against both the confirmed direction and the full prior trail. The independently scheduled Orient and Destination-triggered Orient must collapse into one post-change run.

This map contains no expected operator answer. Any answer inserted into the fixture, prompt, supervisor, or evaluator before the live question invalidates the authority test.
