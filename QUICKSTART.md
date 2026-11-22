# 10-Minute First Successful Run

A minimal, copy-pasteable path to one real run that produces real evidence. Aim is one usable trail entry in under ten minutes.

## Prerequisites (1 minute)

1. A target repo you have write access to (yours or a fork).
2. A terminal in that repo's root.
3. VS Code with GitHub Copilot Chat, or any agent that loads `.copilot/skills/`.
4. A shared ACM memory repository, cloned once, with its absolute path as a line of `~/.acm/memories` (Windows: `%USERPROFILE%\.acm\memories`). The target is bound by `repositories/<id>/repository.json` listing its root commit (`git rev-list --max-parents=0 HEAD`); the agent offers to create it with your confirmation. Without a binding the run still works but is not recorded. See [Record](./record/SKILL.md#where-memory-lives).

## Install the skills (1 minute)

From a clone of this repo:

```
bash install.sh                                                       # macOS / Linux
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1     # Windows
```

The default installer includes the five operational skills and omits Probe, keeping the visible command surface focused on normal use. ARF researchers can add it with `bash install.sh --research` or `powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Research`.

Or copy the five operational skill folders into `<your-repo>/.copilot/skills/`: `intent/`, `destination/`, `improve/`, `record/`, `learn/`. Add `probe/` only if you are conducting ARF research.

The operator workflow is **Run Improve**. Intent interprets each prompt, Record writes each result, and Improve automatically triggers Destination or Learn when accumulated evidence makes durable direction or a refreshed map useful. Probe is optional scientific instrumentation and is not required for this workflow.

## Run one improve iteration (7 minutes)

Pick one small, verifiable thing. Then ask the agent:

```
/improve <one concrete, testable task in this repo>
```

Examples:

- `/improve remove unused imports across src/ and verify nothing breaks`
- `/improve tighten the README quickstart so a new user can run the first example in under five minutes`

The agent applies Intent and asks you to **Confirm**, **Stop**, or **Specify** its reading. After examination, Improve states one proposed change and asks you to **Proceed**, **Stop**, or **Specify** before implementation. Specify restarts the reasoning with your added information. A completed run makes one change, verifies it, applies Record, and ends with one short change-and-verification summary.

Once the suite has earned your trust, explicitly delegate either routine gate in the prompt or in Destination. Delegation does not silence the narration, the final summary, unresolved Destination questions, or operator-declared consequential gates. Host autopilot alone grants no such authority.

If continuing safely requires broader direction, Improve explains why and invokes Destination after the completed run to ask one sourced question at a time.

Done when: the bound scope's `records/` has a new record (legacy in-repo memory: `.acm/audit-trail.md` has a new entry) with `outcome:` and `delta:`.

## Confirm evidence exists (1 minute)

Open these and skim:

1. The new trail record — it has interpretation, decision, action, and outcome.
2. The change itself in the working tree.
3. The scope's `destination.md`, if Improve found enough directional evidence to trigger Destination.

The first two are sufficient for a successful first run. Destination is created when the work needs durable cross-run direction, not as setup ceremony.

## Learning happens automatically

You do not need to count iterations or remember a Learn step. A material Destination change schedules Learn. Improve also evaluates learning freshness after every recorded run and schedules Learn when the trail forms a meaningful arc, contradicts the current learning, or approaches convergence.

For a diagnostic arc-read at any time, you can still run:

```
/learn read the accumulated trail and tell me whether the loop is still working on the right things
```

Manual `/learn` is an override, not part of the normal workflow.

## Optional: lock in trail discipline

The one-line installer does not copy optional tooling. From your target repo, invoke the hook installer by its path in your cloned skills suite:

```
bash /path/to/autonomous-agent-skills/harness/tools/install-hooks.sh
powershell -NoProfile -ExecutionPolicy Bypass -File C:\path\to\autonomous-agent-skills\harness\tools\install-hooks.ps1
```

The installer respects `core.hooksPath` and stops without overwriting a different existing hook. Review the reported path before installing into a shared hook directory; see [INSTALLING.md](./INSTALLING.md) for existing-hook handling.

For legacy in-repo trails only: this rejects staged changes outside `.acm/`, including deletions, unless the commit also adds or modifies `.acm/audit-trail.md` or `.acm/<task>/audit-trail.md`. Commits confined to `.acm/` are allowed. The hook checks staged paths; it does not validate entry truthfulness or append-only integrity.

## If something went wrong

1. No audit entry appended → re-run `/improve` with a smaller, more concrete task.
2. Agent did not narrate intent → retry and report that automatic Intent composition failed; manually invoking `/intent` is a diagnostic, not a normal workflow step.
3. Destination triggered without directional evidence → ask the agent to name the accepted mandates or unresolved choice that triggered it; a missing file or iteration count is not sufficient.
