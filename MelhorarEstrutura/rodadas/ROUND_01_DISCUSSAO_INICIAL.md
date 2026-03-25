# ROUND 01 - DISCUSSAO INICIAL

Data: 2026-03-19
Fase: posicoes iniciais
Status: decisao preliminar

## 1) Pergunta da rodada

Qual e o menor recorte de estrutura que reduz a dor agora sem criar um segundo sistema pesado demais?

## 2) Evidencias usadas

- `R0`: `ROUND_00_DIAGNOSTICO.md`
- `E1`: `docs/MAPA_EXECUCAO_PROJETO.md`
- `E2`: `build/fases/sementes.py`
- `E3`: `apps/web/lib/content/loader.ts`
- `E4`: `apps/web/lib/contracts/lesson-structure.ts`
- `E5`: `vercel.json`

## 3) Posicao inicial dos experts

### Estrategista de Estrutura

A revisao esta acontecendo direto no artefato final. O problema central nao e template, e sim fronteira ruim da unidade revisavel. Essa leitura nasce de `R0`, reforcada por `E1` e `E2`.

### Vercel First

Vercel continua sendo o default mais seguro para o curto prazo. Nada aqui justifica introduzir runtime stateful ou banco local para resolver um problema que e editorial e estrutural. Essa posicao se apoia em `E1` e `E5`.

### Contrato de Licao

Uma licao inteira ainda e grande demais. O proximo nivel natural de organizacao e contrato por blocos como `hero`, `preparacao_portador`, `ritual_entrada`, `jornada`, `concreto`, `narramos_juntos`, `fechamento` e QA. Essa leitura vem de `E4` e do diagnostico em `R0`.

### Revisao Escalavel

Hoje o HTML ainda e a camada principal de refinamento editorial. A pergunta correta nao e negar isso, e sim decidir se isso continua no curto prazo ou se deve virar apenas validacao mais adiante. Essa posicao combina `R0`, `E1` e `E2`.

### Mae Regente Real

Se a nova estrutura obrigar abrir arquivos demais para entender uma unica licao, ela piora o problema em vez de resolver. Essa tensao nasce de `R0`: sair do HTML gigante nao pode virar fragmentacao cega.

## 4) Tensoes reais

### Tensao 1 - Fragmentar ou nao fragmentar

- a favor: blocos menores reduzem contexto e permitem revisao localizada
- contra: fragmentacao excessiva pode quebrar a inteligibilidade da licao

### Tensao 2 - Vercel como restricao ou como guia

- leitura madura: Vercel nao define a pedagogia
- leitura pratica: Vercel ajuda a cortar solucoes desnecessariamente stateful nesta fase

### Tensao 3 - Continuar no YAML unico ou aproximar o piloto atomico

- manter YAML unico e mais barato no curtissimo prazo
- aproximar o piloto atomico parece mais promissor para escala de revisao

## 5) Consensos provisorios

- o problema principal e estrutural/editorial, nao de banco
- Vercel continua adequado para o curto prazo
- o HTML e hoje a principal unidade real de revisao
- a proxima conversa deve discutir fronteiras de bloco, nao stack completa

## 6) O que Vercel favorece

- build previsivel
- saida estatica
- Next com SSG/artefatos
- deploy simples conectado ao GitHub
- separacao entre conteudo e runtime

## 7) O que Vercel desincentiva nesta conversa

- depender de SQLite local no runtime
- resolver dor editorial com backend stateful
- misturar problema de revisao com problema de persistencia de usuario

## 8) Decisao provisoria

Recomendacao preliminar:

- manter Vercel como base inicial
- nao tocar no pipeline principal ainda
- usar esta pasta para amadurecer contrato por blocos menores que a licao inteira
- pensar em revisao por camadas:
  - camada 1: HTML como superficie operacional atual
  - camada 2: contrato e continuidade como apoio e clarificacao
  - camada 3: eventual transicao futura, se ela se provar melhor

Observacao importante:

Ainda nao decidimos se o formato final sera `1 YAML`, `varios arquivos por licao` ou outra variacao. A decisao desta rodada e anterior a isso: primeiro definir a fronteira conceitual do bloco.

## 9) Perguntas em aberto

- qual o tamanho ideal do bloco para nao perder fluidez pedagogica?
- o bloco `jornada` deve continuar unido ou virar sub-blocos por cena?
- qual informacao precisa ficar em `meta/lore` e qual precisa ficar no bloco de ensino?
- como representar continuidade entre licao anterior e proxima sem reintroduzir arquivos gigantes?
