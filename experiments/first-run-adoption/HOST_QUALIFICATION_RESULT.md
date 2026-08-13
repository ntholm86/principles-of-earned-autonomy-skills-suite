# First-Run Host Qualification Result

Status: available on the exact proxy route

## Result

The one authorized non-experimental qualification call completed through the frozen proxy route:

- GitHub Copilot CLI `1.0.79`
- model `claude-sonnet-4-5`
- Anthropic BYOK through `llm-harness-proxy` at `127.0.0.1:8475`
- proxy binary SHA-256 `241626F7D51A945F9C48286EFF26E055FDDA9137C2635DE1FD35094D391701C3`
- identity encoding
- fresh `COPILOT_HOME` containing the five operational skills plus `PRINCIPLES.md`
- minimal effort and no available model tools

The CLI exited `0` after 6.065 seconds. It reported wire model `claude-sonnet-4-5`, returned exactly `HOST_OK`, made no tool request, and modified no files.

The proxy wrote one hash-chained ledger entry with model `claude-sonnet-4-5`, response `HOST_OK`, no action, and provider-reported usage of 10 input tokens and 55 output tokens. The exact route is therefore classified **Available**.

## Session identifier observation

The requested `X-Harness-Session` value was `APJJ0P9SCKW2KEQHWF57WGRWDB`, while the proxy emitted ledger SID `01KZXVWYQ2PEY3PSM297AW7MEK`. The single ledger was unambiguous because the disposable harness root was empty before the call and contains exactly one session file afterward. The mismatch is preserved as a host detail and should not be described as caller-controlled session identity in a future protocol without further qualification.

## Scope

This call established current availability only for the exact proxy route. It did not invoke Improve, use the first-run fixture or prompt, create ACM, test automatic services, or establish simulated operability or human adoption.

A new cold-start attempt still requires a fresh preregistered authorization. It should reuse this exact route while separately capturing immediate target eligibility at its own invocation boundary.
