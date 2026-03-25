# TASK ROBUSTA - EXECUCAO FASEADA DO PRODUTO PUBLICADO E SUPERFICIES DE SEMENTES

Data: 2026-03-25
Status: task-mae oficial da trilha
Escopo: somente `MelhorarEstrutura`
Modo: execucao faseada com checkpoints de evidencia

## 1) Missao desta task

Esta task existe para executar, de ponta a ponta, a trilha de melhoria do produto publicado de `Sementes` sem misturar backlog, contrato, superficie e piloto.

A meta e sair de uma conversa boa para um fluxo operativo que:

1. mapeia o estado real;
2. fecha o contrato da superficie publica;
3. melhora a entrada de `Sementes`;
4. ajusta a leitura da licao;
5. explicita arcos e progressao;
6. testa um piloto minimo;
7. consolida uma decisao final defensavel.

## 2) Verdade operacional de partida

Esta task assume explicitamente:

1. a revisao real ainda acontece no HTML;
2. `MelhorarEstrutura` continua sendo laboratorio, nao a arquitetura oficial;
3. o backstage editorial ja esta mais inteligente que o front publico;
4. o produto publicado ainda vaza linguagem interna em varios pontos;
5. o ajuste precisa melhorar a vida da mae real sem exigir stack nova;
6. nada aqui deve depender de backend stateful, editor novo ou troca de runtime.

## 3) Relacao com os demais documentos

### Base de estado

1. `README.md`
2. `AI_CONTEXT.md`
3. `MelhorarEstrutura/README.md`
4. `MelhorarEstrutura/ENTENDA_MELHORAR_ESTRUTURA.md`

### Base de convergencia

1. `MelhorarEstrutura/TASK_ROBUSTA_CONVERGENCIA_SUGESTAO_SEMENTES.md`
2. `MelhorarEstrutura/discussoes/2026-03-20_1440_PRODUTO_PUBLICADO_SEMENTES.md`
3. `MelhorarEstrutura/TASK_ROBUSTA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`

### Evidencia tecnica e de produto

1. `docs/MAPA_EXECUCAO_PROJETO.md`
2. `site/manual-portador.html`
3. `site/sementes/*.html`
4. `site/sementes/style.css`
5. `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml`
6. `curriculo/01_SEMENTESV6/*.yaml`

## 4) Principios inegociaveis

### 4.1 Familia no centro

Se a mudanca melhora o sistema e piora a vida da mae real, ela reprova.

### 4.2 Clareza antes de engenhosidade

Se a mudanca e elegante no papel, mas confusa em casa, ela reprova.

### 4.3 Backstage nao vaza para a frente

O front publico precisa falar a lingua da familia, nao a lingua da operacao interna.

### 4.4 HTML continua sendo a realidade

O HTML ainda e a superficie operacional real. Esta task nao finge o contrario.

### 4.5 Progresso sem culpa

Progressao por arcos precisa aliviar, nao pressionar.

### 4.6 Pequena mudanca, grande leitura

O piloto precisa ser pequeno o bastante para caber, mas forte o bastante para ensinar.

## 5) Mapa das fases

| Fase | Objetivo | Entrada principal | Saida obrigatoria |
|---|---|---|---|
| 0 | Reentrada e inventario | contexto vivo + superficie atual | mapa de superficies e vazamentos |
| 1 | Contrato da superficie publica | evidencias + discussoes + produto atual | contrato curto da face publica |
| 2 | Entrada de `Sementes` | contrato + homepage atual | entrada clara e familiar |
| 3 | Superficie da licao | HTML, CSS e orientacao do Portador | licao mais legivel e conducivel |
| 4 | Arcos e progressao | leitura de jornada + produto atual | progressao visivel sem culpa |
| 5 | Piloto minimo | fase 0-4 fechadas | recorte pequeno com antes/depois |
| 6 | Consolidacao e decisao | piloto + feedback + rubrica | recomendacao final e backlog |

## 6) Regra de execucao

1. nao avancar de fase com `BLOCK` duro aberto;
2. registrar a saida de cada fase antes de abrir a seguinte;
3. se uma fase expor nova ambiguidade estrutural, voltar uma fase e corrigir o contrato;
4. nao abrir discussao de piloto antes de fechar contrato e superficie;
5. nao transformar o piloto em nova arquitetura.

## 7) Fase 0 - Reentrada e inventario

### Objetivo

1. confirmar o estado real do produto publicado;
2. identificar onde a linguagem interna aparece;
3. registrar o que esta dentro e fora de escopo;
4. travar a definicao de sucesso da rodada.

### Passos

1. abrir `AI_CONTEXT.md`;
2. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`;
3. abrir `MelhorarEstrutura/discussoes/2026-03-20_1440_PRODUTO_PUBLICADO_SEMENTES.md`;
4. mapear as superficies publicas afetadas;
5. mapear os vazamentos de linguagem interna;
6. mapear os pontos de possivel mudanca de HTML e CSS;
7. congelar o que nao sera mexido nesta rodada.

### Checkpoints de evidencia

1. onde o site ainda parece painel interno;
2. onde o Portador precisa traduzir mentalmente;
3. onde o ritmo da licao esta presumido, nao explicado;
4. onde os arcos ainda nao aparecem para a familia.

### Saida esperada

- inventario curto das superficies;
- lista de vazamentos;
- criterio de sucesso do piloto;
- delimitacao de escopo.

### Stop condition

Se o inventario nao estiver claro, nao passar para a Fase 1.

### Registro de execucao da Fase 0

Checkpoint executado em `2026-03-25`.

Artefato gerado:

- `MelhorarEstrutura/discussoes/2026-03-25_1631_FASE_0_INVENTARIO_SUPERFICIES.md`

Superficies confirmadas como foco principal:

1. `site/index.html`
2. `site/manual-portador.html`
3. `site/sementes/*.html`
4. `site/sementes/style.css`

Superficies de apoio e laboratorio:

1. `site/landingpage.html`
2. `site/landing_v3_journey.html`
3. `site/sementes/lab_icones.html`
4. `site/public/sementes_teste/*.html`
5. `site/sementes/templates/*.j2`

Vazamentos identificados na face publica:

1. `Orchestrator Dashboard`
2. `Ambiente: Production (Forge V3)`
3. `Sistema`
4. `Configuracoes`
5. `Voltar para o dashboard`

Leitura operacional:

- a home principal ainda parece painel interno;
- o manual esta mais familiar, mas ainda carrega residuos;
- o ciclo `Sementes` e o CSS ja sao o nucleo da experiencia publica;
- as superficies experimentais continuam fora da rota principal.

## 8) Fase 1 - Contrato da superficie publica

### Objetivo

1. decidir o que a familia precisa entender em menos de um minuto;
2. definir a mensagem de entrada de `Sementes`;
3. explicitar o acordo de ritmo;
4. separar leitura, fala e acao.

### Passos

1. definir a promessa curta da entrada;
2. definir o que o adulto precisa ver primeiro;
3. definir o que deve ficar escondido na operacao interna;
4. estabelecer termos visiveis permitidos;
5. estabelecer termos proibidos na face publica;
6. travar uma formula simples de entrada.

### Checkpoints de evidencia

1. a promessa cabe em leitura rapida;
2. o adulto entende o que fazer sem esforco;
3. a linguagem interna foi removida do front;
4. o contrato nao vira texto professoral.

### Saida esperada

- contrato resumido da superficie publica;
- lista de termos permitidos e proibidos;
- copia base de entrada.

### Stop condition

Se a entrada ainda parecer painel, nao passar para a Fase 2.

### Registro de execucao da Fase 1

Checkpoint executado em `2026-03-25 16:33`.

Artefato gerado:

- `MelhorarEstrutura/discussoes/2026-03-25_1633_FASE_1_CONTRATO_SUPERFICIE_PUBLICA.md`

Contrato provisorio fechado em discussao:

1. a superficie publica fala com a familia, nao com a operacao interna;
2. a primeira dobra precisa explicar o que e Sementes sem traducao mental;
3. o ritmo da licao precisa aparecer logo de inicio;
4. leitura, fala e acao precisam ficar visiveis;
5. termos internos como `Dashboard`, `Sistema`, `Configuracoes` e `Production` ficam fora da face publica;
6. `Portador`, `Licao`, `Ritual`, `Jornada` e `Sementes` podem aparecer se ajudarem a orientar;
7. a progressao deve aliviar, nao pressionar.

## 9) Fase 2 - Entrada de `Sementes`

### Objetivo

1. deixar claro que a pagina e para uma familia;
2. explicar o ritmo da licao sem peso;
3. deixar evidente o beneficio imediato;
4. reduzir ansiedade na primeira leitura.

### Passos

1. revisar a primeira dobra da experiencia;
2. revisar o bloco de explicacao de ritmo;
3. revisar chamadas para licao ou trilha;
4. revisar linguagem de alivio para o Portador;
5. revisar se a entrada parece guia, nao dashboard;
6. revisar se a primeira leitura cria paz e orientacao.

### Checkpoints de evidencia

1. o ritmo da licao ficou explicito;
2. o beneficio imediato ficou visivel;
3. a entrada nao sobrecarrega a mae;
4. o site parece mais familiar do que interno.

### Saida esperada

- entrada de `Sementes` mais familiar;
- ritmo mais claro;
- menos cara de dashboard interno.

### Stop condition

Se a entrada ainda exigir traducao mental, nao passar para a Fase 3.

### Registro de execucao da Fase 2

Checkpoint executado em `2026-03-25 16:35`.

Artefato gerado:

- `MelhorarEstrutura/discussoes/2026-03-25_1635_FASE_2_ENTRADA_SEMENTES.md`

Entrada provisoria desenhada em discussao:

1. a entrada precisa dizer rapido que a pagina e para a familia;
2. o ritmo da licao precisa aparecer logo na primeira leitura;
3. a entrada precisa parecer guia, nao dashboard;
4. a mae deve sentir alivio antes de sentir volume;
5. o beneficio imediato precisa ficar visivel sem jargao.

## 10) Fase 3 - Superficie da licao

### Objetivo

1. deixar claro o que se le;
2. deixar claro o que se fala;
3. deixar claro o que a crianca faz;
4. tornar o uso mais calmo e usavel no celular.

### Passos

1. revisar hierarquia visual;
2. revisar labels do tipo "leia", "fale", "faca";
3. revisar blocos de orientacao do Portador;
4. revisar prompts de acao imediata;
5. revisar se a licao continua reconhecivel como `Matematica Viva`;
6. revisar `site/sementes/style.css` quando a hierarquia visual depender de CSS;
7. revisar se o front ainda respira bem em mobile.

### Checkpoints de evidencia

1. o adulto enxerga a funcao de cada bloco sem pensar demais;
2. a oralidade esta visivel;
3. a acao esta visivel;
4. o texto nao colapsa em densidade;
5. o CSS ajuda, nao esconde.

### Saida esperada

- licao com instrucoes mais legiveis;
- menos traducao mental;
- melhor separacao entre texto de conducao e texto de historia.

### Stop condition

Se a licao perder calor ou virar texto seco, nao passar para a Fase 4.

### Registro de execucao da Fase 3

Checkpoint executado em `2026-03-25 16:37`.

Artefato gerado:

- `MelhorarEstrutura/discussoes/2026-03-25_1637_FASE_3_SUPERFICIE_DA_LICAO.md`

Superficie da licao desenhada em discussao:

1. a licao precisa deixar claro o que se le, o que se fala e o que se faz;
2. o Portador precisa bater o olho e entender a funcao de cada bloco;
3. o CSS nao e detalhe tecnico, e parte da experiencia publica;
4. a pagina precisa respirar bem no celular;
5. a historia nao pode engolir a orientacao.

## 11) Fase 4 - Arcos e progressao

### Objetivo

1. mostrar progresso sem pressao;
2. explicar onde a familia esta na jornada;
3. reforcar continuidade sem culpa;
4. tornar a progressao um convite, nao uma cobranca.

### Passos

1. definir quais arcos aparecem na superficie publica;
2. definir como eles sao nomeados;
3. definir como o avanco aparece visualmente;
4. definir o que nao deve ser mostrado para nao virar ansiedade;
5. revisar se o arco ajuda ou distrai;
6. validar se a progressao conversa com o Portador e nao apenas com o sistema.

### Checkpoints de evidencia

1. a familia entende onde esta;
2. a familia entende para onde vai;
3. o progresso nao parece corrida;
4. os arcos ajudam a orientar sem culpar.

### Saida esperada

- mapa simples de arcos;
- linguagem de progresso mais calma;
- leitura de jornada mais clara.

### Stop condition

Se a progressao parecer gamificacao ansiosa, nao passar para a Fase 5.

### Registro de execucao da Fase 4

Checkpoint executado em `2026-03-25 16:38`.

Artefato gerado:

- `MelhorarEstrutura/discussoes/2026-03-25_1638_FASE_4_ARCOS_E_PROGRESSAO.md`

Progressao desenhada em discussao:

1. progressao precisa orientar, nao culpar;
2. a familia precisa entender onde esta e para onde vai;
3. os arcos devem aliviar o caminho, nao virar gamificacao ansiosa;
4. o progresso precisa ser legivel, mas discreto;
5. o Portador nao deve sentir que esta sendo medido.

## 12) Fase 5 - Piloto minimo

### Objetivo

1. aplicar a ideia em um recorte pequeno;
2. confirmar se a melhoria faz sentido na pratica;
3. evitar overengineering;
4. criar referencia concreta para decidir a proxima rodada.

### Passos

1. escolher uma licao ou uma pequena superficie comparavel;
2. aplicar as mudancas definidas nas fases 0-4;
3. registrar antes e depois;
4. medir se o adulto entende mais rapido;
5. medir se o front parece menos interno;
6. medir se a familia percebe a jornada com mais clareza.

### Criterios para o piloto

1. precisa mostrar a diferenca entre backstage e superficie publica;
2. precisa caber em uma observacao curta de qualidade;
3. precisa ser comparavel com o estado anterior;
4. precisa caber na realidade atual do projeto;
5. precisa ser pequeno o bastante para terminar.

### Saida esperada

- piloto escolhido;
- antes e depois bem definido;
- veredito curto sobre utilidade.

### Stop condition

Se o piloto crescer demais, reduzir escopo antes de seguir.

### Registro de execucao da Fase 5

Checkpoint executado em `2026-03-25 16:40`.

Artefato gerado:

- `MelhorarEstrutura/discussoes/2026-03-25_1640_FASE_5_PILOTO_MINIMO.md`

Piloto minimo escolhido em discussao:

1. a licao piloto e `site/sementes/MV-S-005_O_ESCONDERIJO_DA_GLORIA.html`;
2. o recorte e pequeno, real e comparavel;
3. a licao esta no miolo da trilha publicada e conversa com as vizinhas;
4. o piloto precisa mostrar antes/depois sem reescrever o projeto inteiro;
5. o objetivo e provar utilidade, nao maximizacao.

## 13) Fase 6 - Consolidacao e decisao

### Objetivo

1. registrar o que entrou para valer;
2. registrar o que foi recusado;
3. registrar o que fica para depois;
4. decidir se a proposta merece ampliar escopo.

### Passos

1. consolidar achados;
2. comparar com o `North Star`;
3. comparar com o uso real da mae;
4. comparar com o custo operacional;
5. definir proximo tema ou encerramento;
6. produzir a recomendacao final da trilha.

### Checkpoints de evidencia

1. o produto ficou mais familiar;
2. a revisao ficou mais simples de explicar;
3. o piloto provou utilidade;
4. os riscos remanescentes ficaram claros.

### Saida esperada

- recomendacao final;
- backlog enxuto;
- proxima decisao claramente nomeada.

### Registro de execucao da Fase 6

Checkpoint executado em `2026-03-25 16:39`.

Artefato gerado:

- `MelhorarEstrutura/discussoes/2026-03-25_1639_FASE_6_CONSOLIDACAO_E_DECISAO.md`

Decisao provisoria fechada em discussao:

1. o contrato curto da superficie publica entra como criterio;
2. o front continua falando com a familia;
3. a entrada de `Sementes` precisa mostrar ritmo;
4. a licao precisa separar leitura, fala e acao;
5. a progressao fica como orientacao calma;
6. `MV-S-005_O_ESCONDERIJO_DA_GLORIA.html` fica como piloto minimo comparavel;
7. a ampliacao de escopo so deve acontecer depois de validacao humana clara.

## 14) Ordem operacional minima

Se a execucao for feita de forma enxuta, seguir esta ordem:

1. Fase 0 - reentrada e inventario
2. Fase 1 - contrato da superficie publica
3. Fase 2 - entrada de `Sementes`
4. Fase 3 - superficie da licao
5. Fase 4 - arcos e progressao
6. Fase 5 - piloto minimo
7. Fase 6 - consolidacao e decisao

## 15) Riscos e anti-padroes

### Riscos

1. a superficie ficar limpa demais e perder calor;
2. a progressao virar gincana ou culpa;
3. o piloto crescer demais;
4. o backstage voltar a vazar para o front;
5. a fase entrar em implementacao antes de fechar o contrato visual.

### Anti-padroes

1. tratar stack como assunto principal;
2. propor backend como reflexo automatico;
3. multiplicar arquivos sem ganho comprovado;
4. misturar linguagem interna com linguagem familiar;
5. chamar de simples algo que a mae real nao conseguiria sustentar;
6. usar `North Star` como slogan e nao como gate;
7. deixar a IA assumir o juizo final de `TASTE`.

## 16) Definition of Done

Esta task so termina quando conseguirmos responder, sem ambiguidade grande:

1. qual e o contrato da superficie publica;
2. qual e o estado da entrada de `Sementes`;
3. como a licao mostra leitura, fala e acao;
4. como os arcos aparecem sem pressao;
5. qual e o menor piloto para provar a proposta;
6. por que a sugestao vence as alternativas.

## 17) Formula de fechamento esperada

Se a task estiver madura no final, a leitura final deve soar assim:

`Para Sementes, recomendamos manter a revisao no HTML no curto prazo, congelar um contrato canonico de superficie publica, limpar a entrada do ciclo, explicitar leitura-fala-acao, mostrar arcos de modo calmo e executar um piloto minimo antes de ampliar o escopo.`

Se ainda nao for possivel dizer isso com clareza, ainda nao convergimos o suficiente.

## 18) Registro de aplicacao do piloto

Em `2026-03-25 16:41`, o piloto minimo foi aplicado em superficie real:

1. arquivo alvo: `site/sementes/MV-S-005_O_ESCONDERIJO_DA_GLORIA.html`;
2. mudanca aplicada: o retorno do arquivo deixou de falar em `Dashboard`;
3. texto novo: `Voltar para a trilha de Sementes`;
4. `aria-label` alinhado ao mesmo texto;
5. objetivo: validar passagem do contrato para a superficie real sem ampliar escopo.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1641_PILOTO_MINIMO_APLICADO_MV_S_005.md`

## 19) Registro de aplicacao secundaria no manual

Em `2026-03-25 16:43`, um ajuste complementar foi aplicado no manual do Portador:

1. arquivo alvo: `site/manual-portador.html`;
2. `Sistema` foi trocado por `Apoio de leitura`;
3. `Configuracoes` foi trocado por `Ajustes de leitura`;
4. `Voltar para o dashboard` foi trocado por `Voltar para a entrada`;
5. objetivo: reduzir linguagem interna sem mexer na estrutura maior.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1643_APLICACAO_MANUAL_PORTADOR.md`

## 20) Registro de aplicacao na home principal

Em `2026-03-25 16:45`, a home principal recebeu um ajuste de primeira dobra:

1. arquivo alvo: `site/index.html`;
2. `Orchestrator Dashboard` deixou de aparecer na identidade principal;
3. o topo passou a se apresentar como `Entrada de Sementes`;
4. a abertura agora convida a familia com clareza, ritmo e apoio;
5. o rodape foi simplificado para remover a fala de `Forge V3`.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1645_APLICACAO_HOME_PRINCIPAL.md`

## 21) Registro de aplicacao na licao vizinha ao piloto

Em `2026-03-25 16:46`, a licao `MV-S-004_A_ORDEM_DO_DIA.html` recebeu o mesmo criterio de entrada:

1. arquivo alvo: `site/sementes/MV-S-004_A_ORDEM_DO_DIA.html`;
2. o botao de retorno passou a falar em `Voltar para a trilha de Sementes`;
3. o `aria-label` foi alinhado ao mesmo texto;
4. o objetivo foi remover a fala de dashboard de uma licao vizinha ao piloto;
5. a continuidade da trilha ficou mais coerente.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1646_APLICACAO_MV_S_004.md`

## 22) Registro de aplicacao na licao 006

Em `2026-03-25 16:47`, a licao `MV-S-006_O_DESENHO_DO_REI.html` recebeu o mesmo criterio de entrada:

1. arquivo alvo: `site/sementes/MV-S-006_O_DESENHO_DO_REI.html`;
2. o botao de retorno passou a falar em `Voltar para a trilha de Sementes`;
3. o `aria-label` foi alinhado ao mesmo texto;
4. o objetivo foi manter a sequencia publicada coerente;
5. a leitura da trilha ficou mais uniforme.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1647_APLICACAO_MV_S_006.md`

## 23) Registro de aplicacao nas licoes 007 e 008

Em `2026-03-25 16:48`, as licoes `MV-S-007_A_COROA_DA_SEMANA.html` e `MV-S-008_O_PAR_PERFEITO.html` receberam o mesmo criterio de entrada:

1. arquivo alvo 1: `site/sementes/MV-S-007_A_COROA_DA_SEMANA.html`;
2. arquivo alvo 2: `site/sementes/MV-S-008_O_PAR_PERFEITO.html`;
3. ambas deixaram de falar em `Dashboard` no botao de retorno;
4. o texto novo passou a ser `Voltar para a trilha de Sementes`;
5. o `aria-label` foi alinhado ao mesmo criterio;
6. o objetivo foi manter a trilha publicada coerente em uma faixa contigua.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1648_APLICACAO_MV_S_007_E_008.md`

## 24) Registro de aplicacao na licao 009

Em `2026-03-25 16:49`, a licao `MV-S-009_O_CELEIRO_DE_NOE.html` recebeu o mesmo criterio de entrada:

1. arquivo alvo: `site/sementes/MV-S-009_O_CELEIRO_DE_NOE.html`;
2. o botao de retorno passou a falar em `Voltar para a trilha de Sementes`;
3. o `aria-label` foi alinhado ao mesmo texto;
4. o objetivo foi fechar mais uma licao da mesma faixa com a mesma linguagem publica;
5. a leitura da trilha ficou mais uniforme.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1649_APLICACAO_MV_S_009.md`

## 25) Registro de aplicacao na licao 010

Em `2026-03-25 16:50`, a licao `MV-S-010_A_FILA_DA_PROVIDENCIA.html` recebeu o mesmo criterio de entrada:

1. arquivo alvo: `site/sementes/MV-S-010_A_FILA_DA_PROVIDENCIA.html`;
2. o botao de retorno passou a falar em `Voltar para a trilha de Sementes`;
3. o `aria-label` foi alinhado ao mesmo texto;
4. o objetivo foi fechar a sequencia imediata da faixa com a mesma linguagem publica;
5. a leitura da trilha ficou mais uniforme.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1650_APLICACAO_MV_S_010.md`

## 26) Registro de aplicacao nas licoes 011 e 012

Em `2026-03-25 16:51`, as licoes `MV-S-011_A_PLENITUDE_DAS_MAOS.html` e `MV-S-012_O_SEGREDO_DO_FEIXE.html` receberam o mesmo criterio de entrada:

1. arquivo alvo 1: `site/sementes/MV-S-011_A_PLENITUDE_DAS_MAOS.html`;
2. arquivo alvo 2: `site/sementes/MV-S-012_O_SEGREDO_DO_FEIXE.html`;
3. ambas deixaram de falar em `Dashboard` no botao de retorno;
4. o texto novo passou a ser `Voltar para a trilha de Sementes`;
5. o `aria-label` foi alinhado ao mesmo criterio;
6. o objetivo foi manter a trilha publicada coerente em outra faixa contigua.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1651_APLICACAO_MV_S_011_E_012.md`

## 27) Registro de aplicacao nas licoes 013 e 014

Em `2026-03-25 16:52`, as licoes `MV-S-013_O_RIO_QUE_SE_UNE.html` e `MV-S-014_O_CELEIRO_QUE_CRESCE.html` receberam o mesmo criterio de entrada:

1. arquivo alvo 1: `site/sementes/MV-S-013_O_RIO_QUE_SE_UNE.html`;
2. arquivo alvo 2: `site/sementes/MV-S-014_O_CELEIRO_QUE_CRESCE.html`;
3. ambas deixaram de falar em `Dashboard` no botao de retorno;
4. o texto novo passou a ser `Voltar para a trilha de Sementes`;
5. o `aria-label` foi alinhado ao mesmo criterio;
6. o objetivo foi manter a trilha publicada coerente em outra faixa contigua.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1652_APLICACAO_MV_S_013_E_014.md`

## 28) Registro de aplicacao na licao 015

Em `2026-03-25 16:53`, a licao `MV-S-015_A_ESCADA_DE_LUZ.html` recebeu o mesmo criterio de entrada:

1. arquivo alvo: `site/sementes/MV-S-015_A_ESCADA_DE_LUZ.html`;
2. o botao de retorno passou a falar em `Voltar para a trilha de Sementes`;
3. o `aria-label` foi alinhado ao mesmo texto;
4. o objetivo foi manter a trilha publicada coerente na faixa atual;
5. a leitura da trilha ficou mais uniforme.

Artefato de registro:

- `MelhorarEstrutura/discussoes/2026-03-25_1653_APLICACAO_MV_S_015.md`

## 29) Limite de faixa publicado versus construcao

Em `2026-03-25`, a leitura do bloco seguinte mostrou que:

1. `MV-S-016_O_BANDO_QUE_CRESCE.html` ja e uma superficie de construcao;
2. `MV-S-017_O_HORIZONTE_ALEM.html` e `MV-S-018_O_VAZIO_E_A_PLENITUDE.html` estao marcadas como fora da trilha publicada;
3. `MV-S-019_O_RISCO_NA_ROCHA.html` e `MV-S-020_O_SELO_REAL.html` seguem a mesma natureza de superficie de apoio;
4. por isso, esta rodada para na faixa publicada `MV-S-007` ate `MV-S-015`;
5. qualquer limpeza seguinte em `MV-S-016+` deve ser tratada como outra frente, nao como continuidade da trilha publicada.


