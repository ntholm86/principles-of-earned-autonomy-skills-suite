# First-Run Adoption Rerun Result

Status: inconclusive; the frozen model was unavailable before agent execution

## Result

The fixture passed its baseline tests, began from a clean baseline commit with no `.acm/`, and the repaired Windows installer placed exactly the five operational skills plus `PRINCIPLES.md` in a fresh `COPILOT_HOME`.

The one authorized GitHub Copilot CLI invocation then exited with code 1 after 3.692 seconds. Standard error reported:

```text
Error: Model "claude-sonnet-4-5" from --model flag is not available.
```

Standard output contains only the initial `session.mcp_servers_loaded` event. No model reasoning, assistant message, tool execution, target change, or ACM artifact occurred. The fixture remained clean and both focused tests still passed.

The result is therefore **inconclusive** under the preregistered host-failure rule. It is not a failure of Improve, Intent, Trail, or Destination behavior.

## Setup correction before invocation

The first setup command used `$home` as a PowerShell variable. PowerShell variable names are case-insensitive, so this collided with the read-only `$HOME` variable and caused the installer target expression to resolve to `C:\Users\admin\skills`. Inspection showed that directory and all six payload entries shared the command's creation instant and contained only the new installer output. The directory was removed, the fixture test cache was removed, and installation was repeated with `$copilotHome` into the intended isolated temp directory.

No model invocation occurred before this correction. The immediate pre-invocation capture subsequently proved a clean fixture, no `.acm/`, passing tests, the expected CLI version, and exact installed skill hashes.

## Evidence

`rerun-evidence/` preserves:

- the controlled fixture source;
- immediate pre-run state and tests;
- complete CLI JSONL and standard error;
- invocation timing and exit code;
- post-run state and tests;
- the empty target diff.

No independent usage proxy was available, so no token or resource claim is made.

## Scope

This rerun establishes that the repaired installer reaches the CLI invocation boundary under an isolated home. It does not test Intent narration, target improvement, Trail creation, Destination behavior, human recognition, voluntary adoption, or resource efficiency.

The incomplete authorization cannot be replaced after observing its output. A future attempt requires a new protocol and a newly qualified model host.
