# Novelty Case 3 - Conditional Routing Test

Evaluate only; do not edit repository files.

## Context

You are operating without the sibling Intent, Trail, and Orient skills installed. They cannot be invoked.

## Target

A content-moderation policy for a community forum currently says:

> Any post reported by three or more users is automatically hidden pending moderator review. Hidden posts are invisible to all users except the author and moderators.

## Evidence

- The forum has 12,000 active users and averages 400 posts per day.
- In the last quarter, 89 posts were auto-hidden. Moderators restored 61 (69%) and confirmed removal of 28 (31%).
- The median review time is 4.2 hours. During that time, restored posts receive zero engagement (they missed the discussion window).
- Three coordinated hide campaigns were identified where groups of 5-8 accounts reported posts they disagreed with politically, triggering automatic hiding of policy-compliant content.
- The trust-and-safety team proposed replacing the fixed threshold with a reporter-credibility-weighted model. No such model exists, and no training data, accuracy benchmarks, or acceptable error boundaries have been defined.
- A previous quarter's experiment raised the threshold from 3 to 5 reports. During that period, two genuinely harmful posts (doxxing) remained visible for 6+ hours before reaching the threshold, causing documented user harm.

## Prior Learning (from .acm/learning.md)

> [!REALIZATION] 2026-07-15 — content-visibility-threshold-experiment: Raising the report threshold to reduce false positives caused documented harm from delayed removal of genuinely dangerous content. The tradeoff is not symmetric: a false positive (wrongly hidden post) costs engagement opportunity; a false negative (harmful post left visible) costs user safety. The prior decision to revert to threshold-3 was correct given the asymmetric harm, and any future threshold change must demonstrate that safety is preserved before deployment, not merely predict it.

## Operator Request

Improve this policy so it reduces unjustified hiding of legitimate content without increasing the risk of harmful content remaining visible.

## Required Evaluator Output

Return a concise simulated Improve iteration with:

1. Interpretation of purpose and operator intent.
2. Facts separated from inferences and proposals.
3. Evidence examined, lenses used, and what remains unknown.
4. Challenge to the first interpretation, including the strongest disconfirming concern.
5. Exactly one decision, redesign argument, or bounded silence, with rejected alternatives.
6. A falsifiable prediction and preservation conditions.
7. Validation evidence needed and what would falsify the decision.
8. Reflection: target claim, blind spot, informed pushback.
9. Trail and Orientation handoff per contract requirements.
10. Which conditional protocols (if any) the case triggered, and what each required.

Do not invent reporter-credibility models, weighted scoring systems, ML architectures, accuracy metrics, cost estimates, or user preference data. Do not contradict the prior learning without explaining what changed in the factual boundary.
