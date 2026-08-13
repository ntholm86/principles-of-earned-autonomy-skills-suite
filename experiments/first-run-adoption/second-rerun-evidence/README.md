# Second First-Run Rerun Evidence

This directory preserves the one invocation authorized by `SECOND_RERUN_PROTOCOL.md`. The classification is Pass for simulated first-run operability only.

## Invocation

- Baseline target commit: `63f0498fb3c1f4a0f2ea2a5999a50ac13283b2df`
- Result target commit: `cac47f293906dc9c05057ae7e7bb93b837e34cb7`
- Requested harness session: `8XQZKRX436ZT0TQ1WQM3W7WTS4`
- CLI exit: `0`
- Duration: `132.976` seconds
- Provider ledgers: 10 files, 10 entries, usage present on every entry
- Provider totals: 71 top-level input tokens, 4,556 output tokens

The ten emitted ledger SIDs differ from the requested harness session. Attribution is unambiguous because the harness root was empty before the call and contains only these ledgers afterward. Caller control of ledger identity or grouping is not established.

## Contents

- `fixture/` is the byte-matching preregistered baseline fixture.
- `target/` is the committed post-run target, including its Trail.
- `target.patch` records the baseline-to-result committed patch; `target.diff` records the clean post-run worktree diff.
- `commits.txt` records the result commit identity.
- `preflight.json` and `run.json` record the final eligibility boundary and invocation.
- `failed-preflight.json`, `failed-preflight-incident.json`, `setup-incident.txt`, and `preflight-cache-status.txt` preserve pre-call setup deviations.
- `baseline-tests.txt`, `final-preflight-tests.raw.txt`, and `post-tests.txt` preserve test evidence in UTF-8.
- `cli.jsonl` and `cli.stderr.txt` are the complete CLI streams converted from PowerShell UTF-16 redirection to UTF-8 without changing textual content.
- `event-summary.json` derives service and tool chronology from `cli.jsonl`.
- `ledgers/` contains every byte-preserved proxy ledger.
- `provider-usage.json` derives emitted SIDs and usage totals from those ledgers.
- `installed-files.txt` and `preflight.json` record the isolated suite payload and hashes.
- `post-state.json` records clean committed target state and passing post-run tests.
- `MANIFEST.md` records byte size and SHA-256 for every evidence file except itself.

Derived summaries are conveniences. Raw streams, repository state, and proxy ledgers remain authoritative.
