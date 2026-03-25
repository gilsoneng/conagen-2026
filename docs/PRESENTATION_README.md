# Apresentação (slides)

Dois decks em formato [Marp](https://marp.app/): Markdown com separadores `---` entre slides.

| Arquivo | Descrição |
|---------|-----------|
| `presentation_slides.md` | Versão enxuta, foco em código e hands-on |
| **`presentation_conagen_completa.md`** | **Versão completa CONAGEN** — todos os slides com diagramas visuais |

## PDF (formato recomendado para distribuição)

O arquivo **`conagen_completa.pdf`** na pasta `docs/` é a apresentação pronta para abrir em qualquer leitor de PDF.

Para **regenerar** o PDF a partir do Markdown (após editar o `.md` ou trocar imagens em `assets/`):

```bash
npx @marp-team/marp-cli docs/presentation_conagen_completa.md -o docs/conagen_completa.pdf
```

HTML (opcional):

```bash
npx @marp-team/marp-cli docs/presentation_conagen_completa.md -o docs/conagen_completa.html
```

Versão enxuta:

```bash
npx @marp-team/marp-cli docs/presentation_slides.md -o docs/slides.pdf
```

## Diagramas

- **`presentation_conagen_completa.md`**: usa imagens PNG em `assets/` (diagramas pré-renderizados).
- **`presentation_slides.md`**: usa blocos **Mermaid**. Se a exportação falhar, copie o Mermaid para [mermaid.live](https://mermaid.live) e exporte como PNG.

## Durante o Hands-on

- Siga **`docs/HANDS_ON.md`** para setup e ordem dos exemplos.
- O **README** na raiz resume comandos e conceitos.
- **`llm.ipynb`**: execute por blocos, alinhado aos `examples/0X_*.py`.
- Chave: `OPENAI_API_KEY` via `.env` (veja `.env.example`).

## Ordem sugerida na fala

1. Slides até “Arquitetura final”.
2. Abrir o projeto no IDE + notebook.
3. Rodar célula de setup do notebook → depois cada estágio.
4. Voltar aos slides do “Mapa” e “Fechamento” se sobrar tempo.
