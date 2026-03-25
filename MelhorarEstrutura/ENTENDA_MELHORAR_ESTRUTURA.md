# ENTENDA MELHORAR ESTRUTURA

Data de atualizacao: 2026-03-25
Status: experimento ativo
Escopo: somente `MelhorarEstrutura`

## 1) O que e este arquivo

Este arquivo existe para ser o ponto de entrada mais rapido para entender o que estamos fazendo em `MelhorarEstrutura`.

Ele resume:

1. por que esta pasta existe
2. o que ja foi produzido
3. o que esta sendo testado
4. o que ainda nao foi decidido
5. de onde retomar na proxima sessao

## 2) Verdade operacional de partida

Hoje a revisao real das licoes ainda acontece no HTML.

Isso continua sendo verdade.

`MelhorarEstrutura` nao foi criado para fingir que esse problema ja foi resolvido.
Ele foi criado para testar uma abordagem mais inteligente de discussao e convergencia antes de mexer no sistema de verdade.

## 3) O que esta sendo testado aqui

Estamos testando se a seguinte abordagem funciona melhor para pensar a evolucao de `Sementes`:

- experts em `BMAD YAML`
- task robusta de convergencia
- rodadas e discussoes com evidencia real do repo
- decisoes provisorias por etapa
- foco em reduzir custo de contexto sem perder o fio pedagogico

Importante:

isto ainda e um teste.
Nao foi adotado como novo sistema oficial do projeto.
Vamos tentar esta abordagem e avaliar se ela realmente ajuda.

## 4) O que esta pasta nao e

Esta pasta:

- nao substitui `Revisao/`
- nao substitui o fluxo `HTML-first` atual
- nao muda `build/`, `site/`, `apps/web` ou `bmad/`
- nao e ainda a implementacao da nova arquitetura

Ela e um laboratorio de pensamento guiado com embasamento.

## 5) O que ja foi criado

### 5.1 Estrutura base

- `README.md`
- `TASK_ROBUSTA_MELHORAR_ESTRUTURA.md`
- `TASK_ROBUSTA_APLICACAO_EXPERTS.md`
- `TASK_ROBUSTA_CONVERGENCIA_SUGESTAO_SEMENTES.md`
- `TASK_ROBUSTA_EXECUCAO_FASEADA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`
- `TASK_ROBUSTA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`
- `TASK_ROBUSTA_SUPERFICIES_CONSTRUCAO_SEMENTES.md`
- `orchestrator_melhorar_estrutura.yaml`

### 5.2 Experts

- `experts/arquitetura/estrategista_estrutura.yaml`
- `experts/arquitetura/vercel_first.yaml`
- `experts/conteudo/contrato_licao.yaml`
- `experts/operacao/revisao_escalavel.yaml`
- `experts/externos/mae_regente_real.yaml`

### 5.3 Rodadas e discussoes ja escritas

- `rodadas/ROUND_00_DIAGNOSTICO.md`
- `rodadas/ROUND_01_DISCUSSAO_INICIAL.md`
- `rodadas/ROUND_02_BLOCO_MINIMO.md`
- `discussoes/2026-03-19_2204_SEMENTES_PRODUTO_PADRAO_E_REVISAO_INTELIGENTE.md`
- `discussoes/2026-03-19_2223_CONTRATO_CANONICO_SEMENTES.md`
- `discussoes/2026-03-19_2225_ANATOMIA_DO_REVIEW_PACK_POR_BLOCO.md`
- `discussoes/2026-03-19_2228_FLUXO_EDITORIAL_SEMENTES.md`
- `discussoes/2026-03-25_1631_FASE_0_INVENTARIO_SUPERFICIES.md`
- `discussoes/2026-03-25_1633_FASE_1_CONTRATO_SUPERFICIE_PUBLICA.md`
- `discussoes/2026-03-25_1635_FASE_2_ENTRADA_SEMENTES.md`
- `discussoes/2026-03-25_1637_FASE_3_SUPERFICIE_DA_LICAO.md`
- `discussoes/2026-03-25_1638_FASE_4_ARCOS_E_PROGRESSAO.md`
- `discussoes/2026-03-25_1640_FASE_5_PILOTO_MINIMO.md`
- `discussoes/2026-03-25_1639_FASE_6_CONSOLIDACAO_E_DECISAO.md`
- `discussoes/2026-03-25_1641_PILOTO_MINIMO_APLICADO_MV_S_005.md`
- `discussoes/2026-03-25_1643_APLICACAO_MANUAL_PORTADOR.md`
- `discussoes/2026-03-25_1645_APLICACAO_HOME_PRINCIPAL.md`
- `discussoes/2026-03-25_1646_APLICACAO_MV_S_004.md`
- `discussoes/2026-03-25_1647_APLICACAO_MV_S_006.md`
- `discussoes/2026-03-25_1648_APLICACAO_MV_S_007_E_008.md`
- `discussoes/2026-03-25_1649_APLICACAO_MV_S_009.md`
- `discussoes/2026-03-25_1650_APLICACAO_MV_S_010.md`
- `discussoes/2026-03-25_1651_APLICACAO_MV_S_011_E_012.md`
- `discussoes/2026-03-25_1652_APLICACAO_MV_S_013_E_014.md`
- `discussoes/2026-03-25_1653_APLICACAO_MV_S_015.md`
- `discussoes/2026-03-25_1654_FASE_0_INVENTARIO_SUPERFICIES_CONSTRUCAO.md`
- `discussoes/2026-03-25_1655_APLICACAO_SUPERFICIES_CONSTRUCAO_ENTRADA.md`
- `discussoes/2026-03-25_1656_FASE_2_E_3_NAVEGACAO_INTERNA_CONSTRUCAO.md`
- `discussoes/2026-03-25_1657_FASE_4_MICROCOPY_ACAO_PRINCIPAL_CONSTRUCAO.md`
- `discussoes/2026-03-25_1658_CONSOLIDACAO_FRENTE_CONSTRUCAO_SEMENTES.md`

## 6) O que ja saiu como leitura provisoria

### 6.1 Contrato canonico de `Sementes`

Leitura provisoria:

- os `12 topicos` continuam sendo a grade canonica do ciclo
- eles podem ser organizados em camadas sem perder a ordem oficial

### 6.2 Unidade menor de revisao

Leitura provisoria:

- a melhor unidade normal de revisao nao e a licao inteira
- tambem nao e um trecho cru solto
- o melhor candidato ate aqui e `bloco com fronteiras`

### 6.3 Review pack

Leitura provisoria:

- cada bloco deve ser discutido com um `review pack`
- esse pack deve carregar funcao, contexto minimo, fronteiras e perguntas cirurgicas

### 6.4 Fluxo editorial testado

Leitura provisoria:

o fluxo mais promissor ate aqui e:

`macro -> contrato -> review pack -> patch HTML localizado -> costura HTML -> rubrica -> validacao humana`

Importante:

isso ainda e recomendacao provisoria.
Nao e decisao final do projeto.

## 7) O que ainda falta decidir

Ainda faltam pelo menos estas discussoes:

1. `PRODUTO_PUBLICADO_E_SUPERFICIES`
2. `RECOMENDACAO_FINAL`

Tambem falta responder com mais seguranca:

- o que muda ja em `Sementes`
- o que fica so como experimento
- como medir se esta abordagem ajudou de verdade

## 8) Onde retomar na proxima sessao

O ponto de retomada mais seguro e:

1. ler este arquivo
2. ler `README.md` desta pasta
3. ler `TASK_ROBUSTA_CONVERGENCIA_SUGESTAO_SEMENTES.md`
4. ler `discussoes/2026-03-19_2223_CONTRATO_CANONICO_SEMENTES.md`
5. ler `discussoes/2026-03-19_2225_ANATOMIA_DO_REVIEW_PACK_POR_BLOCO.md`
6. ler `discussoes/2026-03-19_2228_FLUXO_EDITORIAL_SEMENTES.md`
7. continuar a partir de `TASK_ROBUSTA_EXECUCAO_FASEADA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`

## 9) Frase de alinhamento para a retomada

Se retomarmos depois:

`Estamos testando se MelhorarEstrutura consegue nos levar a uma recomendacao melhor para Sementes sem mexer cedo demais na stack. Hoje a revisao ainda e HTML-first. O teste atual e ver se experts + task robusta + discussoes com evidencia conseguem produzir uma sugestao mais confiavel e aplicavel.`
