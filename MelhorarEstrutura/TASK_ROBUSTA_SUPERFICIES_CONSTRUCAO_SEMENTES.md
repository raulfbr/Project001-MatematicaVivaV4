# TASK ROBUSTA - SUPERFICIES DE CONSTRUCAO DE SEMENTES

Data: 2026-03-25
Status: task-filha oficial da trilha
Escopo: somente `MelhorarEstrutura`
Modo: execucao faseada com fronteira explicita entre publicado e construcao

## 1) Missao desta task

Esta task existe para tratar as superficies de construcao de `Sementes` como uma frente separada da trilha publicada.

A meta e deixar claro, sem misturar natureza de trabalho, o que:

1. ja faz parte do produto publicado;
2. ainda esta em reconstrucao;
3. precisa falar com a familia;
4. precisa continuar fiel ao contrato da entrada;
5. nao deve fingir estar pronto antes da hora.

## 2) Verdade operacional de partida

Esta task assume explicitamente:

1. a trilha publicada vai ate `MV-S-015`;
2. `MV-S-016` e seguintes pertencem a superficies de construcao;
3. o bloco de construcao nao deve usar linguagem de dashboard;
4. a entrada precisa ser familiar, nao interna;
5. o topo da pagina deve oferecer retorno claro para a entrada;
6. o objetivo nao e publicar mais conteudo agora, e sim limpar a experiencia de reconstrucao.

## 3) Relacao com os demais documentos

### Base de estado

1. `README.md`
2. `AI_CONTEXT.md`
3. `MelhorarEstrutura/README.md`
4. `MelhorarEstrutura/ENTENDA_MELHORAR_ESTRUTURA.md`

### Base de trilha publicada

1. `MelhorarEstrutura/TASK_ROBUSTA_EXECUCAO_FASEADA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`
2. `MelhorarEstrutura/discussoes/2026-03-25_1653_APLICACAO_MV_S_015.md`

### Base de superficies de construcao

1. `site/sementes/MV-S-016_O_BANDO_QUE_CRESCE.html`
2. `site/sementes/MV-S-017_O_HORIZONTE_ALEM.html`
3. `site/sementes/MV-S-018_O_VAZIO_E_A_PLENITUDE.html`
4. `site/sementes/MV-S-019_O_RISCO_NA_ROCHA.html`
5. `site/sementes/MV-S-020_O_SELO_REAL.html`

## 4) Principios inegociaveis

### 4.1 Fronteira limpa

Construcao nao e publicado. Publicado nao e construcao.

### 4.2 Entrada acima de tudo

Mesmo em reconstrucao, a entrada precisa ser clara e familiar.

### 4.3 Nada de painel interno

Nao deve sobrar linguagem de dashboard, sistema ou operacao interna na superficie de construcao.

### 4.4 Pequeno e rastreavel

Mudancas devem ser pequenas o bastante para serem comparadas e revertidas com facilidade.

### 4.5 Nao reescrever o que ainda nao esta pronto

Esta task nao vai ampliar o conteudo das licoes de construcao; vai apenas limpar o acesso e a leitura da fronteira.

## 5) Mapa das fases

| Fase | Objetivo | Entrada principal | Saida obrigatoria |
|---|---|---|---|
| 0 | Inventario e fronteira | paginas de construcao + trilha publicada | mapa claro de superficies |
| 1 | Contrato da entrada de construcao | evidencia + leitura atual | contrato curto da entrada |
| 2 | Limpeza do topo | HTML das paginas 016-020 | entrada consistente e sem dashboard |
| 3 | Navegacao interna da faixa | links internos da faixa 016-020 | navegacao coerente |
| 4 | Consolidacao e decisao | superficie limpa + leitura humana | veredito curto e proximo passo |
| 5 | Encerramento da frente | fase 0-4 fechadas | orientacao final para retomada |

## 6) Regra de execucao

1. nao misturar esta frente com a trilha publicada;
2. nao reabrir a faixa 007-015 nesta task;
3. registrar cada ajuste antes de seguir para o proximo;
4. se uma pagina de construcao pedir reescrita grande, parar e tratar em outra decisao;
5. nao deixar topo ou navegacao falando como dashboard.

## 7) Fase 0 - Inventario e fronteira

### Objetivo

1. identificar as paginas de construcao;
2. separar o que ainda e publicado do que nao e;
3. mapear os vazamentos de linguagem interna;
4. decidir o minimo de limpeza que esta rodada precisa entregar.

### Passos

1. abrir `TASK_ROBUSTA_EXECUCAO_FASEADA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`;
2. abrir `site/sementes/MV-S-016_O_BANDO_QUE_CRESCE.html`;
3. abrir `site/sementes/MV-S-017_O_HORIZONTE_ALEM.html`;
4. abrir `site/sementes/MV-S-018_O_VAZIO_E_A_PLENITUDE.html`;
5. abrir `site/sementes/MV-S-019_O_RISCO_NA_ROCHA.html`;
6. abrir `site/sementes/MV-S-020_O_SELO_REAL.html`;
7. mapear rotulos de topo, retorno e apoio;
8. congelar tudo que nao for fronteira de entrada.

### Saida esperada

- lista curta de paginas de construcao;
- lista de vazamentos;
- criterio de entrada da frente;
- delimitacao clara da faixa.

### Registro de execucao da Fase 0

Checkpoint executado em `2026-03-25`.

Artefato gerado:

- `MelhorarEstrutura/discussoes/2026-03-25_1654_FASE_0_INVENTARIO_SUPERFICIES_CONSTRUCAO.md`

Leitura operacional:

- `MV-S-016` e o ponto de entrada da reconstrucao;
- `MV-S-017` a `MV-S-020` sao superfices de apoio fora da trilha publicada;
- o topo ainda precisa falar como entrada, nao como dashboard;
- a faixa de construcao pode conviver com a trilha publicada sem se confundir com ela.

## 8) Definition of Done

Esta task so termina quando a superficie de construcao:

1. nao usar mais linguagem de dashboard no topo;
2. apresentar o retorno como entrada, nao como painel interno;
3. manter a fronteira com a trilha publicada visivel;
4. tiver sua navegacao interna legivel sem parecer produto pronto;
5. estiver documentada com clareza suficiente para retomada.

## 9) Registro de aplicacao da Fase 1

Em `2026-03-25 16:55`, a entrada da superficie de construcao foi ajustada em superficie real:

1. `MV-S-016_O_BANDO_QUE_CRESCE.html` passou a falar `Voltar para a entrada` no topo e na navegacao de apoio;
2. `MV-S-017_O_HORIZONTE_ALEM.html` passou a falar `Voltar para a entrada` no topo;
3. `MV-S-018_O_VAZIO_E_A_PLENITUDE.html` passou a falar `Voltar para a entrada` no topo;
4. `MV-S-019_O_RISCO_NA_ROCHA.html` passou a falar `Voltar para a entrada` no topo;
5. `MV-S-020_O_SELO_REAL.html` passou a falar `Voltar para a entrada` no topo;
6. o objetivo foi remover linguagem de dashboard da faixa de construcao sem reescrever o conteudo.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1655_APLICACAO_SUPERFICIES_CONSTRUCAO_ENTRADA.md`

## 10) Registro de aplicacao da Fase 2 e 3

Em `2026-03-25 16:56`, a navegacao interna da faixa de construcao foi ajustada em superficie real:

1. `MV-S-016_O_BANDO_QUE_CRESCE.html` passou a falar `Voltar para a entrada` no bloco de navegacao de apoio e `Entrada` no nav final;
2. `MV-S-017_O_HORIZONTE_ALEM.html` passou a falar `Continuar na reconstrucao` e `Voltar para a entrada`;
3. `MV-S-018_O_VAZIO_E_A_PLENITUDE.html` passou a falar `Continuar na reconstrucao` e `Voltar para a entrada`;
4. `MV-S-019_O_RISCO_NA_ROCHA.html` passou a falar `Continuar na reconstrucao` e `Voltar para a entrada`;
5. `MV-S-020_O_SELO_REAL.html` passou a falar `Continuar na reconstrucao` e `Voltar para a entrada`;
6. o objetivo foi deixar a navegacao da frente de construcao legivel, sem falar como dashboard ou mapa interno.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1656_FASE_2_E_3_NAVEGACAO_INTERNA_CONSTRUCAO.md`

## 11) Registro de aplicacao da Fase 4

Em `2026-03-25 16:57`, a acao principal da superficie de construcao 016 foi refinada:

1. `MV-S-016_O_BANDO_QUE_CRESCE.html` deixou de falar `Voltar para a Licao 015`;
2. a copia passou a ser `Voltar para a faixa publicada`;
3. o objetivo foi deixar mais claro que o retorno aponta para a trilha publicada como conjunto, nao para uma licao isolada;
4. isso reforca a fronteira entre reconstrucao e produto publicado.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1657_FASE_4_MICROCOPY_ACAO_PRINCIPAL_CONSTRUCAO.md`

## 12) Consolidacao e decisao

Leitura final desta frente em `2026-03-25`:

1. a faixa de construcao `MV-S-016` ate `MV-S-020` ficou com entrada clara e uniforme;
2. a linguagem de dashboard saiu do topo e da navegacao de apoio;
3. a fronteira com a trilha publicada ficou explicitamente separada;
4. `MV-S-016` agora fala como ponto de reconstrucao, nao como painel;
5. a frente ja esta pronta para pausa ate surgir uma nova necessidade concreta.

Decisao:

- encerrar a rodada atual nesta task-filha;
- manter a frente de construcao documentada e separada;
- retomar apenas se houver nova necessidade de microcopy, navegacao ou fronteira.
