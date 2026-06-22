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

Or copy the six skill folders into `<your-repo>/.copilot/skills/`: `intent/`, `destination/`, `improve/`, `trail/`, `retrospect/`, `probe/`.

## Set the destination (3 minutes)

In your target repo, ask the agent:

```
/destination capture the destination for this repo and write .acm/destination.md
```

When asked, answer briefly. One or two sentences per question is enough. The output is `.acm/destination.md`.

Done when: `.acm/destination.md` exists and you would not rewrite it from scratch tomorrow.

## Run one improve iteration (4 minutes)

Pick one small, verifiable thing. Then ask the agent:

```
/improve <one concrete, testable task in this repo>
```

Examples:

- `/improve remove unused imports across src/ and verify nothing breaks`
- `/improve tighten the README quickstart so a new user can run the first example in under five minutes`

The agent will narrate intent, predict an outcome before acting, make one change, verify it, and append an entry.

Done when: `.acm/audit-trail.md` has a new entry with `outcome:` and `delta:`.

## Confirm evidence exists (1 minute)

Open these and skim:

1. `.acm/destination.md` — destination is captured.
2. `.acm/audit-trail.md` — new entry has interpretation, decision, action, and outcome.
3. The change itself in the working tree.

If all three are present, the loop ran successfully end to end.

## Optional: lock in trail discipline

In your target repo:

```
bash harness/tools/install-hooks.sh     # macOS / Linux
pwsh harness/tools/install-hooks.ps1    # Windows
```

This rejects commits that touch substantive files without a corresponding `.acm/audit-trail.md` entry.

## If something went wrong

1. No `.acm/destination.md` created → re-run `/destination` and answer at least the first question.
2. No audit entry appended → re-run `/improve` with a smaller, more concrete task.
3. Agent did not narrate intent → ask it to apply `/intent` to your prompt first, then retry.
