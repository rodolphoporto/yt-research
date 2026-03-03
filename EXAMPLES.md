# Exemplos de uso

Exemplos práticos do workflow YouTube + NotebookLM no Claude Code.

---

## Exemplo 1 — Igual ao vídeo do Chase AI

> Reproduz exatamente o que foi demonstrado: buscar vídeos sobre Claude Code skills,
> analisar com NotebookLM e gerar um infográfico.

### Passo a passo (separado)

**1. Buscar os vídeos:**
```
/yt-search "claude code skills" 20
```

**2. Criar notebook e adicionar as fontes:**
```
Crie um notebook no NotebookLM chamado "Claude Code Skills Research"
e adicione todos os vídeos que acabamos de buscar como fontes
```

**3. Pedir análise:**
```
Com base nos vídeos do notebook, quais são os top 5 Claude Code skills
mais mencionados e ensinados? Traga a análise completa.
```

**4. Gerar infográfico:**
```
Gere um infográfico no estilo blueprint/manuscrito com os top 5 skills
que o NotebookLM identificou e salve na pasta yt-research/
```

### Prompt único (igual ao demo do vídeo)

```
Use o yt-search para buscar os 20 vídeos mais populares sobre "claude code skills".
Depois crie um notebook no NotebookLM chamado "Claude Code Research" com esses vídeos.
Peça ao NotebookLM para analisar quais são os top 5 Claude Code skills mais ensinados
e gere um infográfico no estilo blueprint/handwritten com essa análise.
Salve o infográfico na pasta yt-research/.
```

---

## Exemplo 2 — Pesquisa de tendências de IA

> Descobrir o que está em alta no mundo de IA agente em 2025.

```
Busque os 15 vídeos mais recentes sobre "AI agents 2025" no YouTube.
Crie um notebook no NotebookLM chamado "AI Trends 2025".
Analise quais ferramentas e frameworks aparecem com mais frequência
e gere um relatório em markdown salvo em yt-research/ai-trends-report.md
```

---

## Exemplo 3 — Preparar estudo sobre um tema

> Estudar um assunto técnico a partir dos melhores vídeos disponíveis.

```
Busque 10 vídeos sobre "RAG com LangChain" no YouTube.
Crie um notebook no NotebookLM chamado "Estudo RAG LangChain".
Gere flashcards em markdown com os conceitos principais
e salve em yt-research/flashcards-rag.md
```

---

## Exemplo 4 — Podcast a partir de pesquisa no YouTube

> Criar um audio overview (podcast) sobre um tema, alimentado por vídeos reais.

```
Busque 10 vídeos sobre "Claude Code MCP servers" no YouTube.
Crie um notebook no NotebookLM chamado "MCP Deep Dive".
Gere um audio overview em português e baixe como podcast.mp3
na pasta yt-research/
```

---

## Exemplo 5 — Análise de concorrentes / criadores

> Ver o que os maiores criadores de conteúdo estão cobrindo sobre um tema.

```
Busque 20 vídeos sobre "cursor vs claude code" no YouTube.
Crie um notebook no NotebookLM chamado "Cursor vs Claude Code".
Analise quais são os argumentos mais usados a favor de cada ferramenta
e gere um slide deck comparativo em PDF salvo em yt-research/
```

---

## Referência rápida de comandos

| O que fazer | Prompt no Claude Code |
|-------------|----------------------|
| Buscar vídeos | `/yt-search "tema" 20` |
| Criar notebook | `Crie um notebook no NotebookLM chamado "Nome"` |
| Adicionar fontes | `Adicione os vídeos ao notebook` |
| Pedir análise | `Qual o resumo dos vídeos? Quais os temas principais?` |
| Infográfico | `Gere um infográfico e salve em yt-research/` |
| Podcast | `Gere um audio overview em português` |
| Flashcards | `Exporte os flashcards em markdown` |
| Mind map | `Exporte o mind map do notebook` |
| Slide deck | `Gere um slide deck em PDF` |
