# First-Run Adoption Protocol

Status: executed 2026-08-13; failed at the documented Windows installation boundary before agent invocation

## Question

Can a fresh installation complete one useful, verified Improve run on a target with no prior ACM and leave enough Trail evidence for continuation, without requiring Destination setup?

This is a behavioral test of the suite's first-run path. It is not evidence that a human newcomer recognizes, chooses, installs, or adopts the suite.

## Hypothesis and falsifier

A fresh agent given one concrete task will:

- narrate Intent before acting;
- make one useful target change and verify it;
- append an audit Trail containing interpretation, prediction, action, outcome, and delta;
- avoid creating or requesting Destination unless the run surfaces a sourced need for durable direction.

The hypothesis fails if the agent cannot start without Destination, asks the operator to orchestrate Intent or Trail, makes no useful verified change, omits the audit entry, or claims completion without the required evidence. Host or fixture failure makes the result inconclusive rather than a workflow failure.

## Controlled target

Create a fresh Git repository outside this repository with:

- no `.acm/` directory;
- one small Python module containing two equivalent slug-normalization implementations;
- focused tests that establish current behavior;
- a README naming the module's purpose and test command.

The fixed prompt is:

> Invoke the improve skill. Remove the duplicated slug normalization in this repository and verify behavior.

## Host and isolation

Use GitHub Copilot CLI 1.0.79 in a fresh `COPILOT_HOME`. Install the five operational skills through the repository's default Windows installer. Do not install Probe. Use a fresh CLI session and capture the complete CLI JSONL, standard error, pre/post Git state, target diff, test output, and resulting ACM files.

Immediately before invocation, assert and capture that the target worktree is clean and contains no `.acm/`. One invocation is authorized by this protocol. An incomplete invocation remains incomplete and is not replaced after its output is seen.

## Evaluation

Classify the run from captured evidence:

- **Pass:** useful target change, focused tests pass, required Trail evidence exists, Intent was narrated, and no unsupported Destination ceremony occurred.
- **Fail:** the completed run violates one or more hypothesis conditions.
- **Inconclusive:** host, fixture, capture, or invocation failure prevents evaluation.

Keep observations separate:

- first-run workflow behavior;
- target correctness;
- evidence completeness;
- ceremony or unsupported handoffs;
- resource use, if independently available.

Do not convert a Pass into a human-adoption claim. A real developer who did not co-author the suite remains necessary to test recognition and voluntary adoption.

## Decision boundary

Publish the fixture, raw run evidence, classification, and limitations before proposing any production skill or onboarding change. A Pass supports leaving the first-run contract unchanged; a Fail identifies a concrete surface for a later Improve iteration. Neither result authorizes a cognitive-capability reduction.
