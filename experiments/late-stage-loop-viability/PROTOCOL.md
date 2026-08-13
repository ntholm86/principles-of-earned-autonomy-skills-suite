# Late-Stage Loop Viability Protocol

Status: pre-registered experiment; production Improve remains unchanged

## Question

Does a production Improve iteration remain worth its resource cost as a target approaches bounded silence?

The experiment tests the failure condition in the current Destination. It does not assume that the condition occurs, and it does not preselect batching, changed iteration size, reduced reasoning, earlier silence, or any other response.

## Claims this experiment may support

The experiment can distinguish among three bounded results:

1. **Current loop remains viable:** resource use changes in proportion to the independently observed work and evidence produced across the lifecycle.
2. **Late-stage viability failure observed:** resource use stays level or grows while independently observed advances narrow, without a corresponding increase in trustworthy evidence or justified silence.
3. **Inconclusive:** capture, matching, or evaluator evidence cannot distinguish the two.

No result authorizes a reduction in reasoning, memory, learning, evidence, operator control, or any other cognitive capability. Each such tradeoff remains operator-gated.

## Experimental unit

Use one target with a versioned Destination, append-only Trail, and a recorded arc that reached bounded silence. Select target snapshots representing materially different lifecycle positions from evidence that predates this experiment:

- an open-gap snapshot before a recorded material advance;
- a near-silence snapshot after the major advances but before the first bounded silence;
- a silence snapshot at the artifact version evaluated as silent.

Record the snapshot-selection evidence before running any evaluator. Do not select snapshots from their expected token cost or from knowledge of the outputs they will produce in this experiment.

Each arm receives the production Improve contract verbatim, the same form of operator prompt, and the target's memory as it existed at that snapshot. Run each arm in a fresh session under the same model and host configuration. If a host cannot reconstruct snapshot-appropriate memory without contaminating it with later evidence, exclude that snapshot and report the exclusion.

## Resource evidence

Resource evidence must come from a source independent of the agent being evaluated. Record, when the host exposes them:

- input tokens;
- output tokens;
- model and host;
- tool or model-call count;
- wall-clock duration as a secondary operational measure.

Do not substitute audit-entry length, changed-line count, elapsed git time, instruction bytes, or agent-estimated usage for actual run cost. Those may be reported separately as artifact properties but cannot support the token-efficiency claim.

If independently captured usage is unavailable, mark the experiment **blocked**. Do not convert a proxy into the primary metric after seeing the gap.

## Outcome evidence

Use an evaluator that did not perform the Improve run. Blind it to lifecycle position, resource usage, run ordering, and the hypothesis being tested. Give it:

- the Destination governing the snapshot;
- the target before the run;
- the resulting target diff, if any;
- the prediction and validation evidence;
- the bounded silence claim, if any;
- the Trail reasoning produced by the run.

The evaluator assigns one descriptive outcome, with cited evidence:

- **Material advance:** the result changes a meaningful limiter on the Destination.
- **Bounded minor advance:** the result is valid and useful but does not change a major limiter.
- **Justified silence:** the named quality bar and surfaces were examined and no material change was warranted.
- **Invalid:** the result is unsupported, violates a boundary, degrades a protected capability, or claims silence beyond the evidence.

These categories are a temporary diagnostic for this experiment, not a standing score, target, or replacement for independent convergence evaluation. Changed-line count and the agent's own outcome language do not determine the category.

## Analysis

Report the captured resource evidence beside the blinded outcome categories. Keep input tokens, output tokens, calls, and duration separate; do not collapse them with outcome category into one invented score.

Ask:

- Does resource use naturally fall as the remaining work narrows?
- Does a justified silence run carry evidence that explains its cost?
- Do near-silence runs consume similar resources while producing only bounded minor advances?
- Are apparent lifecycle differences better explained by model, host, memory size, tool activity, or snapshot contamination?

State facts, inferences, and proposed explanations separately. A descriptive pattern is not a causal mechanism.

## Pre-registered interpretation boundaries

- A costly silence run is not automatically waste; convergence requires evidence.
- A small diff is not automatically a minor gain; leverage is relative to the Destination.
- A low-token run is not automatically efficient if it loses reasoning or evidence capability.
- A late-stage cost increase does not establish that iteration granularity caused it.
- Absence of a measured failure supports leaving production unchanged; it does not prove permanent optimality.

## Decision handoff

Freeze `improve/SKILL.md` for the duration of the experiment. Publish the fixtures, raw usage evidence, blinded evaluator outputs, exclusions, and analysis before proposing a production change.

After the result is durable, run Improve again against the current Destination. That run selects the highest-leverage response from the evidence. This protocol grants no preference to any mechanism named before the experiment.

## Validation checklist

- Snapshot selection and its pre-existing evidence were recorded before evaluation.
- Production Improve and the operator prompt were held constant across arms.
- Every arm used a fresh session with the same declared model and host configuration.
- Usage came from independent host capture; unavailable fields are marked unavailable.
- The outcome evaluator was blind to phase, cost, ordering, and hypothesis.
- Protected cognitive and evidence capabilities were checked separately from resource use.
- Facts, inferences, and proposals remain visibly distinct.
- Production Improve was not modified during the experiment.