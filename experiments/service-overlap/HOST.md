# Service Overlap Interactive Host

Status: preregistered 2026-08-13; not yet invoked

## Frozen identities

- Skills source: committed `main` checkout containing this host record and the frozen fixture.
- GitHub Copilot CLI: `1.0.79`.
- Model: `claude-sonnet-4-5`, high reasoning effort.
- Provider: Anthropic BYOK through `llm-harness-proxy` at `http://127.0.0.1:8475`.
- Proxy binary: `C:\git\pea\llm-harness-proxy\proxy-rust\target\release\llm-harness-proxy.exe`.
- Proxy SHA-256: `241626F7D51A945F9C48286EFF26E055FDDA9137C2635DE1FD35094D391701C3`.
- CLI session UUID: `34c4fdd7-0b91-40c2-9aa5-421bddf2b089`.
- Requested harness session: `KYP13KYMCBJZ2MWJC3XNP97Z31`.
- Provider headers: `Accept-Encoding: identity`, the requested harness session, and a fresh disposable harness root.

The requested harness identifier does not imply control of emitted proxy SIDs. Preserve all emitted SIDs separately.

## Disposable roots

Create fresh roots only after this host record is committed:

- target: `C:\git\pea-service-overlap-target`
- Copilot home: `%TEMP%\pea-service-overlap-copilot-home`
- capture: `%TEMP%\pea-service-overlap-capture`
- harness: `%TEMP%\pea-service-overlap-harness`
- CLI logs: `%TEMP%\pea-service-overlap-capture\cli-logs`

Copy the committed fixture byte for byte, verify `FIXTURE_MANIFEST.md`, regenerate derived ACM in the external target, record any expected derived-hash change, initialize one baseline Git commit, and confirm focused tests pass. Install exactly the five operational skills plus `PRINCIPLES.md` into `<Copilot home>\skills`; Probe must be absent.

## Interaction mechanics

Use interactive mode because prompt mode exits after scripted execution. The terminal must remain attached to the CLI process. Do not pipe the interactive command through `Tee-Object`, `Select-Object`, or another filter that could hide prompts.

Capture through both:

- the persistent terminal stream returned by the execution host;
- CLI logs under the external `--log-dir`.

At the first Destination question, do not answer from fixture text or agent inference. Relay the exact question and sourced hunch to the operator through the editor question UI. Send exactly one operator answer back to the same terminal prompt. If the terminal asks a menu question before the Destination question, preserve and answer only ordinary permission or rendering prompts according to the frozen command; do not interpret a direction question on the operator's behalf.

After the model reports completion, send `/exit` if the interactive shell remains open. Stop the proxy and preserve all state before evaluation.

## Exact invocation

Set the frozen provider variables, then invoke exactly:

```text
copilot -C C:\git\pea-service-overlap-target -i "Invoke the improve skill. Improve this target, verify the result, and run any automatic services whose evidence-based triggers fire." --session-id 34c4fdd7-0b91-40c2-9aa5-421bddf2b089 --name service-overlap-20260813 --model claude-sonnet-4-5 --output-format json --allow-all-tools --deny-tool="shell(git push)" --deny-tool="url" --disallow-temp-dir --disable-builtin-mcps --no-custom-instructions --no-auto-update --no-remote --no-remote-export --stream off --effort high --no-color --no-mouse --log-dir %TEMP%\pea-service-overlap-capture\cli-logs --secret-env-vars=ANTHROPIC_API_KEY,COPILOT_PROVIDER_API_KEY
```

Do not add `--no-ask-user`, `-p`, `--autopilot`, or remote control. Do not resume or replace the session after observed output under this authorization.

## Final preflight-to-call boundary

In the same serial command that starts the CLI, immediately capture and assert:

- skills source and fixture commit identifiers;
- target baseline commit and clean status;
- all current target fixture hashes and the recorded derived-hash delta;
- focused tests pass without creating cache files;
- target has no `destination.md`;
- stale Orientation and all three historical Trail entries are present;
- installed suite names and hashes match committed source;
- CLI first version line is `GitHub Copilot CLI 1.0.79.`;
- exact proxy hash and listener process;
- empty harness root and fixed requested harness session;
- empty/new CLI log directory;
- available Anthropic credential without recording its value.

No setup mutation may occur after the final assertions. Start the one interactive CLI process immediately. Any pre-call assertion failure leaves the invocation authorization unconsumed and must be preserved before repair. Once the CLI process starts, the authorization is consumed even if no model response arrives.

## Host classification boundary

A CLI rendering, logging, input-routing, or session-persistence failure is Inconclusive for service composition. It must not be repaired by silently starting another session. A model or service behavior failure after a usable interaction channel is established is classified under `PROTOCOL.md` rather than as host failure.
