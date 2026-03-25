# TASK ROBUSTA - APLICACAO DOS EXPERTS

Data: 2026-03-19
Status: pronta para uso
Escopo: somente `MelhorarEstrutura`
Modo: deliberacao guiada ate decisao pronta para aplicacao

## Leitura rapida

Papel desta task hoje:

- ela e a ponte entre "temos experts" e "vamos tomar decisoes aplicaveis"
- ela continua valida como regra de conducao
- mas a task-mestra ativa para a trilha atual e `TASK_ROBUSTA_CONVERGENCIA_SUGESTAO_SEMENTES.md`

Se voce estiver retomando o contexto e quiser seguir a frente mais viva agora:

1. leia esta task para entender o protocolo de uso dos experts
2. depois pule para `TASK_ROBUSTA_CONVERGENCIA_SUGESTAO_SEMENTES.md`
3. a partir dali, siga pelas discussoes datadas

## 1) Missao desta task

Transformar o nucleo de experts desta pasta em um processo confiavel para sair de:

- diagnostico e intuicao

para:

- decisao estrutural clara
- criterios objetivos de escolha
- pacote pronto para aplicacao no projeto real

Em outras palavras:

Esta task existe para impedir que a conversa fique bonita, mas inutil. O alvo final e produzir uma decisao que possa ser aplicada depois com ambiguidade minima.

Reconhecimento operacional:

Hoje o time esta revisando direito no HTML. Portanto, esta task nao parte da fantasia de que a camada de revisao ja mudou. Ela parte do HTML como superficie real atual e pergunta qual transicao, se houver, faz sentido.

## 2) Pergunta-mestra

Qual estrutura de conteudo e revisao devemos adotar para reduzir dependencia de HTML longo, manter Vercel como base inicial e preservar a continuidade curricular?

## 2.1 Estado desta task na trilha atual

Leitura honesta:

- esta task ajudou a sair da fase de intuicao
- a trilha ja avancou para a fase de convergencia
- portanto, hoje ela funciona mais como base de metodo do que como documento central de execucao

## 3) O que conta como "pronto para aplicar"

Uma decisao so estara pronta para aplicacao quando existir:

- uma unidade revisavel definida
- uma fronteira clara entre conteudo, contrato, revisao e validacao final
- um fluxo de trabalho simples o bastante para uso real
- uma justificativa com evidencias do repo
- uma recomendacao final com riscos e nao-objetivos explicitos
- um posicionamento claro sobre o papel do HTML no curto prazo

Se faltar um desses pontos, ainda estamos em fase de conversa, nao de aplicacao.

## 4) Entradas obrigatorias

Antes de rodar as proximas discussoes, considerar como base:

- `README.md`
- `TASK_ROBUSTA_MELHORAR_ESTRUTURA.md`
- `orchestrator_melhorar_estrutura.yaml`
- `rodadas/ROUND_00_DIAGNOSTICO.md`
- `rodadas/ROUND_01_DISCUSSAO_INICIAL.md`
- `sinteses/HIPOTESES_INICIAIS.md`

Experts obrigatorios:

- `experts/arquitetura/estrategista_estrutura.yaml`
- `experts/arquitetura/vercel_first.yaml`
- `experts/conteudo/contrato_licao.yaml`
- `experts/operacao/revisao_escalavel.yaml`
- `experts/externos/mae_regente_real.yaml`

## 5) Protocolo de execucao das proximas rodadas

Toda rodada futura deve:

1. abrir com uma pergunta unica
2. listar evidencias reais com tags `E1`, `E2`, `E3`
3. citar a rodada anterior quando relevante com `R0`, `R1`, `R2`
4. fazer cada expert sustentar sua leitura com evidencia ou apontar explicitamente que esta inferindo
5. registrar tensoes reais
6. fechar com decisao provisoria
7. explicitar o que ainda nao foi decidido

Regra:

Nao pular da evidencia para a implementacao. Primeiro consolidar a decisao estrutural.

Regra adicional:

Nao tratar HTML como mero detalhe enquanto ele continuar sendo a superficie operacional real de revisao.

## 6) Sequencia recomendada de rodadas

### ROUND 02 - MENOR BLOCO REVISAVEL

Pergunta:

Qual e a menor unidade de bloco que continua pedagogicamente inteligivel e operacionalmente revisavel?

Evidencias minimas:

- blocos ja nomeados em `apps/web/lib/contracts/lesson-structure.ts`
- exemplos reais das licoes `002`, `004`, `006`, `008`
- sinais de continuidade presentes em YAML e HTML
- o fato de que o patch e a revisao hoje ainda pousam no HTML

Decisao obrigatoria desta rodada:

- `jornada` fica inteira ou pode quebrar
- `concreto` fica inteiro ou pode quebrar
- quais blocos sao obrigatorios em toda licao

Saida esperada:

- `rodadas/ROUND_02_BLOCO_MINIMO.md`

### ROUND 03 - CONTRATO E FRONTEIRAS

Pergunta:

Depois de definir o bloco minimo, quais fronteiras de contrato precisamos para revisar sem duplicar contexto?

Evidencias minimas:

- resultado da `ROUND 02`
- piloto `content/lessons`
- template V6.5 de Sementes

Decisao obrigatoria desta rodada:

- o que pertence a `meta`
- o que pertence a `lore`
- o que pertence a `blocos`
- o que pertence a `qa`

Saida esperada:

- `rodadas/ROUND_03_CONTRATO_E_FRONTEIRAS.md`
- `sinteses/MATRIZ_FRONTEIRAS_PRELIMINAR.md`

### ROUND 04 - FLUXO DE REVISAO E EVIDENCIAS

Pergunta:

Em que ordem o time deve revisar conteudo, contrato e HTML final para reduzir retrabalho?

Evidencias minimas:

- logs de revisao topico a topico
- resultados da `ROUND 03`
- papel atual do HTML no processo

Decisao obrigatoria desta rodada:

- se o HTML continua como camada principal no curto prazo ou vira somente evidencia
- quando o HTML entra, caso deixe de ser camada principal
- quais evidencias precisam existir antes do HTML
- quais gates sao minimos e quais seriam excesso

Saida esperada:

- `rodadas/ROUND_04_FLUXO_DE_REVISAO.md`
- `sinteses/RUNBOOK_REVISAO_MINIMO.md`

### ROUND 05 - PACOTE PRONTO PARA APLICAR

Pergunta:

Qual o menor plano de aplicacao no projeto real que respeita o que foi decidido e nao explode o escopo?

Evidencias minimas:

- resultados das rodadas 02 a 04
- restricoes do deploy atual
- gargalos do pipeline atual

Decisao obrigatoria desta rodada:

- onde aplicar primeiro
- em qual lote aplicar
- o que NAO migrar ainda
- qual artefato vira fonte de verdade na fase piloto

Saida esperada:

- `rodadas/ROUND_05_PLANO_DE_APLICACAO.md`
- `sinteses/DECISAO_ESTRUTURAL_PRONTA_PARA_APLICAR.md`

## 7) Artefatos obrigatorios para encerrar a fase

Ao final desta task, devem existir:

- `ROUND_02_BLOCO_MINIMO.md`
- `ROUND_03_CONTRATO_E_FRONTEIRAS.md`
- `ROUND_04_FLUXO_DE_REVISAO.md`
- `ROUND_05_PLANO_DE_APLICACAO.md`
- `MATRIZ_FRONTEIRAS_PRELIMINAR.md`
- `RUNBOOK_REVISAO_MINIMO.md`
- `DECISAO_ESTRUTURAL_PRONTA_PARA_APLICAR.md`

## 8) Checklist de qualidade por rodada

Cada rodada so passa se:

- usar evidencias reais do repo
- deixar claro onde terminou o fato e comecou a inferencia
- mostrar tensao entre experts
- produzir uma decisao provisoria concreta
- reduzir ambiguidade para a rodada seguinte

## 9) Checklist de qualidade final

O pacote so estara pronto para aplicar se:

- houver uma recomendacao final unica
- os riscos residuais estiverem escritos
- os nao-objetivos estiverem escritos
- o primeiro lote de aplicacao estiver definido
- a compatibilidade com Vercel continuar explicita
- a unidade revisavel estiver nomeada sem ambiguidade
- o papel operacional do HTML estiver decidido sem ambiguidade

## 10) Sinais de desvio

Parar e recalibrar se acontecer qualquer um destes:

- a conversa virar disputa de stack em vez de unidade revisavel
- aparecer backend como resposta default para problema editorial
- os experts repetirem o mesmo argumento com palavras diferentes
- a proposta final aumentar muito o numero de arquivos sem ganho claro
- a discussao perder contato com evidencias reais do repo

## 11) Definition of Ready para aplicacao

Quando esta task terminar, a fase estara pronta para aplicacao se conseguirmos responder de forma curta e objetiva:

1. Qual e a menor unidade revisavel?
2. Qual e o contrato minimo?
3. Qual e o fluxo minimo de revisao?
4. Onde aplicamos primeiro?
5. O que fica para depois?
6. O HTML continua sendo a superficie principal no curto prazo ou nao?

Se a resposta ainda estiver longa, difusa ou cheia de "depende", a fase ainda nao esta pronta.
