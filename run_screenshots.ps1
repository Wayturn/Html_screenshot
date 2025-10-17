param(
    [string]$InputFile = "urls.txt",
    [string]$OutDir = "output",
    [string]$Prefix = "http://localhost:8000",
    [int]$Start = 1,
    [int]$End = 40,
    [string]$WaitState = "load",
    [int]$Timeout = 60000,
    [string]$UserAgent = $null,
    [switch]$NoHeadless,
    [switch]$ActivateVenv
)

# Optionally activate the venv to ensure environment is set (some policies require this)
if ($ActivateVenv) {
    $activate = Join-Path -Path $PSScriptRoot -ChildPath ".\.venv\Scripts\Activate.ps1"
    if (Test-Path $activate) {
        Write-Host "Activating venv..." -ForegroundColor Green
        & $activate
    } else {
        Write-Warning "Activate.ps1 not found at $activate"
    }
}

# Resolve python in local venv
$python = Join-Path -Path $PSScriptRoot -ChildPath ".\.venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    Write-Error "Python executable not found at $python. Ensure .venv exists and dependencies installed."
    exit 2
}

$args = @('--input', $InputFile, '--outdir', $OutDir, '--prefix', $Prefix, '--start', $Start, '--end', $End, '--wait-state', $WaitState, '--timeout', $Timeout)
if ($NoHeadless) { $args += '--no-headless' }
if ($UserAgent) { $args += @('--user-agent', $UserAgent) }

Write-Host "Running batch screenshot with:" -ForegroundColor Cyan
Write-Host "  Input: $InputFile" -ForegroundColor Cyan
Write-Host "  OutDir: $OutDir" -ForegroundColor Cyan
Write-Host "  Prefix: $Prefix" -ForegroundColor Cyan
if ($UserAgent) { Write-Host "  UserAgent: $UserAgent" -ForegroundColor Cyan }

& $python "screenshot.py" $args
