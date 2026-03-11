# REVISAO TOPICO A TOPICO - L008
Data: 2026-03-10
Licao: `MV-S-008_O_PAR_PERFEITO.html`
Status da sessao: em revisao
Escopo congelado: revisar apenas a `L008`; `L007` e `L009` entram somente como fronteiras curriculares
Validacao humana da Familia Rodrigues: pendente

---

## 1) Cerne macro da licao
1. `TGTB ref`: `000-L8 - Matching: Part 1 / Correspondencia: Parte 1`
2. `Guardia`: `Iris (Guardia do Olhar)`
3. `Promessa da licao`: a crianca sentir a paz de quando cada tesouro encontra seu par e seu lugar de repouso.
4. `Lugar`: `Ninho Mirante`
5. `Conceito vivo`: correspondencia um-a-um e percepcao concreta de par, antes de qualquer abstracao grafica.
6. `Papel no curriculo mestre`: abrir a base para correspondencia entre elementos, preparando futuros encontros entre quantidade, simbolo e pareamento.
7. `Imagem dominante`: pequenos tesouros que encontram seu par e descansam juntos sob o olhar atento de Iris.
8. `Fruto do dia`: a crianca conseguir juntar pares reais com calma, percebendo que duas coisas podem se corresponder sem pressa e sem confusao.
9. `Risco de fronteira`: a licao virar classificacao generica, jogo de memoria ou treino seco de "igual diferente".
10. `Risco familia real`: excesso de texto e materiais pouco realistas podem matar a leveza da aplicacao.
11. `Hospitalidade multi-crianca`: um irmao menor pode entregar objetos ou "acordar" os tesouros, enquanto o herdeiro principal forma os pares.

---

## 2) Fronteiras criticas com licao anterior e proxima
1. `L007 -> L008`: a passagem sai da coroa de `6` e `7` para a paz do par; a nova licao nao pode continuar presa a contagem.
2. `L008 -> L009`: a conexao deve abrir para `8` e `9` sem roubar o tema de Noe nem transformar a pagina atual em licao de numero.
3. `004 -> 005`: o Ritual deve revelar `Ninho Mirante`; a Jornada deve revelar `Iris`.
4. `005 -> 006`: a Jornada contempla e ensaia a ideia; `O Concreto` encarna o gesto manual principal.
5. `009 -> 010 -> 011`: `Conexao`, `Sementes` e `Formacao` precisam existir com funcoes distintas.

---

## 3) Diagnostico inicial
### Estruturais
1. `Critico`: pagina ainda em contrato legado, com varios blocos antigos e ordem sem fechamento canonico completo.
2. `Critico`: ausencia de `Sementes para o Dia`.
3. `Critico`: ausencia de `Formacao do Portador`; arquivo termina em `Para a Familia`.
4. `Alto`: `Conexao da Jornada` usa `div onclick`.
5. `Alto`: `Ritual de Abertura` ainda com naming legado.

### Narrativos
1. `Alto`: hero e ritual estao achatados e com mojibake, sem sustain premium da imagem dominante.
2. `Alto`: fronteira `Ritual -> Jornada` esta fraca.
3. `Medio`: `Narramos Juntos` existe, mas ainda soa residual e curto demais.

### Pedagogicos
1. `Alto`: a licao corre risco de virar apenas "achar iguais", sem a paz do repouso e do lugar.
2. `Alto`: `O Concreto` esta funcional, mas ainda sem camada premium e sem ponte forte para narracao.
3. `Medio`: `Para a Familia` explica parte da pedagogia, mas no contrato errado.

### Tecnicos
1. `Critico`: mojibake espalhado pelo documento.
2. `Alto`: links de navegacao com encoding quebrado.
3. `Medio`: markup e semantica ainda presos a wrappers e labels antigos.

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
1. a menor decisao segura e reconstruir a pagina no esqueleto canonico atual, preservando apenas o cerne curricular e algumas intuicoes do legado;
2. o maior risco editorial e confundir `par` com simples semelhanca visual, sem repouso, correspondencia e paz;
3. o maior risco estrutural e corrigir nomes sem corrigir funcoes dos blocos;
4. apos patch, sera obrigatoria reauditoria das fronteiras `004 -> 005`, `005 -> 006`, `008 -> 009`, `009 -> 010` e `010 -> 011`.

---

## 6) Patch executado
1. arquivo legado foi reconstruido no esqueleto canonico atual;
2. mojibake e labels antigas foram removidos;
3. `Ritual de Abertura` foi convertido em `Ritual de Entrada`, com reveal de `Ninho Mirante` antes da entrada de `Iris`;
4. `Conexao da Jornada` passou de `div onclick` para link semantico;
5. `Sementes para o Dia` e `Formacao do Portador` foram criadas nos lugares canonicos;
6. hero, jornada, concreto, narracao, fechamento e navegacao foram reescritos para proteger o cerne de `Matching: Part 1`.

---

## 7) Revisao topico a topico apos patch
### `001_BASE_E_HERO` -> `PASS`
#### Confirmado
1. hero reposicionado no contrato atual;
2. imagem dominante de repouso, par e paz foi preservada;
3. guardia `Iris` ficou explicita sem cair em tom escolar.

### `002_HEADER_SUPERIOR` -> `PASS`
#### Confirmado
1. navegacao superior aponta corretamente para `L007` e `L009`;
2. fronteiras curriculares ficaram honestas.

### `003_PREPARACAO_DO_PORTADOR` -> `PASS`
#### Confirmado
1. foco, fio da jornada, materiais, plano B, fruto e estrategia do mestre estao presentes;
2. preparacao ficou usavel para casa real.

### `004_RITUAL_DE_ENTRADA` -> `PASS`
#### Confirmado
1. o `Ninho Mirante` e revelado antes da guardia;
2. o ritual agora cumpre sua funcao propria e nao invade a Jornada.

### `005_A_JORNADA` -> `PASS`
#### Confirmado
1. a Jornada revela `Iris` com voz propria;
2. o tema do encontro dos pares foi encarnado sem virar contagem.

### `006_O_CONCRETO` -> `PASS`
#### Confirmado
1. atividade concreta se distingue claramente da Jornada;
2. o gesto manual central ficou concreto, simples e repetivel.

### `007_NARRAMOS_JUNTOS` -> `PASS`
#### Confirmado
1. narracao ficou em chave de escuta, sem prova;
2. perguntas abertas ajudam a consolidar o vivido.

### `008_RITUAL_DE_FECHAMENTO` -> `PASS`
#### Confirmado
1. fechamento pousa a experiencia com serenidade;
2. a proxima licao nao invade o fechamento.

### `009_CONEXAO_DA_JORNADA` -> `PASS`
#### Confirmado
1. conexao ficou sem anti-pattern semantico;
2. teaser para `L009` abre o celeiro sem roubar o tema de Noe.

### `010_SEMENTES_PARA_O_DIA` -> `PASS`
#### Confirmado
1. secao restaurada em lugar canonico;
2. os cinco movimentos foram entregues de forma leve.

### `011_FORMACAO_DO_PORTADOR` -> `PASS`
#### Confirmado
1. `Formacao do Portador` substituiu integralmente `Para a Familia`;
2. `TGTB`, `CPA`, `Charlotte Mason`, `curriculo em espiral`, `nota de graca` e `As Sementes Continuam` estao presentes.

### `012_NAVEGACAO_INFERIOR` -> `PASS`
#### Confirmado
1. navegacao inferior fecha a pagina com consistencia;
2. links para `L007` e `L009` foram mantidos.

---

## 8) Fronteiras criticas finais
1. `003 -> 004` -> `PASS`
Preparacao orienta o olhar; o Ritual abre o `Ninho Mirante` sem gastar a aparicao de `Iris`.
2. `004 -> 005` -> `PASS`
o lugar e revelado primeiro; a guardia entra depois, ja dentro da experiencia.
3. `005 -> 006` -> `PASS`
a Jornada contempla o encontro; `O Concreto` entrega o gesto manual.
4. `006 -> 007` -> `PASS`
o pareamento vivido desemboca naturalmente em narracao.
5. `008 -> 009` -> `PASS`
o fechamento pousa antes da conexao olhar para amanha.
6. `009 -> 010` -> `PASS`
Conexao aponta a trilha; `Sementes` abre continuacoes leves.
7. `010 -> 011` -> `PASS`
atividades opcionais nao invadem a camada formativa do adulto.
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
3. links locais principais apontam para `MV-S-007_A_COROA_DA_SEMANA.html` e `MV-S-009_O_CELEIRO_DE_NOÉ.html`;
4. o arquivo final esta em UTF-8 e sem sinais residuais de encoding quebrado na leitura de validacao.

---

## 11) Veredito honesto
### O que ficou impecavel
1. a pagina saiu integralmente do legado e entrou no contrato canonico atual;
2. a ideia viva de `O Par Perfeito` foi preservada como repouso, encontro e paz entre pares;
3. `Sementes para o Dia` e `Formacao do Portador` foram restauradas com funcao propria;
4. as fronteiras narrativas e pedagogicas principais ficaram nitidas.

### O que ainda ficou em risco
1. nao houve validacao visual em navegador nesta passada;
2. `L009` ainda esta em contrato legado, portanto a experiencia de continuidade externa continua dependente da futura revisao da proxima pagina.

### Decisao
1. `L008` passou na revisao topico a topico por IA;
2. estado final: alinhada ao protocolo e pronta para futura validacao humana, sem necessidade de nova passada de patch antes disso, salvo ajuste visual de layout.
