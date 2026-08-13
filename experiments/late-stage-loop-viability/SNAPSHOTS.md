# Late-Stage Loop Viability Snapshots

Status: pre-registered 2026-08-13; no experiment evaluator has run

This manifest applies `PROTOCOL.md` to `C:\git\pea\work-skill`. Snapshot selection uses only Git history and Trail evidence that existed before this experiment. It does not use expected token cost or knowledge of future experimental outputs.

## Target eligibility

Work is eligible for lifecycle reconstruction:

- `.acm/destination.md` existed from commit `bf7b972605f90f5f32cce07ba998ff0e52204b33` on 2026-07-03, before every selected snapshot.
- Every selected commit contains `.acm/destination.md`, `.acm/audit-trail.md`, `work/SKILL.md`, and `README.md`.
- The selected arc records a material reasoning-contract advance, a later narrowing sequence, and bounded silence.
- The bounded-silence commit `54fe407cb20b8a92f555817bcd11e589b4763cbf` changes only `.acm/audit-trail.md`; the evaluated target artifact is unchanged from its parent.

The current `work-skill` checkout has unrelated untracked `docs/` content. Experimental arms must use detached Git worktrees created from the commits below, not the current checkout.

## Selected snapshots

### Open gap

- Commit: `9f7e83219d563f40dcc170745f3a0a0451dd33aa`
- Commit subject: `Refine Destination around trusted compression and reasoning depth`
- Pre-existing evidence: Trail entry `destination-interview-trusted-compression-and-reasoning-depth` records the confirmed gap. Work must preserve Improve-grade judgment while reducing daily-use cost.
- Selection reason: this is the versioned-Destination state immediately before commit `c7d188c327256de34c4be128a7bd941710cacda3` materially changed the reasoning contract and Orientation.

### Near silence

- Commit: `d42cf6aed7dbc3576c9c4d200ff59213a692a507`
- Commit subject: `Resolve append-only destination history`
- Pre-existing evidence: Trail entry `independently-evaluate-v3-8-1-handoff` records an independent false positive that exposed temporal ambiguity in append-only Destination history, followed by the v3.8.2 repair.
- Selection reason: several major advances were already present, while one further independently observed Trail-timing overclaim remained and was corrected in the next commit.

### Silence

- Commit: `14fcf9f927539a7afb60ec95b611c47c39b3195d`
- Commit subject: `Clarify Trail timing assurance`
- Pre-existing evidence: Trail entry `convert-temporal-destination-resolution` records the v3.8.3 correction and names the remaining untested behavioral boundary. The next commit, `54fe407cb20b8a92f555817bcd11e589b4763cbf`, records `bounded-silence-after-v3-8-3` and changes only `.acm/audit-trail.md`.
- Selection reason: this is the exact target artifact and contemporaneous memory evaluated as bounded silence.

## Reconstruction controls

- Create each arm from its exact commit in a separate detached worktree.
- Do not copy the current Work Destination, Orientation, Trail, README, or skill into an older arm.
- Supply the same production Improve contract and same operator-prompt form to every arm, as required by `PROTOCOL.md`.
- Record exclusions before evaluation if a host cannot keep later Work or skills evidence out of an arm.
- Keep lifecycle labels, commit ordering, expected results, and resource evidence hidden from the blinded outcome evaluator.

## Resource-capture gate

Independent token capture and host fidelity are preregistered. No experiment arm has run.

The owning `llm-harness-proxy` repository added provider-reported usage capture in commit `36c6151` (`feat: capture provider token usage`). Commits `e17e2a8` and `cd33c15` prove buffered and SSE handler-to-ledger integration. The Rust suite passes 43 tests.

A controlled live Anthropic call through the release proxy produced matching response and ledger counts: 13 input tokens and 5 output tokens. The sequence-zero ledger entry also preserved Anthropic's native cache, service-tier, and inference metadata under `usage.raw`. This discharges the prior instrumentation blocker for buffered Anthropic runs; historical sessions remain ineligible and are not retroactively estimated.

Host exploration rejected two substitute paths:

- The VS Code host can execute the production Improve skill but its model traffic is not routed through the local proxy, so independent usage is unavailable.
- `ai-steward` routes all Anthropic calls through the proxy and groups them in an independent session ledger, but it substitutes its own SCAN / IMPLEMENT / REFLECT prompts and scope policy for the snapshot's production Improve contract.

The operator authorized installation and qualification of GitHub Copilot CLI as the fixed host candidate. `HOST.md` freezes Copilot CLI `1.0.79`, Anthropic BYOK through the usage-capturing proxy, `claude-sonnet-4-5`, the exact production suite, prompt, tool policy, isolation controls, and evidence package before arm execution.

A non-arm smoke session loaded Improve `3.17.0`, invoked the skill, narrated Intent, made no file changes, exited successfully, and produced a five-call usage-bearing hash chain. Qualification also established `Accept-Encoding: identity` as mandatory: without it, compressed Anthropic SSE was forwarded but not parsed, causing six retries with empty ledger content.

Do not run an arm through `ai-steward`, a direct Anthropic completion, or another substitute prompt. Those routes would measure a different loop. Every arm MUST follow `HOST.md`; a host, model, suite, prompt, permission, or transport change after the first arm starts invalidates comparison unless all arms are discarded and restarted under a new preregistration.