# 10-Minute First Successful Run

A minimal, copy-pasteable path to one real run that produces real evidence. Aim is one usable trail entry in under ten minutes.

## Prerequisites (1 minute)

1. A target repo you have write access to (yours or a fork).
2. A terminal in that repo's root.
3. VS Code with GitHub Copilot Chat, or any agent that loads `.copilot/skills/`.

## Install the skills (1 minute)

From a clone of this repo:

```
bash install.sh                 # macOS / Linux
pwsh install.ps1                # Windows
```

The default installer includes the five operational skills and omits Probe, keeping the visible command surface focused on normal use. ARF researchers can add it with `bash install.sh --research` or `pwsh install.ps1 -Research`.

Or copy the five operational skill folders into `<your-repo>/.copilot/skills/`: `intent/`, `destination/`, `improve/`, `trail/`, `orient/`. Add `probe/` only if you are conducting ARF research.

The operator workflow is **Run Improve**. Intent interprets each prompt, Trail records each result, and Improve automatically triggers Destination or Orient when accumulated evidence makes durable direction or a refreshed map useful. Probe is optional scientific instrumentation and is not required for this workflow.

## Run one improve iteration (7 minutes)

Pick one small, verifiable thing. Then ask the agent:

```
/improve <one concrete, testable task in this repo>
```

Examples:

- `/improve remove unused imports across src/ and verify nothing breaks`
- `/improve tighten the README quickstart so a new user can run the first example in under five minutes`

The agent automatically applies Intent, explains the mandate it inferred from your prompt, predicts an outcome before acting, makes one change, verifies it, and applies Trail. If continuing safely now requires broader direction, it explains why and invokes Destination after the completed run to ask one sourced question at a time.

Done when: `.acm/audit-trail.md` has a new entry with `outcome:` and `delta:`.

## Confirm evidence exists (1 minute)

Open these and skim:

1. `.acm/audit-trail.md` — the new entry has interpretation, decision, action, and outcome.
2. The change itself in the working tree.
3. `.acm/destination.md`, if Improve found enough directional evidence to trigger Destination.

The first two are sufficient for a successful first run. Destination is created when the work needs durable cross-run direction, not as setup ceremony.

## Orientation happens automatically

You do not need to count iterations or remember an Orient step. A material Destination change schedules Orient. Improve also evaluates orientation freshness after every recorded run and schedules Orient when the trail forms a meaningful arc, contradicts the current orientation, or approaches convergence.

For a diagnostic arc-read at any time, you can still run:

```
/orient read the accumulated trail and tell me whether the loop is still working on the right things
```

Manual `/orient` is an override, not part of the normal workflow.

## Optional: lock in trail discipline

The one-line installer does not copy optional tooling. From your target repo, invoke the hook installer by its path in your cloned skills suite:

```
bash /path/to/autonomous-agent-skills/harness/tools/install-hooks.sh
pwsh C:\path\to\autonomous-agent-skills\harness\tools\install-hooks.ps1
```

This rejects commits that touch substantive files without a corresponding `.acm/audit-trail.md` entry.

## If something went wrong

1. No audit entry appended → re-run `/improve` with a smaller, more concrete task.
2. Agent did not narrate intent → retry and report that automatic Intent composition failed; manually invoking `/intent` is a diagnostic, not a normal workflow step.
3. Destination triggered without directional evidence → ask the agent to name the accepted mandates or unresolved choice that triggered it; a missing file or iteration count is not sufficient.
