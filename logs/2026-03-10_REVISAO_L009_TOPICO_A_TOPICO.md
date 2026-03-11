# REVISAO TOPICO A TOPICO - L009
Data: 2026-03-10
Licao: `MV-S-009_O_CELEIRO_DE_NOÉ.html`
Status da sessao: em revisao
Escopo congelado: revisar apenas a `L009`; `L008` e `L010` entram somente como fronteiras curriculares
Validacao humana da Familia Rodrigues: pendente

---

## 1) Cerne macro da licao
1. `TGTB ref`: `000-L9 - Numbers 8 to 9`
2. `Guardiao`: `Noe`
3. `Promessa da licao`: a crianca perceber que `8` e `9` sao quantidades grandes, mas ainda acolhiveis e contaveis com paz.
4. `Lugar`: `Arvore do Silencio` como portal de entrada para o celeiro de Noe.
5. `Conceito vivo`: contar `8` e `9` em objetos reais, sem pressa, como quem guarda fardos para o tempo certo.
6. `Papel no curriculo mestre`: ampliar a contagem para alem de `7`, preparando o caminho para novas quantidades sem romper a serenidade do concreto.
7. `Imagem dominante`: fardos e tesouros guardados no celeiro, contados com paciencia sob o olhar de Noe.
8. `Fruto do dia`: a crianca conseguir contar ate `8` e `9` com objetos reais, sem atropelo e sem perder o fio.
9. `Risco de fronteira`: a licao virar treino escolar seco de numerais ou repeticao cansada da coroa de `6` e `7`.
10. `Risco familia real`: densidade excessiva e pressa adulta matarem a experiencia de calma que o guardiao exige.
11. `Hospitalidade multi-crianca`: um irmao menor pode entregar os fardos um a um, enquanto o herdeiro principal faz a contagem.

---

## 2) Fronteiras criticas com licao anterior e proxima
1. `L008 -> L009`: sair do encontro dos pares para a guarda paciente de `8` e `9`, sem manter a licao presa ao tema do par.
2. `L009 -> L010`: abrir a trilha para ordem/posicao sem transformar a pagina atual em ordinalidade.
3. `004 -> 005`: o Ritual deve revelar o portal de Noe; a Jornada deve abrir o celeiro e o gesto da guarda.
4. `005 -> 006`: a Jornada contempla e interpreta; `O Concreto` encarna a contagem dos fardos.
5. `009 -> 010 -> 011`: `Conexao`, `Sementes` e `Formacao` precisam existir com funcao distinta.

---

## 3) Diagnostico inicial
### Estruturais
1. `Critico`: pagina ainda em contrato legado.
2. `Critico`: `Sementes para o Dia` ausente.
3. `Critico`: `Formacao do Portador` ausente; arquivo termina em `Para a Familia`.
4. `Alto`: `Conexao da Jornada` com `div onclick`.
5. `Alto`: `Ritual de Abertura` ainda em naming legado.

### Narrativos
1. `Alto`: hero, ritual e jornada estao achatados, com tom menos premium e encoding quebrado.
2. `Alto`: risco de perder a imagem dominante do celeiro e da paciencia de Noe.
3. `Medio`: narracao final ainda curta e escolarizada.

### Pedagogicos
1. `Alto`: a licao tende a virar apenas "conte ate 9".
2. `Alto`: falta separacao forte entre Jornada e `O Concreto`.
3. `Medio`: `Para a Familia` traz parte da intencao, mas no contrato errado.

### Tecnicos
1. `Critico`: mojibake espalhado.
2. `Alto`: links de navegacao com encoding quebrado.
3. `Medio`: wrappers e labels antigos.

---

## 4) Matriz inicial `001-012`
1. `001_BASE_E_HERO` -> `BLOCK`
2. `002_HEADER_SUPERIOR` -> `GAP`
3. `003_PREPARACAO_DO_PORTADOR` -> `GAP`
4. `004_RITUAL_DE_ENTRADA` -> `BLOCK`
5. `005_A_JORNADA` -> `GAP`
6. `006_O_CONCRETO` -> `GAP`
7. `007_NARRAMOS_JUNTOS` -> `GAP`
8. `008_RITUAL_DE_FECHAMENTO` -> `GAP`
9. `009_CONEXAO_DA_JORNADA` -> `BLOCK`
10. `010_SEMENTES_PARA_O_DIA` -> `BLOCK`
11. `011_FORMACAO_DO_PORTADOR` -> `BLOCK`
12. `012_NAVEGACAO_INFERIOR` -> `GAP`

---

## 5) Hipoteses e riscos
1. a menor decisao segura e reconstruir a pagina no esqueleto canonico atual, preservando o cerne de Noe, da paciencia e do celeiro;
2. o maior risco editorial e virar treino escolar de `8` e `9` sem atmosfera, guardiao e provisao;
3. o maior risco estrutural e corrigir apenas nomes, deixando as funcoes dos blocos colapsadas;
4. apos patch, sera obrigatoria reauditoria das fronteiras `004 -> 005`, `005 -> 006`, `008 -> 009`, `009 -> 010` e `010 -> 011`.

---

## 6) Patch executado
1. arquivo legado foi reconstruido no esqueleto canonico atual;
2. mojibake, labels antigas e wrappers legados foram removidos;
3. `Ritual de Abertura` foi convertido em `Ritual de Entrada`;
4. `Conexao da Jornada` passou de `div onclick` para link semantico;
5. `Sementes para o Dia` e `Formacao do Portador` foram criadas em lugar canonico;
6. hero, jornada, concreto, narracao e fechamento foram reescritos para preservar o celeiro, os fardos e a paciencia de Noe.

---

## 7) Revisao topico a topico apos patch
### `001_BASE_E_HERO` -> `PASS`
#### Confirmado
1. hero reposicionado no contrato atual;
2. a imagem dominante do celeiro e dos fardos foi preservada;
3. `8` e `9` aparecem como crescimento sereno, nao como pressa escolar.

### `002_HEADER_SUPERIOR` -> `PASS`
#### Confirmado
1. navegacao superior aponta corretamente para `L008` e `L010`;
2. as fronteiras curriculares ficaram honestas.

### `003_PREPARACAO_DO_PORTADOR` -> `PASS`
#### Confirmado
1. foco, fio da jornada, materiais, plano B, fruto e estrategia do mestre estao presentes;
2. preparacao ficou realista para casa viva.

### `004_RITUAL_DE_ENTRADA` -> `PASS`
#### Confirmado
1. a `Arvore do Silencio` abre o portal antes da aparicao de Noe;
2. o ritual prepara o clima de paciencia e nao invade a Jornada.

### `005_A_JORNADA` -> `PASS`
#### Confirmado
1. a Jornada apresenta Noe e o celeiro com voz propria;
2. o `8` e o `9` aparecem como provisao guardada, nao apenas como numeral novo.

### `006_O_CONCRETO` -> `PASS`
#### Confirmado
1. `O Concreto` ficou distinto da Jornada;
2. o gesto manual central de guardar e contar um a um ficou claro.

### `007_NARRAMOS_JUNTOS` -> `PASS`
#### Confirmado
1. narracao ficou em chave de escuta e memoria do vivido;
2. perguntas abertas consolidam a experiencia.

### `008_RITUAL_DE_FECHAMENTO` -> `PASS`
#### Confirmado
1. fechamento repousa a experiencia com serenidade;
2. a proxima licao nao invade o encerramento.

### `009_CONEXAO_DA_JORNADA` -> `PASS`
#### Confirmado
1. conexao ficou sem anti-pattern semantico;
2. teaser para `L010` abre a fila sem roubar a licao de ordinalidade.

### `010_SEMENTES_PARA_O_DIA` -> `PASS`
#### Confirmado
1. secao restaurada em lugar canonico;
2. os cinco movimentos foram entregues com leveza.

### `011_FORMACAO_DO_PORTADOR` -> `PASS`
#### Confirmado
1. `Formacao do Portador` substituiu integralmente `Para a Familia`;
2. `TGTB`, `CPA`, `Charlotte Mason`, `curriculo em espiral`, `nota de graca` e `As Sementes Continuam` estao presentes.

### `012_NAVEGACAO_INFERIOR` -> `PASS`
#### Confirmado
1. navegacao inferior fecha a pagina com consistencia;
2. links para `L008` e `L010` foram mantidos.

---

## 8) Fronteiras criticas finais
1. `003 -> 004` -> `PASS`
Preparacao orienta a calma; o Ritual abre o portal de Noe sem gastar a Jornada.
2. `004 -> 005` -> `PASS`
o silencio prepara; o celeiro e o guardiao entram na hora certa.
3. `005 -> 006` -> `PASS`
a Jornada contempla a guarda; `O Concreto` entrega o gesto manual da contagem.
4. `006 -> 007` -> `PASS`
o ato de guardar e contar desemboca naturalmente em narracao.
5. `008 -> 009` -> `PASS`
o fechamento pousa antes de a conexao olhar para amanha.
6. `009 -> 010` -> `PASS`
Conexao aponta a trilha; `Sementes` abre extensoes leves e domesticas.
7. `010 -> 011` -> `PASS`
as atividades opcionais nao invadem a formacao do adulto.
8. `011 -> 012` -> `PASS`
formacao fecha antes da navegacao tecnica.

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
1. nao houve match para `\[Foco:\]`, `Ritual de Abertura`, `Atividade Concreta`, `Para a Familia` ou `div onclick`;
2. parser HTML simples retornou `OK`;
3. links locais principais apontam para `MV-S-008_O_PAR_PERFEITO.html` e `MV-S-010_A_FILA_DA_PROVIDÊNCIA.html`;
4. o arquivo final esta em UTF-8 e sem sinais residuais de encoding quebrado na leitura de validacao.

---

## 11) Veredito honesto
### O que ficou impecavel
1. a pagina saiu integralmente do legado e entrou no contrato canonico atual;
2. a imagem dominante do celeiro, dos fardos e da paciencia de Noe foi preservada;
3. `Sementes para o Dia` e `Formacao do Portador` foram restauradas com funcao propria;
4. `8` e `9` deixaram de soar como treino seco e passaram a operar como experiencia concreta de guarda e contagem.

### O que ainda ficou em risco
1. nao houve validacao visual em navegador nesta passada;
2. `L010` ainda esta em contrato legado, entao a continuidade externa continua dependente da futura revisao da proxima pagina.

### Decisao
1. `L009` passou na revisao topico a topico por IA;
2. estado final: alinhada ao protocolo e pronta para futura validacao humana, sem necessidade de nova passada de patch antes disso, salvo ajuste visual de layout.
