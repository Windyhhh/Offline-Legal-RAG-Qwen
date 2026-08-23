param(
    [string]$Python = "python"
)
$ErrorActionPreference = 'Stop'

# Resolve project root (parent of scripts folder)
$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..\")
Set-Location $ProjectRoot

Write-Host "[1/6] Creating virtual environment at: $ProjectRoot\.venv" -ForegroundColor Cyan
& $Python -m venv .venv

$VenvActivate = Join-Path $ProjectRoot ".venv\Scripts\Activate.ps1"
. $VenvActivate

Write-Host "[2/6] Upgrading pip/setuptools/wheel" -ForegroundColor Cyan
python -m pip install -U pip setuptools wheel

Write-Host "[3/6] Installing project requirements" -ForegroundColor Cyan
pip install -r (Join-Path $ProjectRoot "requirements.txt")

Write-Host "[4/6] Creating data directories" -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot "legal_docs") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot "chroma_db") | Out-Null

Write-Host "[5/6] Adding sample legal text (if none)" -ForegroundColor Cyan
$sample = Join-Path $ProjectRoot "legal_docs\sample.txt"
if (-not (Test-Path $sample)) {
  @"
《民法典》合同编节选（示例）
第一百一十一条 当事人一方不履行合同义务或者履行合同义务不符合约定的，应当承担继续履行、采取补救措施或者赔偿损失等违约责任。
"@ | Out-File -FilePath $sample -Encoding UTF8
}

Write-Host "[6/6] Verifying dependency health" -ForegroundColor Cyan
pip check | Write-Host

Write-Host "Setup finished. Activate with: . .\.venv\Scripts\Activate.ps1" -ForegroundColor Green

