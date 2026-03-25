# ROUND 02 - BLOCO MINIMO

Data: 2026-03-19
Fase: bloco minimo
Status: decisao provisoria

## 1) Pergunta da rodada

Qual e a menor unidade de bloco que continua pedagogicamente inteligivel e operacionalmente revisavel?

## 2) Evidencias usadas

- `R0`: `rodadas/ROUND_00_DIAGNOSTICO.md`
- `R1`: `rodadas/ROUND_01_DISCUSSAO_INICIAL.md`
- `E1`: `apps/web/lib/contracts/lesson-structure.ts` ja nomeia um contrato por blocos com `hero`, `preparacao_portador`, `ritual_entrada`, `jornada`, `concreto`, `narramos_juntos`, `fechamento`, `estrategias`, `formacao_portador` e `auditoria_qa`
- `E2`: `curriculo/01_SEMENTESV6/002_PEDRAS_FORTALEZA.yaml`, `004_A_ORDEM_DO_DIA.yaml`, `006_O_DESENHO_DO_REI.yaml` e `008_O_PAR_PERFEITO.yaml` mostram que a licao real ja vem agrupada em macro-partes como `para_portador`, `ritual_abertura`, `jornada`, `narracao`, `ritual_fechamento`, `para_familia` e `auditoria_qa`
- `E3`: `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`, `MV-S-004_A_ORDEM_DO_DIA.html`, `MV-S-006_O_DESENHO_DO_REI.html` e `MV-S-008_O_PAR_PERFEITO.html` repetem uma ordem estavel de secoes como `Preparacao do Portador`, `Ritual de Entrada`, `A Jornada`, `O Concreto`, `Narramos Juntos`, `Ritual de Fechamento`, `Conexao da Jornada`, `Sementes para o Dia` e `Formacao do Portador`
- `E4`: `logs/2026.03.13/2026-03-13_REVISAO_L004_TOPICO_A_TOPICO.md` revisa a licao inteira por topicos `001-012` e registra fronteiras criticas entre blocos, especialmente `006 -> 007`
- `E5`: `logs/2026.03.10/2026-03-10_REVISAO_L006_TOPICO_A_TOPICO.md` mostra uma licao forte no macro, com patch pequeno e localizado em `Formacao do Portador`, sem reescrita ampla de `Jornada` ou `O Concreto`
- `E6`: `docs/MAPA_EXECUCAO_PROJETO.md`, `build/fases/sementes.py` e `vercel.json` confirmam que a publicacao continua em build estatico para Vercel, o que favorece simplificacao editorial e nao atomizacao excessiva por runtime

## 3) Fatos observados antes da discussao

- `E1`, `E2` e `E3` apontam para a mesma direcao: o projeto ja pensa a licao em macro-blocos estaveis, mesmo com nomes ainda desalinhados entre piloto, YAML e HTML
- `E2` mostra que cenas e passos ja existem hoje, mas como estrutura interna de `jornada` e `concreto`, nao como unidades principais de contrato
- `E3`, `E4` e `E5` mostram que a revisao real ja pousa em secoes reconheciveis no HTML, nao em paragrafos soltos
- `E4` e `E5` mostram que os problemas mais relevantes aparecem ou dentro de um macro-bloco inteiro, ou na fronteira entre dois macro-blocos

Leitura consolidada:

A pergunta desta rodada nao e "qual e o menor pedaco possivel". A pergunta correta e "qual e o menor pedaco que ainda preserva sentido pedagogico e reduz releitura".

## 4) Posicao inicial dos experts

### Estrategista de Estrutura

`R1`, `E2` e `E3` mostram que a licao ja tem ossatura suficiente para ser tratada por macro-blocos. Quebrar cedo demais em cenas ou passos criaria um segundo sistema de detalhe antes de validar a fronteira principal.

### Vercel First

`E6` pesa contra qualquer desenho que precise de pecas pequenas demais para funcionar. Vercel nao proibe multi-arquivo, mas tambem nao pede microfragmentacao para resolver um problema que hoje e editorial. O bloco minimo precisa ser pequeno para revisar, nao pequeno por ideologia.

### Contrato de Licao

`E1` e `E2` indicam que `jornada` e `concreto` ja sao blocos com identidade propria. Cenas da Jornada e passos do Concreto podem existir como subestrutura, mas ainda nao se provaram como unidade principal de revisao. O candidato mais forte e o macro-bloco pedagogico.

### Revisao Escalavel

`E4` e `E5` mostram que a equipe ja revisa melhor quando pensa por topicos amplos e fronteiras criticas. Se a discussao for quebrada em cenas por padrao, a carga mental pode cair numa armadilha nova: menos linhas por arquivo, mas mais arquivos por licao.

### Mae Regente Real

`E3`, `E4` e `E5` apontam para um criterio simples: se para entender uma licao eu precisar abrir muitos pedacos pequenos antes de agir, a estrutura perdeu. A unidade boa precisa ser clara o bastante para eu ler um bloco e saber o que mudou.

## 5) Tensoes reais

### Tensao 1 - `jornada` fica inteira ou vira cenas?

- a favor de quebrar: cenas sao menores e parecem mais faceis de revisar
- contra quebrar: `E2`, `E4` e `E5` mostram que a inteligibilidade da Jornada depende do arco inteiro e da ponte com `O Concreto`

Leitura dos experts:

- `contrato_licao`: cena e boa como submapa interno, mas fraca como unidade principal porque perde o fio narrativo
- `revisao_escalavel`: se surgir um problema localizado, a equipe pode entrar na cena como lupa; isso nao obriga promover cena a bloco canonicamente revisavel
- `mae_regente_real`: revisar "Cena 2" sem lembrar a chegada, o guardiao e a saida para o concreto tende a aumentar traducao mental

### Tensao 2 - `concreto` fica inteiro ou vira passos?

- a favor de quebrar: os passos ja existem em `instrucoes_portador` em `E2`
- contra quebrar: `E5` mostra que o valor do Concreto esta na atividade como experiencia completa, com material, fala, variacao e ponte para narracao

Leitura dos experts:

- `estrategista_estrutura`: passo e checklist interno, nao fronteira principal
- `revisao_escalavel`: revisar passo por passo como default faria o time perder a visao da atividade inteira
- `mae_regente_real`: quem usa a licao precisa saber "o que vamos fazer aqui", nao reconstruir a atividade a partir de quatro microblocos

### Tensao 3 - `Conexao da Jornada`, `Sementes para o Dia` e `Formacao do Portador` sao blocos reais ou anexos?

- a favor de tratar como anexos: parecem camadas de apoio, nao o nucleo da experiencia da crianca
- contra tratar como anexos: `E3`, `E4` e `E5` mostram que eles reaparecem de forma estavel no HTML e nos logs, carregando continuidade curricular e traducao para o adulto

Leitura dos experts:

- `contrato_licao`: sao blocos reais de revisao, mesmo que a fonte upstream deles ainda esteja espalhada
- `estrategista_estrutura`: esta e uma pista importante para a `ROUND 03`; ha blocos reais no HTML que ainda nao estao nomeados com a mesma clareza no contrato
- `vercel_first`: isso nao pede backend nem runtime novo; pede contrato melhor

### Tensao 4 - `hero`, header e navegacao entram no mesmo nivel dos blocos pedagogicos?

- a favor: aparecem em todas as licoes e afetam leitura
- contra: `E3`, `E4` e `E5` sugerem que eles funcionam mais como moldura de publicacao do que como unidade editorial da licao

Leitura dos experts:

- `estrategista_estrutura`: `hero` continua importante, mas convem separa-lo como bloco de shell/publish
- `revisao_escalavel`: header e navegacao devem continuar auditados, sem disputar o mesmo espaco mental dos blocos pedagogicos
- `mae_regente_real`: quem revisa conteudo precisa saber o que e "miolo da licao" e o que e "moldura"

## 6) Consensos provisorios

- a menor unidade revisavel desta fase e o macro-bloco pedagogico, nao a cena e nao o paragrafo
- `jornada` continua inteira como bloco principal; cenas viram subestrutura interna quando necessario
- `concreto` continua inteiro como bloco principal; passos viram checklist interno quando necessario
- `Conexao da Jornada`, `Sementes para o Dia` e `Formacao do Portador` devem continuar tratados como blocos reais de revisao no fluxo atual
- `hero` deve continuar existindo, mas como camada de shell/publish, nao como a principal unidade da discussao pedagogica
- header superior e navegacao inferior precisam seguir auditados, mas fora do nucleo do contrato pedagogico

## 7) Matriz preliminar do bloco minimo

| unidade canonica provisoria | papel nesta fase | observacao |
| --- | --- | --- |
| `hero` | shell obrigatorio | existe sempre, mas nao lidera a discussao pedagogica |
| `preparacao_portador` | bloco obrigatorio | hoje aparece como secao estavel no HTML e como `para_portador` no YAML |
| `ritual_entrada` | bloco obrigatorio | hoje aparece com naming drift para `ritual_abertura` no YAML |
| `jornada` | bloco obrigatorio | permanece inteiro; cenas ficam internas |
| `concreto` | bloco obrigatorio | permanece inteiro; passos ficam internos |
| `narramos_juntos` | bloco obrigatorio | hoje conversa com `narracao` no YAML |
| `fechamento` | bloco obrigatorio | hoje aparece como `ritual_fechamento` no YAML |
| `conexao_jornada` | bloco obrigatorio no fluxo de revisao | precisa mapeamento melhor na `ROUND 03` |
| `sementes_do_dia` | bloco obrigatorio no fluxo de revisao | precisa mapeamento melhor na `ROUND 03` |
| `formacao_portador` | bloco obrigatorio no fluxo de revisao atual | precisa mapeamento melhor na `ROUND 03` |
| `auditoria_qa` | bloco obrigatorio | segue como gate tecnico-editorial |

## 8) Decisao provisoria

Fatos observados:

- `E1` mostra que o piloto ja pensa em blocos maiores que paragrafo
- `E2` mostra que cenas e passos ja existem, mas aninhados
- `E3`, `E4` e `E5` mostram que a revisao humana real acontece melhor em macro-secoes e em fronteiras entre elas
- `E6` mostra que a restricao principal do curto prazo nao e runtime, e sim clareza editorial compativel com build estatico

Inferencia:

A melhor aposta para o projeto agora e assumir como unidade revisavel principal o macro-bloco pedagogico. Esse recorte e pequeno o bastante para reduzir contexto e grande o bastante para preservar sentido.

Decisao desta rodada:

- `jornada` fica inteira no contrato preliminar
- `concreto` fica inteiro no contrato preliminar
- cenas e passos nao viram blocos canonicos nesta fase
- o fluxo de revisao deve considerar como blocos reais, alem do nucleo pedagogico, `conexao_jornada`, `sementes_do_dia` e `formacao_portador`
- `ROUND 03` deve resolver o mapeamento entre bloco real de revisao e fonte upstream, porque hoje parte desse bloco ainda esta espalhada entre YAML, template e HTML

## 9) Perguntas em aberto

- onde exatamente `conexao_jornada`, `sementes_do_dia` e `formacao_portador` vivem na futura fronteira de contrato?
- `hero` deve ser modelado como bloco de conteudo ou bloco de publish?
- quais aliases oficiais precisamos aceitar para conviver com `para_portador`, `ritual_abertura`, `narracao` e `ritual_fechamento` sem criar ambiguidade?
- qual e a menor matriz de campos que permite revisar um bloco sem reabrir a licao inteira?
- como o HTML continua operando no curto prazo sem voltar a virar fonte unica de verdade?
