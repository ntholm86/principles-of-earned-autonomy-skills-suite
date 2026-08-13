# Host Qualification Evidence

This directory preserves the single non-experimental call authorized by `HOST_QUALIFICATION.md`.

- `preflight.json` records CLI version, proxy binary identity, installed skill names, and skill hashes.
- `run.json` records requested harness session value, UTC timestamps, duration, and exit code.
- `cli.jsonl` and `cli.stderr.txt` are the complete CLI streams converted from PowerShell 5.1 UTF-16 redirection to UTF-8 without changing textual content.
- `ledger.jsonl` is the byte-preserved proxy ledger.
- `work-state.json` records that the disposable working directory remained empty.
- `MANIFEST.md` records byte size and SHA-256 for every evidence file except itself.

The requested harness session header and emitted ledger SID differ. Because the disposable ledger root contains exactly one session file, attribution of this call is unambiguous; caller control of the ledger SID is not established.
