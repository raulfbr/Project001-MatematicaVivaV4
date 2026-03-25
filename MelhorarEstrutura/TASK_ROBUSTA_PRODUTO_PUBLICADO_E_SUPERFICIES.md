# TASK ROBUSTA - PRODUTO PUBLICADO E SUPERFICIES DE SEMENTES

Data: 2026-03-20
Status: subtask de superficies, apoiada pela task-mae de execucao faseada
Escopo: somente `MelhorarEstrutura`
Modo: planejamento operacional com aplicacao fase a fase

## 1) Missao desta task

Esta task agora funciona como apoio detalhado da task-mae
`TASK_ROBUSTA_EXECUCAO_FASEADA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`.

Transformar a leitura sobre `produto publicado` em um plano aplicavel, pequeno e progressivo para `Sementes`.

Esta task existe para responder, com criterio pratico, a pergunta:

qual e o menor conjunto de mudancas nas superficies publicadas que faz `Sementes` parecer mais familia, mais claro e mais fiel ao `North Star`, sem trocar a stack cedo demais?

## 2) Verdade operacional de partida

Esta task assume explicitamente:

1. a revisao real ainda acontece no HTML;
2. o experimento `MelhorarEstrutura` ainda e um laboratorio, nao a arquitetura oficial;
3. o produto publicado ainda vaza linguagem interna em varios pontos;
4. o backstage ja tem contrato e review pack mais claros;
5. agora a decisao precisa virar superficie publica mais limpa e mais coerente;
6. nao ha motivo para introduzir backend stateful, editor novo ou troca de runtime nesta fase.

## 3) Pergunta-mestra

Se o backstage ficou mais inteligente, o que precisa mudar na superficie publicada para a familia perceber:

1. o ritmo da licao;
2. o beneficio imediato;
3. a separacao entre ler, falar e fazer;
4. a progressao por arcos;
5. a identidade de `Matematica Viva` sem cara de painel interno?

## 4) O que esta task precisa decidir

Ao final desta task, precisamos ter decisoes claras sobre:

1. qual linguagem interna deve desaparecer do front publicado;
2. como a entrada de `Sementes` explica o ritmo e reduz ansiedade;
3. como a licao mostra claramente o que o adulto le, diz e conduz;
4. como a progressao por arcos aparece sem virar culpa;
5. qual e o menor piloto que prova a melhoria;
6. o que fica como recomendacao de superficie e o que fica como backlog.

## 5) Fontes obrigatorias de verdade

### Contexto macro

1. `README.md`
2. `AI_CONTEXT.md`
3. `MelhorarEstrutura/README.md`
4. `MelhorarEstrutura/ENTENDA_MELHORAR_ESTRUTURA.md`

### Base da discussao

1. `MelhorarEstrutura/discussoes/2026-03-19_2204_SEMENTES_PRODUTO_PADRAO_E_REVISAO_INTELIGENTE.md`
2. `MelhorarEstrutura/discussoes/2026-03-19_2223_CONTRATO_CANONICO_SEMENTES.md`
3. `MelhorarEstrutura/discussoes/2026-03-19_2225_ANATOMIA_DO_REVIEW_PACK_POR_BLOCO.md`
4. `MelhorarEstrutura/discussoes/2026-03-19_2228_FLUXO_EDITORIAL_SEMENTES.md`
5. `MelhorarEstrutura/discussoes/2026-03-20_1440_PRODUTO_PUBLICADO_SEMENTES.md`

### Evidencia tecnica e de produto

1. `docs/MAPA_EXECUCAO_PROJETO.md`
2. `site/manual-portador.html`
3. `site/sementes/*.html`
4. `site/sementes/style.css`
5. `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml`
6. `curriculo/01_SEMENTESV6/*.yaml`

## 6) Principios inegociaveis

### 6.1 Familia no centro

Se a mudanca melhora o sistema, mas piora a vida da mae real, ela reprova.

### 6.2 Clareza antes de engenhosidade

Se a mudanca e elegante no papel, mas dificil de entender em casa, ela reprova.

### 6.3 Backstage nao deve vazar para a frente

O produto publicado precisa falar a lingua da familia, nao a lingua da operacao interna.

### 6.4 Vercel-first e HTML como realidade

Nada nesta fase deve depender de backend novo para existir.

### 6.5 Progresso sem culpa

Se a progressao narrativa ou visual gera pressao indevida, ela esta mal desenhada.

### 6.6 Pequena mudanca, grande leitura

O piloto precisa ser pequeno o bastante para caber, mas forte o bastante para ensinar.

## 7) Hipoteses em disputa

### Hipotese A - Limpeza de linguagem apenas

Remover labels internas da face publica e melhorar a leitura visual sem mexer no significado profundo da jornada.

Vantagem:

- menor custo;
- menor risco;
- entrega valor rapido.

Risco:

- pode melhorar a aparencia sem resolver a compreensao de ritmo.

### Hipotese B - Superficie familiar com contrato visivel

Reorganizar a entrada de `Sementes` para explicitar ritmo, previsibilidade, leitura e acao do adulto.

Vantagem:

- conversa com a dor real da mae;
- melhora a primeira impressao do produto.

Risco:

- exige mais cuidado de copy e hierarquia visual.

### Hipotese C - Superficie por arcos

Mostrar a progressao de `Sementes` como caminhada narrativa, com arcos claros e marcos de avanco.

Vantagem:

- fortalece a sensacao de jornada;
- ajuda a familia a entender onde esta.

Risco:

- se exagerar, vira gamificacao ansiosa.

## 8) Sequencia fase a fase

Esta task deve ser aplicada em fases pequenas, com verificacao entre elas.

### Fase 0 - Reentrada e congelamento

Objetivo:

1. confirmar o estado real do produto publicado;
2. identificar onde a linguagem interna aparece;
3. registrar o que esta dentro e fora de escopo;
4. travar a definicao de sucesso do piloto.

Passos:

1. abrir `AI_CONTEXT.md`;
2. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`;
3. abrir a discussao `MelhorarEstrutura/discussoes/2026-03-20_1440_PRODUTO_PUBLICADO_SEMENTES.md`;
4. listar superficies publicas afetadas;
5. marcar os vazamentos de linguagem interna;
6. congelar o que nao sera mexido nesta rodada.

Saida esperada:

- mapa curto das superficies;
- lista de vazamentos;
- criterio de sucesso do piloto;
- delimitacao de escopo.

### Fase 1 - Contrato da superficie publica

Objetivo:

1. decidir o que a familia precisa entender em menos de um minuto;
2. definir a mensagem de entrada de `Sementes`;
3. explicitar o acordo de ritmo;
4. separar leitura, fala e acao.

Passos:

1. definir a promessa curta da entrada;
2. definir o que o adulto precisa ver primeiro;
3. definir o que deve ficar escondido na operacao interna;
4. estabelecer os termos visiveis que podem aparecer no front;
5. estabelecer os termos proibidos na face publica.

Saida esperada:

- contrato resumido da superficie publica;
- lista de termos permitidos e proibidos;
- copia base de entrada.

### Fase 2 - Entrada de Sementes

Objetivo:

1. deixar claro que a pagina e para uma familia;
2. explicar o ritmo da licao sem peso;
3. deixar evidente o beneficio imediato;
4. reduzir ansiedade na primeira leitura.

Passos:

1. revisar a primeira dobra da experiencia;
2. revisar o bloco de explicacao de ritmo;
3. revisar chamadas para licao ou trilha;
4. revisar linguagem de alivio para o Portador;
5. revisar se a entrada parece guia ou painel.

Saida esperada:

- entrada de Sementes mais familiar;
- ritmo mais claro;
- menos cara de dashboard interno.

### Fase 3 - Superficie da licao

Objetivo:

1. deixar claro o que se le;
2. deixar claro o que se fala;
3. deixar claro o que a crianca faz;
4. tornar o uso mais calmo e usavel no celular.

Passos:

1. revisar hierarquia visual;
2. revisar labels do tipo "leia", "fale", "faca";
3. revisar blocos de orientacao do Portador;
4. revisar prompts de acao imediata;
5. revisar se a licao continua reconhecivel como `Matematica Viva`.
6. revisar `site/sementes/style.css` quando a hierarquia visual depender de regras de CSS.

Saida esperada:

- licao com instrucoes mais legiveis;
- menos traducao mental;
- melhor separacao entre texto de conducao e texto de historia.

### Fase 4 - Arcos e progressao

Objetivo:

1. mostrar progresso sem pressao;
2. explicar onde a familia esta na jornada;
3. reforcar continuidade sem culpa;
4. tornar a progressao um convite, nao uma cobranca.

Passos:

1. definir quais arcos aparecem na superficie publica;
2. definir como eles sao nomeados;
3. definir como o avanco aparece visualmente;
4. definir o que nao deve ser mostrado para nao virar ansiedade;
5. revisar se o arco ajuda ou distrai.

Saida esperada:

- mapa simples de arcos;
- linguagem de progresso mais calma;
- leitura de jornada mais clara.

### Fase 5 - Piloto minimo

Objetivo:

1. aplicar a ideia em um recorte pequeno;
2. confirmar se a melhoria faz sentido na pratica;
3. evitar overengineering;
4. criar referencia concreta para decidir a proxima rodada.

Criterios para o piloto:

1. precisa mostrar a diferenca entre backstage e superficie publica;
2. precisa caber em uma observacao curta de qualidade;
3. precisa ser comparavel com o estado anterior;
4. precisa caber na realidade atual do projeto;
5. precisa ser pequeno o bastante para terminar.

Saida esperada:

- um piloto escolhido;
- um antes e depois bem definido;
- um veredito curto sobre utilidade.

### Fase 6 - Consolidacao e decisao

Objetivo:

1. registrar o que entrou para valer;
2. registrar o que foi recusado;
3. registrar o que fica para depois;
4. decidir se a proposta merece ampliar escopo.

Passos:

1. consolidar achados;
2. comparar com o `North Star`;
3. comparar com o uso real da mae;
4. comparar com o custo operacional;
5. definir proximo tema ou encerramento.

Saida esperada:

- recomendacao final;
- backlog enxuto;
- proxima decisao claramente nomeada.

## 9) Sequencia operacional minima

Se esta task for executada de forma enxuta, seguir esta ordem:

1. Fase 0 - reentrada e congelamento
2. Fase 1 - contrato da superficie publica
3. Fase 2 - entrada de Sementes
4. Fase 3 - superficie da licao
5. Fase 4 - arcos e progressao
6. Fase 5 - piloto minimo
7. Fase 6 - consolidacao e decisao

## 10) Criterios de saida por fase

### Fase 0

- escopo congelado;
- vazamentos mapeados;
- criterio de sucesso definido.

### Fase 1

- linguagem interna catalogada;
- copy base definida;
- termos proibidos definidos.

### Fase 2

- entrada mais clara;
- ritmo mais legivel;
- menos ansiedade visual.

### Fase 3

- licao mais conducivel;
- menos traducao mental;
- celular mais amigavel.

### Fase 4

- progresso visivel sem culpa;
- arcos entendiveis;
- leitura de jornada natural.

### Fase 5

- piloto pequeno e real;
- comparacao antes/depois possivel;
- valor percebido comprovado.

### Fase 6

- decisao final registravel;
- backlog menor;
- proxima fase clara.

## 11) Riscos

1. A superficie ficar limpa demais e perder calor.
2. A progressao virar gincana ou culpa.
3. O piloto crescer demais.
4. O backstage voltar a vazar para o front.
5. A fase entrar em implementacao antes de fechar o contrato visual.

## 12) Regra de uso desta task

1. esta task nao substitui `003`, `004` ou `023`;
2. ela organiza a proxima evolucao da superficie publica;
3. ela deve ser lida junto com a discussao `MelhorarEstrutura/discussoes/2026-03-20_1440_PRODUTO_PUBLICADO_SEMENTES.md`;
4. ela deve ser aplicada fase por fase, sem saltar direto para solucao grande;
5. quando uma fase fechar, registrar a saida antes de abrir a proxima.

## 13) Proximo passo natural

Depois desta task, o melhor proximo movimento e:

1. abrir a discussao `2026-03-20_1440_PRODUTO_PUBLICADO_SEMENTES.md` com esta task ao lado;
2. derivar o contrato curto da superficie publica;
3. escolher o piloto minimo.
