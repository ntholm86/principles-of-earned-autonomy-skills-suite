# 10-Minute First Successful Run

A minimal, copy-pasteable path to one real run that produces real evidence. Aim is one usable trail entry in under ten minutes.

## Prerequisites (1 minute)

1. A target repo you have write access to (yours or a fork).
2. A terminal in that repo's root.
3. VS Code with GitHub Copilot Chat, or any agent that loads skills from `~/.copilot/skills` (personal) or `.github/skills` (project; `.claude/skills` and `.agents/skills` are also recognised).
4. A memory repository for the records. Without one the run still works but is not recorded; [set one up below](#set-up-a-memory-and-make-a-first-record) (5 minutes, once).
5. Python 3 (`python`, or `python3` on macOS and Linux) and git for the optional helper scripts in `harness/tools/`.

## Install the skills (1 minute)

From a clone of this repo:

```
bash install.sh                                                       # macOS / Linux
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1     # Windows
```

The default installer includes the five operational skills and omits Probe, keeping the visible command surface focused on normal use. ARF researchers can add it with `bash install.sh --research` or `powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Research`.

Or copy the five operational skill folders into `~/.copilot/skills/` (all projects) or `<your-repo>/.github/skills/` (one project): `intent/`, `destination/`, `improve/`, `record/`, `learn/`. Add `probe/` only if you are conducting ARF research.

The operator workflow is **Run Improve**. Intent interprets each prompt, Record writes each result, and Improve automatically triggers Destination or Learn when accumulated evidence makes durable direction or a refreshed map useful. Probe is optional scientific instrumentation and is not required for this workflow.

## Set up a memory and make a first record

`<suite>` is your checkout of `principles-of-earned-autonomy-skills-suite`. Memory is a repository of its own, never a folder in your code.

```
git init <memory-folder>
```

Create an empty file `.acm-root` in it (`touch <memory-folder>/.acm-root`, or `New-Item <memory-folder>\.acm-root` in PowerShell), and a `.gitattributes` file containing `* text=auto eol=lf` so a mandate hashes the same on every operating system. Add the folder's absolute path as one line of `~/.acm/memories` (Windows: `%USERPROFILE%\.acm\memories`; UTF-8, with or without a BOM; create the file if missing; the environment variable `ACM_MEMORIES_FILE` names a different registry file).

In the work repository, bind it:

```
python <suite>/harness/tools/record.py resolve
```

It prints `unbound: ...` and the repository's root commit (a shallow clone is reported: fetch the full history first). With your confirmation, create `<memory-folder>/repositories/<id>/repository.json` using the full commit from `git rev-list --max-parents=0 HEAD`:

```json
{"id": "<id>", "root_commits": ["<that commit>"], "locators": ["<optional remote url>"]}
```

Now the mandate, `<memory-folder>/repositories/<id>/destination.md`:

```markdown
<!-- current-destination: complete -->
Make the checkout module easier to test without changing its public API.

## Human gate
A maintainer reviews every pull request before it merges. Before that review the agent may edit and test on a branch; without it, it may not merge or release.
<!-- destination-history -->
```

Make the first record from the work repository:

```
python <suite>/harness/tools/record.py new --slug first-run
```

It creates `<memory-folder>/repositories/<id>/records/<UTC yyyyMMddTHHmmssZ>-first-run.md`, a stub the agent fills in (the stub continues with the interpretation, decision, prediction, validation and reflection sections that `record/SKILL.md` describes):

```markdown
## 2026-11-22 — first-run

- record: 20261122T083358Z-first-run
- time: 2026-11-22T08:33:58Z
- scope: repositories/<id>
- repository: <id> @ <root commit>
- target: TODO
- operator: TODO
- agent: TODO (model family and version as the host exposes or the operator states; "unknown" if neither, never invented)
- authority: TODO (the prompt, destination or delegation this work acts under)
- session: TODO (the host's session or run identifier; "unknown" when not exposed)
- mandate: sha256:3aca039a5f52
- skill: improve
- outcome: TODO
- delta: TODO
```

`mandate:` is the first 12 hex characters of the governing `destination.md` (`none` when no destination governs). If the name already exists the command exits non-zero and writes nothing; run it again for a new timestamp. Replace every `TODO` before the record counts; the checker below warns about the ones left. Finally:

```
python <suite>/harness/tools/memory_check.py <memory-folder>
```

`PASS: 2 scope(s) checked, 0 failure(s), 0 warning(s)` means the layout, the binding, every mandate's Human gate and the record names are valid. Any failure exits non-zero and names the file.

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

Done when: the bound scope's `records/` has a new record (legacy in-repo memory: `.acm/audit-trail.md` has a new entry) with `outcome:` and `delta:`, and the run stated its mandate (a `mandate:` line, or that the run was ungoverned).

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
bash /path/to/principles-of-earned-autonomy-skills-suite/harness/tools/install-hooks.sh
powershell -NoProfile -ExecutionPolicy Bypass -File C:\path\to\principles-of-earned-autonomy-skills-suite\harness\tools\install-hooks.ps1
```

The installer respects `core.hooksPath` and stops without overwriting a different existing hook. Review the reported path before installing into a shared hook directory; see [INSTALLING.md](./INSTALLING.md) for existing-hook handling.

For legacy in-repo trails only: this rejects staged changes outside `.acm/`, including deletions, unless the commit also adds or modifies `.acm/audit-trail.md` or `.acm/<task>/audit-trail.md`. Commits confined to `.acm/` are allowed. The hook checks staged paths; it does not validate entry truthfulness or append-only integrity.

## If something went wrong

1. No audit entry appended → re-run `/improve` with a smaller, more concrete task.
2. Agent did not narrate intent → retry and report that automatic Intent composition failed; manually invoking `/intent` is a diagnostic, not a normal workflow step.
3. Destination triggered without directional evidence → ask the agent to name the accepted mandates or unresolved choice that triggered it; a missing file or iteration count is not sufficient.
