# yt-research

> Workflow de pesquisa com IA: busque vídeos no YouTube, analise com NotebookLM e gere entregáveis — tudo dentro do Claude Code, sem sair do terminal.

Inspirado no vídeo do [Chase AI](https://www.youtube.com/watch?v=usTeU4Uh0iM).

![Infográfico gerado pelo workflow](top5-skills-blueprint.png)

---

## Como funciona

```
/yt-search "seu tema" 20
        ↓
  URLs dos vídeos
        ↓
  NotebookLM (RAG gratuito, processado pelo Google)
        ↓
  Infográfico / Podcast / Flashcards / Slide deck
```

Com um único prompt no Claude Code você:
1. Busca os vídeos mais relevantes sobre qualquer tema no YouTube
2. Cria um notebook no NotebookLM e adiciona os vídeos como fontes
3. Pede análise — o processamento é feito pelo Google, sem gastar tokens
4. Recebe o entregável salvo direto na sua pasta

---

## Pré-requisitos

- [Claude Code](https://claude.ai/code) instalado
- Python 3.10+
- Conta Google (para o NotebookLM)

---

## Instalação

```bash
git clone https://github.com/seu-usuario/yt-research
cd yt-research

# Criar ambiente virtual e instalar dependências
uv venv && uv pip install "notebooklm-py[browser]" yt-dlp

# Instalar o Chromium (necessário para autenticação)
.venv/bin/playwright install chromium

# Instalar os skills no Claude Code
.venv/bin/notebooklm skill install
```

Depois crie o skill `yt-search` manualmente:

```bash
mkdir -p ~/.claude/skills/yt-search
cp skills/yt-search.md ~/.claude/skills/yt-search/SKILL.md
```

> Edite o `SKILL.md` para apontar para o caminho absoluto do `yt_search.py` na sua máquina.

---

## Autenticação (uma única vez)

```bash
.venv/bin/notebooklm login
```

Abre o Chrome — faça login com sua conta Google. Suas credenciais ficam salvas em `~/.notebooklm/` e nunca vão para o repositório.

---

## Uso no Claude Code

### Buscar vídeos
```
/yt-search "claude code skills" 20
```

### Criar notebook e adicionar fontes
```
Crie um notebook no NotebookLM chamado "Research" com os vídeos que acabamos de buscar
```

### Analisar
```
Com base nos vídeos, quais são os top 5 temas mais abordados? Traga análise completa.
```

### Gerar entregável
```
Gere um infográfico estilo blueprint e salve na pasta yt-research/
```

### Fluxo completo em um prompt
```
Busque os 20 vídeos mais populares sobre "claude code skills", crie um notebook
no NotebookLM chamado "Research", analise os top 5 skills ensinados e gere um
infográfico estilo blueprint salvo na pasta yt-research/
```

---

## Entregáveis suportados pelo NotebookLM

| Tipo | Comando |
|------|---------|
| Infográfico (PNG) | `Gere um infográfico e salve em yt-research/` |
| Podcast (MP3) | `Crie um audio overview em português` |
| Slide deck (PDF) | `Gere um slide deck com os principais pontos` |
| Flashcards (Markdown) | `Exporte os flashcards em markdown` |
| Mind map (JSON) | `Exporte o mind map do notebook` |
| Relatório (Markdown) | `Gere um relatório detalhado` |

---

## Estrutura do projeto

```
yt-research/
├── yt_search.py         # Script de busca no YouTube via yt-dlp
├── skills/
│   └── yt-search.md     # Skill do Claude Code para busca no YouTube
├── EXAMPLES.md          # Exemplos de uso prontos
├── .gitignore
└── README.md
```

---

## Dependências

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — scraping de metadados do YouTube
- [notebooklm-py](https://github.com/teng-lin/notebooklm-py) — API não-oficial do NotebookLM (by Tang Ling)
- [Claude Code](https://claude.ai/code) — agente que orquestra o workflow
