# ESQUELETO GERAL - LICAO CANONICA SEMENTES
Data: 2026-03-06
Status: canonico
Escopo: `MV-S-001+`
Excecao formal: `MV-S-000` (ver `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/007_EXCECAO_L000_PORTAL.md`)

---

## 1) Missao deste arquivo
Este documento define a estrutura oficial da licao padrao do ciclo Sementes.

Ele existe para:
1. dar um esqueleto unico para revisao de HTML;
2. impedir drift entre licoes;
3. permitir revisao modular por IA e por humano;
4. servir como indice-mestre para os arquivos da pasta `Revisao/`.

Regra:
1. se uma licao `MV-S-001+` conflitar com este esqueleto, a licao deve ser ajustada;
2. se este esqueleto conflitar com HTML real validado e houver motivo forte, o esqueleto deve ser atualizado conscientemente, nao ignorado.

---

## 2) Escopo e nao-escopo
Escopo:
1. ordem da experiencia da licao;
2. blocos obrigatorios;
3. blocos recomendados;
4. nomes legados ainda encontrados no acervo;
5. relacao entre secoes.

Nao-escopo:
1. CSS detalhado linha por linha;
2. lista exaustiva de icones;
3. instrucoes profundas de reescrita por topico;
4. excecoes especiais do Portal.

Esses itens vivem nos arquivos por topico e nas transversais.

---

## 3) Contrato geral da licao padrao
Toda licao `MV-S-001+` deve seguir esta ordem:

1. Base do Documento
2. Hero
3. Header Superior Canonico
4. Preparacao do Portador
5. Ritual de Entrada
6. A Jornada
7. O Concreto
8. Narramos Juntos
9. Ritual de Fechamento
10. Conexao da Jornada
11. Sementes para o Dia
12. Formacao do Portador
13. Navegacao Inferior

Regra de ouro:
1. a licao deve parecer uma experiencia unica e fluida, nao uma pilha de blocos independentes.
2. a licao so esta correta de verdade se permanecer fiel ao `LORE/north_star.yaml`.

---

## 4) Status por bloco

| ID | Bloco | Status | Observacao |
|---|---|---|---|
| B0 | Base do Documento | Obrigatorio | Estrutura tecnica minima do HTML |
| B1 | Hero | Obrigatorio | Abre identidade, promessa e clima |
| B2 | Header Superior Canonico | Obrigatorio | Norte de navegacao no topo |
| B3 | Preparacao do Portador | Obrigatorio | Bastidores e leitura do adulto |
| B4 | Ritual de Entrada | Obrigatorio | Transicao para o Reino e local |
| B5 | A Jornada | Obrigatorio | Encontro com o guardiao e nucleo narrativo |
| B6 | O Concreto | Obrigatorio | Nucleo concreto da licao |
| B7 | Narramos Juntos | Obrigatorio | Reconto, escuta e consolidacao viva |
| B8 | Ritual de Fechamento | Obrigatorio | Volta com dignidade e fio de ouro |
| B9 | Conexao da Jornada | Obrigatorio | Gancho para a licao seguinte |
| B10 | Sementes para o Dia | Obrigatorio no padrao premium | Pode existir legado incompleto |
| B11 | Formacao do Portador | Obrigatorio | Educacao do pai/mae e meta-pedagogia |
| B12 | Navegacao Inferior | Obrigatorio | Fechamento tecnico da pagina |

---

## 5) Regras de nomenclatura
Titulos alvo das secoes:

1. `Preparacao do Portador`
2. `Ritual de Entrada`
3. `A Jornada`
4. `O Concreto`
5. `Narramos Juntos`
6. `Ritual de Fechamento`
7. `Conexao da Jornada`
8. `Sementes para o Dia`
9. `Formacao do Portador`

Nomes legados ainda encontrados no acervo:

1. `Atividade Concreta` -> nome antigo que deve convergir para `O Concreto`

Regra:
1. em documentacao nova, usar apenas `O Concreto`;
2. no acervo existente, corrigir para `O Concreto` sempre que a secao for revisada.

---

## 6) Descricao funcional de cada bloco

### B0 - Base do Documento
Funcao:
1. garantir que a licao carregue com integridade tecnica.

Inclui:
1. `<head>`
2. `<body>`
3. `home-btn`
4. `lesson-container`

Nao pode:
1. quebrar carregamento de fontes, icones ou CSS;
2. omitir estrutura base de navegacao da pagina.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/001_BASE_E_HERO.md`

### B1 - Hero
Funcao:
1. abrir a identidade da licao e preparar emocionalmente o adulto para o tom do encontro.

Inclui:
1. meta-tag;
2. titulo;
3. frase de impacto;
4. imagem principal coerente.

Nao pode:
1. parecer capa genérica;
2. prometer algo desconectado do corpo da licao.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/001_BASE_E_HERO.md`

### B2 - Header Superior Canonico
Funcao:
1. dar orientacao espacial imediata no topo da pagina.

Inclui:
1. licao anterior;
2. selo `Sementes` no centro;
3. proxima licao.

Nao pode:
1. usar "Voltar" genérico nas licoes padrao;
2. perder a simetria basica do topo.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/002_HEADER_SUPERIOR.md`

### B3 - Preparacao do Portador
Funcao:
1. preparar o adulto para conduzir a licao com seguranca, leveza e intencao.

Inclui:
1. foco;
2. dica do coracao;
3. materiais;
4. descoberta da crianca;
5. segredo do maravilhamento;
6. nota de graca.

Nao pode:
1. virar texto academico;
2. exigir preparo inviavel para uma familia real.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/003_PREPARACAO_DO_PORTADOR.md`

### B4 - Ritual de Entrada
Funcao:
1. tirar a familia do cotidiano e introduzir o local da licao.

Inclui:
1. bastidores;
2. voz unica do Portador;
3. reveal do local;
4. imersao sensorial.

Nao pode:
1. antecipar o guardiao;
2. fragmentar a voz do Portador em varios blocos sem necessidade.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/004_RITUAL_DE_ENTRADA.md`

### B5 - A Jornada
Funcao:
1. realizar o encontro com o guardiao e dramatizar o conceito em movimento.

Inclui:
1. apresentacao do guardiao;
2. cenas;
3. instrucoes de acao;
4. script com tom;
5. progressao clara.

Nao pode:
1. poluir a tela com card repetido;
2. cair em exposicao didatica seca.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/005_A_JORNADA.md`

### B6 - O Concreto
Funcao:
1. trazer o conceito para as maos, corpo, objetos e experiencia concreta.

Inclui:
1. objetivo;
2. atividade concreta;
3. adaptacao simples;
4. transicao para o reconto.

Nao pode:
1. soar como tarefa escolar fria;
2. trocar o concreto por explicacao abstrata.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/006_O_CONCRETO.md`

### B7 - Narramos Juntos
Funcao:
1. consolidar a experiencia pela fala da crianca e pela escuta do adulto.

Inclui:
1. instrucoes de escuta;
2. pergunta principal;
3. perguntas do coracao.

Nao pode:
1. interrogar a crianca como prova oral;
2. transformar a narracao em checklist de respostas certas.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/007_NARRAMOS_JUNTOS.md`

### B8 - Ritual de Fechamento
Funcao:
1. encerrar a aventura sem brusquidao e deixar um fio de ouro.

Inclui:
1. despedida do guardiao;
2. fala final do Portador;
3. transicao de volta.

Nao pode:
1. terminar abruptamente;
2. perder o tom de dignidade e descanso.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/008_RITUAL_DE_FECHAMENTO.md`

### B9 - Conexao da Jornada
Funcao:
1. ligar a licao atual a proxima aventura.

Inclui:
1. teaser;
2. link claro;
3. senso de continuidade.

Nao pode:
1. ser descartada como detalhe;
2. quebrar a progressao curricular.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/009_CONEXAO_DA_JORNADA.md`

### B10 - Sementes para o Dia
Funcao:
1. abrir extensoes leves e opcionais para o resto do dia.

Inclui:
1. introducao;
2. 5 atividades;
3. frase final.

Nao pode:
1. virar obrigacao extra;
2. repetir exatamente o que ja foi feito na licao.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/010_SEMENTES_PARA_O_DIA.md`

### B11 - Formacao do Portador
Funcao:
1. educar o pai/mae enquanto ele ensina.

Inclui:
1. estrategia do mestre;
2. por que importa;
3. CPA;
4. Charlotte Mason;
5. TGTB;
6. espiral;
7. graca;
8. sementes continuam.

Nao pode:
1. parecer apendice sem alma;
2. usar boxes quebradas ou texto cansativo.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/011_FORMACAO_DO_PORTADOR.md`

### B12 - Navegacao Inferior
Funcao:
1. fechar a pagina tecnicamente com navegacao segura.

Inclui:
1. anterior;
2. proxima;
3. footer simples.

Nao pode:
1. apontar para licoes erradas;
2. deixar a pagina sem fechamento.

Referencia:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/012_NAVEGACAO_INFERIOR.md`

---

## 7) Fluxo vivo da experiencia
A licao deve produzir esta curva:

1. Orientacao
2. Preparacao
3. Entrada no Reino
4. Encontro narrativo
5. Experiencia concreta
6. Reconto
7. Fechamento
8. Continuidade
9. Formacao do adulto
10. Navegacao tecnica

Se uma secao enfraquece essa curva, ela precisa ser revista mesmo que "esteja presente".

---

## 8) Gates do esqueleto

### Gate Estrutural
PASS quando:
1. todos os blocos obrigatorios estao presentes;
2. a ordem macro esta correta;
3. a navegacao superior e inferior estao coerentes.

BLOCK quando:
1. falta bloco obrigatorio;
2. `Conexao da Jornada` some;
3. `Formacao do Portador` esta mutilada;
4. `O Concreto` nao existe funcionalmente.

### Gate Narrativo
PASS quando:
1. o local aparece no Ritual;
2. o guardiao aparece na Jornada;
3. a volta acontece no Fechamento.

BLOCK quando:
1. o guardiao aparece cedo demais;
2. a licao parece fragmentada;
3. o Portador perde sua dignidade narrativa.

### Gate Pedagogico
PASS quando:
1. o concreto esta no centro;
2. a narracao ajuda a fixar;
3. a formacao do adulto explica o por que.

BLOCK quando:
1. o concreto vira abstrato;
2. a licao depende de explicacao escolar;
3. a extensao do dia vira sobrecarga.

### Gate North Star
PASS quando:
1. a familia permanece no centro;
2. o tom e redentor para o adulto;
3. a crianca e tratada com dignidade;
4. a licao ainda parece Matemática Viva e nao material generico.

BLOCK quando:
1. a licao culpa, pesa ou complica;
2. a beleza e sacrificada;
3. o Reino vira verniz;
4. a experiencia se afasta do North Star.

---

## 9) Mapa dos documentos complementares
Arquivos centrais:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`

Topicos:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/001_BASE_E_HERO.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/002_HEADER_SUPERIOR.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/003_PREPARACAO_DO_PORTADOR.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/004_RITUAL_DE_ENTRADA.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/005_A_JORNADA.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/006_O_CONCRETO.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/007_NARRAMOS_JUNTOS.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/008_RITUAL_DE_FECHAMENTO.md`
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/009_CONEXAO_DA_JORNADA.md`
10. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/010_SEMENTES_PARA_O_DIA.md`
11. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/011_FORMACAO_DO_PORTADOR.md`
12. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/012_NAVEGACAO_INFERIOR.md`

Transversais:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/001_ICONES_CORES_E_ASSETS.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/002_REGRAS_DE_HTML_E_ANTI_PATTERNS.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/003_TOM_NARRATIVO_E_DIRECAO_DO_PORTADOR.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/004_GUARDIOES_CARDS_E_REVEAL.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/005_CRITERIOS_PEDAGOGICOS_CM_CPA_TGTB.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/006_ENCODING_E_SANITY_CHECK.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/007_EXCECAO_L000_PORTAL.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`

---

## 10) Definition of Ready do esqueleto
Podemos iniciar a criacao dos arquivos por topico quando:
1. este esqueleto estiver estavel;
2. os aliases legados estiverem decididos;
3. `Conexao da Jornada` estiver definitivamente recolocada no contrato.

---

## 11) Definition of Done do sistema
O sistema de revisao so fica realmente usavel quando:
1. este esqueleto estiver criado;
2. existir protocolo operacional;
3. existir rubrica premium;
4. existirem guias por topico;
5. existirem regras transversais;
6. o piloto `001-003` confirmar que o esqueleto cobre o HTML real.
