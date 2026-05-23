# Benchmarks

This file publishes a small, rerunnable benchmark set for evaluating the skills on non-trivial targets with explicit replication rules.

Scope: benchmark definitions, current evidence, and replication protocol.

## Replication Rules (required)

A benchmark run counts as replication evidence only if all conditions are met:

1. Fresh session (no prior evaluator context in the same chat/thread).
2. Evaluator family recorded (for example: Claude, GPT, Gemini).
3. Target and task are the same benchmark ID and acceptance criteria.
4. Trail entry is appended with outcome, delta, and session-file link.
5. Independent rerun by at least one additional evaluator family.

## Benchmark Set v0.1

| ID | Benchmark | Target class | Required skills | Replication evidence | Status |
|---|---|---|---|---|---|
| B1 | External improve correctness pass | Foreign codebase (not authored by operator) | Improve + Trail | `.trail/audit-trail.md` entry slug `external-proof-vectorium-improve-run` and follow-up external arc entries | Seed evidence published |
| B2 | External cross-session learning carry-forward | Same foreign codebase across at least 2 sessions | Improve + Retrospect + Trail | `.trail/audit-trail.md` entries documenting session 1 realization and session 2 acted-on follow-up | Seed evidence published |
| B3 | Cold-target vision inference | Foreign codebase with no pre-seeded vision/trail | Vision + Trail | `.trail/audit-trail.md` Vision-on-cold-target entries; operator confirmation captured in session file | Seed evidence published |
| B4 | Independent evaluator convergence check | Skills repo convergence pass under protocol | Improve + Trail | Three distinct evaluator families declaring silence under protocol (see README convergence claim) | Replicated |

## Current Evidence Notes

- B1/B2/B3 have public seed evidence in this repository trail, but should still be replicated by additional independent evaluator families on equivalent targets.
- B4 has cross-family replication evidence (Claude, GPT, Gemini) and serves as the current strongest independence signal in-repo.
- Confidential professional deployments remain out of scope for this file unless de-identified and legally publishable.

## How to Add a New Benchmark

Add one row to the table with:

- benchmark ID and one-sentence task definition
- target class (what kind of repo/system)
- required skills
- exact acceptance criteria and evidence location
- replication status

Prefer benchmarks where pass/fail is observable from artifacts, not only narrative claims.
