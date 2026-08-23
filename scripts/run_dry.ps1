$ErrorActionPreference = 'Stop'

# Resolve project root (parent of scripts folder)
$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..\")
Set-Location $ProjectRoot

# Activate venv
$VenvActivate = Join-Path $ProjectRoot ".venv\Scripts\Activate.ps1"
if (-not (Test-Path $VenvActivate)) {
  Write-Host "Virtual environment not found. Run scripts/setup.ps1 first." -ForegroundColor Yellow
  exit 1
}
. $VenvActivate

# DRY RUN: skip LLM and use TinyHashEmbedding
$env:NO_LLM = '1'
$env:DRY_RUN = '1'

Write-Host "Launching app in DRY_RUN (no LLM) mode on http://localhost:7860" -ForegroundColor Cyan
python code.py

