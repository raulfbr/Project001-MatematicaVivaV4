# REVISAO TOPICO A TOPICO - L013
Data: 2026-03-16
Licao: `MV-S-013_O_RIO_QUE_SE_UNE.html`
Status da sessao: reauditoria de fechamento concluida
Escopo congelado: revisar apenas a `L013`; `L012` e `L014` entram apenas como fronteiras curriculares
Validacao humana da familia: pendente

---

## 1) Cerne macro da licao
1. `TGTB ref`: `000-L13 - Plus and Equals Signs / Sinais de Mais e Igual`
2. `Guardiao`: `Melquior`
3. `Promessa da licao`: a crianca descobrir que `+` significa juntar e `=` significa o resultado da uniao, por meio de uma historia concreta.
4. `Lugar`: `Jardim Central`
5. `Conceito vivo`: simbolos matematicos como linguagem de uma experiencia real, nao como decoracao abstrata.
6. `Papel no curriculo mestre`: introduzir `+` e `=` como reconhecimento visual de uma acao concreta ja vivida.
7. `Imagem dominante`: dois rios de pedras que se encontram e revelam um rio maior.
8. `Fruto do dia`: a crianca juntar dois grupos, contar o total e perceber que os sinais contam essa historia.
9. `Risco de fronteira`: a licao virar apresentacao fria de simbolos ou performance de leitura precoce.
10. `Risco familia real`: a mae precisar traduzir demais o momento de mostrar cards e separar acao de simbolo.
11. `Hospitalidade multi-crianca`: um irmao pode entregar um dos grupos enquanto a crianca principal junta e conta.

---

## 2) Fontes e lentes ativadas
1. HTML da licao `L013`
2. Licoes de fronteira `L012` e `L014`
3. Curriculo mestre `013_O_RIO_QUE_SE_UNE.yaml`
4. `023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
5. `003_PROTOCOLO_REVISAO_POR_LICAO.md`
6. `004_RUBRICA_PREMIUM_REVISAO.md`
7. `008_NORTH_STAR_OPERACIONAL.md`
8. `009_TASTE_EDITORIAL_E_AUTORIA_HUMANA.md`
9. Revisao anterior de `2026-03-10`

---

## 3) Diagnostico desta rodada
1. O coracao pedagógico da licao ja estava forte: concreto primeiro, simbolo depois.
2. A fronteira `L012 -> L013` segue boa: sai-se do feixe para a linguagem que conta uniao, sem abstração precoce.
3. A fronteira `L013 -> L014` continua honesta: o `+` prepara o celeiro que cresce sem invadir a proxima licao.
4. O `North Star` segue preservado no tema e na pedagogia.
5. O problema desta rodada era de contrato de interface e de gramatica ritual: ainda havia marcadores legados no HTML visivel.

---

## 4) Findings objetivos encontrados
1. `Ritual de Entrada` ainda usava o label `Lugar revelado`, em vez de instruir claramente a mae.
2. Ainda havia `Sussurro do Portal` em licao comum, o que contraria a gramatica ritual atual.
3. A primeira cena da Jornada ainda estava sem reveal moderno do guardiao e com naming de cena mais legado.
4. `Conexao da Jornada` ainda usava `journey-connection-card`.
5. A navegacao inferior ainda usava `lesson-footer-nav` e `lesson-footer-link`.
6. O fechamento ainda nao pousava na formula canonica `Respire fundo. A casa volta devagar.`.

---

## 5) Matriz topica `001-012`
1. `001_BASE_E_HERO` -> `PASS`
2. `002_HEADER_SUPERIOR` -> `PASS`
3. `003_PREPARACAO_DO_PORTADOR` -> `PASS`
4. `004_RITUAL_DE_ENTRADA` -> `PASS`
5. `005_A_JORNADA` -> `PASS`
6. `006_O_CONCRETO` -> `PASS`
7. `007_NARRAMOS_JUNTOS` -> `PASS`
8. `008_RITUAL_DE_FECHAMENTO` -> `PASS`
9. `009_CONEXAO_DA_JORNADA` -> `PASS`
10. `010_SEMENTES_PARA_O_DIA` -> `PASS`
11. `011_FORMACAO_DO_PORTADOR` -> `PASS`
12. `012_NAVEGACAO_INFERIOR` -> `PASS`

---

## 6) Fronteiras criticas
1. `004 -> 005` -> `PASS`
O Ritual entrega o Jardim antes de Melquior revelar os dois rios.
2. `005 -> 006` -> `PASS`
A Jornada contempla a uniao; `O Concreto` entrega o gesto manual de juntar e so depois nomear os sinais.
3. `006 -> 007` -> `PASS`
O gesto vivido desemboca naturalmente no reconto.
4. `008 -> 009` -> `PASS`
O fechamento pousa antes da conexao abrir a proxima dobra.
5. `009 -> 010` -> `PASS`
`Conexao` sela a licao; `Sementes` abre prolongamentos leves.
6. `010 -> 011` -> `PASS`
O opcional domestico nao invade a formacao do adulto.

---

## 7) Patch aplicado
1. `Ritual de Entrada`
   ganhou `Card do lugar` claro para a mae e entrou na formula canonica `Respire fundo.`.
2. Label do card do local
   `Lugar revelado` -> `Mostre este card a crianca`.
3. `Sussurro do Portal`
   removido por contrariar a gramatica atual de licao comum.
4. Reveal da Jornada
   a primeira cena ganhou `journey-scene--reveal`, card visivel do Melquior e naming mais vivo.
5. Cena 2 e Cena 3
   titulos ajustados para formulacoes menos legadas e mais narrativas.
6. `Ritual de Fechamento`
   passou a pousar em `Respire fundo. A casa volta devagar.`
7. `Conexao da Jornada`
   saiu de `journey-connection-card` e foi convertida para `instruction-box` + `connection-link-card`.
8. `Navegacao inferior`
   saiu de `lesson-footer-nav` e foi alinhada a `lesson-nav`.

---

## 8) Sanity checks
1. `Lugar revelado`: ausente
2. `Sussurro do Portal`: ausente
3. `ritual-whisper-box`: ausente
4. `journey-connection-card`: ausente
5. `lesson-footer-nav`: ausente
6. `lesson-footer-link`: ausente
7. `Mostre este card a crianca`: presente em entidades no Ritual e no reveal da Jornada
8. `Respire fundo.`: presente no Ritual
9. `A casa volta devagar`: presente no fechamento
10. Leitura explicita em UTF-8 confirmou links corretos para `L012` e `L014`

---

## 9) Juizes consultados
1. `North Star Operacional`: aprova porque a mae agora recebe instrucoes mais claras sem perda de nobreza.
2. `TASTE`: aprova porque a imagem dos rios continua viva, mas com menos traducao mental.
3. `Susan Macaulay + Mae Ansiosa`: aprovam a troca de labels e a eliminacao de componentes legados que sobrecarregavam a leitura.
4. `Charlotte Mason + Jerome Bruner`: aprovam a preservacao da ordem correta `acao concreta -> simbolo`.

---

## 10) Veredito sincero
1. `L013` fecha esta rodada em `PASS PREMIUM`.
2. Aqui houve patch real, mas disciplinado: contrato visual e ritual foram alinhados sem reescrever o coracao da licao.
3. O ganho principal foi reduzir traducao mental da mae e devolver a pagina ao canone atual.

---

## 11) Risco residual
1. validacao humana com familia real continua sendo o proximo gate fora da IA;
2. os logs desta data ainda podem exibir ruido de encoding no terminal, mesmo quando o HTML esta correto.
