
try {
    $venvActivate = Join-Path $PSScriptRoot 'venv\Scripts\Activate.ps1'
    if (Test-Path $venvActivate) {
        & $venvActivate
    }
} catch {
    Write-Host 'Could not activate virtual environment — continuing without activation.' -ForegroundColor Yellow
}

Write-Host 'Starting Streamlit app...' -ForegroundColor Green
streamlit run app.py
