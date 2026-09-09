# Install the PEA hook at Git's effective hook location.
# Run from the target repo root.
$ErrorActionPreference = 'Stop'

$repoRoot = (git rev-parse --show-toplevel 2>$null)
if (-not $repoRoot) {
    Write-Error "Not inside a git repo."
    exit 1
}

$hooksSrc = Join-Path $PSScriptRoot 'hooks'
$hookSource = Join-Path $hooksSrc 'pre-commit'
$hookTarget = git rev-parse --path-format=absolute --git-path hooks/pre-commit
if ($LASTEXITCODE -ne 0 -or -not $hookTarget) {
    throw 'Cannot resolve the Git hook location.'
}

if (Test-Path -LiteralPath $hookTarget) {
    if (-not (Test-Path -LiteralPath $hookTarget -PathType Leaf) -or
        (Get-FileHash -LiteralPath $hookSource).Hash -ne (Get-FileHash -LiteralPath $hookTarget).Hash) {
        throw "Existing hook differs: $hookTarget. Review and integrate it manually; nothing was overwritten."
    }
} else {
    New-Item -ItemType Directory -Path (Split-Path -Parent $hookTarget) -Force | Out-Null
    Copy-Item -LiteralPath $hookSource -Destination $hookTarget
}

Write-Host "Installed pre-commit hook to $hookTarget"
