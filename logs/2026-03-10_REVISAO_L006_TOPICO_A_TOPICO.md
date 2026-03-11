# REVISAO L006 TOPICO A TOPICO
Data: 2026-03-10
Licao: `MV-S-006_O_DESENHO_DO_REI.html`
Metodo: `023` + `003` + `004` + `011_TOPICOS/001-012` + pacote transversal minimo `002/003/005/006/008`
Escopo congelado: revisar apenas `L006`, usando `L005` e `L007` como fronteiras curriculares; sem commit; sem push

---

## 1) Cerne macro da licao
1. `TGTB ref`: `000-L6 - Number Practice / Pratica de Numeros`.
2. `Tema principal / ideia viva`: `O Desenho do Rei` - sentir a curva perfeita do algarismo como se fosse o rastro de beleza que a Pardal ve na areia da praia.
3. `Guardiao`: `Iris`.
4. `Lugar`: `Ninho Mirante`.
5. `Conceito vivo`: perceber que cada numeral de `1` a `5` tem uma forma propria e que o corpo pode aprender esse caminho antes da escrita formal.
6. `Papel no curriculo mestre`: dar corpo e beleza ao reconhecimento dos numerais antes da ampliacao para `6` e `7`.
7. `Imagem dominante`: `galeria / assinatura / rastro / areia / caminho do numero`.
8. `Promessa da licao`: a crianca contempla, distingue e percorre formas numericas com o corpo e com os dedos.
9. `Fruto do dia`: a crianca reconhece, aponta ou percorre ao menos um caminho numerico com sentido.
10. `Risco de descaracterizacao`: a licao virar treino grafomotor seco ou pre-caligrafia escolar, perdendo a beleza da forma viva.
11. `Risco de fronteira`: `Jornada -> O Concreto` pode colapsar se o gesto no ar gastar toda a experiencia manual; `Conexao -> L007` precisa apontar para ampliacao da trilha sem roubar o tema da coroa.
12. `Risco familia real`: transformar reconhecimento de forma em exigencia de escrita bonita cedo demais.
13. `Hospitalidade multi-crianca`: um irmao menor pode repetir o gesto no ar ou escolher cartoes, sem deslocar o foco da crianca-alvo.

---

## 2) Diagnostico inicial
### Estado encontrado
1. arquivo esta amplamente alinhado ao contrato canonico atual;
2. estrutura, narrativa e fluxo dos blocos estao fortes;
3. nao ha residuos legados como `Ritual de Abertura`, `Atividade Concreta`, `Para a Familia` ou `div onclick`;
4. a leitura do terminal sugeriu encoding corrompido nos `hrefs` para `L005`, mas a extracao em UTF-8 confirmou que os links reais do arquivo estavam corretos;
5. `Formacao do Portador` estava boa, mas ainda pouco precisa na explicitacao do `TGTB ref`.

### Findings iniciais por severidade
#### Medios
1. `011_FORMACAO_DO_PORTADOR` com `Conexao TGTB` correta em espirito, mas imprecisa em referencia explicita ao passo curricular.
2. a sessao exigiu validacao adicional de encoding por causa de falso positivo do terminal na exibicao dos `hrefs`.

#### Baixos
1. `favicon.ico` segue como divida tecnica transversal do lote.

---

## 3) Matriz inicial `001-012`
1. `001_BASE_E_HERO` -> `PASS`
Motivo: base, hero e asset central estao coerentes com a licao.
2. `002_HEADER_SUPERIOR` -> `PASS`
Motivo: links reais em UTF-8 estao corretos; a corrupcao aparecia apenas na leitura do terminal.
3. `003_PREPARACAO_DO_PORTADOR` -> `PASS`
Motivo: preparacao robusta, concreta e leve.
4. `004_RITUAL_DE_ENTRADA` -> `PASS`
Motivo: ritual revela o lugar e protege o reveal de Iris para a Jornada.
5. `005_A_JORNADA` -> `PASS`
Motivo: jornadas e cenas distinguem contemplacao da forma e preparo do gesto corporal.
6. `006_O_CONCRETO` -> `PASS`
Motivo: atividade principal distinta da Jornada e bem amarrada.
7. `007_NARRAMOS_JUNTOS` -> `PASS`
Motivo: escuta e narracao alinhadas ao contrato.
8. `008_RITUAL_DE_FECHAMENTO` -> `PASS`
Motivo: fechamento sereno e digno.
9. `009_CONEXAO_DA_JORNADA` -> `PASS`
Motivo: memoria viva e teaser para `L007` estao bem costurados.
10. `010_SEMENTES_PARA_O_DIA` -> `PASS`
Motivo: bloco canonico completo e leve.
11. `011_FORMACAO_DO_PORTADOR` -> `GAP`
Motivo: precisa maior precisao na ancora `TGTB`.
12. `012_NAVEGACAO_INFERIOR` -> `PASS`
Motivo: links reais em UTF-8 estao corretos e coerentes com o topo.

---

## 4) Fronteiras criticas iniciais
1. `003 -> 004` -> `PASS`
Preparacao desemboca naturalmente no Ritual.
2. `004 -> 005` -> `PASS`
Ritual revela o lugar e a Jornada revela Iris no tempo correto.
3. `005 -> 006` -> `PASS`
Jornada contempla e ensaia no ar; `O Concreto` leva o dedo para a superficie real.
4. `006 -> 007` -> `PASS`
Ponte para narracao esta clara.
5. `008 -> 009` -> `PASS`
Fechamento pousa antes da conexao.
6. `009 -> 010` -> `PASS`
Conexao olha para amanha e `Sementes` abre continuidade leve.
7. `010 -> 011` -> `PASS`
`Sementes` e `Formacao` seguem bem separadas.
8. `011 -> 012` -> `PASS`
`Formacao` fecha antes da navegacao tecnica, e os links finais batem com o topo e com os arquivos reais.

---

## 5) Hipoteses de trabalho
1. a licao precisa de patch pequeno e cirurgico, nao de reescrita ampla;
2. o principal trabalho e explicitar melhor o `000-L6` na `Formacao do Portador`;
3. o falso positivo de encoding precisava ser encerrado com verificacao direta em UTF-8 para nao contaminar o status da licao.

---

## 6) Riscos residuais antecipados
1. como a pagina esta forte no macro, existe risco de subestimar defeito tecnico de navegação;
2. nao houve validacao visual em navegador ate aqui;
3. o lote vizinho pode continuar com drift de encoding em referencias cruzadas fora desta licao.

---

## 7) Revisao executada `001-012`
### `001_BASE_E_HERO` -> `PASS`
#### Confirmado
1. base do documento, hero e asset central estao coerentes com `O Desenho do Rei`;
2. a imagem dominante da forma viva do numero aparece desde a abertura.
#### Tensionado
1. nenhuma tensao suficiente para patch nesta camada.
#### Alterado
1. nenhum patch necessario.

### `002_HEADER_SUPERIOR` -> `PASS`
#### Confirmado
1. links reais para `L005` e `L007` estao corretos em UTF-8;
2. o selo central e a topologia de tres zonas continuam alinhados ao contrato.
#### Tensionado
1. a exibicao do terminal sugeriu corrupcao no `href`, mas a leitura direta do arquivo confirmou que o problema era apenas de visualizacao no shell.
#### Alterado
1. nenhum patch necessario.

### `003_PREPARACAO_DO_PORTADOR` -> `PASS`
#### Confirmado
1. foco, fio, materiais, descoberta, estrategia e nota de graca estao fortes;
2. a preparacao honra bem a transicao `L005 -> L006 -> L007`.
#### Tensionado
1. verifiquei especialmente se a pagina nao antecipava escrita bonita cedo demais; passou.
#### Alterado
1. nenhum patch necessario.

### `004_RITUAL_DE_ENTRADA` -> `PASS`
#### Confirmado
1. ritual revela `Ninho Mirante` e protege Iris para a Jornada;
2. tom contemplativo e respiravel.
#### Tensionado
1. nenhuma tensao relevante.
#### Alterado
1. nenhum patch necessario.

### `005_A_JORNADA` -> `PASS`
#### Confirmado
1. Iris aparece com voz propria e a Jornada encarna o tema como galeria, assinatura e caminho;
2. a progressao de cenas e clara e nao escolarizada.
#### Tensionado
1. a principal checagem foi garantir que o gesto no ar nao esgotasse `O Concreto`; a fronteira se manteve boa.
#### Alterado
1. nenhum patch necessario.

### `006_O_CONCRETO` -> `PASS`
#### Confirmado
1. atividade principal distinta da Jornada, com superficie real, variacoes e ponte clara para narracao;
2. a crianca toca a forma, nao apenas a observa.
#### Tensionado
1. a secao foi relida para confirmar que nao virou repeticao do gesto no ar da Jornada; passou.
#### Alterado
1. nenhum patch necessario.

### `007_NARRAMOS_JUNTOS` -> `PASS`
#### Confirmado
1. escuta, disparador, reconto, perguntas do coracao e formas legitimas de narracao estao fortes;
2. a licao honra o encontro com a forma, nao avalia caligrafia.
#### Tensionado
1. nenhuma tensao forte apos reauditoria.
#### Alterado
1. nenhum patch necessario.

### `008_RITUAL_DE_FECHAMENTO` -> `PASS`
#### Confirmado
1. fechamento sereno com Iris e retorno domestico real.
#### Tensionado
1. nenhuma tensao forte.
#### Alterado
1. nenhum patch necessario.

### `009_CONEXAO_DA_JORNADA` -> `PASS`
#### Confirmado
1. memoria viva e teaser para `L007` estao bem dosados;
2. link semantico correto para a proxima licao.
#### Tensionado
1. a fronteira `L006 -> L007` foi protegida sem antecipar a coroa inteira cedo demais.
#### Alterado
1. nenhum patch necessario.

### `010_SEMENTES_PARA_O_DIA` -> `PASS`
#### Confirmado
1. ancora `Escolha 1 ou 2` presente;
2. cinco movimentos canonicos presentes e distintos;
3. opcionalidade segue clara.
#### Tensionado
1. verifiquei se `Criacao` nao repetia literalmente `O Concreto`; passou por mudar o gesto e o material.
#### Alterado
1. nenhum patch necessario.

### `011_FORMACAO_DO_PORTADOR` -> `PASS`
#### Confirmado
1. ordem canonica das subsecoes preservada;
2. formacao quente, clara e ligada ao que a familia viveu.
#### Tensionado
1. faltava precisao explicita no `TGTB ref`.
#### Alterado
1. `Conexao TGTB` foi ajustada para explicitar `000-L6 - Number Practice / Pratica de Numeros`.

### `012_NAVEGACAO_INFERIOR` -> `PASS`
#### Confirmado
1. navegacao inferior bate com topo e com `Conexao da Jornada`;
2. links reais para `L005` e `L007` estao corretos.
#### Tensionado
1. o mesmo falso positivo de encoding do terminal precisou ser descartado aqui tambem.
#### Alterado
1. nenhum patch necessario.

---

## 8) Fronteiras criticas finais
1. `003 -> 004` -> `PASS`
Preparacao desemboca naturalmente no Ritual.
2. `004 -> 005` -> `PASS`
Ritual revela o lugar e a Jornada revela Iris no tempo certo.
3. `005 -> 006` -> `PASS`
Jornada contempla e ensaia no ar; `O Concreto` leva o gesto para a superficie real.
4. `006 -> 007` -> `PASS`
a experiencia concreta vira linguagem com ponte clara.
5. `008 -> 009` -> `PASS`
o fechamento pousa antes da conexao olhar para amanha.
6. `009 -> 010` -> `PASS`
Conexao projeta; `Sementes` prolonga com leveza.
7. `010 -> 011` -> `PASS`
opcionalidade pratica e leitura formativa do adulto permanecem distintas.
8. `011 -> 012` -> `PASS`
Formacao fecha antes da navegacao tecnica, sem ruido.

---

## 9) Matriz final `001-012`
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

## 10) Sanity checks finais
1. busca por residuos legados nao encontrou `\[Foco:\]`, `Ritual de Abertura`, `Atividade Concreta`, `Para a Familia` nem `div onclick`;
2. parser HTML simples retornou `OK`;
3. leitura direta em UTF-8 confirmou que os `hrefs` para `L005` e `L007` estao corretos;
4. `Conexao TGTB` agora explicita `000-L6 - Number Practice / Pratica de Numeros`.

---

## 11) Veredito honesto
### O que ficou impecavel
1. a licao ja estava forte estrutural e narrativamente, e continua assim;
2. `Jornada`, `O Concreto`, `Narramos` e `Formacao` cumprem papeis distintos e bem costurados;
3. a ancora curricular agora ficou mais precisa.

### O que ainda ficou em risco
1. nao houve validacao visual em navegador nesta passada;
2. o terminal do Windows continua podendo sugerir falso positivo de encoding em leitura bruta, mas o arquivo real esta limpo.

### Decisao
1. `L006` passou na revisao topico a topico por IA.
2. estado final: pronta para futura validacao humana, sem necessidade de nova passada de patch antes disso, salvo se a validacao visual encontrar ajuste de layout.

---

## 12) Reauditoria pela skill `revisao-sementes-topico-a-topico`
Data: 2026-03-10
Modo: confirmacao de fechamento via skill

### Leitura de conselho
1. `Charlotte Mason` confirmou que a licao continua tratando a crianca como pessoa e nao como caligrafia em miniatura.
2. `Jerome Bruner` confirmou que a ordem `contemplacao -> gesto no ar -> superficie real -> narracao` permanece viva e inteligivel.
3. `Susan Macaulay` confirmou que a licao continua praticavel para casa real, com preparo leve e sem peso desnecessario para a mae.
4. `Mae Ansiosa` nao abriu alerta novo: a pagina nao pressiona desempenho nem sugere comparacao.
5. `Mae Veterana` nao abriu alerta novo: a experiencia segue realista para o primeiro mes e nao promete maestria instantanea.
6. `Beatrix Potter` nao abriu alerta textual novo: a imagem dominante do rastro bonito na areia continua organica e coerente.
7. `Design` nao abriu alerta estrutural novo: navegacao, blocos e hierarquia continuam claros.
8. `Engenharia` confirmou integridade tecnica basica nesta passada: sem residuos legados, `hrefs` corretos em UTF-8 e parser HTML `OK`.

### Confirmado nesta reauditoria
1. nenhum finding novo foi aberto no HTML da licao;
2. nao houve necessidade de patch adicional em `MV-S-006_O_DESENHO_DO_REI.html`;
3. o estado final da pagina permanece `PASS` em `001-012`;
4. o melhor curso nesta sessao foi preservar o arquivo e registrar a confirmacao formal no log.
