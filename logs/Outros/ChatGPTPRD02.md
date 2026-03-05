# PRD Prévio (Preflight) — Project001-MatematicaVivaV4

## Status deste documento
Este é um **PRD preliminar de alinhamento**, criado antes da execução profunda, conforme solicitado.

> **Bloqueio atual**: não foi possível acessar o repositório remoto informado (`https://github.com/raulfbr/Project001-MatematicaVivaV4`) neste ambiente por erro de rede (`CONNECT tunnel failed, response 403`).
>
> Também não foram localizados, neste workspace atual, a pasta **LORE** e o arquivo **north_start** para leitura direta.

---

## Objetivo do pedido (como entendi)
Você quer:
1. Um **PRD detalhado** do projeto Matemática Viva V4.
2. Uma **task robusta de entendimento completo** do projeto.
3. Um recorte de escopo em três níveis:
   - **Foco principal: SEMENTES** (fase 1)
   - **Depois: BROTOS** (fase 2)
   - **No máximo: início de RAÍZES (1º ano)** (fase 3)
4. Que a análise seja conduzida principalmente por:
   - Pasta **LORE**
   - Arquivo **north_start**
5. Que haja um **planejamento prévio com perguntas de alinhamento** antes de execução profunda.

---

## Planejamento proposto (antes da execução profunda)

### Fase A — Ingestão e Mapeamento de Base (LORE + north_start)
- Ler integralmente `LORE/` e `north_start`.
- Extrair visão de produto, taxonomia pedagógica, personas, hipóteses e decisões já tomadas.
- Consolidar um “Mapa de Verdades do Produto” (o que é premissa vs. o que é hipótese aberta).

### Fase B — Diagnóstico Estrutural do Projeto
- Levantar arquitetura (frontend/backend/dados/conteúdo).
- Mapear fluxos de usuário e jornadas por etapa educacional.
- Identificar dependências críticas, gargalos e dívidas técnicas/produto.
- Classificar itens por impacto no recorte Sementes/Brotos.

### Fase C — PRD Formal por Fases (Sementes → Brotos → Raízes-1)
- Definir objetivos de negócio e de aprendizagem por fase.
- Definir métricas (adoção, retenção, resultado pedagógico, satisfação).
- Detalhar backlog por épicos/funcionalidades/aceites.
- Definir roadmap com marcos, riscos e mitigação.

### Fase D — Plano de Execução e Governança
- Definir ciclo de entrega (sprints), rituais e artefatos.
- Definir critérios de qualidade de conteúdo pedagógico.
- Definir monitoramento e ciclo de melhoria contínua.

---

## Pré-PRD (estrutura detalhada que será preenchida após acesso)

## 1) Visão do Produto
- **Problema que o Matemática Viva V4 resolve**
- **Público-alvo primário**
- **Proposta de valor por etapa (Sementes/Brotos/Raízes-1)**

## 2) Escopo por Fase

### 2.1 Sementes (Fase 1 — prioridade máxima)
**Objetivo**
- Construir base de alfabetização matemática com experiência guiada, curta e altamente repetível.

**Possíveis capacidades de produto (placeholder até ler LORE/north_start)**
- Trilhas curtas por microcompetência.
- Feedback imediato e linguagem acessível.
- Atividades com progressão de dificuldade adaptativa simples.
- Painel mínimo para responsável/professor (progresso e bloqueios).

**KPIs esperados**
- Ativação inicial (D1)
- Conclusão de trilha básica
- Retenção semanal
- Taxa de acerto por habilidade fundamental

### 2.2 Brotos (Fase 2)
**Objetivo**
- Aprofundar autonomia, resolução de problemas e consolidação da base.

**Possíveis capacidades**
- Missões contextualizadas.
- Revisão espaçada orientada por erro.
- Metas individuais e evolução visível.

**KPIs esperados**
- Evolução de proficiência por competência
- Frequência de uso por semana
- Queda de erros recorrentes

### 2.3 Raízes — 1º ano (Fase 3, limite máximo do escopo atual)
**Objetivo**
- Introduzir estrutura curricular de longo prazo de forma controlada.

**Escopo mínimo sugerido**
- 1 unidade piloto do 1º ano de Raízes.
- Instrumentação completa de métricas para validar expansão.

---

## 3) Task robusta de entendimento do projeto (Discovery Task)

**Nome sugerido:** `DISCOVERY_360_MatematicaVivaV4_Sementes_Brotos`

**Objetivo da task**
Compreender integralmente o projeto para produzir PRD executável e roadmap realista, com foco em Sementes e Brotos, e apenas uma preparação inicial de Raízes-1.

**Entradas obrigatórias**
- `LORE/` completo
- `north_start`
- Código-fonte atual
- Materiais de produto/conteúdo existentes
- Histórico de decisões (issues/docs/changelog)

**Saídas obrigatórias**
1. Mapa de arquitetura do produto
2. Mapa curricular por fase (Sementes/Brotos/Raízes-1)
3. Matriz de gaps (produto, conteúdo, dados, UX, operação)
4. Priorização por impacto x esforço
5. PRD final + roadmap trimestral

**Checklist operacional**
- [ ] Inventariar módulos e responsabilidades
- [ ] Identificar funcionalidades ativas vs. planejadas
- [ ] Mapear dependências externas
- [ ] Avaliar qualidade de conteúdo por competência
- [ ] Validar instrumentação de métricas
- [ ] Definir riscos e premissas de lançamento

**Critérios de aceite da task**
- O PRD final deve conter objetivos mensuráveis por fase.
- Deve existir backlog priorizado com critérios de aceite testáveis.
- Deve existir plano de rollout para Sementes e Brotos.
- Raízes-1 deve ficar limitado a piloto e preparação.

---

## 4) Proposta de melhoria na criação do projeto (meta-processo)

### 4.1 Melhorias de processo
- Adotar um **Product Operating Rhythm** semanal (discovery + delivery).
- Criar **Definition of Ready** para conteúdo pedagógico e funcionalidade.
- Criar **Definition of Done** com critérios de aprendizado (não só técnicos).

### 4.2 Melhorias de estrutura documental
- Transformar LORE em fonte única versionada (padrão de seção + status).
- Padronizar `north_start` como resumo executivo vivo (visão + norte + métricas).
- Manter ADRs para decisões de arquitetura e pedagogia.

### 4.3 Melhorias de priorização
- Usar quadro por fase: Sementes (70%), Brotos (25%), Raízes-1 (5%).
- Toda feature nova deve apontar KPI educacional e KPI de produto.

### 4.4 Melhorias de qualidade
- Validar conteúdo com rubricas pedagógicas por competência.
- Instrumentar funil de aprendizagem ponta a ponta.
- Implantar ciclo quinzenal de revisão de dados e ajustes de trilha.

---

## 5) Perguntas de alinhamento (antes da execução profunda)
1. Você pode disponibilizar o conteúdo de `LORE/` e do arquivo `north_start` aqui no workspace (ou colar os principais trechos)?
2. O PRD final deve priorizar mais **escolas/professores** ou **famílias/alunos** como usuário principal?
3. Existe algum framework curricular obrigatório (BNCC, rede específica, material próprio)?
4. Qual horizonte do roadmap você prefere no PRD final: 3, 6 ou 12 meses?
5. Quer que eu já estruture o PRD final em formato “executivo + backlog técnico” (duas camadas)?

---

## Próximo passo imediato (após seu ok)
Assim que eu tiver acesso ao `LORE` e `north_start`, eu entrego:
- PRD completo e detalhado;
- backlog faseado (Sementes/Brotos/Raízes-1);
- plano de execução com métricas e riscos;
- recomendações objetivas de melhoria do projeto.