# ==============================================================================
# Daily AI/ML Learning Journey Sync Script
# Run: .\scripts\sync.ps1 (from repo root) or run directly from anywhere
# ==============================================================================

# Ensure script executes relative to repository root
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

Write-Host ">>> Staging all new notebooks, code, and documentation..." -ForegroundColor Cyan
git add .

$status = git status --porcelain
if (-not $status) {
    Write-Host ">>> No changes to commit. Everything is up to date!" -ForegroundColor Yellow
    exit 0
}

$commitMsg = Read-Host "Enter commit message (Press Enter for auto-date message)"
if ([string]::IsNullOrWhiteSpace($commitMsg)) {
    $currentDate = Get-Date -Format "yyyy-MM-dd HH:mm"
    $commitMsg = "feat: daily AI/ML learning update ($currentDate)"
}

Write-Host ">>> Committing: $commitMsg" -ForegroundColor Cyan
git commit -m "$commitMsg"

Write-Host ">>> Pushing to GitHub (origin/main)..." -ForegroundColor Cyan
git push origin main

Write-Host "`n>>> Successfully synced to GitHub!" -ForegroundColor Green
Write-Host ">>> Live URL: https://github.com/yousufkidiya17/aiml-journey" -ForegroundColor Green
