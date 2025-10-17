<#
One-line install script for Windows PowerShell:
 - creates and activates a venv (.venv)
 - upgrades pip
 - installs requirements
 - runs `python -m playwright install`
#>

Param()

Write-Host "Creating virtual environment .venv..." -ForegroundColor Green
python -m venv .venv

Write-Host "Activating virtual environment..." -ForegroundColor Green
& .\.venv\Scripts\Activate.ps1

Write-Host "Upgrading pip..." -ForegroundColor Green
python -m pip install --upgrade pip

Write-Host "Installing requirements..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "Installing Playwright browsers..." -ForegroundColor Green
python -m playwright install

Write-Host "Done. You can now run screenshot.py or .\run_screenshots.ps1" -ForegroundColor Cyan
