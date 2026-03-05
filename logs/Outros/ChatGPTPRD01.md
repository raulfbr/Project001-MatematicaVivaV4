
# PRD (Draft) — Project001-MatematicaVivaV4

## Status deste documento
- **Estado:** Draft de planejamento estratégico e escopo.
- **Objetivo do draft:** Organizar uma task robusta para entender o projeto completo e orientar a execução por fases, com foco inicial em **SEMENTES** e **BROTOS**, deixando **RAÍZES (1º ano)** como Fase 3.
- **Limitação atual:** Não foi possível acessar o repositório remoto `raulfbr/Project001-MatematicaVivaV4` por bloqueio de rede (erro 403 no clone), e também não foram localizados no workspace atual a pasta `LORE` nem o arquivo `north_start`.

---

## 1) Visão de Produto (interpretada do pedido)
Criar uma experiência de aprendizagem de Matemática Viva, orientada por jornada de crescimento:
1. **Sementes** (fundação): despertar, diagnóstico inicial, microvitórias, base conceitual mínima.
2. **Brotos** (consolidação inicial): formação de hábito, progressão guiada, resolução contextualizada.
3. **Raízes — 1º ano** (fase posterior): estruturação curricular completa e persistência de longo prazo.

### Tese pedagógica (hipótese)
- Aprendizagem melhora quando o aluno tem:
  - objetivos curtos e claros;
  - prática diária curta;
  - feedback imediato;
  - sensação de progresso visível.

---

## 2) Escopo por Fases

### Fase 1 — SEMENTES (MVP pedagógico-operacional)
**Meta:** Colocar o aluno em movimento com mínima fricção.

**Inclui:**
- Onboarding extremamente curto.
- Diagnóstico de entrada (rápido, adaptativo e não punitivo).
- Trilhas de microlições (5–10 min).
- Exercícios de vitória rápida.
- Feedback automático simples.
- Métricas básicas de engajamento.

**Não inclui (nesta fase):**
- Profundidade curricular extensa.
- Gamificação complexa.
- Relatórios avançados para gestão.

### Fase 2 — BROTOS (escala de aprendizagem)
**Meta:** Transformar continuidade em hábito.

**Inclui:**
- Sequência de conteúdos com pré-requisitos explícitos.
- Revisão espaçada (spaced repetition) para retenção.
- Trilha adaptativa por desempenho.
- Painel de progresso do aluno.
- Rotinas semanais e metas de consistência.

**Não inclui (nesta fase):**
- Cobertura integral do currículo anual.
- Modelos avançados de personalização com IA generativa.

### Fase 3 — RAÍZES (1º ano)
**Meta:** Consolidar uma base anual robusta (somente após Sementes/Brotos estáveis).

**Inclui:**
- Mapa curricular do 1º ano (sequência anual).
- Avaliações periódicas somativas + formativas.
- Plano de recuperação contínua.
- Integração docente/família (se aplicável).

---

## 3) Task Robusta de Descoberta (entendimento completo do projeto)

## Macro-Task A — Leitura Estrutural do Projeto
- Inventariar pastas, arquivos centrais e documentação de arquitetura.
- Mapear fluxos principais (usuário, conteúdo, avaliação, métricas).
- Levantar tecnologias, dependências, ambientes e riscos de execução.

**Entregáveis:**
- Mapa de módulos.
- Diagrama de fluxo de usuário.
- Lista de lacunas documentais.

## Macro-Task B — Leitura Pedagógica (foco Sementes/Brotos)
- Identificar objetivos de aprendizagem por nível.
- Classificar conteúdos em:
  - entrada (fundação),
  - progressão (consolidação),
  - aprofundamento (adiado).
- Definir critérios de “pronto para avançar” entre etapas.

**Entregáveis:**
- Matriz de objetivos por fase.
- Regras de progressão.

## Macro-Task C — Produto e Experiência
- Mapear jornada ponta a ponta:
  1) descoberta,
  2) onboarding,
  3) primeira sessão,
  4) retorno no dia seguinte,
  5) retenção semanal.
- Definir fricções e oportunidades por etapa.

**Entregáveis:**
- Jornada do aluno com pontos de abandono.
- Hipóteses de melhoria priorizadas.

## Macro-Task D — Dados e Métricas
- Definir North Star e métricas auxiliares.
- Estruturar eventos mínimos de tracking.
- Estabelecer metas por fase (Sementes/Brotos).

**Entregáveis:**
- Dicionário de eventos.
- Painel mínimo de métricas.

## Macro-Task E — Execução Técnica
- Validar arquitetura atual para suportar iteração rápida.
- Definir backlog técnico por impacto/risco.
- Planejar estratégia de testes (funcional + pedagógica).

**Entregáveis:**
- Backlog priorizado.
- Plano de releases curtos.

---

## 4) PRD Proposto (versão inicial orientada a execução)

## 4.1 Objetivo
Permitir que alunos iniciantes em matemática criem base sólida com progresso perceptível em ciclos curtos, iniciando em Sementes e evoluindo para Brotos com consistência.

## 4.2 Público-alvo (hipótese)
- Alunos em estágio inicial de base matemática.
- Responsáveis/professores que acompanham evolução.

## 4.3 Problemas que resolvemos
- Falta de base conceitual.
- Baixa continuidade de estudo.
- Frustração por dificuldade precoce.

## 4.4 Proposta de valor
- Começo simples, progresso visível e constância.
- Aprendizagem ativa e incremental.

## 4.5 Funcionalidades (MVP Sementes)
- Diagnóstico inicial leve.
- Plano de estudo diário curto.
- Exercícios com correção imediata.
- Dashboard de progresso essencial.

## 4.6 Funcionalidades (Brotos)
- Trilhas adaptativas por desempenho.
- Revisão espaçada automática.
- Metas semanais e rotina.

## 4.7 Critérios de sucesso
- Ativação D1 (primeira sessão concluída).
- Retenção semanal (W1/W2/W4).
- Evolução de acerto por competência.
- Tempo médio em prática com conclusão.

## 4.8 Não-objetivos (agora)
- Cobertura completa do 1º ano antes de validar retenção.
- Features avançadas de gamificação.

## 4.9 Riscos
- Escopo amplo demais no início.
- Métricas sem instrumentação desde o início.
- Jornada inicial complexa (queda de ativação).

## 4.10 Mitigações
- Reduzir escopo para Sementes com alta cadência.
- Instrumentar eventos no MVP.
- Rodar ciclos quinzenais com revisão por dados.

---

## 5) Melhorias sugeridas na criação do projeto
1. **Iniciar pelo loop de valor mínimo:** aprender algo + acertar algo + ver progresso (mesmo dia).
2. **Definir North Star cedo:** ex. “sessões concluídas com progresso por semana”.
3. **Separar claramente camadas:** conteúdo, lógica pedagógica, produto/UX, dados.
4. **Criar baseline de experimentos:** A/B simples para onboarding e rotina diária.
5. **Instrumentação antes de escala:** sem evento não há priorização confiável.
6. **Governança de escopo:** checklist de entrada/saída por fase (Sementes/Brotos/Raízes).

---

## 6) Perguntas em aberto (antes de execução profunda)
1. Você pode disponibilizar o conteúdo da pasta **LORE** e do arquivo **north_start** (ou confirmar o caminho correto)?
2. O foco de “Sementes” e “Brotos” é para qual faixa etária/série inicialmente?
3. Há stack técnica já definida no projeto alvo (frontend/backend/dados)?
4. Existe métrica North Star já escolhida no projeto original?
5. Quer que eu já estruture o próximo passo como **backlog executável (épicos + user stories + critérios de aceite)**?

---

## 7) Próximo passo recomendado
Após receber LORE/north_start, gerar:
- PRD v1 completo e validado por evidências do repositório;
- Mapa de arquitetura atual;
- Backlog priorizado para 8 semanas (Sementes/Brotos);
- Plano de Fase 3 (Raízes 1º ano) apenas como blueprint.