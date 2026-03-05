# PRD Norteador para IA — Projeto001 Matemática Viva V4

> **Status de contexto nesta execução:** acesso externo ao GitHub bloqueado (HTTP 403 no ambiente), e este repositório local está vazio além de `.gitkeep`.
> 
> Este documento foi desenhado para ser **operacionalmente útil agora** e, ao mesmo tempo, servir como **estrutura-mãe** para assimilação profunda quando os arquivos `NORTH STAR`, pasta `LORE` e pasta/arquivos `LOGS` forem disponibilizados localmente.

---

## 1) Objetivo deste documento

Este arquivo existe para orientar uma IA (e também humanos) em quatro frentes:

1. **Entendimento sistêmico do projeto** (produto, pedagogia, operação e tecnologia).
2. **Memória operacional** com rastreabilidade entre decisões, hipóteses, experimentos e resultados.
3. **Padronização de leitura e escrita** para manter consistência entre múltiplas interações de IA.
4. **Base para execução de roadmap** com critérios claros de sucesso.

Resultado esperado: qualquer IA que leia este documento consiga entrar no projeto com contexto suficiente para **diagnosticar**, **priorizar** e **executar** mudanças com baixo risco.

### 1.1 Diretriz estratégica 2026 (ordem obrigatória de foco)

Para reduzir dispersão e aumentar impacto pedagógico, este projeto adota a seguinte ordem de execução:

1. **SEMENTES** (foco total inicial)
2. **BROTOS** (somente após critérios mínimos de maturidade de SEMENTES)
3. **RAÍZES** (somente após estabilidade inicial de BROTOS; escopo do 1º ano fica por último)

Regra operacional: enquanto a etapa ativa não atingir os critérios de pronto definidos neste documento, iniciativas da próxima etapa ficam em modo de **descoberta leve** (sem consumir capacidade principal de entrega).

---

## 2) Escopo e fonte de verdade

### 2.1 Fontes canônicas (ordem de precedência)

Quando disponíveis no repositório local, a IA deve usar esta hierarquia:

1. `NORTH STAR` (visão, missão, princípios e metas de longo prazo)
2. `LORE/` (conhecimento vivo do domínio, regras, convenções e decisões arquiteturais/pedagógicas)
3. `LOGS/` (histórico factual: decisões, incidentes, testes, mudanças)
4. Código-fonte e testes automatizados
5. Issues/PRs e documentação satélite

### 2.2 Regra de conflito

Se houver conflito entre documentos:

- **Direção estratégica**: `NORTH STAR` vence.
- **Implementação e contratos internos**: `LORE` vence.
- **Evidência do que aconteceu**: `LOGS` vence para fatos históricos.
- **Comportamento real do sistema**: código + testes vencem para estado atual executável.

---

## 3) Perguntas-mestre que a IA deve responder

Após leitura profunda, a IA deve conseguir responder com objetividade:

1. Qual problema educacional o projeto resolve e para quem?
2. Qual transformação de aprendizagem ele promete (antes/depois)?
3. Quais princípios não-negociáveis orientam decisões?
4. Quais fluxos críticos de usuário sustentam valor real?
5. Quais métricas de sucesso do produto e da aprendizagem?
6. Quais dívidas técnicas/pedagógicas estão no caminho?
7. O que **não** deve ser alterado sem validação explícita?

---

## 4) Mapa de entendimento profundo (framework para leitura)

### 4.1 Camada Norte (NORTH STAR)

Extrair e registrar:

- **Missão**: por que o projeto existe.
- **Visão**: que futuro pretende criar.
- **Tese pedagógica**: como estudantes aprendem melhor neste contexto.
- **Princípios orientadores**: o que sempre priorizar em trade-offs.
- **Não-objetivos**: o que conscientemente fica fora de escopo.
- **North-star metric**: indicador principal de sucesso.

### 4.2 Camada de conhecimento operativo (LORE)

Mapear:

- Linguagem e taxonomia oficial (termos canônicos).
- Modelos mentais pedagógicos (sequência, dificuldade, feedback, avaliação).
- Regras de domínio matemático (notação, validação, tolerâncias, edge cases).
- Padrões de implementação (arquitetura, naming, estrutura de módulos).
- Regras de UX/didática (clareza, progressão, acessibilidade).
- Decisões antigas e seus motivos (evitar regressão contextual).

### 4.3 Camada factual temporal (LOGS)

Organizar sinais históricos:

- Mudanças relevantes por data e impacto.
- Bugs recorrentes e causa raiz.
- Hipóteses testadas e resultados.
- Riscos que já se materializaram.
- Ações que funcionaram vs. ações que fracassaram.

---

## 5) Estrutura de memória para IA (compacta e reutilizável)

A IA deve manter este quadro atualizado a cada ciclo de trabalho:

- **Estado do produto**: estável | em refatoração | em expansão.
- **Hipóteses ativas**: lista curta com risco e confiança.
- **Decisões abertas**: pendências de produto/técnica.
- **Restrições**: técnicas, pedagógicas, prazo, equipe.
- **Próxima melhor ação**: item único de maior alavanca.

---

## 6) PRD operacional (versão IA-friendly)

### 6.0 Macrovisão por estágios (SEMENTES → BROTOS → RAÍZES)

#### Estágio 1 — SEMENTES
- Objetivo: construir base de aprendizagem, linguagem e experiência inicial sem fricção.
- Foco: clareza conceitual, onboarding, progressão curta e feedback imediato.
- Critério de passagem: consistência de uso e evidência de valor nas métricas de entrada.

#### Estágio 2 — BROTOS
- Objetivo: expandir repertório e aumentar profundidade pedagógica mantendo engajamento.
- Foco: ampliação de trilhas, reforço adaptativo e monitoramento de evolução.
- Critério de passagem: retenção e desempenho sustentados após expansão.

#### Estágio 3 — RAÍZES
- Objetivo: consolidar domínio estrutural de aprendizagem (base durável e transferível).
- Foco: competências estruturantes, avaliação longitudinal e robustez curricular.
- Entrada no estágio: apenas após base confiável dos dois estágios anteriores.

## 6.1 Problema

Definir com clareza:

- Quem é o usuário principal (ex.: estudante, professor, coordenação).
- Quais dores atuais (fricção, baixa retenção, baixa compreensão, etc.).
- Qual impacto se nada mudar.

## 6.2 Objetivo

- Meta principal com prazo.
- Métricas primárias e secundárias.
- Critérios de sucesso mensuráveis.

## 6.3 Público e personas

- Persona primária: necessidades, contexto, limitações.
- Persona secundária: influência no ciclo de adoção.
- Antipersona: para quem a solução não é otimizada.

## 6.4 Proposta de valor

- Ganho pedagógico esperado.
- Ganho de usabilidade e engajamento.
- Diferencial em relação a soluções alternativas.

## 6.5 Escopo funcional

- **In scope** (MVP e incremental).
- **Out of scope** (explicitar para evitar dispersão).
- Dependências técnicas e de conteúdo.

## 6.6 Requisitos

### Funcionais
- Fluxos essenciais do usuário.
- Comportamentos esperados em cenários comuns e de exceção.

### Não-funcionais
- Performance, segurança, disponibilidade.
- Acessibilidade e qualidade pedagógica mínima.
- Observabilidade (logs, métricas e alertas).

## 6.7 Riscos e mitigação

- Risco pedagógico (aprendizagem superficial).
- Risco técnico (quebras regressivas).
- Risco operacional (falta de telemetria).
- Plano de contingência por risco crítico.

## 6.8 Plano de validação

- Testes automatizados e critérios de aceite.
- Testes de usabilidade/eficácia pedagógica.
- Rollout progressivo e monitoramento pós-lançamento.

### 6.9 Política de alocação de energia (priorização anual)

#### Regra sugerida para o ciclo atual
- **100% da energia de entrega em SEMENTES** até atingir critérios de maturidade.
- BROTOS: somente atividades preparatórias (pesquisa, hipóteses, design de baixo custo).
- RAÍZES: apenas registro de visão e dependências futuras.

#### Critérios de maturidade para liberar passagem SEMENTES → BROTOS
Considerar passagem quando TODOS os itens forem verdadeiros por janela contínua (ex.: 4–8 semanas):

1. Fluxo principal com baixa fricção e baixa taxa de abandono.
2. Indicadores de aprendizagem inicial em tendência positiva.
3. Qualidade mínima técnica (erros críticos sob controle, observabilidade funcional).
4. Operação estável (capacidade de suporte sem retrabalho excessivo).

#### Critérios de maturidade para liberar passagem BROTOS → RAÍZES
1. Retenção sustentada após expansão de conteúdo/fluxos.
2. Evidência de progressão real de competências.
3. Arquitetura e conteúdo estáveis para evolução de longo prazo.

---

## 7) Protocolo de leitura específica de `NORTH STAR`, `LORE` e `LOGS`

Quando os arquivos existirem localmente, aplicar o processo abaixo sem pular etapas.

### Etapa A — Leitura do `NORTH STAR`

1. Marcar frases com caráter de **princípio**.
2. Extrair metas explícitas e implícitas.
3. Converter visão em critérios operáveis (o que fazer / o que evitar).
4. Gerar “mandamentos de decisão” em formato curto.

### Etapa B — Leitura da pasta `LORE/`

1. Inventariar todos os arquivos com uma linha-resumo por arquivo.
2. Consolidar um glossário oficial.
3. Mapear regras invariantes (não quebrar).
4. Identificar padrões arquiteturais e anti-patterns já conhecidos.

### Etapa C — Leitura da pasta `LOGS/`

1. Construir timeline de eventos relevantes.
2. Ligar evento → causa raiz → ação tomada → efeito observado.
3. Separar sinal de ruído (eventos episódicos vs. sistêmicos).
4. Criar lista de “erros que não podem se repetir”.

### Etapa D — Síntese cruzada

- Cruzar `NORTH STAR` (intenção) com `LOGS` (realidade).
- Identificar gaps de execução.
- Priorizar 3 iniciativas de maior impacto e menor risco.

---

## 8) Formato padrão de saída para futuras análises da IA

Sempre produzir:

1. **Resumo executivo** (5–10 bullets).
2. **Mapa de aderência ao North Star** (alto/médio/baixo + evidência).
3. **Diagnóstico técnico-pedagógico**.
4. **Plano tático de 30 dias** com marcos semanais.
5. **Riscos ativos** e sinais de monitoramento.

---

## 9) Backlog inicial recomendado (agnóstico a stack)

1. Consolidar índice vivo dos artefatos (`NORTH STAR`, `LORE`, `LOGS`).
2. Implementar rastreabilidade decisão ↔ commit ↔ resultado.
3. Definir métricas mínimas de aprendizagem e adoção.
4. Padronizar critérios de aceite técnico + pedagógico.
5. Criar rotina de revisão quinzenal de alinhamento ao North Star.

### 9.1 Backlog priorizado por estágio

#### Prioridade máxima — SEMENTES
1. Definir com precisão o que é “SEMENTES” no produto (escopo pedagógico + funcional).
2. Fechar fluxo principal ponta a ponta com telemetria mínima.
3. Instrumentar métricas de ativação, conclusão e aprendizagem inicial.
4. Reduzir fricções de UX no primeiro contato.
5. Estabelecer rituais de revisão semanal focados só em SEMENTES.

#### Prioridade futura — BROTOS (somente preparação)
1. Mapear hipóteses de expansão sem desenvolvimento pesado.
2. Definir critérios de entrada e sucesso de BROTOS.

#### Prioridade posterior — RAÍZES (visão)
1. Registrar macroarquitetura curricular/tecnológica de longo prazo.
2. Listar pré-requisitos bloqueantes para iniciar RAÍZES no momento certo.

---

## 10) Template de “Snapshot de Contexto” (para cada ciclo)

> Preencher ao início e ao fim de cada ciclo de desenvolvimento.

- **Data/Ciclo:**
- **Objetivo do ciclo:**
- **Hipótese principal:**
- **Mudanças realizadas:**
- **Evidências coletadas:**
- **Resultado:**
- **Impacto no North Star:**
- **Próximo passo recomendado:**

---

## 11) Lacunas identificadas nesta execução

Como não foi possível acessar o repositório remoto e não há conteúdo local além de `.gitkeep`, as seguintes lacunas permanecem:

- Sem leitura factual do arquivo `NORTH STAR`.
- Sem análise concreta dos arquivos da pasta `LORE/`.
- Sem auditoria histórica dos arquivos em `LOGS/`.
- Sem validação de arquitetura/código/stack atual do projeto original.

**Ação recomendada imediata:** disponibilizar no repositório local uma cópia dos artefatos (`NORTH STAR`, `LORE/`, `LOGS/`) para geração da versão 2 deste PRD com diagnóstico factual completo.

---

## 12) Definição de pronto para a versão 2 (factual)

A versão 2 deste norteador será considerada pronta quando incluir:

1. Resumo fiel do `NORTH STAR` com citações por seção.
2. Mapa completo da `LORE/` com glossário e invariantes.
3. Linha do tempo crítica da `LOGS/` com aprendizados.
4. Priorização de roadmap baseada em evidência.
5. Recomendações técnicas e pedagógicas contextualizadas no código real.

---

## 13) Nota final

Este documento foi estruturado para já funcionar como “sistema operacional de contexto” para IA. Assim que os artefatos reais forem disponibilizados localmente, ele pode ser enriquecido de forma incremental sem perder consistência histórica.

---

## 14) Perguntas de alinhamento com a visão do produto (a responder antes da V2 factual)

### 14.1 Sobre SEMENTES (foco imediato)
1. Em termos práticos, quais módulos/funcionalidades representam SEMENTES hoje?
2. Qual problema mais crítico de aprendizagem SEMENTES precisa resolver primeiro?
3. Qual métrica única define “SEMENTES está funcionando”?
4. Qual público é prioritário na etapa SEMENTES (perfil, faixa etária, contexto)?
5. O que está explicitamente fora de escopo de SEMENTES neste semestre?

### 14.2 Sobre BROTOS (próxima etapa)
1. Quais sinais concretos autorizam iniciar BROTOS?
2. Qual risco você mais teme ao entrar cedo demais em BROTOS?
3. Que parte de BROTOS pode ser pesquisada sem tirar foco de SEMENTES?

### 14.3 Sobre RAÍZES (1º ano por último)
1. Para você, RAÍZES é mais curricular, tecnológico, avaliativo ou uma combinação?
2. Qual seria um marco mínimo de RAÍZES ao fim do 1º ano?
3. O que não pode faltar em RAÍZES para preservar a essência da Matemática Viva?

### 14.4 Sobre governança e decisão
1. Quem decide oficialmente a passagem de fase (SEMENTES → BROTOS → RAÍZES)?
2. Qual cadência de revisão estratégica você prefere (semanal, quinzenal, mensal)?
3. Você quer um modelo de “gate de fase” com checklist formal e evidências obrigatórias?

---

## 15) Decisões consolidadas com base no alinhamento atual

> Esta seção transforma suas respostas em diretrizes operacionais para execução imediata.

### 15.1 Estrutura de produto para SEMENTES (versão atual)

- **Escopo oficial de SEMENTES:**
  - **Lição 000**: introdução do Reino, contexto, contrato narrativo e apresentação dos Guardiões.
  - **Lições 001–120**: núcleo do primeiro ciclo com progressão leve, concreta e imersiva.
- **Regra de foco:** toda energia de conteúdo, produto e validação deve priorizar essas 121 lições (000 + 120).
- **Regra de estabilidade:** melhorias são permitidas, mas sem quebrar continuidade narrativa e coerência da LORE.

### 15.2 Objetivo pedagógico central de SEMENTES

Objetivo principal: criar vínculo afetivo-cognitivo com a matemática por meio de narrativa imersiva, natureza e experiências concretas, com pressão mínima de formalização antes dos 7 anos.

### 15.3 Faixa etária e intensidade pedagógica

- Faixa principal: **5, 6 e 7 anos**.
- Princípio de progressão:
  - 5–6 anos: predominância de linguagem concreta, imagética, oralidade, observação e jogo.
  - 7 anos: transição gradual para maior formalização (ainda leve), sem ruptura da imersão.
- Diretriz neuroeducacional adotada neste PRD:
  - formalização simbólica intensa só deve aumentar após base atencional, emocional e sensório-motora estar estabelecida.

### 15.4 Questão-chave de produto (adesão e participação dos pais)

Hipótese orientadora: em SEMENTES, a adesão cresce quando os pais percebem três ganhos simultâneos:

1. a criança engaja com alegria e curiosidade;
2. existe estrutura clara para aplicação em casa;
3. há evidência observável de progresso (mesmo que inicial e qualitativo).

Implicação prática: o produto deve tratar pais como coparticipantes do processo pedagógico, com orientação simples, clara e acionável.

---

## 16) Arquitetura imersiva para narração e LORE (base replicável)

### 16.1 Objetivo da arquitetura

Criar uma estrutura narrativa profunda e reproduzível para as 121 lições iniciais, capaz de manter coerência de mundo, progressão pedagógica e reaproveitamento nos ciclos seguintes (BROTOS/RAÍZES).

### 16.2 Princípios de imersão (inspirações literárias e pedagógicas)

- **Mundo vivo e coerente**: regras internas estáveis do Reino (inspiração em fantasia clássica de mundo consistente).
- **Encantamento com sentido**: beleza narrativa sempre conectada ao aprendizado matemático.
- **Narração com imagens mentais fortes**: cenas curtas, concretas e memoráveis.
- **Progressão por encontros**: cada lição amplia o mundo e a competência, sem sobrecarga.
- **Tom pedagógico de “gentle learning”**: leveza, hábito, observação e relação com natureza.

> Referências inspiracionais solicitadas para estilo e direção: C.S. Lewis, Tolkien e princípios de Charlotte Mason (sem transformar o PRD em tratado acadêmico).

### 16.3 Modelo canônico de cada lição (template de produção)

Cada lição (000–120) deve conter blocos mínimos:

1. **Portal narrativo** (abertura imersiva curta).
2. **Cena do Reino** (evento concreto com personagens/Guardiões).
3. **Semente matemática** (conceito-alvo em linguagem apropriada à idade).
4. **Ação concreta** (atividade com objetos reais/natureza/corpo).
5. **Pergunta viva** (estimula curiosidade, não prova formal).
6. **Ritual de fechamento** (síntese afetiva + memória da jornada).
7. **Guia dos pais** (como conduzir em 5–15 min extras, sem fricção).

### 16.4 Mapa da LORE amarrado às 121 lições

Para evitar inconsistência, cada lição precisa declarar:

- ID da lição (000 a 120).
- Elemento da LORE acionado (lugar, personagem, símbolo, regra do mundo).
- Conceito matemático principal.
- Conceito matemático secundário (opcional).
- Habilidade de desenvolvimento predominante (atenção, linguagem, memória, coordenação, raciocínio inicial).
- Nível de concretude (alto/médio/baixo; em SEMENTES priorizar alto).
- Evidência esperada de aprendizagem (observável pelos pais).

---

## 17) Respostas propostas para pontos que ficaram “não entendi”

### 17.1 O que está fora de escopo de SEMENTES neste semestre?

Resposta proposta:

- formalização matemática pesada (abstração extensa, notação complexa e treino mecânico intensivo);
- expansão de escopo para além das 121 lições iniciais;
- produção extensa de trilhas avançadas de BROTOS/RAÍZES antes de validar SEMENTES;
- complexidade técnica que não aumente imersão nem aprendizagem inicial.

### 17.2 Marco mínimo de RAÍZES ao fim do 1º ano

Resposta proposta:

- LORE contínua e coesa com SEMENTES;
- documento de continuidade pedagógica SEMENTES→RAÍZES aprovado;
- 1 trilha-piloto de RAÍZES definida (não necessariamente totalmente executada), com critérios de entrada e saída;
- evidência de que a transição preserva imersão narrativa e progressão matemática.

### 17.3 “Gate de fase” (o que significa e como aplicar)

Resposta proposta:

- Gate de fase = checklist objetivo para decidir se pode avançar para BROTOS/RAÍZES.
- Deve conter evidências mínimas pedagógicas + de uso familiar.
- Sem gate validado, não há mudança de foco principal.

---

## 18) BROTOS e RAÍZES reinterpretados conforme sua diretriz

### 18.1 BROTOS

- natureza 100% concreta e leve;
- material inicial enxuto (ex.: 1 a 3 PDFs orientadores para pais e crianças);
- baixa complexidade operacional;
- continuidade estética e narrativa com SEMENTES.

### 18.2 RAÍZES

- continuação orgânica de SEMENTES (não ruptura);
- LORE como fio condutor obrigatório;
- imersão mantida como premissa central;
- evolução de profundidade sem perder encantamento.

---

## 19) Governança pedagógica e métrica de famílias (versão inicial)

### 19.1 Quem decide avanço de fase

Decisão proposta para versão inicial:

- Responsável primário: pais (sinal de uso e resposta da criança).
- Responsável metodológico: Matemática Viva (critérios por idade, atenção, prontidão e observáveis pedagógicos).
- Modelo: decisão conjunta orientada por evidências simples e recorrentes.

### 19.2 Cadência de revisão

- mínimo semanal;
- opcionalmente duas revisões na mesma semana em ciclos críticos.

### 19.3 Score pedagógico leve de prontidão (família)

Criar um score simples de 0–2 por item (0 = não observado, 1 = parcial, 2 = consistente):

1. Engajamento espontâneo da criança.
2. Tempo de atenção compatível com a idade.
3. Participação ativa na atividade concreta.
4. Recuperação narrativa (recorda personagens/cenas).
5. Sinal inicial de compreensão matemática (linguagem/ação).
6. Facilidade de aplicação pelos pais.

Interpretação sugerida:

- 0–5: manter leveza máxima e reduzir carga.
- 6–9: progressão cautelosa.
- 10–12: prontidão para ampliar gradualmente.

---

## 20) Próximo passo operacional (imediato)

1. Congelar o escopo oficial de SEMENTES em 000–120.
2. Definir template final de lição (seção 16.3) e publicar como padrão.
3. Criar matriz 000–120 (LORE × matemática × desenvolvimento × evidência).
4. Produzir piloto completo (ex.: lições 000–005) e validar com pais.
5. Rodar revisão semanal com score pedagógico leve (seção 19.3).
