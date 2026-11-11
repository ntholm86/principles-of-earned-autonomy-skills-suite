# Try accountable AI work on one bounded task

**Principles of Earned Autonomy** is Nils Wendelboe Holmager's proposed
governance framework. The **PEA Skills Suite** is a practical reference
implementation, not a certificate that an agent is safe.

This pilot makes a narrower question testable: can an agent deliver a working
change and leave enough evidence for you to examine its interpretation,
prediction, decisions and verification?

## Try it yourself

Requirements: Git, Node.js 22+ and an existing supported AI coding-agent account.
The fixture has no npm dependencies. No email, signup or telemetry is added.

1. Clone the suite and note `git rev-parse HEAD`.
2. Copy this directory's `fixture` folder to a new disposable directory outside
   your real projects; open that copy in your agent.
3. Run `node --test cart.test.mjs`: the six baseline tests should pass.
4. Install the five operational skills using the suite's
   [installation guide](../../INSTALLING.md). Use a supported project-local
   discovery path for your host; do not overwrite existing personal skills.
5. Invoke Improve with the [frozen task](./PROTOCOL.md#common-task-verbatim).
   Inspect the interpretation, approve only the bounded change and stop if
   it asks for broader authority.
6. Rerun the tests. From this pilot directory, independently run
   `node acceptance.mjs "ABSOLUTE_PATH_TO_YOUR_FIXTURE_COPY"`.
   All 17 checks must pass to meet this fixture's functional acceptance.
7. Inspect the new `.acm/audit-trail.md`. Can you find what was intended,
   predicted, changed, verified and left uncertain? Compare it with the actual
   diff and host transcript, not merely the agent's final answer.

Before the task, the unmodified fixture intentionally passes only 5/17 feature
checks. That is the missing feature, not a baseline-agent result. Do not copy
an expected implementation into the fixture before trying it.

## Reproduce the author-run comparison

Read [PROTOCOL.md](./PROTOCOL.md) before invoking anything. Four new sessions
consume your existing AI allowance; the runner caps each at 240 seconds and
5 CLI credits. It never replaces failed attempts.

On Windows PowerShell, from this directory:

```powershell
$env:PILOT_COPILOT = (Get-Command copilot).Source
node .\run.mjs "$env:TEMP\pea-pilot-UNIQUE-RUN-NAME"
```

The output directory must not already exist. On macOS/Linux, set
`PILOT_COPILOT` to the actual CLI executable and supply a new absolute output
path. The runner is initially qualified only on the recorded Windows host;
verify your host's discovery/authentication behavior rather than assuming it.

The runner isolates each session's home/config and preserves all original
outputs outside the writable fixture. Isolation is an experimental control,
not an OS security sandbox. Review captured files before sharing: your host
may include account details or other private metadata.

## Seeking five independent practitioners

Try one bounded, nonconfidential task of your own. A useful report includes:

- Host, model if known, suite commit and task.
- What you expected; what actually happened, including failures.
- Tests and diff supporting functional results.
- Whether the evidence helped you understand or challenge a decision.
- Time/cost if actually recorded; whether you chose to use it again.

[Open a pilot report](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite/issues/new?template=pilot-report.yml).
Do not post credentials, employer code, private transcripts or personal data.
You can report a failed installation or abandon the pilot; no positive
testimonial is expected. Reporting publicly is optional.

No participant has been recruited merely because this invitation exists.
Independent use, permission to quote and permission to name an organization
are separate decisions.

## Limits

This synthetic task is small and explicitly specified; a baseline agent can
solve it without PEA. Neither passing tests nor a persuasive trail demonstrates
faithful internal reasoning, general safety, clinical validity or broad
adoption. This task does not test cross-session memory or independent
convergence. Existing [benchmark replication rules](../../harness/BENCHMARKS.md)
remain separate.

Author: [Nils Wendelboe Holmager](https://nilsholmager.com/).
Code and documents in this pilot use the suite's [MIT license](../../LICENSE).
Framework: [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy).
