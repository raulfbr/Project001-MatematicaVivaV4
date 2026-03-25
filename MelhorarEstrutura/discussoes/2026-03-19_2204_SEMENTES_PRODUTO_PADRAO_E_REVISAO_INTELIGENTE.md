# DISCUSSAO - SEMENTES PRODUTO PADRAO E REVISAO INTELIGENTE

Data: 2026-03-19
Hora: 22:04
Tema: como melhorar a dinamica de produto e revisao de `Sementes` sem depender de releitura integral do HTML
Status: recomendacoes iniciais

## Leitura em 30 segundos

Esta foi a primeira discussao de abertura mais ampla desta trilha.

Saida principal:

- o problema nao e so "HTML grande"
- o problema e misturar produto, estrutura pedagogica e render final no mesmo artefato
- a melhor direcao inicial parecia ser `contrato de bloco + review pack por bloco`

Papel deste arquivo hoje:

- ele continua util como abertura de visao
- mas as decisoes mais especificas avancaram depois dele

Se voce estiver lendo em sequencia, o proximo arquivo mais importante e:

- `discussoes/2026-03-19_2223_CONTRATO_CANONICO_SEMENTES.md`

## 1) Pergunta central

Como transformar `Sementes` em um produto mais fiel ao `North Star` e, ao mesmo tempo, criar um sistema mais inteligente para revisar cada licao sem explodir contexto da IA nem cansar quem revisa?

## 2) Fontes de evidencia desta discussao

- `E1`: `LORE/north_star.yaml`
- `E2`: `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`
- `E3`: `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/009_TASTE_EDITORIAL_E_AUTORIA_HUMANA.md`
- `E4`: `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md`
- `E5`: `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml`
- `E6`: `MelhorarEstrutura/TASK_ROBUSTA_MELHORAR_ESTRUTURA.md`
- `E7`: `MelhorarEstrutura/TASK_ROBUSTA_APLICACAO_EXPERTS.md`
- `E8`: `https://matematicavivav4.vercel.app/` em 2026-03-19
- `E9`: `site/sementes/MV-S-004_A_ORDEM_DO_DIA.html` e `site/sementes/MV-S-006_O_DESENHO_DO_REI.html`
- `E10`: `logs/2026.03.13/2026-03-13_REVISAO_L004_TOPICO_A_TOPICO.md` e `logs/2026.03.10/2026-03-10_REVISAO_L006_TOPICO_A_TOPICO.md`

## 3) O que as evidencias estao dizendo

### 3.1 Produto

`E1`, `E2` e `E8` juntos mostram uma tensao importante:

- o `North Star` pede familia no centro, alivio para o adulto, encantamento para a crianca e clareza para conduzir
- mas a home publicada hoje ainda se apresenta como `Orchestrator Dashboard`, com linguagem mais interna do que familiar

Leitura:

O site atual consegue exibir o acervo, mas ainda nao encarna totalmente a promessa principal do produto para a familia final.

### 3.2 Estrutura das licoes

`E4`, `E5`, `E9` e `E10` mostram que `Sementes` ja tem um padrao muito forte e repetivel:

- Preparacao do Portador
- Ritual de Entrada
- Jornada
- Concreto
- Narramos Juntos
- Ritual de Fechamento
- Conexao da Jornada
- Sementes para o Dia
- Formacao do Portador

Leitura:

Isso e uma boa noticia. Quando um ciclo tem padrao forte, o sistema nao precisa reinventar a licao toda a cada arquivo. Ele precisa proteger o contrato desse padrao.

### 3.3 Gargalo de revisao

`E2`, `E4`, `E6`, `E7`, `E9` e `E10` apontam para o mesmo gargalo:

- hoje a revisao operacional real ainda pousa no HTML
- os problemas reais aparecem por bloco e por fronteira entre blocos
- mas o artefato que concentra a decisao ainda e grande demais

Leitura:

O custo de contexto nao esta vindo so do tamanho do HTML. Ele esta vindo de uma mistura de tres camadas no mesmo artefato:

1. produto e experiencia final
2. estrutura pedagogica da licao
3. renderizacao final publicada

## 4) Sugestao principal

Minha sugestao central nao e migrar imediatamente para muitos arquivos pequenos.

Minha sugestao central e criar uma camada intermediaria entre `fonte da licao` e `HTML final`:

`contrato de bloco + review pack por bloco`

Isso preserva o que hoje funciona e reduz o custo de revisao.

## 5) O que eu sugiro melhorar no produto

### 5.1 Separar superficie interna de superficie familiar

O site atual parece misturar:

- painel interno
- biblioteca de licoes
- experiencia de descoberta da familia

Sugestao:

- manter uma superficie interna tipo dashboard para operacao e governanca
- criar uma superficie familiar mais clara para `Sementes`

Sinais disso em `E8`:

- `Orchestrator Dashboard`
- `Ambiente: Production (Forge V3)`
- `Configuracoes`

Esses elementos fazem sentido para operacao, mas nao sao a melhor entrada para a familia pioneira.

### 5.2 Fazer o padrao de `Sementes` aparecer como valor do produto

Hoje a familia ve cards de licoes, mas ainda nao ve com clareza:

- como toda licao funciona
- por que o metodo acalma o adulto
- o que se repete de forma segura

Sugestao:

na area de `Sementes`, mostrar um bloco fixo:

- `Toda licao de Sementes segue este ritmo`
- preparo rapido
- ritual curto
- descoberta concreta
- narracao
- continuidade leve em casa

Isso conversa diretamente com `E1`, `E2` e `E4`.

### 5.3 Deixar o beneficio para o Portador mais explicito

O `North Star` insiste em:

- reduzir culpa
- aliviar pressao
- permitir ler e conduzir ao mesmo tempo

Sugestao de produto:

cada card de licao ou pagina de licao poderia mostrar, de forma muito curta:

- tempo de preparo
- materiais essenciais
- gesto central da licao
- o que a crianca vai descobrir
- o que o Portador precisa fazer primeiro

Isso aproxima o produto do `abra e faca`.

### 5.4 Organizar `Sementes` por arco, nao so por lista

Os guardioes evoluem, o curriculo espirala e o ciclo tem uma caminhada.

Sugestao:

- manter a navegacao por licao
- mas tambem explicitar pequenos arcos de progresso dentro de `Sementes`

Exemplo:

- inicio do Reino
- quantidades pequenas e ordem
- formas e reconhecimento
- pares e correspondencia
- caminho ate o dez

Isso ajuda a familia a sentir progressao e ajuda a revisao editorial a respeitar a espiral.

## 6) O que eu sugiro melhorar na estrutura editorial

### 6.1 Criar um contrato canonico de padrao por ciclo

Hoje ja existe um padrao forte, mas ha drift de naming e de ordem entre:

- template
- HTML
- forma de pensar da equipe
- prompts de revisao

Exemplo da propria conversa:

- voce trouxe uma ordem com `006_MOMENTO_DE_CONEXAO`
- o contrato e o HTML atual usam `O Concreto`

Isso e um sinal de que o padrao existe, mas ainda nao esta congelado como contrato simples e inevitavel.

Sugestao:

para cada ciclo, ter um arquivo proprio de padrao:

- `Sementes`
- `Raizes 1`
- `Raizes 2`
- etc

Cada um define:

- ids canonicos dos blocos
- ordem editorial
- funcao do bloco
- o que pertence ao bloco
- perguntas minimas de QA do bloco

### 6.2 Nao quebrar a licao inteira em muitos arquivos agora

Minha recomendacao hoje nao e:

- um arquivo por frase
- um arquivo por cena
- um arquivo por microacao

Porque isso conflitaria com `E2`, `E3`, `E4` e `E10`, que pedem:

- paz para o adulto
- texto que sai da boca
- menos traducao mental

Sugestao:

manter a fonte em uma unidade razoavel por licao no curto prazo, mas gerar artefatos menores para revisao.

### 6.3 Criar `review packs` por bloco

Esta e a sugestao mais forte desta discussao.

Em vez de revisar o HTML inteiro, gerar um pacote de revisao por bloco contendo apenas:

- metadados essenciais da licao
- resumo da licao anterior e da proxima
- guardiao e imagem dominante
- bloco alvo
- fronteira anterior e posterior
- perguntas de `North Star`, `TX10` e `TASTE` aplicaveis ao bloco
- texto atual do bloco
- campo para decisao

Exemplo de review packs para uma licao:

- `003_preparacao_portador.review.md`
- `004_ritual_entrada.review.md`
- `005_jornada.review.md`
- `006_concreto.review.md`
- `007_narramos_juntos.review.md`
- `008_ritual_fechamento.review.md`
- `009_conexao_jornada.review.md`
- `010_sementes_dia.review.md`
- `011_formacao_portador.review.md`

Isso reduziria muito o contexto necessario para a IA e para a revisao humana.

### 6.4 Manter o HTML como gate final, nao como unica superficie

No curto prazo, eu nao removeria o HTML do processo.

Mas eu mudaria a funcao dele:

- antes: lugar principal de revisao editorial
- depois: lugar de validacao final de fluidez, costura e visual

Isso respeita a verdade operacional atual sem deixar o HTML mandar sozinho em tudo.

## 7) Sistema recomendado para `Sementes` agora

### Camada 1 - Padrao do ciclo

Um contrato simples de `Sementes` dizendo:

- quais blocos existem
- qual a ordem
- qual a funcao de cada um
- quais transversais pesam mais em cada bloco

### Camada 2 - Fonte da licao

Continuar com uma fonte razoavel por licao no curto prazo.

O importante agora nao e trocar o formato por trocar.
O importante agora e a fonte obedecer ao contrato.

### Camada 3 - Review pack gerado

Gerar automaticamente um markdown por bloco para revisao.

Este artefato seria o melhor lugar para:

- IA discutir
- humano revisar
- registrar decisao

### Camada 4 - HTML final

Usar para:

- leitura corrida
- checagem de fronteiras
- confirmacao de voz
- validacao visual e navegacao

## 8) O que isso prepara para os outros anos

Seu instinto aqui esta certo:

se cada ano ou ciclo tiver padrao forte, o sistema precisa crescer por `contratos de ciclo`, nao por improviso licao a licao.

Modelo sugerido:

- um `padrao canonico por ciclo/ano`
- varias licoes que instanciam esse padrao
- review packs gerados segundo o padrao daquele ciclo

Assim:

- `Sementes` hoje vira o primeiro caso maduro
- `Raizes` depois reaproveita a governanca, mudando o contrato
- a IA nao precisa reaprender o sistema inteiro a cada fase

## 9) Sugestao de prompt melhorado para discussao estrutural

```text
Use como fontes obrigatorias:
- LORE/north_star.yaml
- TX08 North Star Operacional
- TX09 Taste Editorial e Autoria Humana
- TX10 Lente de Encantamento Encarnado e Revelacao Matematica
- TEMPLATE canonico do ciclo atual
- tarefa robusta vigente
- licao ou bloco alvo

Contexto obrigatorio:
- hoje a revisao operacional real ainda acontece no HTML
- o objetivo nao e redesenhar toda a plataforma
- o foco atual e Sementes
- a prioridade e reduzir carga mental de revisao sem perder fidelidade editorial

Sua tarefa:
- diagnosticar a tensao principal entre produto, estrutura e revisao
- separar fato observado de inferencia
- propor o menor recorte util para melhorar
- respeitar o North Star: aliviar o adulto, encantar a crianca, preservar a matematica e a voz do Reino

Nao faca:
- nao proponha backend stateful como resposta default
- nao proponha fragmentacao excessiva
- nao trate HTML como se ja nao fosse a superficie real atual

Entregue:
1. diagnostico
2. tensoes reais
3. recomendacao principal
4. riscos
5. proximo passo
```

## 10) Sugestao de prompt melhorado para revisao por bloco

```text
Revise apenas o bloco informado, nao a licao inteira.

Bloco alvo:
[nome do bloco]

Use como criterio:
- North Star Operacional
- TX10 Encantamento Encarnado
- Taste Editorial
- funcao canonica do bloco no ciclo Sementes

Considere tambem:
- licao anterior e proxima
- guardiao da licao
- imagem dominante
- fronteira com o bloco anterior e o seguinte

Objetivo:
- reduzir traducao mental do Portador
- preservar a dignidade da crianca
- manter concretude forte
- garantir que narrativa e instrucao nao virem linguagens concorrentes

Entregue:
1. o que esta forte
2. onde ha friccao
3. se o problema e de tom, funcao, gesto, ordem ou clareza
4. patch sugerido apenas para este bloco
5. risco residual

Restricao:
- nao reescreva outros blocos
- nao proponha mudancas fora do escopo sem marcar como observacao
```

## 11) Recomendacao final desta discussao

Se eu tivesse que escolher a menor mudanca de maior impacto agora, seria esta:

1. congelar o contrato canonico de `Sementes`
2. gerar `review packs` por bloco
3. usar o HTML apenas como validacao final e checagem de costura
4. separar melhor a face interna do sistema da face familiar do produto

## 12) Proximo arquivo sugerido

Tema:

`CONTRATO_CANONICO_SEMENTES_E_REVIEW_PACKS`

Pergunta:

quais ids, ordem, funcoes e gates minimos cada bloco de `Sementes` precisa ter para podermos gerar um review pack inteligente?
