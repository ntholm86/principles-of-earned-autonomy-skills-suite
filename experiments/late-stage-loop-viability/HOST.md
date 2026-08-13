# Late-Stage Loop Viability Host Configuration

Status: pre-registered and frozen 2026-08-13; execution evidence is reported in `RESULTS.md`

This file freezes the execution host required by `PROTOCOL.md` and `SNAPSHOTS.md`. Changing any item below after the first arm starts invalidates same-host comparison unless every arm is discarded and restarted under a newly preregistered configuration.

## Host

- Product: GitHub Copilot CLI
- Version: `1.0.79`
- Mode: non-interactive prompt mode
- Provider mode: Anthropic BYOK through local `llm-harness-proxy`
- Proxy source commits: `36c6151` usage capture, `e17e2a8` buffered integration proof, `cd33c15` SSE integration proof
- Proxy endpoint: `http://127.0.0.1:8475`
- Model ID and wire model: `claude-sonnet-4-5`
- Reasoning effort: `high`
- Streaming: `off`
- Auto-update: disabled
- Remote control and export: disabled
- Built-in MCP servers: disabled
- Custom instructions: disabled
- Prompt-mode memory: disabled by omission of `--enable-memory`
- Operator questions: disabled with `--no-ask-user`

The executable and release proxy binary MUST be built or installed before the first arm and MUST NOT change between arms.

## Frozen suite

Each arm gets a fresh isolated `COPILOT_HOME` containing only exact copies of these five files from skills commit `3676411`:

| Skill | Version | SHA-256 |
|---|---:|---|
| `improve` | 3.17.0 | `194BBC64A6E9FACA407B8EAC3611703BB3C9E468B0DB8AB901D247A152D2F035` |
| `intent` | 1.7.0 | `9DF886398B4FD95CDA59A527E63099E9F5BE400BB7BEEDA6748D8E4BB8FB1AC2` |
| `trail` | 2.5.1 | `E002B5F82856CDD72C5E1CF599DAB82DDAFF405BF39CA1AF4D2DD988CA1EF04A` |
| `destination` | 2.7.0 | `0FC52CAC353FFDDF43BD21518C37A480CBB844EADA81740A7541AAAAB02A4465` |
| `orient` | 2.7.0 | `7882260F4C2808070A60ACD5C767C26BD9B73C8316655040B337608F09A07930` |

Direct Git comparison confirms all five files are unchanged between commit `3676411` and current preregistration commit. Built-in CLI skills remain discoverable but are unrelated to the fixed prompt and built-in MCP servers are disabled.

## Prompt

Every arm receives this exact operator prompt:

> Invoke the improve skill. Improve this target.

The working directory identifies the target. No lifecycle label, commit subject, expected result, hypothesis, or resource information appears in the prompt.

## Tool and path policy

- Run from the root of one detached snapshot worktree.
- Use `--allow-all-tools` so production Improve can inspect, edit, validate, record, and commit.
- Keep normal CLI path confinement to the worktree and add `--disallow-temp-dir`.
- Deny `shell(git push)`.
- Deny URL access.
- Do not add directories outside the detached worktree.
- Start from a clean worktree and preserve the complete post-run repository state for outcome packaging.

## Provider and ledger controls

Set these environment variables separately for each arm:

- `COPILOT_HOME`: fresh arm-specific isolated directory containing the frozen suite.
- `COPILOT_PROVIDER_BASE_URL=http://127.0.0.1:8475`
- `COPILOT_PROVIDER_TYPE=anthropic`
- `COPILOT_PROVIDER_API_KEY`: sourced directly from `ANTHROPIC_API_KEY`; never written to an artifact.
- `COPILOT_MODEL=claude-sonnet-4-5`
- `COPILOT_PROVIDER_HEADERS`: exactly three provider-only headers:
  - `Accept-Encoding: identity`
  - `X-Harness-Session: <fresh 26-character ULID>`
  - `X-Harness-Root: <detached-worktree>/.acm`

`Accept-Encoding: identity` is mandatory. Host qualification without it produced six retries whose ledger entries had empty `reason` and `usage: null`. Repeating the same qualification with it produced a valid five-entry hash chain with provider-reported usage on every model call.

Start the release proxy with `HARNESS_LISTEN=127.0.0.1:8475`. Per-request `X-Harness-Root` and `X-Harness-Session` remain authoritative.

## Command shape

Run each arm once using this fixed argument shape, substituting only arm-local paths and the fresh session ULID:

```text
copilot -C <detached-worktree> -p "Invoke the improve skill. Improve this target." --output-format json --allow-all-tools --deny-tool="shell(git push)" --deny-tool="url" --disallow-temp-dir --disable-builtin-mcps --no-custom-instructions --no-ask-user --no-auto-update --no-remote --no-remote-export --stream off --effort high --secret-env-vars=ANTHROPIC_API_KEY,COPILOT_PROVIDER_API_KEY
```

Capture stdout JSONL and wall-clock start/end outside the arm worktree. Do not feed host output from one arm into another.

## Evidence per arm

Preserve before evaluation:

- snapshot commit and detached worktree path;
- CLI version and suite hashes;
- fresh CLI session ID and harness ULID;
- complete CLI JSONL output;
- complete hash-chained harness session JSONL;
- sum of provider-reported `input_tokens` and `output_tokens` across ledger entries;
- ledger entry count as model-call count;
- wall-clock duration;
- pre-run and post-run Git status, HEAD, diff, and commits;
- validation outputs and the Trail entry produced by Improve.

Do not collapse cached-input fields into `input_tokens`. Preserve every native usage object under `usage.raw` for later analysis.

## Qualification evidence

No selected arm was used for qualification.

A read-only smoke prompt under Copilot CLI `1.0.79` loaded Improve `3.17.0`, invoked its skill tool, narrated Intent, made zero file changes, and exited successfully when routed through the instrumented proxy with identity encoding. Its five ledger entries contained exact provider usage and one hash chain. The smoke also showed that installing Improve alone triggers standalone Intent fallback; the frozen host therefore installs all five production-suite skills in every fresh arm home.

Qualification establishes host capability, not an experiment result. Arm execution remains prohibited until this file and the corresponding manifest update are committed.
