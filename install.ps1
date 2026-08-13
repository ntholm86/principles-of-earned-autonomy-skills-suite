# install.ps1 — copy PEA skills into a Copilot skills directory.
#
# Usage:
#   pwsh install.ps1 [-Target <path>] [-Research]
#
# Default target: $HOME\.copilot\skills (user-global).
param(
    [string]$Target = (Join-Path $HOME '.copilot\skills'),
    [switch]$Research
)

$ErrorActionPreference = 'Stop'

$skills = @('intent', 'destination', 'improve', 'trail', 'orient')
if ($Research) {
    $skills += 'probe'
}
$src = $PSScriptRoot

if (-not (Test-Path $Target)) {
    New-Item -ItemType Directory -Path $Target -Force | Out-Null
}

foreach ($skill in $skills) {
    $skillSrc = Join-Path $src "$skill\SKILL.md"
    if (Test-Path $skillSrc) {
        $skillDst = Join-Path $Target $skill
        New-Item -ItemType Directory -Path $skillDst -Force | Out-Null
        Copy-Item $skillSrc (Join-Path $skillDst 'SKILL.md') -Force
        Write-Host "  installed: $skill"
    } else {
        Write-Host "  skipped:   $skill (no SKILL.md found)"
    }
}

$principles = Join-Path $src 'PRINCIPLES.md'
if (Test-Path $principles) {
    Copy-Item $principles (Join-Path $Target 'PRINCIPLES.md') -Force
    Write-Host "  installed: PRINCIPLES.md"
}

Write-Host ""
Write-Host "Installed PEA skills to: $Target"
Write-Host "Action: Run (/improve)"
Write-Host "Automatic: intent before work; trail afterward; destination and orientation when evidence requires them"
if ($Research) {
    Write-Host "Research: /probe installed for ARF experiments"
} else {
    Write-Host "Probe omitted. Re-run with -Research only for ARF experiments"
}
