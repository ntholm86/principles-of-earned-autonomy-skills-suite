# Evidence Layout

The `open-gap/` and `near-silence/` directories contain the two eligible completed arms. Their raw CLI JSONL, provider ledger, state captures, usage summary, and target diff are preserved together.

The `silence-excluded/` directory preserves both ineligible invocations:

- `first-incomplete-ledger.jsonl` is the authorized first attempt. It ended mid-reasoning without a CLI completion artifact, Trail entry, or tracked target change.
- Files prefixed `duplicate-` are the accidental second invocation. Its `duplicate-pre-run.json` records `pre_status: "?? .acm/sessions/"`, so it began from a dirty worktree and cannot substitute for the incomplete attempt.

The first attempt has no reconstructed CLI JSONL, pre-run capture, post-run capture, or duration. None is inferred. Both ledgers are retained so the exclusion remains independently inspectable.

The `blinded/` directory contains the exact opaque packages supplied for outcome evaluation. `case-lumen` maps to the open-gap arm, `case-cedar` maps to the near-silence arm, and `case-flint` maps to the invalid duplicate. The mapping was withheld from evaluators until after classification.

`git-status.txt` files were regenerated from the experiment worktrees as UTF-8 because the original PowerShell 5.1 captures were UTF-16 and the skills repository requires UTF-8 text. All other copied evidence is byte-preserved. `MANIFEST.md` records byte sizes and SHA-256 hashes for the published evidence files; it excludes itself.
