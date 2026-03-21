# Apresentação (slides)

O arquivo **`presentation_slides.md`** é um deck em formato [Marp](https://marp.app/): Markdown com separadores `---` entre slides.

## Como gerar PDF ou HTML

1. Instale a extensão **Marp for VS Code** (ou o CLI `@marp-team/marp-cli`).
2. Abra `docs/presentation_slides.md`.
3. Exporte para **PDF** ou **HTML** pelo comando da extensão / CLI.

### CLI (exemplo)

```bash
npx @marp-team/marp-cli docs/presentation_slides.md -o docs/slides.pdf
npx @marp-team/marp-cli docs/presentation_slides.md -o docs/slides.html
```

## Diagramas

Os diagramas usam blocos **Mermaid** (` ```mermaid `). Se a exportação falhar, use a pré-visualização Marp ou copie o Mermaid para [mermaid.live](https://mermaid.live) e exporte como PNG para colar no PowerPoint/Google Slides.

## Durante o Hands-on

- Mostre o **README** (`README.md`) como índice do repositório.
- Execute **`llm.ipynb`** por blocos, citando o **`examples/0X_*.py`** correspondente.
- Variável de ambiente: `OPENAI_API_KEY` (ver `.env.example`).

## Ordem sugerida na fala

1. Slides até “Arquitetura final”.
2. Abrir o projeto no IDE + notebook.
3. Rodar célula de setup do notebook → depois cada estágio.
4. Voltar aos slides do “Mapa” e “Fechamento” se sobrar tempo.
