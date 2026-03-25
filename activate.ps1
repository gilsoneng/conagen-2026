# Ativa o ambiente Python do projeto (adiciona ao PATH da sessao atual)
# Uso: . .\activate.ps1   (note o ponto no inicio!)
# Depois: python examples/01_base.py

$venvPath = "$PSScriptRoot\.venv\Scripts"
if (Test-Path "$venvPath\python.exe") {
    $env:PATH = "$venvPath;$env:PATH"
    $env:PYTHONPATH = "$PSScriptRoot\src"
    Write-Host "Ambiente ativado. Use: python examples/01_base.py" -ForegroundColor Green
} else {
    Write-Host "Erro: .venv nao encontrado. Execute primeiro: .\.venv\Scripts\pip.exe install -r requirements.txt" -ForegroundColor Red
}
