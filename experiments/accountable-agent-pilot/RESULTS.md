# First author-run pilot: useful code, missing decision records

Date: 2026-11-11. Author-run exploratory evidence, not independent validation.

**All four agents passed the 17 external feature checks. Neither PEA-labeled
session produced the required audit trail. This run does not demonstrate a
PEA advantage.**

## Frozen identity

- Protocol/runner revision at model invocation: the complete immutable revision
  is recorded in [the machine-readable evidence](./evidence.json).
- Parent public suite revision: `a2bb654e2a93e0a72564131c66a1eb20339aa37f`.
- Host: Windows; GitHub Copilot CLI 1.0.79; Node.js version in evidence.
- The runtime reported `claude-sonnet-5` in all four sessions. No model or
  reasoning override was supplied. These are one model family, not four
  independent evaluators.

## Outcomes

| Attempt | External feature checks | Original regression checks | Audit trail present | Observed wall time |
|---|---:|---:|---|---:|
| baseline-1 | 17/17 | 6/6 | No | 28.320 s |
| pea-1 | 17/17 | 6/6 | No | 38.319 s |
| pea-2 | 17/17 | 6/6 | No | 27.069 s |
| baseline-2 | 17/17 | 6/6 | No | 30.222 s |

Original regression checks were also rerun from an observer-owned copy after
the attempts, rather than trusting the agent-edited test file.
Wall time includes CLI/host overhead; do not infer an efficiency advantage
from these four observations. Each CLI result reported one premium request;
that is the CLI's unit, not a measured token total or monetary cost.

## What did and did not reach the model

Fresh discovery and runtime `session.skills_loaded` events listed exactly the
five project skills for PEA conditions, and no project skills for baseline
conditions. Both retained the CLI's same two built-in skills.

However, neither PEA transcript contains an operational SKILL.md content read
or an Improve invocation, and neither fixture contains an `.acm/audit-trail.md`.
The treatment was discoverable but was not demonstrated to have been applied.
One PEA run searched relative paths from the run directory before finding the
target, exposing working-directory ambiguity. We cannot separate host routing,
activation failure and instruction noncompliance from this evidence.

The functional result is valid for this fixture. The intended comparison of
PEA-governed versus baseline work is **inconclusive**, and the end-to-end
trace requirement was **not met** in the PEA-labeled attempts. Do not silently
discard these attempts or describe installation as successful activation.

## Host failures retained before the four model sessions

Earlier host-only checks invoked no model:

1. A target under the real user-directory ancestry inherited unrelated skills
   despite isolated HOME/config values. The runner refused to invoke.
2. The VS Code executable shim failed to start its Windows command wrapper.
3. The native CLI rejected the initial 5-credit cap; its minimum was 30.
   The owner then explicitly approved 30 per session, four sessions maximum.

No unfavorable completed model run was replaced.

## Reproducibility and next experiment

[evidence.json](./evidence.json) contains source hashes, all acceptance cases,
the final public fixture code/tests, recorded model identity and observable
tool-name sequences. Private raw host transcripts are retained by the author;
they are not published as independent reasoning evidence.

The current runner adds explicit `-C` targeting, removes three unknown tool
aliases, and reruns the original tests outside the agent-editable fixture.
These are harness corrections, not retroactive corrections to this result.
They have local harness tests, not a new successful live-model result.

A subsequent comparison requires a separately recorded protocol revision and
authorization. It must confirm actual skill activation before claiming that
PEA was exercised, retain the original failed/inconclusive attempt, and include
independent practitioners on nonconfidential tasks. No speed, general safety,
reasoning-faithfulness, cross-session-memory or adoption claim follows here.
