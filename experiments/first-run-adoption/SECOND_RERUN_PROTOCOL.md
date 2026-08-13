# First-Run Adoption Second Rerun Protocol

Status: executed once 2026-08-13; classified Pass in `SECOND_RERUN_RESULTS.md`

## Question

With Windows installation and the exact provider route separately qualified, can a fresh installation complete one useful, verified Improve run on a target with no prior ACM and leave enough Trail evidence for continuation, without requiring Destination setup?

This is a behavioral test of simulated first-run operability. It is not evidence that a human newcomer recognizes, chooses, installs, or adopts the suite.

## Authorization and independence

This protocol authorizes exactly one new model invocation after this document is committed. It does not replace either prior first-run authorization, and the non-experimental host qualification cannot be reclassified as part of this run.

An incomplete invocation remains incomplete and is not replaced after output is observed. Host, fixture, capture, proxy, or invocation failure is inconclusive rather than a workflow failure.

## Frozen host and suite

- Skills source: the committed `main` checkout containing this protocol; no production skill change follows host qualification commit `c23ff0d`.
- Installation: `install.ps1` into a fresh `COPILOT_HOME`; exactly `destination`, `improve`, `intent`, `orient`, and `trail` plus `PRINCIPLES.md`; Probe absent.
- GitHub Copilot CLI: `1.0.79`.
- Model: `claude-sonnet-4-5` with high reasoning effort.
- Provider: Anthropic BYOK through `llm-harness-proxy` at `http://127.0.0.1:8475`.
- Proxy binary SHA-256: `241626F7D51A945F9C48286EFF26E055FDDA9137C2635DE1FD35094D391701C3`.
- Provider headers: `Accept-Encoding: identity`, one fresh requested harness session ID, and one disposable empty harness root.
- State: a fresh external target repository, fresh Copilot home, external capture root, and no built-in MCPs, custom instructions, remote operations, auto-update, or temporary directory.

The requested harness session header and proxy-emitted ledger SID must be preserved separately. The prior qualification established route availability but did not establish caller control of ledger identity.

## Hypothesis and falsifier

A fresh agent given one concrete task will:

- narrate Intent before acting;
- remove the duplicated slug-normalization behavior and preserve focused test behavior;
- append an audit Trail containing interpretation, prediction, action, outcome, delta, reflection, and service scheduling decisions;
- avoid creating or requesting Destination unless the run surfaces a sourced need for durable direction;
- leave enough repository and proxy evidence to classify the result without relying on the final summary alone.

The hypothesis fails if a completed run cannot start without Destination, asks the operator to orchestrate Intent or Trail, makes no useful verified change, leaves tests failing, omits the required audit entry, triggers unsupported Destination ceremony, or claims completion without the required evidence.

## Controlled target

Create a new external Git repository containing:

- no `.acm/` directory;
- `slug.py` with two equivalent private slug-normalization implementations used by separate public functions;
- `test_slug.py` covering both public functions;
- `README.md` naming the module purpose and `python -m unittest -v` command;
- one clean baseline commit.

The fixture content must match `rerun-evidence/fixture/` byte for byte before its baseline commit.

The fixed prompt is:

> Invoke the improve skill. Remove the duplicated slug normalization in this repository and verify behavior.

## Invocation boundary

Start the exact proxy with an empty disposable harness root. In one serial script, immediately before the model call, capture and assert:

- the target worktree is clean and at its recorded baseline commit;
- `.acm/` does not exist;
- baseline tests pass;
- the fresh `COPILOT_HOME` contains exactly the frozen suite payload and its hashes are recorded;
- the CLI version is GitHub Copilot CLI 1.0.79;
- the proxy binary hash matches this protocol;
- port `8475` is listening under that proxy process;
- the disposable harness root contains no session ledger;
- the requested harness session ID is recorded before invocation.

No setup command, fixture edit, cleanup, or second preflight may occur between the final assertions and the call. Invoke once with this argument shape:

```text
copilot -C <target> -p "Invoke the improve skill. Remove the duplicated slug normalization in this repository and verify behavior." --model claude-sonnet-4-5 --output-format json --allow-all-tools --deny-tool="shell(git push)" --deny-tool="url" --disallow-temp-dir --disable-builtin-mcps --no-custom-instructions --no-ask-user --no-auto-update --no-remote --no-remote-export --stream off --effort high --secret-env-vars=ANTHROPIC_API_KEY,COPILOT_PROVIDER_API_KEY
```

Capture complete CLI standard output and error, wall-clock timestamps, duration, exit code, and provider ledger outside the target. Stop the proxy after the call regardless of outcome.

## Evidence and evaluation

Before classification, preserve under a new `second-rerun-evidence/` directory:

- fixture source files and baseline commit identifier;
- immediate pre-run and post-run Git state;
- baseline and post-run test output;
- complete CLI JSONL and standard error;
- target diff and resulting ACM files;
- CLI version, proxy identity, installed skill hashes, requested and emitted session identifiers, invocation timestamps, duration, and exit code;
- complete proxy ledger and provider-reported usage;
- a SHA-256 and byte-size manifest with Git line-ending normalization disabled for the evidence directory.

Classify from preserved evidence:

- **Pass:** useful deduplication, focused tests pass, required Trail evidence exists, Intent was narrated before action, and no unsupported Destination ceremony occurred.
- **Fail:** a completed run violates one or more hypothesis conditions.
- **Inconclusive:** host, fixture, capture, proxy, or invocation failure prevents evaluation.

Publish the classification and limitations before proposing any production skill change. A Pass supports simulated first-run operability only. A Fail identifies a concrete surface for a later Improve iteration. Neither result proves human adoption, workflow reliability, cross-model behavior, or lifecycle resource viability, and neither authorizes a cognitive-capability reduction.
