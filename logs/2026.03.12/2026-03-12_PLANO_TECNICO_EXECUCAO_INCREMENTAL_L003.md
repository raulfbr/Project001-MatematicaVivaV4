# PLANO TECNICO DE EXECUCAO INCREMENTAL - L003
Data: 2026-03-12
Licao alvo: `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html`
Arquivos previstos:
1. `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html`
2. `site/sementes/style.css`
3. log final desta rodada

Objetivo:
Traduzir o plano editorial em execucao tecnica segura, incremental e auditavel.

Regra desta rodada:
1. preservar o cerne da licao;
2. preservar a identidade do Reino;
3. preservar blocos de cor como ajuda visual real;
4. corrigir linguagem operacional, ordem de acao e hierarquia visual;
5. evitar overcorrection.

---

## 1) Estado tecnico atual
### O que o HTML ja oferece
1. a pagina ja esta no esqueleto canonico `001-012`;
2. ha blocos reutilizaveis suficientes para quase todas as correções:
   a. `instruction-box`
   b. `strategy-box`
   c. `graca-box`
   d. `sementes-box`
   e. `journey-script`
   f. `journey-instruction-box`
3. `Narramos Juntos` pode ser reestruturado sem alterar a arquitetura macro da licao;
4. o CSS ja tem uma base forte de cards coloridos e caixas semanticas.

### O que falta tecnicamente
1. microcopy mais precisa;
2. reordenacao de alguns blocos em `A Jornada`;
3. maior separacao semantica em `Narramos Juntos`;
4. um destaque melhor para a ponte `O Concreto -> Narramos Juntos`;
5. pequenos ajustes de classes para manter a leitura modular.

### Conclusao tecnica
Nao e necessario criar novo sistema.
Basta:
1. reorganizar HTML local;
2. adicionar poucas classes novas ao CSS;
3. reaproveitar os componentes existentes.

---

## 2) Estrategia de execucao
A execucao sera feita em 4 lotes pequenos.

### Lote 1
Frases centrais, `Preparacao do Portador`, `Ritual de Entrada` e abertura da `Jornada`.

### Lote 2
`O Concreto` e a transicao para `Narramos Juntos`.

### Lote 3
Reestruturacao profunda de `Narramos Juntos`.

### Lote 4
`Ritual de Fechamento`, `Conexao da Jornada`, `Sementes para o Dia` e ajuste leve da `Formacao do Portador`.

Depois:
1. reauditoria;
2. sanity check de encoding;
3. log final.

---

## 3) Quebra maxima de tasks
## T00 - Congelar escopo
Status esperado: antes de qualquer patch

Escopo:
1. mexer apenas em `L003`;
2. nao alterar governanca do sistema;
3. nao mexer em `L002` ou `L004`;
4. permitir pequenos ajustes em `style.css` apenas para suportar esta licao.

Criterio de aceite:
1. nenhum arquivo fora do escopo alterado sem necessidade tecnica real.

## T01 - Normalizar vocabulario central da licao
Arquivo:
1. `MV-S-003_A_ESTRELA_DO_REINO.html`

Trechos:
1. `prep-focus-tag`
2. `prep-bridge-box`
3. `O Concreto`
4. `Conexao da Jornada`
5. `Sementes para o Dia`

Objetivo:
1. reduzir `acender/respirar/nascer` em zonas operacionais;
2. fixar `borda`, `centro`, `forma`, `desenho`, `estrela`.

Criterio de aceite:
1. a mae entende o foco sem precisar traduzir;
2. o texto nao fica seco nem escolar.

## T02 - Corrigir o foco da licao
Trecho:
1. `prep-focus-tag`

Objetivo:
1. trocar a formulacao antiga;
2. alinhar com o feedback da Marina;
3. manter a promessa pedagogica.

Criterio de aceite:
1. frase curta;
2. concreta;
3. coerente com hero e com o restante da pagina.

## T03 - Ajustar `Fio da Jornada`
Trecho:
1. `prep-bridge-box`

Objetivo:
1. remover abstracao desnecessaria;
2. manter a ponte `L002 -> L003 -> L004`.

Criterio de aceite:
1. leitura fluida;
2. promessa curricular clara;
3. nenhuma quebra de atmosfera.

## T04 - Ajustar `Descoberta da Crianca`
Trecho:
1. lista em `prep-section`

Objetivo:
1. reescrever o item `numero e desenho podem aparecer juntos na mesma experiencia`;
2. manter a ideia elogiada pela Marina: numero em forma.

Criterio de aceite:
1. a ideia fica mais clara;
2. a formula continua viva.

## T05 - Ajustar `Sinal de Fruto`
Trecho:
1. `prep-section` do fruto

Objetivo:
1. trocar `reorganizando as pecas em silencio` por expressao domestica;
2. preservar a legitimidade da narracao nao verbal.

Criterio de aceite:
1. a mae entende o gesto;
2. a frase continua pedagogicamente digna.

## T06 - Revisar fala final do `Ritual de Entrada`
Trecho:
1. ultimo paragrafo do `Portador da Tocha` no ritual

Objetivo:
1. tornar a fala mais concreta;
2. preparar o reveal sem soar vaga.

Criterio de aceite:
1. a fala pode ser lida em voz alta sem estranhamento;
2. ela prepara o proximo gesto.

## T07 - Reordenar tecnicamente a abertura da Jornada
Trecho:
1. bloco `journey-scene journey-scene--reveal`

Objetivo:
1. explicitar que o card da guardia deve ser mostrado;
2. reorganizar a sequencia para `card -> fala -> gesto`;
3. manter a personalidade de Iris.

Acao tecnica:
1. mover o `script-persona-block` para cima do `journey-instruction-box`;
2. trocar a label do card;
3. revisar o texto do box de gesto para deixar claro que vem depois.

Criterio de aceite:
1. a mae nao pergunta mais `mostro o card ou nao?`;
2. a jornada continua fluida.

## T08 - Revisar microcopy do gesto da Jornada
Trecho:
1. `journey-instruction-box` do primeiro bloco da Jornada

Objetivo:
1. substituir a genericidade de `Gesto do Portador` por sequencia mais clara;
2. reduzir a confusao de ordem.

Criterio de aceite:
1. o box comunica o que fazer depois da fala da guardia.

## T09 - Revisar objetivo de `O Concreto`
Trecho:
1. primeiro `instruction-box` de `O Concreto`

Objetivo:
1. trocar `acendendo o centro`;
2. manter o cerne matematico.

Criterio de aceite:
1. texto claro e coerente com o foco da licao.

## T10 - Revisar frase final da atividade principal
Trecho:
1. passo 5 da atividade principal

Objetivo:
1. reduzir metafora operacional;
2. manter a ideia de repeticao leve.

Criterio de aceite:
1. passo continua natural para a mae executar.

## T11 - Reescrever `Adaptacao para casa real`
Trecho:
1. `strategy-box` de `O Concreto`

Objetivo:
1. explicar `material igual` com criterio domestico claro;
2. explicitar o que importa quando os materiais forem mistos.

Criterio de aceite:
1. a mae entende o que fazer sem pensar em teoria.

## T12 - Reescrever `Sinal de fruto do dia` em `O Concreto`
Trecho:
1. `strategy-box` de `O Concreto`

Objetivo:
1. traduzir `apontando ou reorganizando em silencio`;
2. preparar melhor a passagem para a narracao.

Criterio de aceite:
1. a frase explica claramente a observacao esperada.

## T13 - Destacar visualmente a ponte para `Narramos Juntos`
Trechos:
1. remover ou reduzir o paragrafo de ponte dentro do `strategy-box`
2. criar bloco proprio logo abaixo

Arquivo tecnico:
1. HTML
2. CSS

Objetivo:
1. transformar a transicao em acao visivel;
2. aproveitar a preferencia da Marina por blocos de cor.

Acao tecnica:
1. criar classe local nova, por exemplo `bridge-highlight-box`;
2. dar cor propria e hierarquia clara.

Criterio de aceite:
1. a ponte salta aos olhos;
2. continua coerente com o design da pagina.

## T14 - Ajustar postura de escuta em `Narramos Juntos`
Trecho:
1. primeiro `instruction-box` da secao

Objetivo:
1. manter o valor pedagogico;
2. trocar o que soa estranho por linguagem mais clara.

Criterio de aceite:
1. a mae entende que pode acolher fala pequena ou gesto.

## T15 - Reescrever a pergunta inicial de Iris
Trecho:
1. `script-persona-block` da secao `Narramos Juntos`

Objetivo:
1. sair de `como o desenho nasceu hoje`;
2. manter voz propria da guardia;
3. tornar o reconto concreto.

Criterio de aceite:
1. pergunta falavel;
2. pergunta respondiveis;
3. sem perder encanto.

## T16 - Criar bloco de orientacao para a mae sobre quantas perguntas fazer
Trechos:
1. novo bloco antes das perguntas de reconto

Arquivo tecnico:
1. HTML
2. talvez CSS opcional

Objetivo:
1. explicitar `escolha 1 ou 2 perguntas`;
2. dizer que nao precisa fazer todas;
3. instruir a esperar a resposta da crianca.

Criterio de aceite:
1. a inseguranca da mae cai;
2. a secao fica escaneavel no celular.

## T17 - Reescrever as perguntas de reconto
Trecho:
1. lista atual de perguntas

Objetivo:
1. substituir abstração por gesto observavel;
2. garantir que a propria mae saberia responder.

Criterio de aceite:
1. perguntas concretas;
2. poucas;
3. sem sobrecarga.

## T18 - Separar `Perguntas do coracao` em bloco proprio
Trechos:
1. remover do bloco compartilhado atual
2. criar card colorido proprio

Objetivo:
1. deixar claro que sao opcionais;
2. manter a camada afetiva.

Arquivo tecnico:
1. HTML
2. possivel nova classe CSS `heart-questions-box`

Criterio de aceite:
1. visualmente nao compete com reconto principal.

## T19 - Separar `Formas legitimas de narracao`
Trecho:
1. criar bloco proprio

Objetivo:
1. preservar o ponto pedagogico;
2. dar alivio visual.

Acao tecnica:
1. reutilizar `graca-box` ou classe equivalente.

Criterio de aceite:
1. a mae identifica este bloco como permissao, nao como mais tarefa.

## T20 - Separar `Adaptacao digna e inclusiva`
Trecho:
1. criar bloco proprio

Objetivo:
1. nao competir com as perguntas;
2. proteger multi-crianca e fala pequena.

Acao tecnica:
1. reutilizar `sementes-box` ou classe equivalente.

Criterio de aceite:
1. adaptacao fica clara e secundaria, nao embolada.

## T21 - Revisar fala de Iris no fechamento
Trecho:
1. `Ritual de Fechamento`

Objetivo:
1. tirar filosofizacao excessiva;
2. manter o clima do Reino.

Criterio de aceite:
1. Iris ainda parece Iris;
2. a mae entende e consegue oralizar.

## T22 - Definir tecnicamente o papel do `Portador da Tocha` no fechamento
Trecho:
1. bloco final do fechamento

Objetivo:
1. escolher entre `fala real` ou `instrucao`;
2. remover ambiguidade.

Decisao tecnica inicial:
1. tentar manter como fala real;
2. se soar artificial, converter para `instruction-box`.

Criterio de aceite:
1. o usuario le e sabe imediatamente se aquilo e para falar ou para fazer.

## T23 - Revisar `Memoria viva`
Trecho:
1. `Conexao da Jornada`

Objetivo:
1. alinhar vocabulario com o resto da pagina;
2. remover `acender o centro` se continuar operacionalmente fraco.

Criterio de aceite:
1. conexao resume a licao sem tropeço verbal.

## T24 - Revisar `Sementes para o Dia` - dramatizacao
Trecho:
1. item `Dramatizacao`

Objetivo:
1. trocar `acender o centro` por gesto mais concreto.

Criterio de aceite:
1. continua imagetico, mas mais usavel.

## T25 - Revisar `Sementes para o Dia` - narracao
Trecho:
1. item `Narracao`

Objetivo:
1. trocar `se a fala vier curta`.

Criterio de aceite:
1. frase natural de mae para mae.

## T26 - Revisar `Sementes para o Dia` - reflexao
Trecho:
1. item `Reflexao`

Objetivo:
1. remover pergunta filosofica demais;
2. manter continuacao domestica concreta.

Criterio de aceite:
1. a reflexao parece opcional e realista.

## T27 - Ajuste leve em `Formacao do Portador`
Trechos:
1. titulo da estrategia, se necessario
2. pontos de repeticao de vocabulario criticado

Objetivo:
1. alinhar o meta-texto sem desmontar a camada formativa.

Criterio de aceite:
1. secao continua mais rica que os blocos operacionais;
2. nao repete exatamente as formulas criticadas.

## T28 - Adicionar CSS minimo de suporte
Arquivo:
1. `style.css`

Possiveis classes:
1. `bridge-highlight-box`
2. `heart-questions-box`
3. `narration-meta-box`
4. ajustes pequenos em listas internas, se necessario

Objetivo:
1. suportar separacao visual nova;
2. preservar a logica de blocos coloridos;
3. evitar regressao no mobile.

Criterio de aceite:
1. nenhuma classe nova sem uso;
2. nada quebra responsividade.

## T29 - Reauditar fronteiras criticas
Fronteiras:
1. `004 -> 005`
2. `005 -> 006`
3. `006 -> 007`
4. `007 -> 008`
5. `009 -> 010`

Objetivo:
1. garantir que o patch nao embaralhou funcoes.

Criterio de aceite:
1. Ritual continua revelando local;
2. Jornada continua revelando guardia e movimento;
3. O Concreto continua sendo gesto central;
4. Narramos continua sendo reconto;
5. Fechamento continua fechando;
6. extensoes nao invadem formacao.

## T30 - Rodar sanity check de encoding
Comando alvo:
`rg -n "\xC3|\xC2|\xE2|\b\w+\?\w+\b" site/sementes/MV-S-00[0-9]*.html`

Objetivo:
1. garantir que o patch nao corrompeu encoding.

## T31 - Registrar log final desta rodada
Arquivo previsto:
1. `logs/2026.03.12/2026-03-12_EXECUCAO_INCREMENTAL_L003_POS_FEEDBACK_MARINA.md`

Objetivo:
1. registrar findings;
2. registrar o que foi executado;
3. fechar veredito honesto.

---

## 4) Ordem segura de execucao
1. `T00-T08`
2. `T09-T13`
3. `T14-T20`
4. `T21-T27`
5. `T28`
6. `T29-T31`

---

## 5) Riscos tecnicos desta rodada
1. simplificar demais a voz de Iris;
2. quebrar a atmosfera do Reino ao esclarecer comandos;
3. criar excesso de caixas novas e deixar a pagina cansada;
4. alterar listas e spacing de modo ruim no mobile;
5. resolver um trecho e criar repeticao verbal em outro.

Mitigacoes:
1. reutilizar classes existentes sempre que possivel;
2. criar no maximo o minimo de classes novas;
3. separar por funcao, nao por vaidade visual;
4. reler a secao inteira apos cada lote.

---

## 6) Definition of Done desta execucao
1. a Marina consegue ler a `L003` e entender melhor o que falar e fazer;
2. o encanto do Reino permanece;
3. a secao `Narramos Juntos` fica visivelmente mais modular;
4. os blocos de cor continuam ajudando a visualizacao;
5. `acender/respirar/nascer` deixam de atrapalhar em zonas operacionais;
6. nao ha regressao estrutural nem tecnica;
7. o resultado fica pronto para nova rodada curta de validacao humana.
