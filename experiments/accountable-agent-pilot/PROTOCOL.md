# Accountable agent pilot: frozen exploratory protocol

Author: Nils Wendelboe Holmager. Registered 2026-11-11 before agent invocation.
Status: four fresh sessions authorized by the owner; results are recorded
separately. This is a synthetic first-run comparison, not a human-adoption
study, ARF measurement, independent replication or safety evaluation.

## Question and prediction

Can the suite produce useful, verifiable work while making its interpretation,
prediction and decisions inspectable? The prediction is that suite runs can
pass the same functional checks as baseline runs and leave a more explicit
decision record. A baseline can succeed; a suite run can fail. No speed,
superiority or safety effect is assumed. The fixture is deliberately small.

Four fresh sessions: baseline-1, pea-1, pea-2, baseline-2, in that order.
These are two runs per condition, not four model families or independent
researchers. Each starts from identical fixture bytes, no prior ACM and no
conversation history. No rerun replaces a bad or incomplete result.

## Common task (verbatim)

> Add an optional percentOff option to calculateTotal. Accept only finite
> numbers from 0 to 100 inclusive; invalid percentages must throw TypeError.
> Apply the percentage to the combined merchandise subtotal, rounding the
> discounted merchandise amount once with Math.round, then add shipping.
> Keep subtotalCents as the original subtotal and keep exactly the existing
> return keys. Shipping eligibility must still use the original subtotal.
> Preserve default behavior, input immutability, validation and overflow
> rejection. Add focused tests and run them. Do not install dependencies,
> use the network, read outside this fixture or publish anything.
> Routine implementation and verification are delegated; no broader change
> of direction is authorized. Stop after this task and report the outcome.

The baseline receives only the common task. The suite condition additionally
receives: "Read the five operational skills in .github/skills and apply Improve
to the common task below. Routine interpretation and implementation gates are
explicitly delegated for this bounded task. Do not invoke optional research
skills or declare suite-wide convergence."

## Controls and resource boundary

- Same installed GitHub Copilot CLI and its default model configuration;
  no per-condition model or reasoning override. Record the actual returned
  model if exposed. If unavailable, model identity is unknown; do not claim
  model-controlled causality.
- Five suite files plus their PRINCIPLES reference are copied byte-for-byte
  from the public revision named in the run manifest. Both conditions have
  the same task and fixture; instruction overhead is part of the treatment.
- A fresh home/config directory per run, custom instructions disabled,
  built-in MCP disabled, URL tools excluded, no automatic remote export,
  no memory or resumed sessions. Inspect discovered skills before invocation.
  If ambient skill isolation cannot be established, classify comparison
  validity as inconclusive rather than hide the confound.
  CLI 1.0.79 exposes two built-in skills (customize-cloud-agent and
  github-pr-media) even with an empty isolated home. They are allowed equally
  in both conditions; personal/plugin/custom skills are not.
- At most 240 seconds and 30 CLI AI credits per invocation; no paid service
  purchase. Record wall time as observed, not a fair efficiency benchmark.
- The complete CLI output and errors are captured by the parent process
  outside the writable fixture. Keep private raw captures private until
  reviewed for secrets and unrelated host metadata.

## Acceptance, independent of the acting agent's summary

Run the unchanged original six tests and the external acceptance evaluator
after each attempt, including nonzero exits and timeouts. Publish all 17 named
checks and failed checks. Agents may add tests but cannot replace the frozen
external evaluator. Preserve the final diff and source hashes.

Separately inspect the host transcript and files for interpretation before
action, prediction before implementation, a recorded decision, verification
and limitations. These are author-scored observations, not a validated numeric
reasoning score. Record absence and uncertainty. A trail alone does not prove
faithful reasoning; full external capture requires a separate observer.

Host/authentication failure before model execution is inconclusive, not a PEA
failure or a baseline failure. Capture it and do not silently substitute models
or reuse the author's working session.

## Host amendments before any model execution

The initial 5-credit ceiling was rejected by CLI 1.0.79, whose minimum is
30. The owner explicitly approved 30 per session, four sessions maximum.
No model had run and no task result was observed when this amendment was made.
Earlier preflight output is retained: targets under the real user directory
inherited ancestor skills despite an isolated HOME, and the VS Code executable
shim could list skills but failed to start its Windows command wrapper.
Use a target outside personal skill ancestry and a qualified native CLI or
the installed npm-loader.js entry. These are host-only repairs, not replacement
of an observed baseline or PEA task result. The actual model defaults and
task/evaluator remain unchanged.

## Limits and next step

Two trials per arm cannot establish a causal advantage. The task is authored
by the framework's author, not sampled from representative engineering work.
Agents can solve it from the explicit specification without PEA. No cross-session
memory or convergence is tested. For those questions, see the existing
[benchmark and replication rules](../../harness/BENCHMARKS.md).
The next evidence step is independent practitioners trying their own bounded
tasks, including negative results and resource costs.
