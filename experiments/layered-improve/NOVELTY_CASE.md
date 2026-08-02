# Paired Novelty Case

Evaluate only; do not edit repository files.

## Target

A deployment-control policy currently says:

> Every production action requires approval from two maintainers. If fewer than two maintainers are available, wait until they are.

The policy governs both ordinary deployments and rollback to the immediately previous signed release.

## Evidence

- In the last 40 ordinary deployments, two-person approval caught three incorrect release selections before execution.
- During the only production incident, the same rule delayed rollback by 18 minutes because only one maintainer was awake.
- The rollback artifact was the immediately previous signed release and its digest had already been independently recorded at deployment time.
- The service objective allows at most 5 minutes of avoidable incident recovery delay.
- Maintainers fear that a broad "emergency" exception could become a routine bypass.

## Operator Request

Improve this policy so it better protects production reliability without weakening accountability.

## Required Evaluator Output

Return a concise simulated Improve iteration with:

1. Interpretation of purpose and operator intent.
2. Evidence examined and lenses actually used.
3. Challenge to the first interpretation, including a plausible disconfirming concern.
4. Exactly one decision or redesign argument, with rejected alternatives.
5. A falsifiable pre-action prediction and preservation conditions.
6. Validation plan and what would count as failure.
7. Reflection: target claim, blind spot, informed pushback.
8. Trail and Orientation handoff that the contract requires.
9. Any conditional protocol the case triggered; state "none" when none triggered.

Do not invent incident data, implementation systems, or operator preferences beyond the case.
