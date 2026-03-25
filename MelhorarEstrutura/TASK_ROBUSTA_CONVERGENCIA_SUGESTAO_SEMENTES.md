# TASK ROBUSTA - CONVERGENCIA DA SUGESTAO ESTRUTURAL DE SEMENTES

Data: 2026-03-19
Status: pronta para deliberacao aprofundada
Escopo: somente `MelhorarEstrutura`
Modo: discussao guiada ate recomendacao final com embasamento forte

## Leitura rapida

Esta e a task central da trilha atual.

Ela existe para levar `MelhorarEstrutura` da exploracao para uma recomendacao unica e defensavel sobre `Sementes`.

Leitura do estado hoje:

- esta abordagem ainda e um teste
- a revisao real ainda acontece no HTML
- a discussao atual nao esta tentando trocar a stack inteira
- a discussao atual esta tentando descobrir o menor sistema que melhora revisao, produto e fidelidade

Onde ja avancamos:

1. o contrato canonico de `Sementes` ja foi discutido
2. a anatomia do `review pack` por bloco ja foi discutida
3. o fluxo editorial recomendado para esta fase ja foi discutido

Onde retomar:

- seguir para `TASK_ROBUSTA_EXECUCAO_FASEADA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`

## 1) Missao desta task

Levar a pasta `MelhorarEstrutura` da fase de exploracao para uma fase de convergencia.

Em termos praticos:

esta task existe para impedir que a conversa fique eternamente em boas intuicoes.

Ela deve nos levar a uma resposta clara para esta pergunta:

qual e a melhor sugestao estrutural, editorial e de produto para `Sementes` agora, considerando:

- fidelidade ao `North Star`
- usabilidade para a familia real
- carga mental da revisao
- custo de contexto para IA
- padrao forte das licoes do ciclo
- compatibilidade com o site atual e com Vercel no curto prazo

## 2) Verdade operacional de partida

Esta task assume explicitamente:

- hoje a revisao operacional real ainda acontece no HTML
- o site atual em producao ainda mistura linguagem interna e superficie familiar
- `Sementes` ja tem um padrao estrutural bastante repetivel
- cada palavra da licao importa
- o custo de revisar HTML inteiro esta alto demais para humanos e para IA
- o objetivo agora nao e trocar toda a stack
- o objetivo agora e descobrir o menor sistema que melhora revisao, fidelidade e produto

## 3) Pergunta-mestra

Qual e o menor sistema editorial e estrutural que:

1. reduz a dependencia de revisao no HTML inteiro
2. preserva a qualidade palavra por palavra
3. reforca o `North Star` no produto
4. funciona primeiro em `Sementes`
5. prepara um modelo reaproveitavel para os ciclos seguintes

## 4) O que esta task quer decidir ao final

Ao terminar esta task, precisamos ter uma recomendacao unica, curta e defensavel sobre:

- o papel do HTML no curto prazo
- o contrato canonico de blocos de `Sementes`
- o artefato ideal de revisao
- o que muda no produto publicado
- o que fica para depois

Se sairmos com varias opcoes sem hierarquia, esta task falhou.

## 5) Fontes obrigatorias de verdade

Toda discussao desta task deve consultar, quando relevante:

### Identidade e criterio

- `LORE/north_star.yaml`
- `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`
- `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/009_TASTE_EDITORIAL_E_AUTORIA_HUMANA.md`
- `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md`

### Padrao de `Sementes`

- `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml`
- `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md`
- licoes reais do ciclo em YAML e HTML

### Estado tecnico e operacional

- `docs/MAPA_EXECUCAO_PROJETO.md`
- `build/fases/sementes.py`
- `vercel.json`
- `apps/web/lib/contracts/lesson-structure.ts`
- `apps/web/lib/content/loader.ts`

### Evidencia de revisao real

- logs topico a topico ja produzidos
- tasks robustas de revisao premium
- feedbacks de maes reais quando houver sintese consolidada

### Base ja criada em `MelhorarEstrutura`

- `TASK_ROBUSTA_MELHORAR_ESTRUTURA.md`
- `TASK_ROBUSTA_APLICACAO_EXPERTS.md`
- `rodadas/ROUND_00_DIAGNOSTICO.md`
- `rodadas/ROUND_01_DISCUSSAO_INICIAL.md`
- `rodadas/ROUND_02_BLOCO_MINIMO.md`
- `discussoes/2026-03-19_2204_SEMENTES_PRODUTO_PADRAO_E_REVISAO_INTELIGENTE.md`

## 6) Principios inegociaveis desta task

Toda sugestao futura precisa obedecer estes principios:

### 6.1 Familia no centro

Se a solucao melhora o sistema, mas piora a vida da mae real, ela reprova.

### 6.2 Clareza antes de engenhosidade

Se a solucao e elegante no papel, mas dificil de explicar e sustentar, ela reprova.

### 6.3 Contrato antes de formato

Primeiro decidir a funcao e a fronteira dos blocos.
So depois discutir se isso vira YAML unico, multi-arquivo, JSON ou outra forma.

### 6.4 HTML como realidade atual

Nao tratar o HTML como se ele ja tivesse deixado de ser a camada principal.

### 6.5 Produto e revisao andam juntos

Se a estrutura de revisao sugerida melhora o backstage, mas nao aproxima o produto da promessa familiar, a resposta esta incompleta.

### 6.6 Sementes primeiro

Toda decisao precisa ser justificavel em `Sementes` antes de virar modelo para outros anos.

## 7) Hipoteses em disputa

Esta task nao parte de uma resposta pronta. Ela vai tensionar estas hipoteses:

### Hipotese A - HTML melhor assistido

Continuar revisando no HTML, mas com prompts, task robusta e checklist melhores.

Vantagem:

- menor mudanca imediata

Risco:

- a unidade revisavel continua grande demais

### Hipotese B - Contrato de blocos + review packs

Manter fonte razoavel por licao, mas gerar artefatos menores de revisao por bloco.

Vantagem:

- reduz custo de contexto sem explodir numero de arquivos canonicos

Risco:

- exige contrato de ciclo bem definido

### Hipotese C - Multi-arquivo atomico por licao

Quebrar a licao em varios arquivos de conteudo como fonte primaria.

Vantagem:

- granularidade maxima de revisao

Risco:

- pode aumentar fragmentacao, abertura de arquivos e carga operacional

### Hipotese D - Superficie dupla de produto

Separar melhor a interface interna da interface familiar, mesmo sem mudar drasticamente a fonte da licao.

Vantagem:

- melhora a coerencia de produto mais rapido

Risco:

- nao resolve sozinho o gargalo editorial

## 8) Sequencia obrigatoria de discussoes

Esta task deve ser executada em uma escada de discussoes. Cada etapa precisa gerar um arquivo novo em `discussoes/`.

### DISC 01 - PADRAO CANONICO DE SEMENTES

Pergunta:

qual e a lista canonica de blocos de `Sementes`, em que ordem eles aparecem e qual e a funcao de cada um?

Temas obrigatorios:

- naming canonico
- aliases legados
- ordem editorial
- papel de cada bloco
- o que e bloco pedagogico e o que e moldura de publish

Saida esperada:

- `discussoes/YYYY-MM-DD_HHMM_CONTRATO_CANONICO_SEMENTES.md`

### DISC 02 - ANATOMIA DO REVIEW PACK

Pergunta:

qual e o menor artefato de revisao por bloco que entrega contexto suficiente sem reabrir a licao inteira?

Temas obrigatorios:

- campos obrigatorios
- evidencias minimas
- fronteiras anterior e posterior
- perguntas especificas por bloco
- relacao com `North Star`, `TX10` e `TASTE`

Saida esperada:

- `discussoes/YYYY-MM-DD_HHMM_REVIEW_PACKS_POR_BLOCO.md`

### DISC 03 - FLUXO EDITORIAL IDEAL

Pergunta:

em que ordem o time deve passar por contrato, bloco, HTML e validacao final?

Temas obrigatorios:

- o que revisar antes
- o que revisar durante
- o que revisar so no final
- quando a IA entra
- quando o humano precisa julgar

Saida esperada:

- `discussoes/YYYY-MM-DD_HHMM_FLUXO_EDITORIAL_SEMENTES.md`

### DISC 04 - PRODUTO PUBLICADO E SUPERFICIES

Pergunta:

o que no site publicado precisa mudar para que `Sementes` pareca mais fiel ao `North Star` e menos painel interno?

Temas obrigatorios:

- linguagem interna versus linguagem familiar
- entrada do ciclo
- explicacao do ritmo da licao
- beneficio para o Portador
- progressao por arcos

Saida esperada:

- `discussoes/YYYY-MM-DD_HHMM_PRODUTO_PUBLICADO_SEMENTES.md`

### DISC 05 - PILOTO MINIMO

Pergunta:

qual e o menor piloto que prova a sugestao sem explodir escopo?

Temas obrigatorios:

- qual licao ou pequeno lote usar
- quais artefatos gerar
- como medir se melhorou
- o que NAO mexer ainda

Saida esperada:

- `discussoes/YYYY-MM-DD_HHMM_PILOTO_MINIMO_SEMENTES.md`

### DISC 06 - RECOMENDACAO FINAL

Pergunta:

qual sugestao final vence, por que ela vence e quais riscos restam?

Temas obrigatorios:

- recomendacao principal
- recomendacoes descartadas
- riscos residuais
- lote inicial
- papel do HTML
- papel do contrato
- papel do produto

Saida esperada:

- `sinteses/SUGESTAO_FINAL_SEMENTES_COM_EMBASAMENTO.md`

## 9) Estrutura obrigatoria de cada novo arquivo de discussao

Cada discussao nova deve seguir esta estrutura:

1. titulo
2. data
3. hora
4. tema
5. pergunta central
6. fontes de evidencia
7. fatos observados
8. tensoes reais
9. hipoteses ou opcoes
10. leitura consolidada
11. recomendacao provisoria
12. riscos
13. proximo tema sugerido

## 10) Protocolo de argumentacao

Toda argumentacao nesta task deve:

- citar evidencia do repo, do site ou de discussoes anteriores
- separar fato de inferencia
- dizer quando algo e apenas intuicao
- evitar frases vagas como `parece melhor` sem criterio
- explicitar o custo da opcao rejeitada

Regra adicional:

quando houver duas boas opcoes, comparar:

- custo de contexto
- custo operacional
- fidelidade ao `North Star`
- facilidade para a familia
- escalabilidade para o lote restante

## 11) O que precisa ser medido em cada sugestao

Toda sugestao precisa ser avaliada nas seguintes dimensoes:

### 11.1 Fidelidade editorial

- ajuda a manter cada palavra intencional?
- reduz traducao mental?
- preserva o `TASTE` humano?

### 11.2 Usabilidade para o Portador

- ajuda a ler e conduzir ao mesmo tempo?
- reduz releitura?
- deixa claro o que falar, mostrar e fazer?

### 11.3 Aprendizagem da crianca

- preserva a ordem `perceber -> relacionar -> nomear`?
- protege concretude?
- evita antecipar abstracao?

### 11.4 Operacao de revisao

- reduz o contexto necessario para revisar?
- permite trabalhar por bloco?
- torna o processo mais repetivel?

### 11.5 Produto

- aproxima o site da promessa da marca?
- deixa `Sementes` mais compreensivel como ciclo?
- reforca o valor percebido para a familia?

## 12) Anti-padroes desta task

Parar e recalibrar se a discussao comecar a:

- tratar stack como assunto principal
- propor banco ou backend como reflexo automatico
- multiplicar arquivos canonicos sem ganho comprovado
- misturar linguagem de operacao interna com linguagem familiar
- chamar de `simples` algo que a mae real nao conseguiria sustentar
- usar o `North Star` como slogan e nao como gate
- deixar a IA assumir juizo final de `TASTE`

## 13) Entregaveis obrigatorios

Ao fim desta task, devem existir:

- 5 novos arquivos de discussao em `discussoes/`
- 1 sintese final em `sinteses/`
- 1 matriz clara de recomendacao
- 1 pacote de prompts refinados
- 1 recorte de piloto minimo

## 14) Definition of Done

Esta task so termina quando conseguirmos responder, sem ambiguidade grande:

1. Qual e o contrato canonico de `Sementes`?
2. Qual e o artefato ideal de revisao?
3. Qual e o papel do HTML no curto prazo?
4. O que muda no produto publicado?
5. Qual e o menor piloto para provar a proposta?
6. Por que essa sugestao vence as outras?

## 15) Formula de fechamento esperada

Se a task estiver madura no final, a resposta final deve soar assim:

`Para Sementes, recomendamos manter a fonte atual no curto prazo, congelar um contrato canonico de blocos, gerar review packs por bloco, mover a revisao estrutural para esses pacotes e deixar o HTML como gate final de costura e validacao. No produto, recomendamos separar melhor a face interna da face familiar e tornar o ritmo do ciclo mais explicito para o Portador.`

Se ainda nao conseguirmos dizer algo nesse nivel de clareza, ainda nao convergimos o suficiente.
