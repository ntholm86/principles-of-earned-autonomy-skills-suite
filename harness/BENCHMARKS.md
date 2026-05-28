# Benchmarks

A small, rerunnable benchmark set for evaluating the skills on non-trivial targets with explicit replication rules and a public results matrix.

This file is the public surface for replication evidence. It defines benchmarks, lists current results, and is the place new evaluator-family runs are recorded.

## Replication Rules (required)

A benchmark run counts as replication evidence only if all conditions are met:

1. Fresh session (no prior evaluator context in the same chat/thread).
2. Evaluator family recorded (for example: Claude, GPT, Gemini).
3. Target and task are the same benchmark ID and acceptance criteria.
4. Trail entry is appended with outcome, delta, and session-file link.
5. At least one additional evaluator family reruns the same benchmark before the result is marked **Replicated**.

## Historical-Era Policy

The verifier enforces structural fidelity rules forward-only, from `SESSION_FIDELITY_CONTRACT_DATE` in `verify.py`. Entries strictly before that date are the **pre-contract era**.

- Pre-contract evidence may be cited as background but does not count toward Replicated status on its own.
- Replicated status requires at least one in-era run (on or after the contract date) for the same benchmark, by an evaluator family distinct from the seed.
- Pre-contract sessions are not retroactively rewritten; they remain as historical artifacts.

## Benchmark Set v0.1

| ID | Benchmark | Target class | Required skills | Acceptance criteria |
|---|---|---|---|---|
| B1 | External improve correctness pass | Foreign codebase (not authored by operator) | Improve + Trail | One verifiable correctness improvement landed; trail entry with prediction and outcome |
| B2 | External cross-session learning carry-forward | Same foreign codebase across at least 2 sessions | Improve + Retrospect + Trail | Session 2 acts on a Session 1 `[!REALIZATION]` without re-diagnosing it |
| B3 | Cold-target destination inference | Foreign codebase with no pre-seeded destination/trail | Destination + Trail | Operator confirms at least one inferred direction was correct and previously unwritten |
| B4 | Independent evaluator convergence check | Skills repo convergence pass under protocol | Improve + Trail | Three distinct evaluator families declare silence in succession under protocol |
| B5 | Benchmark target existence check | Local filesystem | verify.py | `verify.py` checks for the existence of `benchmark-b5-target/main.py` |

## Results Matrix v0.1

Status legend:
1. **Seed** — initial in-repo evidence, single evaluator family.
2. **In progress** — additional evaluator family run started, not yet completed.
3. **Replicated** — meets the replication rules and historical-era policy above.
4. **Pending** — no run by this evaluator family yet on this benchmark.

| Benchmark | Claude family | GPT family | Gemini family | Status |
|---|---|---|---|---|
| B1 | Seed (audit-trail entry `external-proof-vectorium-improve-run`) | Pending | Pending | Seed |
| B2 | Seed (audit-trail entry `external-proof-vectorium-arc`) | Pending | Pending | Seed |
| B3 | Seed (audit-trail Destination-on-cold-target entries) | Pending | Pending | Seed |
| B4 | Replicated (silence-1 / silence-2 / silence-3 entries) | Replicated (same chain) | Replicated (same chain) | Replicated |
| B5 | Pending | Pending | Pending | Pending |

## How to Add a New Run

1. Pick a benchmark ID from the set above.
2. Run it in a fresh session under the listed evaluator family.
3. Append an audit entry to `.trail/audit-trail.md` with `outcome`, `delta`, and `session-file:`.
4. Update the matching cell in the Results Matrix above with a short anchor to the audit entry.
5. If a benchmark reaches the replication rules and historical-era policy, mark its Status as **Replicated**.

## Out of Scope

- Confidential professional deployments are not published here unless de-identified and legally publishable.
- Benchmarks whose pass/fail is only inferable from narrative claims (no artifact-level evidence) are not added.
