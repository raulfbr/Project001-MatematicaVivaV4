# DISCUSSAO - FLUXO EDITORIAL DE SEMENTES

Data: 2026-03-19
Hora: 22:28
Tema: definir em que ordem o time deve passar por contrato, bloco, HTML e validacao final
Status: recomendacao provisoria

## Leitura em 30 segundos

Decisao provisoria deste arquivo:

- o HTML continua sendo a realidade operacional de curto prazo
- mas ele nao precisa continuar sendo a primeira superficie de pensamento para toda pergunta
- o fluxo mais promissor ate aqui e:
  `macro -> contrato -> review pack -> patch HTML localizado -> costura HTML -> rubrica -> validacao humana`

Papel deste arquivo hoje:

- fechar a melhor sequencia editorial provisoria para esta fase
- preparar a proxima discussao sobre produto publicado

Se voce estiver retomando a trilha, o proximo tema sugerido e:

- `PRODUTO_PUBLICADO_E_SUPERFICIES`

## 1) Pergunta central

Se hoje a revisao real ainda acontece no HTML, qual e o melhor fluxo editorial para:

- preservar a forca do protocolo canonico
- reduzir custo de contexto para IA e para humano
- manter a costura da licao inteira
- nao inventar uma plataforma paralela
- preparar um caminho mais inteligente para `Sementes`

## 2) Fontes de evidencia

- `E1`: `TASK_ROBUSTA_CONVERGENCIA_SUGESTAO_SEMENTES.md`
- `E2`: `discussoes/2026-03-19_2223_CONTRATO_CANONICO_SEMENTES.md`
- `E3`: `discussoes/2026-03-19_2225_ANATOMIA_DO_REVIEW_PACK_POR_BLOCO.md`
- `E4`: `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
- `E5`: `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
- `E6`: `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
- `E7`: `logs/2026.03.13/2026-03-13_REVISAO_L004_TOPICO_A_TOPICO.md`
- `E8`: `logs/2026.03.10/2026-03-10_REVISAO_L006_TOPICO_A_TOPICO.md`
- `E9`: `docs/MAPA_EXECUCAO_PROJETO.md`

## 3) Fatos observados

### 3.1 O protocolo canonico ja tem uma boa ordem de pensamento

`E4` e `E5` mostram que o sistema atual nao e caos puro.

Pelo contrario, ele ja protege uma sequencia forte:

- ativacao e leitura minima
- congelamento de escopo
- cerne macro
- matriz `001-012`
- auditoria de fronteiras
- patch estrutural
- patch narrativo
- patch pedagogico
- radiacao local
- reauditoria
- validacao final

Leitura:

o maior problema atual nao e "falta de ordem mental".
O maior problema atual e "toda essa ordem ainda descarrega cedo demais no HTML inteiro".

### 3.2 O HTML hoje cumpre funcoes demais ao mesmo tempo

`E5`, `E7` e `E8` mostram que o HTML atual esta sendo usado como:

- superficie de leitura
- superficie de diagnostico
- superficie de patch
- superficie de auditoria de fronteiras
- superficie de validacao visual
- superficie final publicada

Leitura:

isso explica por que a revisao fica cara.
Um unico artefato esta carregando quase todo o trabalho editorial.

### 3.3 A rubrica ja trata validacao como etapa tardia

`E6` e claro: a pontuacao premium so deve acontecer depois de:

- cerne macro
- matriz completa
- fronteiras auditadas
- passada premium
- radiacao local
- passada final

Leitura:

isso e bom.
Significa que o proprio sistema atual ja sabe que "avaliar cedo demais" gera falso conforto.

### 3.4 Os logs mostram que existe uma diferenca real entre revisar e validar

`E7` e `E8` mostram um padrao repetido:

- primeiro vem o diagnostico e a matriz
- depois o patch
- depois a reauditoria
- so entao vem o veredito

Em `L006`, `E8` ainda explicita que a licao estava pronta para futura validacao humana, mesmo sem uma nova rodada de patch.

Leitura:

ja existe, na pratica, uma diferenca entre:

- trabalho editorial
- gate de fechamento
- validacao humana

O fluxo ideal precisa deixar isso mais claro, nao mais confuso.

### 3.5 O repo ja permite melhorar o processo sem trocar a infra

`E9` mostra que o projeto hoje opera com build estatico e publish simples.

Leitura:

isso ajuda muito.
Melhorar o fluxo editorial nao exige mudar Vercel nem reescrever a stack nesta fase.

## 4) Tensoes reais

### Tensao 1 - HTML-first puro ou fluxo em camadas?

- a favor de `HTML-first puro`: zero mudanca de operacao
- contra: custo de contexto continua alto e a IA segue pensando em markup cedo demais

### Tensao 2 - review pack antes do patch ou patch direto?

- a favor de patch direto: mais rapido em casos obvios
- contra: reabre o arquivo inteiro e mistura diagnostico com reescrita

### Tensao 3 - humano entra so no fim ou tambem no meio?

- a favor de so no fim: menos interrupcao
- contra: certas decisoes de tom, clareza oral e carga mental sao humanas demais para serem empurradas inteiras para o final

### Tensao 4 - um fluxo so para tudo ou dois tempos?

- a favor de um fluxo unico: mais simples
- contra: nao distingue a realidade de hoje do alvo de amanha

## 5) Leitura dos experts

### 5.1 `estrategista_estrutura`

Leitura:

`E4` e `E5` mostram que ja existe um esqueleto bom.
Logo, o melhor caminho nao e demolir o processo, mas separar melhor as superficies.

Posicao:

- proteger a ordem `macro -> bloco -> costura -> gate`
- impedir que a equipe volte a pensar direto no HTML inteiro para qualquer decisao
- nao criar um segundo sistema operacional paralelo nesta fase

### 5.2 `vercel_first`

Leitura:

`E9` mostra que o deploy atual nao exige mexida para melhorar a discussao editorial.

Posicao:

- qualquer melhoria agora deve nascer fora da infra
- `review pack` e contrato editorial sao seguros porque nao exigem novo runtime
- HTML pode continuar como realidade operacional de curto prazo sem travar a melhoria do metodo

### 5.3 `contrato_licao`

Leitura:

`E2` definiu o contrato canonico e `E3` definiu o pacote minimo por bloco.

Posicao:

- antes de patchar, a equipe precisa saber "qual bloco esta em jogo" e "qual e a funcao dele"
- sem essa nomeacao, a revisao vira prosa boa sem fronteira clara
- a costura entre blocos precisa ser revisada como objeto proprio

### 5.4 `revisao_escalavel`

Leitura:

`E3`, `E7` e `E8` mostram que muito retrabalho nasce porque a mesma leitura serve para tudo.

Posicao:

- IA deve entrar primeiro no macro e depois em packs menores
- HTML inteiro deve voltar com peso total apenas na costura final
- a unidade normal de trabalho precisa ser "bloco com fronteiras", nao "pagina inteira a cada pergunta"

### 5.5 `mae_regente_real`

Leitura:

`E4`, `E5`, `E6`, `E7` e `E8` convergem num ponto: a mae sofre quando a formulacao exige traducao mental.

Posicao:

- o julgamento humano mais importante nao e "se o HTML esta bonito"
- o julgamento humano mais importante e "se eu consigo usar isso com voz natural e sem cansaco extra"
- por isso a validacao humana final continua necessaria

## 6) Hipoteses consideradas

### Hipotese A - manter fluxo atual e apenas caprichar nos prompts

Vantagem:

- menor mudanca imediata

Risco:

- o gargalo central permanece
- a IA continua gastando contexto no artefato errado cedo demais

### Hipotese B - fluxo em 4 superficies, mas com patch ainda no HTML

Superficies:

1. `macro da licao`
2. `review pack do bloco`
3. `HTML de trabalho`
4. `HTML final + rubrica + validacao humana`

Vantagem:

- respeita a realidade atual
- reduz releitura integral
- cria disciplina de pensamento antes do patch

Risco:

- exige mais rigor na selecao do bloco-alvo

### Hipotese C - migrar ja para fonte multi-arquivo e deixar HTML so para publish

Vantagem:

- melhor granularidade futura

Risco:

- muda coisa demais cedo demais
- pode misturar discussao editorial com migracao tecnica

## 7) Leitura consolidada

A melhor aposta agora e a `Hipotese B`.

Nao porque ela seja a forma final do sistema,
mas porque ela cria um fluxo melhor sem negar a verdade operacional de hoje.

Em outras palavras:

- o protocolo macro atual continua valido
- o bloco entra como unidade normal de revisao
- o HTML deixa de ser a primeira superficie de pensamento para toda pergunta
- o HTML continua sendo a superficie real de patch no curto prazo
- o HTML volta com forca total na costura e na validacao final

## 8) Recomendacao provisoria

### 8.1 O fluxo ideal de `Sementes` agora

O fluxo editorial recomendado para esta fase e:

1. `ativacao da sessao`
2. `congelamento de escopo`
3. `cerne macro da licao`
4. `confirmacao do contrato canonico da licao`
5. `selecao do bloco-alvo e da fronteira critica`
6. `leitura do review pack do bloco`
7. `diagnostico do bloco e da fronteira`
8. `patch no HTML atual`
9. `radiacao local para vizinhos imediatos`
10. `releitura do HTML na costura dos blocos tocados`
11. `rubrica premium e veredito`
12. `validacao humana final`

### 8.2 O que revisar antes do patch

Antes de qualquer reescrita, revisar:

- promessa da licao
- imagem dominante
- fruto do dia
- pergunta principal respondiveI
- frase de boca do Portador
- bloco-alvo
- fronteira anterior e posterior
- transversal obrigatoria quando houver abstracao ou ancora frouxa

Regra:

nao abrir o HTML inteiro como primeira resposta para uma duvida de bloco.

### 8.3 O que revisar durante o patch

Durante o patch, revisar:

- funcao do bloco
- clareza da transicao com o vizinho anterior
- clareza da transicao com o vizinho seguinte
- oralidade
- comando visivel
- risco de repeticao
- risco de vazamento de funcao

Regra:

o patch deve ser local primeiro.
Radiacao vem depois, com criterio.

### 8.4 O que revisar so no final

So no final revisar com peso total:

- scroll da pagina como experiencia inteira
- ordem e respiracao dos blocos
- navegacao superior e inferior
- consistencia visual
- mobile
- links
- rubrica dos 5 eixos
- gate de cobertura topica
- gate de fronteiras
- validacao humana de voz, leveza e usabilidade real

Leitura:

o HTML inteiro continua necessario.
Mas ele entra forte no fechamento, nao como unico campo de pensamento do inicio ao fim.

## 9) Quando a IA entra e quando o humano precisa julgar

### 9.1 Entradas fortes da IA

A IA ajuda mais em:

- formar o cerne macro
- tensionar contrato e fronteiras
- revisar o review pack do bloco
- propor patch localizado
- reauditar vizinhos imediatos
- fechar matriz e rubrica com disciplina

### 9.2 Julgamentos que continuam humanos

O humano deve pesar especialmente em:

- congelamento de escopo quando ha risco de deriva
- decisao sobre tom final quando ha duas versoes boas
- verificacao de voz natural do Portador
- checagem de carga mental real para a familia
- validacao final antes de tratar a licao como pronta

## 10) O papel de cada superficie

### 10.1 Superficie 1 - Macro da licao

Serve para:

- proteger o todo
- impedir patch cego

### 10.2 Superficie 2 - Review pack

Serve para:

- reduzir contexto
- concentrar a conversa no bloco certo
- explicitar fronteiras e perguntas

### 10.3 Superficie 3 - HTML de trabalho

Serve para:

- aplicar o patch real hoje
- verificar se o texto funciona dentro do produto existente

### 10.4 Superficie 4 - HTML final + rubrica + validacao humana

Serve para:

- costura final
- verificacao tecnica
- veredito premium
- decisao de prontidao

## 11) Mini protocolo operacional sugerido

Quando uma nova revisao de licao comecar, usar esta sequencia minima:

1. abrir `023`
2. preencher cerne macro
3. marcar blocos-alvo e fronteiras
4. abrir o review pack do primeiro bloco
5. discutir e diagnosticar
6. patchar o HTML
7. reler bloco tocado + vizinho anterior + vizinho seguinte
8. so depois reler a pagina inteira
9. fechar rubrica
10. registrar risco residual e pendencia humana

## 12) Sinais de que o fluxo esta errado

O fluxo deve ser considerado fora do trilho quando:

- a conversa volta a abrir a licao inteira para qualquer ajuste pequeno
- o bloco-alvo nao e nomeado
- a fronteira nao e discutida
- a IA comeca a reescrever antes de formar diagnostico
- o time usa a rubrica cedo demais
- a validacao humana vira formalidade vazia

## 13) Decisao provisoria

Para `Sementes`, o melhor fluxo editorial agora e:

`macro -> contrato -> review pack -> patch HTML localizado -> costura HTML -> rubrica -> validacao humana`

Esta formula respeita tres verdades ao mesmo tempo:

- o HTML ainda e a realidade operacional
- a unidade normal de revisao precisa ficar menor
- a validacao final continua pertencendo a um humano real

## 14) Proximo tema sugerido

O proximo debate mais natural e:

`PRODUTO_PUBLICADO_E_SUPERFICIES`

Pergunta:

se o metodo editorial ficar melhor, o que no site publicado precisa mudar para o produto soar mais como Matematica Viva para a familia e menos como painel interno?
