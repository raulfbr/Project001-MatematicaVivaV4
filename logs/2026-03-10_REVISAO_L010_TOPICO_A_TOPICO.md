# REVISAO TOPICO A TOPICO - L010
Data: 2026-03-10
Licao: `MV-S-010_A_FILA_DA_PROVIDÊNCIA.html`
Status da sessao: em revisao
Escopo congelado: revisar apenas a `L010`; `L009` e `L011` entram somente como fronteiras curriculares
Validacao humana da Familia Rodrigues: pendente

---

## 1) Cerne macro da licao
1. `TGTB ref`: `000-L10 - Ordinal Numbers: Part 1 / Numeros Ordinais: Parte 1`
2. `Guardia`: `Celeste`
3. `Promessa da licao`: a crianca perceber que posicao conta uma historia e que `primeiro`, `segundo`, `terceiro` nomeiam lugares na fila, nao quantidades.
4. `Lugar`: `Rua das Familias` como portal vivo para filas, passagens e ordem de chegada.
5. `Conceito vivo`: ordinalidade concreta em fila real de objetos ou personagens, com foco inicial ate o quinto lugar.
6. `Papel no curriculo mestre`: introduzir numeros ordinais como relacoes de posicao, distintos dos cardinais.
7. `Imagem dominante`: a fila da providencia, em que cada lugar carrega um papel e uma historia.
8. `Fruto do dia`: a crianca conseguir identificar quem vem primeiro, segundo, terceiro, quarto e quinto numa fila concreta.
9. `Risco de fronteira`: a licao virar vocabulario abstrato ou confundir cardinalidade com ordinalidade.
10. `Risco familia real`: excesso de explicacao e pouca manipulacao concreta.
11. `Hospitalidade multi-crianca`: um irmao menor pode mover personagens ou trocar suas posicoes enquanto a crianca principal nomeia os lugares.

---

## 2) Fronteiras criticas com licao anterior e proxima
1. `L009 -> L010`: sair de quantidade guardada para posicao em fila, sem a pagina ficar presa ao `8` e `9`.
2. `L010 -> L011`: apontar para o `10` sem roubar o tema das duas maos completas.
3. `004 -> 005`: o Ritual deve abrir a rua/fila; a Jornada deve revelar `Celeste` e a corrida/ordem.
4. `005 -> 006`: a Jornada contempla a fila; `O Concreto` encarna o gesto de reposicionar e nomear.
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
1. `Alto`: hero, ritual e jornada ainda achatados e com encoding quebrado.
2. `Alto`: risco de perder a imagem dominante da fila da providencia, reduzindo tudo a corrida ou jogo.
3. `Medio`: narracao final ainda escolarizada.

### Pedagogicos
1. `Alto`: forte risco de confundir cardinal com ordinal.
2. `Alto`: falta separacao forte entre Jornada e `O Concreto`.
3. `Medio`: `Para a Familia` traz parte da pedagogia, mas no contrato errado.

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
1. a menor decisao segura e reconstruir a pagina no esqueleto canonico atual;
2. o maior risco editorial e trocar `fila da providencia` por exercicio generico de ordem;
3. o maior risco pedagogico e misturar quantidade com posicao;
4. apos patch, sera obrigatoria reauditoria das fronteiras `004 -> 005`, `005 -> 006`, `008 -> 009`, `009 -> 010` e `010 -> 011`.

---

## 6) Patch executado
1. arquivo legado foi reconstruido no esqueleto canonico atual;
2. mojibake, labels antigas e wrappers legados foram removidos do corpo da licao;
3. `Ritual de Abertura` foi convertido em `Ritual de Entrada`;
4. `Conexao da Jornada` passou de `div onclick` para link semantico;
5. `Sementes para o Dia` e `Formacao do Portador` foram criadas em lugar canonico;
6. hero, jornada, concreto, narracao e fechamento foram reescritos para proteger a ideia viva de ordinalidade como historia de lugares.

---

## 7) Revisao topico a topico apos patch
### `001_BASE_E_HERO` -> `PASS`
#### Confirmado
1. hero reposicionado no contrato atual;
2. a imagem dominante da fila da providencia foi preservada;
3. ordinalidade deixou de soar como vocabulario escolar seco.

### `002_HEADER_SUPERIOR` -> `PASS`
#### Confirmado
1. navegacao superior aponta para `L009` e `L011` com os nomes reais em disco;
2. as fronteiras curriculares ficaram honestas.

### `003_PREPARACAO_DO_PORTADOR` -> `PASS`
#### Confirmado
1. foco, fio da jornada, materiais, plano B, fruto e estrategia do mestre estao presentes;
2. preparacao ficou realista para casa viva.

### `004_RITUAL_DE_ENTRADA` -> `PASS`
#### Confirmado
1. a `Rua das Familias` abre o portal antes da entrada plena de `Celeste`;
2. o ritual prepara o olhar para lugar e ordem, nao para quantidade.

### `005_A_JORNADA` -> `PASS`
#### Confirmado
1. a Jornada apresenta `Celeste` com voz propria;
2. a fila aparece como historia de posicoes, nao como grupo contado.

### `006_O_CONCRETO` -> `PASS`
#### Confirmado
1. `O Concreto` ficou distinto da Jornada;
2. o gesto manual central de mover a fila e nomear lugares ficou claro.

### `007_NARRAMOS_JUNTOS` -> `PASS`
#### Confirmado
1. narracao ficou em chave de escuta e reconto do que mudou na fila;
2. perguntas abertas consolidam a diferenca entre lugar e quantidade.

### `008_RITUAL_DE_FECHAMENTO` -> `PASS`
#### Confirmado
1. fechamento repousa a experiencia com serenidade;
2. a proxima licao nao invade o encerramento.

### `009_CONEXAO_DA_JORNADA` -> `PASS`
#### Confirmado
1. conexao ficou sem anti-pattern semantico;
2. teaser para `L011` aponta para o `10` sem roubar o tema das duas maos.

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
2. links para `L009` e `L011` foram mantidos com o naming real do repositorio.

---

## 8) Fronteiras criticas finais
1. `003 -> 004` -> `PASS`
Preparacao orienta o olhar; o Ritual abre a rua e a fila antes da Jornada.
2. `004 -> 005` -> `PASS`
o lugar aparece primeiro; `Celeste` entra depois para ler a ordem da fila.
3. `005 -> 006` -> `PASS`
a Jornada contempla a mudanca de lugar; `O Concreto` entrega o gesto manual de reorganizar.
4. `006 -> 007` -> `PASS`
o movimento da fila desemboca naturalmente em narracao.
5. `008 -> 009` -> `PASS`
o fechamento pousa antes da conexao olhar para amanha.
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
3. links locais principais apontam para `MV-S-009_O_CELEIRO_DE_NOÉ.html` e para o nome real em disco de `L011`, `MV-S-011_A_PLENITUDE_DAS_MÃOS.html`;
4. o unico resquicio visual de `Ã` na validacao automatica esta no proprio nome do arquivo vizinho `L011`, que ja entra assim no repositorio e portanto foi preservado como naming exato em disco.

---

## 11) Veredito honesto
### O que ficou impecavel
1. a pagina saiu integralmente do legado e entrou no contrato canonico atual;
2. a ideia viva da fila da providencia foi preservada como historia de lugares, nao de quantidade;
3. `Sementes para o Dia` e `Formacao do Portador` foram restauradas com funcao propria;
4. a diferenca entre cardinalidade e ordinalidade ficou muito mais nitida.

### O que ainda ficou em risco
1. nao houve validacao visual em navegador nesta passada;
2. `L011` continua com naming legado no proprio nome de arquivo do repositorio, o que contamina buscas cegas por encoding.

### Decisao
1. `L010` passou na revisao topico a topico por IA;
2. estado final: alinhada ao protocolo e pronta para futura validacao humana, sem necessidade de nova passada de patch antes disso, salvo ajuste visual de layout.
