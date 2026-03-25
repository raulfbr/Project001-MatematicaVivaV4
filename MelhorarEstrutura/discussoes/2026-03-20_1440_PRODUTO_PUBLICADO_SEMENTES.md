# DISCUSSAO - PRODUTO PUBLICADO E SUPERFICIES DE SEMENTES

Data: 2026-03-20
Hora: 14:40
Tema: definir o que no site publicado precisa mudar para que Sementes pareca mais fiel ao North Star e menos painel interno
Status: recomendacao provisoria

## Leitura em 30 segundos

Decisao provisoria deste arquivo:

- o produto final (site) precisa parar de vazar a linguagem de operacao interna (tags, IDs de blocos) para o Portador
- a entrada do ciclo deve explicitar o acordo de previsibilidade: qual o ritmo da licao, o que exigir e o que relevar
- o layout dos blocos deve criar transicoes claras (o que eu leio, o que eu falo, o que a crianca faz)
- a progressao por arcos deve ser visivel, premiando o avanco da familia de forma gamificada ou narrativa

Papel deste arquivo hoje:

- fechar a visao de produto que justifica a nova fase de Sementes
- alimentar a task-mae `TASK_ROBUSTA_EXECUCAO_FASEADA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`
- preparar a proxima discussao sobre o Piloto Minimo

Se voce estiver retomando a trilha, o proximo tema sugerido e:

- `PILOTO_MINIMO_SEMENTES`

## 1) Pergunta central

Se o metodo editorial ficar melhor no backstage, o que no site publicado precisa mudar para que `Sementes` pareca mais fiel ao `North Star` e menos percepcao de "painel interno de criacao"?

## 2) Fontes de evidencia

- `E1`: `TASK_ROBUSTA_CONVERGENCIA_SUGESTAO_SEMENTES.md`
- `E2`: `LORE/north_star.yaml`
- `E3`: `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`
- `E4`: `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml`
- `E5`: Visual atual das licoes de `Sementes` publicadas (Vercel/HTMLs de producao)

## 3) Fatos observados

### 3.1 Vazamento de painel interno

`E4` e `E5` mostram que o produto final muitas vezes exibe estruturas como "Bloco 2", "Bloco 3", ou metadados de gestao que resolvem a vida de quem redige, mas poluem a visao de quem le e conduz.

Leitura: o site atual ainda funciona, em parte, como um "Word online" formatado, sem blindar o backstage visualmente.

### 3.2 O ritmo e presumido, nao ensinado ao visitante

`E2` (Abra e Faca) e `E3` reforcam a necessidade de reducao de carga mental. Porem, a porta de entrada (a landing page ou a aba inicial do ciclo `Sementes`) muitas vezes nao estabelece o "acordo" de como essas aulas funcionam (preparacao rapida, interacao intensa, resolucao curta).

Leitura: as maes estao descobrindo o ritmo so porque sao resilientes, nao porque o painel explana facilmente o beneficio de previsibilidade do ciclo.

### 3.3 A leitura do Portador compete com a leitura da Crianca

Nas licoes reais do ciclo, a quebra de texto (o que e lore para a mae vs. o que ela fala em voz alta) as vezes ainda depende de ler com atencao todo o CSS ou interpretacao de bold/italico espalhado.

Leitura: a interface nao esta aliviando totalmente a carga no calor do momento.

## 4) Tensoes reais

### Tensao 1 - Linguagem editorial forte vs Interface minimalista familiar

- a favor editorial forte: garante que nenhuma informacao pedagogica se perca
- contra: assusta a familia. A mae ve muito texto (orientacao pedagogica profunda) e acha que tem que estudar antes de aplicar.

### Tensao 2 - Revelar muita progressao vs Reduzir pressao final

- a favor de revelar: mapas visuais dos arcos criam senso de missao
- contra: gamificar em excesso pode gerar culpa atrasada se a mae perde rimo semanal em `Sementes`.

## 5) Leitura dos experts

### 5.1 `estrategista_estrutura`

Leitura: a separacao entre "o que e contrato editorial" e "o que exibe na tela" esta fraca.

Posicao: devemos usar o fato de que estruturamos `review packs` confiaveis no backstage para desenhar duas interfaces reais. Uma visualizacao para revisao (com todos os meta-campos) e o front do Vercel estrito para a mae (purgado de qualquer jargao tecnico).

### 5.2 `vercel_first`

Leitura: ja temos React/Next.js/Tailwind suficiente no stack atual (`E5`). O HTML final que empurramos pode ser renderizado com muito mais clareza sem nenhum plugin fantastico.

Posicao: esconder campos que pertencem a `meta` e formatar diferentemente o que e instrucao e o que e oralidade. Nao precisa de banco de dados, apenas parse de CSS condizente com a hierarquia das licoes.

### 5.3 `contrato_licao`

Leitura: se o bloco "anexar semente" ou "ancora" esta bem classificado no contrato editorial (`E1`), o front end pode desenhar icones fortes em cima disso em vez de usar nomes de sessoes textuais longas.

Posicao: o produto deve exibir a intencao (Ex: "Fale para ele:", "Mostre:", "Facam juntos:"), enquanto o JSON/YAML do contrato mantem o naming canonico "bloco_ancoragem". A traducao deve ser 1-para-1, mas sem vazar do backend pro lar.

### 5.4 `revisao_escalavel`

Leitura: isolar o design final das orientacoes de backstage ajuda a IA e o revisor a nao se preocuparem em reescrever um bloco de "como a mae deve sentar" toda vez que quiserem melhorar apenas a frase da matematica.

Posicao: no produto final, o HTML deve ser uma visualizacao limpia. Durante a revisao, avaliamos o rigor. Nao e a mae que tem que ver o rigor tecnico desnudado.

### 5.5 `mae_regente_real`

Leitura: a experiencia real falha quando a pagina parece um relatorio de consultoria ou um plano de ensino de coordenador. `Sementes` devia parecer um script de exploracao encantada.

Posicao:

- Quero bater o olho e saber: "ok, isso e pra eu ler em silencio", "isso e pra eu falar alto".
- Quero ver onde eu estou no grande ciclo sem me sentir julgada se perdi 3 dias.
- Quero linguajar afetuoso, voltado a mim ("Mae, preste atencao nesse arranjo..."), nao a academicos.

## 6) Hipoteses ou opcoes

### Hipotese A - Melhorar CSS sobre HTML atual

Deixar o texto como esta, mas fazer um esforco puro de estilo: cores de fundo para diferenciar fala, acao e contexto. Menu lateral novo so em Sementes para mostrar "Arco 1, Arco 2".

Vantagem: barata, usa o HTML estatico como base atual, facil de aplicar.
Desvantagem: a matriz de textos internos / labels continuaria la, apenas pintada de outra cor.

### Hipotese B - Filtragem de contrato ('Purge' Editorial) antes do build

Usar a definicao de review packs e blocos canonicos para gerar um HTML especial para o build final: tudo que e meta, instrucao densa de validacao etc., fica cortado. Traducao automatica das tags internas para blocos super-simples: [ Ler ], [ Falar ], [ Fazer ].

Vantagem: defende a Mae Regente do overload de texto. O painel fica limpo, focado só no "Abra e Faca".
Desvantagem: Requer mexer na fase final de transformacao textual para separar backstage de front-stage.

### Hipotese C - Painel complexo de 'Dashboard' na entrada

Criar uma area logada forte onde a mae escolhe como quer ver a licao: modo "Aprofundamento" (todas as justificativas) ou modo "Execucao Express" (so scripts e acoes).

Vantagem: atende ambos os publicos.
Desvantagem: hiper-engenharia, falha redondamente no quesito de simplicidade absoluta do North Star no primeiro clique. Foge do escopo "Vercel Default Simples".

## 7) Leitura consolidada

A Hipotese B e a unica que encarna verdadeiramente o nosso `North Star` de "familia no centro" sem estourar infraestrutura.

Nos ja sofremos com carga mental na revisao. Passar essa carga pra mae atraves de um produto que parece um "Google Doc bem formatado" quebra o contrato de `Sementes`.

A resolucao estrutural que separa o contrato (os blocos e as funcoes) nos permite fazer essa purificacao no build:
- O backstage segura a complexidade pedagogica.
- O site expoe clareza, previsibilidade de ritmo e prompts visuais rapidos (corolario do "Abra e Faca").

A "entrada do ciclo" precisa ganhar uma sub-home que apresente `Sementes` como uma jornada de 4-5 arcos, mostrando o tesouro ao final, preparando o Portador, e com isso absorvendo a funcao intridutora que hoje vaza para o cabecalho de algumas licoes iniciais.

## 8) Recomendacao provisoria

Para o produto de Sementes, recomendamos a "Filtragem de Contrato" e as mudancas ativas de superficie de comunicacao:

1. Linguagem familiar: Todas as labels tecnicas e nomes internos de blocos devem desaparecer do frontend publicado. Substituir por verbos de execucao (Ex: Fale, Pergunte, Espere).
2. O ritmo da licao deve ficar mudo na teoria, mas gritante na UI: caixas visualmente distintas para instrucao calada vs roteiro falado.
3. Arcos e Progressao: Antes das licoes, `Sementes` ganha uma tela macro de progresso narrativo dividida por arcos, reduzindo a angustia existencial de "onde estamos indo".
4. Beneficio imediato: no topo de cada licao, o foco da ui nao e listar dependencias pedagogicas, mas dar o beneficio da sessao ("Em 15 minutos de brincadeira, hoje voces verao a correspondencia espacial explodir na mesa.").

## 9) Riscos

- Demorar tanto separando interface interna da externa na extracao (render HTML) que paralise o pipeline atual.
- A "tela de onboarding dos arcos" exigir muito conteudo novo que nao esta mapeado.
- Perder a riqueza da intencionalidade pedagogica - se for tao esteticamente podado, a licao parecer "pobre". Deve ser simples, nao superficial.

## 10) Proximo tema sugerido

`PILOTO_MINIMO_SEMENTES`

Pergunta:
Se os blocos estao definidos, o fluxo editorial esta resolvido e a mudanca de produto desejada esta clara, qual e o menor piloto (qual licao, com quais entregaveis reais) que prova essa sugestao no `MelhorarEstrutura` sem explodir o escopo?
