# First-Run Host Qualification

Status: executed 2026-08-13; exact proxy route available

## Purpose

Determine whether the exact model and provider route previously used by the lifecycle experiment is currently available before authorizing another first-run adoption invocation.

This is a non-experimental host smoke. It does not invoke Improve, use the adoption fixture or prompt, consume an adoption-protocol authorization, or produce evidence about first-run behavior or human adoption.

## Frozen route

- GitHub Copilot CLI: `1.0.79`
- Provider: Anthropic BYOK through local `llm-harness-proxy`
- Proxy source: commit `cd33c15`, including usage-capture commits `36c6151` and `e17e2a8`
- Proxy binary SHA-256: `241626F7D51A945F9C48286EFF26E055FDDA9137C2635DE1FD35094D391701C3`
- Endpoint: `http://127.0.0.1:8475`
- Model: `claude-sonnet-4-5`
- Provider headers: `Accept-Encoding: identity`, a fresh harness session ID, and a disposable harness root
- Copilot state: fresh `COPILOT_HOME` with the five operational skills plus `PRINCIPLES.md`
- Streaming: off
- Reasoning effort: minimal
- Tools: unavailable to the model

## Qualification call

Use the fixed prompt:

> Reply with exactly HOST_OK. Do not use tools or modify files.

Capture complete CLI standard output and standard error, exit code, timestamps, CLI version, proxy binary hash, installed skill hashes, and the complete harness ledger in a disposable external directory.

## Classification

- **Available:** CLI exits zero, a model response is present, the wire model is `claude-sonnet-4-5`, and the proxy ledger contains provider-reported usage.
- **Unavailable:** the exact route rejects the model or cannot produce a model response.
- **Inconclusive:** setup, capture, proxy, or credential failure prevents route classification.

Publish the result before any new cold-start protocol. One qualification call is authorized by this document. It cannot be reclassified as adoption evidence or silently replaced after output is observed.
