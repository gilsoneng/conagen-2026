# Progressive LLM: Base -> RAG -> Prompt Control -> Fine-tuning

Projeto demonstrando a evolucao de um sistema LLM em quatro estagios e uma arquitetura final combinada.

**Hands-on passo a passo:** [`docs/HANDS_ON.md`](docs/HANDS_ON.md)

**Apresentação:** PDF em [`docs/conagen_completa.pdf`](docs/conagen_completa.pdf) — fonte Marp em `docs/presentation_conagen_completa.md` (detalhes em `docs/PRESENTATION_README.md`).

## Contexto

Estamos construindo um sistema LLM progressivo que evolui em estagios:

1. **LLM Base**
   - Sem conhecimento de dominio
   - Comportamento de referencia
2. **RAG**
   - Injecao de conhecimento de dominio por busca vetorial
   - Melhora correcao factual
3. **Controle por Prompt**
   - Restricoes comportamentais via prompt de sistema
   - Simula aplicacao de politicas
4. **Ajuste Fino**
   - Treinamento supervisionado para internalizar comportamento
   - Reduz dependencia de prompt

Objetivo principal:

- Demonstrar a diferenca entre **injecao de conhecimento** (RAG) e **controle de comportamento** (fine-tuning).

Distincao importante:

- **RAG = conhecimento externo**
- **Fine-tuning = comportamento interno**

Arquitetura final:

- **RAG (conhecimento) + modelo ajustado (comportamento)**

---

## Estrutura do projeto

```text
.
├── docs/
│   ├── HANDS_ON.md              # guia prático (comece aqui)
│   ├── conagen_completa.pdf     # apresentação (PDF)
│   ├── presentation_conagen_completa.md
│   └── PRESENTATION_README.md
├── assets/                      # diagramas da apresentação
├── examples/
│   ├── 01_base.py … 05_hybrid.py
├── src/progressive_llm/
├── llm.ipynb
├── activate.ps1                 # Windows: ativa venv + PYTHONPATH
├── run_example.ps1
├── .env.example
├── requirements.txt
└── README.md
```

---

## Requisitos

- Python 3.12+
- Conta OpenAI com permissao para os modelos/recursos usados

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

Configure a chave:

```bash
cp .env.example .env
export OPENAI_API_KEY="sua-chave-aqui"
```

**Windows (PowerShell):** Se `python` nao for encontrado, use o venv:

```powershell
# Opcao 1: Ativar ambiente e usar python normalmente
. .\activate.ps1
python examples/01_base.py

# Opcao 2: Script auxiliar (configura tudo)
.\run_example.ps1

# Opcao 3: Caminho direto do venv
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe examples/01_base.py
```

> Dica: para execucao local, tambem vale usar `direnv`, `dotenv` ou variavel no shell.

---

## Como executar

Defina o `PYTHONPATH` para enxergar `src/`:

```bash
export PYTHONPATH=src
```

### 1) LLM Base

```bash
python examples/01_base.py
```

### 2) RAG (conhecimento externo)

```bash
python examples/02_rag.py
```

### 3) RAG + Controle por Prompt

```bash
python examples/03_prompt_control.py
```

### 4) Fine-tuning (comportamento interno)

```bash
python examples/04_fine_tuning.py
```

Esse script:

- gera `train.jsonl`
- cria arquivo de treino na OpenAI
- cria job de fine-tuning (tentando modelos candidatos)
- faz polling ate o status final
- imprime erro detalhado em caso de `failed`

### 5) Arquitetura final: RAG + modelo ajustado

Edite `examples/05_hybrid.py` com o id real do seu modelo ajustado e execute:

```bash
python examples/05_hybrid.py
```

---

## Diagnostico rapido de falha no fine-tuning

Se o status for `failed`, os motivos comuns sao:

- modelo base sem suporte de fine-tuning na sua conta/regiao
- formato do JSONL invalido
- exemplos insuficientes ou inconsistentes

O script `04_fine_tuning.py` ja imprime o campo `error` para facilitar o debug.

---

## Observacoes de seguranca

- **Nao commitar chaves** de API no notebook ou codigo.
- Use `OPENAI_API_KEY` via variavel de ambiente.
- O `.gitignore` ja ignora `.env`, `.venv` e `train.jsonl`.

