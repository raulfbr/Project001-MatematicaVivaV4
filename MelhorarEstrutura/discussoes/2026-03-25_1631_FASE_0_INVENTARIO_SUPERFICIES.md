# DISCUSSAO - FASE 0 INVENTARIO DE SUPERFICIES

Data: 2026-03-25
Hora: 16:31
Tema: mapear as superficies publicas reais de Sementes e localizar vazamentos de linguagem interna
Status: checkpoint inicial executado

## Leitura em 30 segundos

Decisao provisoria desta Fase 0:

- a superficie publica principal ainda inclui um home com linguagem interna de operacao
- o manual do Portador ja e bem mais familiar, mas ainda carrega vestigios de "dashboard"
- o ciclo `Sementes` ja tem a licao publica como nucleo de produto
- o CSS e parte da superficie publica e precisa entrar no escopo das fases seguintes
- existem superficies de laboratorio e teste que nao devem ser tratadas como face principal da familia

Papel deste arquivo hoje:

- registrar o inventario inicial da superficie publica
- separar o que e face familiar, face operacional e face experimental
- fixar o escopo das proximas fases com base em evidencia real

## 1) Pergunta central

Quais superficies publicas existem de fato hoje, onde a linguagem interna ainda vaza, e quais arquivos precisam entrar nas fases seguintes para melhorar `Sementes` sem confundir produto com laboratorio?

## 2) Fontes de evidencia

- `site/index.html`
- `site/manual-portador.html`
- `site/landingpage.html`
- `site/landing_v3_journey.html`
- `site/sementes/*.html`
- `site/sementes/style.css`
- `site/sementes/lab_icones.html`
- `site/public/sementes_teste/*.html`
- `site/sementes/templates/*.j2`

## 3) Fatos observados

### 3.1 A home principal ainda parece painel interno

Evidencias visiveis em `site/index.html`:

- `Orchestrator Dashboard` no titulo
- `Ambiente: Production (Forge V3)` na abertura
- `Configuracoes` no menu lateral
- `Sistema` como secao de navegacao

Leitura:

o home principal ainda fala muito com operacao interna e pouco com a familia.

### 3.2 O Manual do Portador ja esta mais familiar, mas ainda mistura vocabulario

Evidencias visiveis em `site/manual-portador.html`:

- `Voltar para o dashboard`
- secao lateral `Sistema`
- item `Configuracoes`
- texto de entrada ja focado em celular, Licao 000 e conduta familiar

Leitura:

o manual esta mais perto da familia do que da operacao, mas ainda carrega residuos de linguagem de sistema.

### 3.3 O ciclo `Sementes` ja e a superficie publica central

Evidencias visiveis em `site/sementes/*.html`:

- `Preparacao do Portador`
- `Ritual de Entrada`
- `A Jornada`
- `O Concreto`
- `Narramos Juntos`
- `Ritual de Fechamento`
- `Conexao da Jornada`
- `Sementes para o Dia`
- `Formacao do Portador`

Leitura:

essa familia de blocos ja e o contrato visual e pedagogico vivo da fase publica.

### 3.4 O CSS e parte da experiencia publica

Evidencia:

- `site/sementes/style.css` existe como superficie de acabamento real do produto.

Leitura:

na Fase 3, CSS nao pode ser tratado como detalhe tecnico secundario. Ele e parte da experiencia da familia.

### 3.5 Existem superficies experimentais e de teste que nao sao face principal

Evidencias:

- `site/landingpage.html`
- `site/landing_v3_journey.html`
- `site/sementes/lab_icones.html`
- `site/public/sementes_teste/*.html`

Leitura:

essas superficies ajudam a experimentar, mas nao devem ser tratadas como rota principal da familia sem decisao explicita.

## 4) Vazamentos de linguagem interna

### Vazamentos fortes

- `Orchestrator Dashboard`
- `Ambiente: Production (Forge V3)`
- `Sistema`
- `Configuracoes`

### Vazamentos moderados

- `Voltar para o dashboard`
- alguns ramos de navegacao ainda falam como produto interno, nao como jornada familiar

### Vazamentos de contexto

- o lab de icones usa nomes como `Header / Jornada / Mapa`
- o material de teste em `site/public/sementes_teste` nao deve ser confundido com face publicada canonica

## 5) Delimitacao de escopo para as proximas fases

### Entram como foco principal

1. `site/index.html`
2. `site/manual-portador.html`
3. `site/sementes/*.html`
4. `site/sementes/style.css`

### Entram como apoio de leitura

1. `site/landingpage.html`
2. `site/landing_v3_journey.html`
3. `site/sementes/lab_icones.html`
4. `site/public/sementes_teste/*.html`
5. `site/sementes/templates/*.j2`

### Ficam fora da mudanca imediata

1. runtime
2. backend
3. banco de dados
4. editor novo
5. troca de stack

## 6) Hipoteses iniciais

### Hipotese A

Limpar primeiro a home e o manual, porque eles sao a entrada e ainda carregam a maior parte da fala interna.

### Hipotese B

Tratar a experiencia `Sementes` como superficie principal e deixar a home servir a jornada familiar, nao o sistema.

### Hipotese C

Usar CSS e hierarquia visual para tornar a leitura publica mais clara antes de inventar novas superficies.

## 7) Recomendacao provisoria desta fase

A melhor leitura inicial e:

1. a Fase 1 deve nascer do contrato da superficie publica;
2. a primeira limpeza evidente deve acontecer na home principal;
3. o manual deve perder o pouco de vocabulario de dashboard que ainda carrega;
4. `Sementes` deve permanecer como o corpo principal da experiencia publica;
5. o CSS deve entrar na revisao formal do front.

## 8) Riscos

- mexer demais nas superficies experimentais antes de fechar o contrato
- considerar o lab como produto final
- melhorar a estetica sem resolver a lingua interna
- esquecer que o manual e a home ainda educam a percepcao da familia

## 9) Proximo passo sugerido

`FASE 1 - CONTRATO DA SUPERFICIE PUBLICA`

Pergunta:

se a familia precisa entender o produto em menos de um minuto, quais palavras, blocos e hierarquias podem aparecer na face publica sem vazar linguagem interna?

