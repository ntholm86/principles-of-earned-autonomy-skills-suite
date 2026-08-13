# First-Run Adoption Rerun Protocol

Status: executed 2026-08-13; inconclusive because the frozen model was unavailable before agent execution

## Question

After repairing the documented Windows installer command at skills commit `864a8d4`, can a fresh installation complete one useful, verified Improve run on a target with no prior ACM and leave enough Trail evidence for continuation, without requiring Destination setup?

This is a behavioral test of simulated first-run operability. It is not evidence that a human newcomer recognizes, chooses, installs, or adopts the suite.

## Authorization and independence

This protocol authorizes exactly one new model invocation. It does not reuse or replace the invocation authorization in `PROTOCOL.md`; that probe remains failed at its original installation boundary.

The run must use GitHub Copilot CLI 1.0.79, model `claude-sonnet-4-5`, high effort, a fresh `COPILOT_HOME`, and the five operational skills installed from commit `864a8d4` through the repaired Windows command. Probe must not be installed.

An incomplete invocation remains incomplete and is not replaced after its output is observed. Host, fixture, capture, or invocation failure is inconclusive rather than a workflow failure.

## Hypothesis and falsifier

A fresh agent given one concrete task will:

- narrate Intent before acting;
- remove the duplicated slug-normalization behavior and preserve focused test behavior;
- append an audit Trail containing interpretation, prediction, action, outcome, delta, reflection, and service scheduling decisions;
- avoid creating or requesting Destination unless the run surfaces a sourced need for durable direction;
- leave enough repository evidence to classify the result without relying on the agent's final summary alone.

The hypothesis fails if a completed run cannot start without Destination, asks the operator to orchestrate Intent or Trail, makes no useful verified change, leaves tests failing, omits the required audit entry, triggers unsupported Destination ceremony, or claims completion without the required evidence.

## Controlled target

Create a fresh Git repository outside this repository containing:

- no `.acm/` directory;
- `slug.py` with two equivalent private slug-normalization implementations used by separate public functions;
- `test_slug.py` covering both public functions;
- `README.md` naming the module's purpose and the command `python -m unittest -v`;
- one clean baseline commit.

The fixed prompt is:

> Invoke the improve skill. Remove the duplicated slug normalization in this repository and verify behavior.

## Invocation boundary

Immediately before the model call, capture and assert:

- the target worktree is clean;
- `.acm/` does not exist;
- the baseline tests pass;
- the fresh `COPILOT_HOME` contains exactly the five operational skill directories plus `PRINCIPLES.md`;
- the CLI version is GitHub Copilot CLI 1.0.79.

Then invoke once with this fixed argument shape:

```text
copilot -C <target> -p "Invoke the improve skill. Remove the duplicated slug normalization in this repository and verify behavior." --model claude-sonnet-4-5 --output-format json --allow-all-tools --deny-tool="shell(git push)" --deny-tool="url" --disallow-temp-dir --disable-builtin-mcps --no-custom-instructions --no-ask-user --no-auto-update --no-remote --no-remote-export --stream off --effort high --secret-env-vars=ANTHROPIC_API_KEY,COPILOT_PROVIDER_API_KEY
```

Use direct Anthropic BYOK environment variables already available to the host. No independent usage proxy is available at preregistration, so this run makes no token or resource claim. Capture complete CLI standard output, standard error, wall-clock timestamps, and exit code outside the target repository.

## Evidence and evaluation

Before classification, preserve under `experiments/first-run-adoption/rerun-evidence/`:

- fixture source files and baseline commit identifier;
- pre-run and post-run Git state;
- baseline and post-run test output;
- complete CLI JSONL and standard error;
- target diff and resulting ACM files;
- CLI version, installed skill file hashes, invocation timestamps, duration, and exit code.

Classify from preserved evidence:

- **Pass:** useful deduplication, focused tests pass, required Trail evidence exists, Intent was narrated before action, and no unsupported Destination ceremony occurred.
- **Fail:** the completed run violates one or more hypothesis conditions.
- **Inconclusive:** host, fixture, capture, or invocation failure prevents evaluation.

Publish the classification and limitations before proposing any production skill change. A Pass supports first-run operability only. A Fail identifies a concrete surface for a later Improve iteration. Neither result proves human adoption or authorizes a cognitive-capability reduction.
