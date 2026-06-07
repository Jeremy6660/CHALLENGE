$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonExe = Join-Path $projectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $pythonExe)) {
    Write-Error "Virtual environment Python not found: $pythonExe. Please create .venv and install dependencies first."
}

Set-Location $projectRoot
$env:STREAMLIT_BROWSER_GATHER_USAGE_STATS = "false"
& $pythonExe -m streamlit run main.py --server.headless true
