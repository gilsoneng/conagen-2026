# Guia prático — Hands-on CONAGEN

Este guia é o roteiro mínimo para deixar o projeto funcionando e seguir os exemplos na ordem certa.

## O que você precisa

- **Python 3.12+** (recomendado instalar de [python.org](https://www.python.org/downloads/) e marcar *Add Python to PATH* no Windows).
- Conta **OpenAI** com créditos e permissão para chat e (se for usar) fine-tuning.
- **Chave de API** em `OPENAI_API_KEY` (nunca commite o arquivo `.env`).

## 1. Clonar e entrar na pasta

```bash
git clone https://github.com/gilsoneng/conagen-2026.git
cd conagen-2026
```

## 2. Ambiente virtual e dependências

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

**Windows (PowerShell)**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements.txt
```

Se o comando `python` não for encontrado após ativar, use:

```powershell
. .\activate.ps1
```

(Note o ponto no início: isso coloca o Python do `.venv` no PATH da sessão.)

## 3. Configurar a chave da API

```bash
cp .env.example .env
```

Edite `.env` e coloque:

```text
OPENAI_API_KEY=sk-...
```

O código carrega o `.env` automaticamente (`python-dotenv` em `config.py`).

**Alternativa:** exportar no terminal:

```bash
export OPENAI_API_KEY="sk-..."
```

```powershell
$env:OPENAI_API_KEY = "sk-..."
```

## 4. Variável PYTHONPATH

O pacote `progressive_llm` fica em `src/`. Sempre que rodar scripts na raiz:

**Linux / macOS**

```bash
export PYTHONPATH=src
```

**Windows**

```powershell
$env:PYTHONPATH = "src"
```

O script `activate.ps1` já define `PYTHONPATH` para `src` na sessão.

## 5. Ordem dos exemplos (protocolo sugerido)

| Ordem | Comando | O que valida |
|-------|---------|----------------|
| 1 | `python examples/01_base.py` | LLM sem domínio (baseline) |
| 2 | `python examples/02_rag.py` | RAG com documentos do domínio |
| 3 | `python examples/03_prompt_control.py` | RAG + regras no system prompt |
| 4 | `python examples/04_fine_tuning.py` | Job de fine-tuning (gera `train.jsonl`, pode demorar) |
| 5 | Editar `examples/05_hybrid.py` com o ID do modelo ajustado, depois `python examples/05_hybrid.py` | RAG + modelo fine-tuned |

**Atalho no Windows:** `.\run_example.ps1` (equivalente ao `01_base` por padrão; ajuste o script se quiser outros exemplos).

## 6. Notebook `llm.ipynb`

- Abra no VS Code / Cursor com o kernel apontando para `.venv`.
- Execute as células na ordem: setup → cada bloco alinhado aos `examples/0X_*.py`.

## 7. Apresentação

- **PDF pronto para assistir:** `docs/conagen_completa.pdf`
- **Fonte editável (Marp):** `docs/presentation_conagen_completa.md` — ver `docs/PRESENTATION_README.md` para exportar PDF/HTML de novo.

## 8. Problemas comuns

| Sintoma | O que fazer |
|---------|-------------|
| `Python não foi encontrado` | Use `.\.venv\Scripts\python.exe` ou `. .\activate.ps1` |
| `OPENAI_API_KEY nao configurada` | Confira `.env` na raiz ou variável de ambiente |
| Fine-tuning `failed` | Ver mensagem `error` no script; modelo pode não estar disponível na conta/região |
| Import de `progressive_llm` | `PYTHONPATH=src` ou rodar a partir da raiz com `activate.ps1` |

## 9. Segurança

- Não commite `.env`, chaves ou `train.jsonl` com dados sensíveis.
- O `.gitignore` já ignora `.env` e `.venv`.
