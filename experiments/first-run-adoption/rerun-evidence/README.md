# Rerun Evidence

This directory preserves the single invocation authorized by `RERUN_PROTOCOL.md`.

- `fixture/` is the exact clean target source at baseline commit `395a3bafd37b21d1e3c897dfecb2dbb0c274a815`.
- `pre-run.json` records immediate eligibility state, CLI version, installed skills, and skill hashes.
- `pre-tests.txt` and `post-tests.txt` preserve focused test output.
- `cli.jsonl` and `cli.stderr.txt` are the complete CLI streams, decoded from PowerShell 5.1 UTF-16 redirection to UTF-8 without changing textual content.
- `run.json` records UTC timestamps, duration, and exit code.
- `post-run.json` records the unchanged target state.
- `target.diff` is intentionally empty because the model was unavailable before agent execution.

The external disposable target and isolated `COPILOT_HOME` are not evidence sources after this package is committed and may be removed.
