# Executa examples/01_base.py (e outros exemplos)
# Uso: .\run_example.ps1
# OU: .\run_example.ps1 02_rag
# Requer: OPENAI_API_KEY no ambiente ou arquivo .env

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Carrega .env se existir
if (Test-Path ".env") {
    Get-Content ".env" | ForEach-Object {
        if ($_ -match "^\s*([^#][^=]+)=(.*)$") {
            $key = $matches[1].Trim()
            $val = $matches[2].Trim().Trim('"').Trim("'")
            [Environment]::SetEnvironmentVariable($key, $val, "Process")
        }
    }
}

$env:PYTHONPATH = "src"
$example = if ($args[0]) { "examples/$($args[0]).py" } else { "examples/01_base.py" }

if (-not (Test-Path $example)) {
    Write-Host "Arquivo nao encontrado: $example"
    exit 1
}

if (-not $env:OPENAI_API_KEY) {
    Write-Host "AVISO: OPENAI_API_KEY nao configurada." -ForegroundColor Yellow
    Write-Host "Crie um arquivo .env com OPENAI_API_KEY=sua-chave" -ForegroundColor Yellow
    Write-Host "Ou execute: `$env:OPENAI_API_KEY = 'sua-chave'`n" -ForegroundColor Yellow
}

& ".\.venv\Scripts\python.exe" $example
