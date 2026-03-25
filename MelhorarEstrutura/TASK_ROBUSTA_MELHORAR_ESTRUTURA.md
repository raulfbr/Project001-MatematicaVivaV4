# TASK ROBUSTA - MELHORAR ESTRUTURA

Data: 2026-03-19
Status: discussao inicial
Escopo: somente `MelhorarEstrutura`
Modo: pre-implementacao

## 1) Objetivo da investigacao

Definir um recorte inicial, pequeno e solido, para melhorar a estrutura de revisao das licoes do projeto sem depender da releitura constante de HTMLs longos e sem quebrar a continuidade curricular.

## 2) Dor atual confirmada no repo

Fatos observaveis:

- o trilho principal atual e `YAML -> Jinja -> HTML estatico -> Vercel`
- o repo ja tem um piloto `apps/web` com `content/lessons/*` e contrato por blocos
- as licoes revisadas hoje sao trabalhadas operacionalmente direto no HTML
- os YAMLs e pilotos alternativos existem, mas ainda nao substituiram o HTML como superficie real de revisao

Amostra real levantada:

- `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`: 615 linhas
- `site/sementes/MV-S-004_A_ORDEM_DO_DIA.html`: 618 linhas
- `site/sementes/MV-S-006_O_DESENHO_DO_REI.html`: 644 linhas
- `site/sementes/MV-S-008_O_PAR_PERFEITO.html`: 662 linhas

Comparativo da mesma camada de conteudo:

- `curriculo/01_SEMENTESV6/002_PEDRAS_FORTALEZA.yaml`: 270 linhas
- `curriculo/01_SEMENTESV6/004_A_ORDEM_DO_DIA.yaml`: 208 linhas
- `curriculo/01_SEMENTESV6/006_O_DESENHO_DO_REI.yaml`: 208 linhas
- `curriculo/01_SEMENTESV6/008_O_PAR_PERFEITO.yaml`: 257 linhas

Piloto atomico atual:

- `content/lessons/MV-S-000/sayings.pt-BR.json`: 26 linhas
- `content/lessons/MV-S-001/sayings.pt-BR.json`: 28 linhas
- `content/lessons/MV-S-022/sayings.pt-BR.json`: 26 linhas

Leitura operacional:

- o problema nao e apenas gerar HTML
- o problema e que a unidade real de revisao hoje ainda e o HTML da licao inteira
- qualquer proposta futura precisa partir desse fato, e nao fingir que o time ja revisa em outra camada

## 3) Hipoteses em disputa

### Hipotese A
Continuar com o HTML como superficie principal de revisao, mas melhorar o processo e os artefatos de apoio por cima.

### Hipotese B
Manter o HTML como artefato principal no curto prazo, mas introduzir contrato por blocos menores como camada de apoio e preparacao de migracao.

### Hipotese C
Migrar a fonte de verdade para pastas por licao com arquivos atomicos, aproximando o piloto `apps/web`.

## 4) Criterios de decisao

Uma boa estrutura inicial precisa:

- reduzir carga mental da revisao
- preservar sequencia pedagogica entre licoes
- manter compatibilidade com Vercel no curto prazo
- evitar banco local/stateful no runtime desta fase
- permitir crescimento para mais 105 licoes sem explodir contexto
- produzir evidencias claras de qualidade
- continuar pequena o bastante para o time sustentar

## 5) Definition of Done desta fase

Esta fase estara boa quando:

- houver uma leitura clara da dor atual
- as hipoteses iniciais estiverem explicitadas
- os experts tiverem papeis distintos
- a recomendacao preliminar estiver registrada
- a proxima conversa estiver bem enquadrada

## 6) Nao-objetivos explicitos

Para evitar overengineering, esta fase NAO vai:

- alterar `bmad/`
- alterar `apps/web/`
- alterar `build/`
- criar banco, API ou editor novo
- decidir toda a arquitetura do projeto 0-18
- criar sistema completo de workflows

## 7) Sinais de fracasso desta fase

Esta fase falha se:

- os experts ficarem redundantes
- a proposta exigir backend para resolver dor editorial
- a discussao tentar fechar stack completa cedo demais
- a unidade revisavel continuar grande demais para reduzir contexto
- a nova estrutura ficar mais dificil de explicar do que a dor atual

## 8) Defaults travados

- escopo inicial: mini nucleo
- foco inicial: revisao escalavel
- relacao com BMAD atual: satelite
- outside voice: 1 externo
- infra inicial recomendada: Vercel-first
- unidade-alvo de debate: blocos menores que a licao inteira

## 9) Pergunta operacional da proxima rodada

Qual e a menor unidade de bloco que continua pedagogicamente inteligivel e operacionalmente revisavel?

## 10) Protocolo obrigatorio de embasamento

Toda rodada futura deve obedecer:

- abrir com uma pergunta explicita
- listar evidencias reais do repo em uma secao `Evidencias usadas`
- usar tags simples como `E1`, `E2`, `E3`
- fazer cada expert citar ao menos uma evidencia ou uma rodada anterior
- separar fato observado de inferencia
- declarar a decisao final como `provisoria`, nunca como definitiva cedo demais

Regra de ouro:

Argumento sem evidencia rastreavel e apenas intuicao. Pode aparecer, mas deve ser tratado como hipotese fraca.

## 11) Template minimo de rodada

Cada rodada deve conter, nesta ordem:

1. pergunta da rodada
2. evidencias usadas
3. posicao inicial dos experts
4. tensoes reais
5. consensos provisorios
6. decisao provisoria
7. perguntas em aberto

## 12) Entregaveis desta pasta

- 1 orchestrator local
- 5 experts YAML
- 2 rodadas de discussao
- 1 sintese curta com hipoteses iniciais
