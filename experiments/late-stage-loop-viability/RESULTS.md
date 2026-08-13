# Late-Stage Loop Viability Results

Status: executed 2026-08-13; inconclusive because the silence snapshot has no eligible completed arm

## Execution summary

All eligible calls used the frozen host in `HOST.md`: GitHub Copilot CLI `1.0.79`, `claude-sonnet-4-5`, high effort, Anthropic BYOK through the release proxy, identity encoding, and exact copies of the five frozen suite skills.

| Lifecycle position | Snapshot | Opaque case | Outcome | Calls | Input tokens | Output tokens | Duration |
|---|---|---|---|---:|---:|---:|---:|
| Open gap | `9f7e83219d563f40dcc170745f3a0a0451dd33aa` | `case-lumen` | Material advance | 32 | 4,111 | 20,003 | 549.787 s |
| Near silence | `d42cf6aed7dbc3576c9c4d200ff59213a692a507` | `case-cedar` | Bounded minor advance | 23 | 4,799 | 13,134 | 360.827 s |
| Silence | `14fcf9f927539a7afb60ec95b611c47c39b3195d` | `case-flint` | Excluded | unavailable | unavailable | unavailable | unavailable |

Input and output counts are provider-reported fields summed independently from the hash-chained proxy ledger. Cached-input fields remain only in each entry's native `usage.raw` object and are not added to `input_tokens`.

## Silence-snapshot exclusion

The first silence-snapshot invocation used harness session `01KZXH0ZZMVDBVD355023C1FC7`. It began after the all-arm clean preflight, made 22 usage-bearing model calls between 12:20:03Z and 12:23:50Z, and ended mid-reasoning. It produced no CLI completion record, no Trail entry, and no tracked target change. Its ledger contains 8,235 input tokens and 7,832 output tokens, but those resource values describe an incomplete attempt and are ineligible for lifecycle comparison.

A second invocation, session `01KZXH8WBF8R16SS42A4QTHEFP`, was accidentally launched at 12:24:08Z. Its own `pre-run.json` records `?? .acm/sessions/`, proving that it violated the clean-worktree precondition. It exited 0 after nine calls by asking whether the repository was the intended target, despite `--no-ask-user`; it produced no Trail and no tracked change. This duplicate is preserved but excluded. It cannot replace or repair the authorized first attempt.

The blinded `case-flint` package was built from the duplicate before the contamination was discovered. Independent adjudication classified it `Invalid`. That evaluator result is retained as evidence about the duplicate, not reported as the silence arm's outcome.

## Blinded outcomes

The evaluator received opaque cases in non-lifecycle order and no resource usage, run ordering, snapshot commits, lifecycle labels, or experiment hypothesis.

- `case-lumen`: **Material advance**. The run implemented the confirmed Destination requirement that Standard and Full share Improve-grade reasoning operations while differing in recording depth; it updated the skill and README to v3.7.0, recorded full Trail reasoning, and refreshed Orientation against the changed Destination basis.
- `case-cedar`: **Bounded minor advance**. The run removed one external Destination reference that violated the stranger-accessibility bar, preserved behavior and version, and recorded compact prediction and validation evidence.
- `case-flint`: **Invalid**. The duplicate stopped without completing work or mandatory Trail evidence; empty target output was not supported as bounded silence.

## Facts

- From open gap to near silence, model calls fell from 32 to 23, output tokens fell from 20,003 to 13,134, and duration fell from 549.787 seconds to 360.827 seconds.
- Provider-reported input tokens rose from 4,111 to 4,799.
- The independently evaluated outcome narrowed from Material advance to Bounded minor advance.
- Every ledger entry in both eligible arms contained usage.
- No eligible completed silence arm exists.

## Interpretation

The two eligible observations are compatible with resource use falling as work narrows for calls, output tokens, and duration, but input tokens move in the opposite direction. Two lifecycle positions cannot establish the late-stage pattern, and the missing silence outcome prevents assessing whether convergence evidence explains silence cost.

Under `PROTOCOL.md`, the experiment is **inconclusive**. It supports neither a production change nor a claim of permanent loop viability. Production Improve remains frozen and unchanged by this experiment.

## Evidence layout

- `evidence/open-gap/`: raw CLI trace, hash-chained ledger, timing and Git state, usage summary, and target diff.
- `evidence/near-silence/`: the same evidence set for the eligible near-silence arm.
- `evidence/silence-excluded/`: both silence-snapshot ledgers, duplicate CLI trace, duplicate pre/post state, and exclusion notes.
- `evidence/blinded/`: the exact opaque packages supplied to evaluators.
- `EVALUATION.md`: evaluator outputs and adjudication record.
