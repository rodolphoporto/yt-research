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

## Exemplos voltados a Desenvolvimento

---

### Dev 1 — System Design

> Pesquisar padrões de arquitetura para uma decisão técnica, gerar um documento de referência e um mind map para compartilhar com o time.

```
Busque 15 vídeos sobre "system design microservices vs monolith" no YouTube.
Crie um notebook no NotebookLM chamado "System Design Research".
Analise os trade-offs mais discutidos entre as duas abordagens,
quais padrões (event-driven, CQRS, saga) aparecem como solução
e em que cenários cada arquitetura é recomendada.
Gere um slide deck comparativo salvo em yt-research/system-design-deck.pdf
```

**Variações úteis:**
```
/yt-search "domain driven design DDD" 15
/yt-search "event sourcing CQRS" 10
/yt-search "clean architecture backend" 12
```

---

### Dev 2 — Escolha de tecnologia / stack

> Pesquisar antes de adotar uma nova ferramenta, framework ou linguagem no projeto.

```
Busque 15 vídeos sobre "Rust vs Go performance backend 2025" no YouTube.
Crie um notebook no NotebookLM chamado "Rust vs Go".
Liste os argumentos mais usados a favor de cada linguagem,
os casos de uso onde cada uma se destaca
e o que a comunidade aponta como armadilhas de cada uma.
Salve o relatório em yt-research/rust-vs-go.md
```

**Variações úteis:**
```
/yt-search "postgres vs mongodb when to use" 10
/yt-search "kubernetes vs docker swarm production" 10
/yt-search "nextjs vs remix 2025" 10
```

---

### Dev 3 — Preparar entrevista técnica

> Estudar um tema de entrevista a partir dos vídeos mais relevantes e gerar flashcards para revisar.

```
Busque 10 vídeos sobre "system design interview preparation" no YouTube.
Crie um notebook no NotebookLM chamado "System Design Interview".
Extraia os frameworks de resposta mais ensinados (ex: STAR, capacity estimation),
os tópicos que aparecem em mais entrevistas
e as perguntas clássicas com suas respostas resumidas.
Gere flashcards em markdown salvos em yt-research/interview-flashcards.md
```

**Variações úteis:**
```
/yt-search "leetcode patterns dynamic programming" 10
/yt-search "behavioral interview software engineer" 8
/yt-search "API design best practices REST GraphQL" 10
```

---

### Dev 4 — Onboarding de tecnologia nova para o time

> Absorver rapidamente o essencial de uma tecnologia e gerar um guia interno.

```
Busque 12 vídeos sobre "Apache Kafka fundamentals" no YouTube.
Crie um notebook no NotebookLM chamado "Kafka Onboarding".
Gere um guia de estudo estruturado cobrindo: conceitos core (topics, partitions,
consumer groups), casos de uso comuns, armadilhas de produção e primeiros passos.
Salve o relatório em yt-research/kafka-guide.md
e gere também um mind map do conteúdo.
```

**Variações úteis:**
```
/yt-search "redis beyond cache use cases" 10
/yt-search "terraform fundamentals infrastructure as code" 10
/yt-search "opentelemetry observability distributed tracing" 8
```

---

### Dev 5 — Pesquisa de segurança / boas práticas

> Levantar boas práticas de segurança para uma stack específica antes de fazer um security review.

```
Busque 10 vídeos sobre "API security best practices OWASP" no YouTube.
Crie um notebook no NotebookLM chamado "API Security".
Liste as vulnerabilidades mais citadas, as mitigações recomendadas
e um checklist de segurança para APIs REST.
Gere um infográfico com o checklist salvo em yt-research/api-security-checklist.png
```

---

### Dev 6 — Acompanhar uma conferência / keynote

> Absorver o conteúdo de uma conferência técnica sem assistir tudo.

```
Busque 20 vídeos sobre "Google I/O 2025 developer" no YouTube.
Crie um notebook no NotebookLM chamado "Google IO 2025".
Analise quais foram os principais anúncios para desenvolvedores,
o que mudou em relação ao ano anterior
e quais tecnologias valem atenção.
Gere um relatório salvo em yt-research/google-io-2025.md
e um audio overview em português para eu ouvir no caminho.
```

**Variações úteis:**
```
/yt-search "AWS re:Invent 2025 highlights" 15
/yt-search "React Conf 2025" 10
/yt-search "KubeCon 2025 highlights" 10
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
