# First-Run Adoption Result

Status: failed at documented installation; no agent invocation occurred

## Result

The documented Windows command is `pwsh install.ps1`. In the Windows and VS Code environment used for this probe, `copilot` 1.0.79 and Python were available but `pwsh` was not installed. QUICKSTART.md lists VS Code with GitHub Copilot Chat as the prerequisite and does not require PowerShell 7.

The probe therefore failed before target creation or model invocation. It did not test Intent narration, target improvement, Trail creation, Destination behavior, human recognition, or voluntary adoption.

## Discriminating control

The same installer succeeded in a disposable location under built-in Windows PowerShell:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Target "$env:TEMP\pea-adoption-install-smoke\skills"
```

It installed `intent`, `destination`, `improve`, `trail`, `orient`, and `PRINCIPLES.md`, then the disposable output was removed. This isolates the observed blocker to the documented shell command or its unstated PowerShell 7 prerequisite; it does not show a defect in the installer body.

## Scope

This is a first-contact workflow failure, not a failure of Improve reasoning. The live `pwsh install.ps1` form appears in README.md, QUICKSTART.md, INSTALLING.md, and the installer usage comment. Those surfaces were inspected after the failure but remain unchanged in this iteration, preserving the preregistered result before any onboarding repair.

No target fixture was created, no `.acm/` was initialized, and the one authorized agent invocation was never launched. A later run may repair the documented Windows command, then preregister a fresh cold-start probe against the changed artifact.