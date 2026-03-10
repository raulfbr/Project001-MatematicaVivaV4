# TASK ROBUSTA - REAUDITORIA TOTAL L003 A L010 POR LICAO COM EXPERTS
Data: 2026-03-10
Status: ativa para execucao controlada
Escopo: reauditar tudo o que ja foi feito e o que ainda sera feito em `MV-S-003` ate `MV-S-010` com protocolo topico a topico, fechamento por licao e validacao por `bmad/experts/`

---

## 1) Objetivo desta task
1. revisar com rigor tudo o que ja foi tocado no lote `L003-L010`;
2. impedir que a revisao vire soma de patches locais sem unidade;
3. usar o protocolo canonico na ordem oficial `001-012`;
4. usar o conselho de `experts` como camada real de validacao, nao como decoracao retorica;
5. entregar um lote pronto para validacao humana posterior, mas so depois de sobreviver a uma reauditoria mais dura.

---

## 2) Decisao metodologica desta rodada
Decisao principal:
1. a execucao primaria desta task sera **por licao**, e nao por topico em lote.

Razao:
1. cada licao tem cerne proprio, imagem dominante, guardiao, lugar, ponte anterior e proxima;
2. revisar `T01` em todas as licoes antes de fechar `T02` tende a otimizar blocos localmente e quebrar unidade macro;
3. os `experts` pedagogicos e de familia julgam melhor a verdade de uma licao inteira do que um bloco solto;
4. a fronteira entre `005 -> 006`, `006 -> 007`, `010 -> 011` e outras so fica visivel quando a pagina toda esta diante dos olhos;
5. hoje o projeto precisa de menos "padronizacao cega por bloco" e mais "coerencia integral por licao".

Decisao secundaria:
1. depois de fechar cada licao inteira, havera uma passada transversal final por topico no lote ja fechado, apenas para capturar drift de consistencia entre paginas.

Sintese:
1. **primeiro fecha por licao; depois varre por topico no lote.**

---

## 3) Relacao desta task com a `029`
1. `029_TASK_ROBUSTA_REVISAO_IMPECAVEL_L003_L010.md` continua sendo a task-macro de execucao do lote;
2. esta `030` governa a **reauditoria criteriosa** do que foi feito e do que ainda sera feito;
3. se houver conflito de cadencia, a `030` prevalece na metodologia fina: `cerne macro -> T01-T12 -> conselho experts -> fronteiras -> so depois proxima licao`.

---

## 4) Escopo desta task
### Em escopo
1. `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html`
2. `site/sementes/MV-S-004_A_ORDEM_DO_DIA.html`
3. `site/sementes/MV-S-005_O_ESCONDERIJO_DA_GLORIA.html` ou arquivo real com acento correspondente
4. `site/sementes/MV-S-006_O_DESENHO_DO_REI.html`
5. `site/sementes/MV-S-007_A_COROA_DA_SEMANA.html`
6. `site/sementes/MV-S-008_O_PAR_PERFEITO.html`
7. `site/sementes/MV-S-009_O_CELEIRO_DE_NOE.html` ou arquivo real com acento correspondente
8. `site/sementes/MV-S-010_A_FILA_DA_PROVIDENCIA.html` ou arquivo real com acento correspondente
9. logs desta rodada
10. tarefas e auditorias canonicas desta fase

### Fora de escopo
1. `Manual do Portador`;
2. validacao humana da Familia Rodrigues;
3. mudanca de governanca em `023`, `003`, `004`, `011_TOPICOS/` ou `012_TRANSVERSAIS/`, salvo contradicao dura;
4. expandir para `L011+` antes de `L003-L010` estar reauditado com veredito honesto.

---

## 5) Fontes obrigatorias
### Nucleo canonico
1. `README.md`
2. `Revisao/README.md`
3. `Revisao/000_COMECAR_AQUI.md`
4. `Revisao/001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
10. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
11. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/000_README.md`
12. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/001_BASE_E_HERO.md` ate `012_NAVEGACAO_INFERIOR.md`
13. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/000_README.md`
14. pacote minimo transversal: `002`, `003`, `005`, `006`, `008`
15. `Revisao/00_SISTEMA_REVISAO_CANONICO/029_TASK_ROBUSTA_REVISAO_IMPECAVEL_L003_L010.md`

### Baselines e logs
1. `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html`
2. `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`
3. `logs/2026-03-10_REVIEW_L003_L004.md`
4. `logs/2026-03-10_WAVE2_L005_L006.md`

### Conselho de `experts`
1. `bmad/experts/pedagogia/charlotte_mason.yaml`
2. `bmad/experts/matematica/jerome_bruner.yaml`
3. `bmad/experts/pedagogia/susan_macaulay.yaml`
4. `bmad/experts/narrativa/beatrix_potter.yaml`
5. `bmad/experts/externos/mae_ansiosa.yaml`
6. `bmad/experts/externos/mae_veterana.yaml`
7. `bmad/experts/engenharia/engenharia.yaml`
8. `bmad/experts/design/design.yaml`
9. `bmad/experts/externos/_pool.yaml`

Regra:
1. usar os `audit_q`, `veto`, `gatilhos` e perguntas centrais desses arquivos;
2. nao improvisar "o que Charlotte diria" ou "o que Susan acharia" sem ter consultado os YAMLs.

---

## 6) Conselho minimo de validacao
### Conselho A - Pedagogia e metodo
1. `Charlotte Mason`: dignidade da crianca, licao curta, narracao, ideias vivas, concreto antes de abstrato, inclusao como honra.
2. `Jerome Bruner`: CPA, discovery learning, curriculo espiral, proibicao de pular o concreto.
3. `Susan Macaulay`: teste da casa real, bebe no colo, feijao no fogo, linguagem simples, aplicabilidade imediata.

### Conselho B - Familia real
1. `Mae Ansiosa`: o texto acalma ou aumenta ansiedade? ha comparacao toxica? o progresso esta comunicavel sem culpa?
2. `Mae Veterana`: isso seria realista no primeiro mes? parece perfeito demais? ajudaria ou assustaria uma mae nova?

### Conselho C - Narrativa e visualidade
1. `Beatrix Potter`: beleza natural, tom nao artificial, imagem dominante coerente, atmosfera que traz paz e maravilha.
2. `Design`: mobile-first, uma mao no celular, clareza, alvos de toque, hierarquia visual sem ruina editorial.

### Conselho D - Integridade tecnica
1. `Engenharia`: SSOT, linguagem ubiqua, sem duplicacao contraditoria, sem drift semantico, QA e checagens tecnicas minimas.

Regra:
1. Charlotte e Bruner podem gerar `BLOCK` pedagogico;
2. Engenharia pode gerar `BLOCK` tecnico;
3. Susan, Mae Ansiosa, Mae Veterana, Beatrix e Design podem gerar `WARN` duro que impede chamar de premium enquanto nao houver resposta.

---

## 7) Gate de veto por expert
### `Charlotte Mason`
BLOCK se:
1. a licao perder dignidade da crianca;
2. a narracao ficar fraca ou interrogatoria;
3. a ideia viva virar fatos secos;
4. a licao pedir materiais raros ou preparo pesado;
5. houver medo, culpa ou pressao como motor.

### `Jerome Bruner`
BLOCK se:
1. a sequencia concreta for pulada;
2. o abstrato aparecer cedo demais;
3. a crianca receber a resposta pronta sem descoberta guiada;
4. a espiral repetir sem profundidade.

### `Susan Macaulay`
WARN duro se:
1. a pagina so funcionar em tese;
2. a mae leiga nao entender na primeira leitura;
3. a licao pedir mais energia do que uma casa real consegue dar.

### `Mae Ansiosa`
WARN duro se:
1. o texto aumentar ansiedade;
2. nao houver claridade de fruto ou progresso;
3. a copy empurrar comparacao com outras criancas.

### `Mae Veterana`
WARN duro se:
1. a promessa soar boa demais para ser verdade;
2. a pagina parecer insustentavel no primeiro mes;
3. o texto esconder atritos reais de aplicacao.

### `Beatrix Potter` e `Design`
WARN duro se:
1. a pagina soar artificial, plastica ou genrica;
2. a hierarquia visual quebrar o respiro;
3. a experiencia em celular perder calma ou clareza.

### `Engenharia`
BLOCK se:
1. houver link quebrado;
2. houver naming incoerente com o arquivo real;
3. houver markup semantico claramente inferior ao contrato atual;
4. houver drift documental ou contradicao com o estado canonico.

---

## 8) Ordem oficial de execucao
### Fase 0 - Preparacao da sessao
1. congelar qual licao sera revista;
2. abrir licao anterior, atual e proxima;
3. abrir `023`, `003`, `004`, os `011_TOPICOS/` e o pacote transversal minimo;
4. abrir os `experts` obrigatorios;
5. registrar cerne macro da licao antes de qualquer patch.

### Fase 1 - Fechamento integral da licao
Para **cada** licao, executar nesta ordem:
1. `T00` - cerne macro;
2. `T01` - `001_BASE_E_HERO.md`
3. `T02` - `002_HEADER_SUPERIOR.md`
4. `T03` - `003_PREPARACAO_DO_PORTADOR.md`
5. `T04` - `004_RITUAL_DE_ENTRADA.md`
6. `T05` - `005_A_JORNADA.md`
7. `T06` - `006_O_CONCRETO.md`
8. `T07` - `007_NARRAMOS_JUNTOS.md`
9. `T08` - `008_RITUAL_DE_FECHAMENTO.md`
10. `T09` - `009_CONEXAO_DA_JORNADA.md`
11. `T10` - `010_SEMENTES_PARA_O_DIA.md`
12. `T11` - `011_FORMACAO_DO_PORTADOR.md`
13. `T12` - `012_NAVEGACAO_INFERIOR.md`
14. `T13` - reler a licao inteira como experiencia una
15. `T14` - passar pelo conselho de `experts`
16. `T15` - auditar fronteiras com anterior e proxima
17. so depois liberar a proxima licao.

### Fase 2 - Ordem das licoes
1. `MV-S-003`
2. `MV-S-004`
3. `MV-S-005`
4. `MV-S-006`
5. `MV-S-007`
6. `MV-S-008`
7. `MV-S-009`
8. `MV-S-010`

Razao da ordem:
1. respeitar trilha curricular;
2. reauditar primeiro o que ja foi mais mexido;
3. impedir que `L007-L010` repitam erros ja corrigiveis em `L003-L006`.

### Fase 3 - Varredura transversal final por topico
Depois que todas as licoes estiverem fechadas individualmente:
1. reler `T01` em `L003-L010`;
2. reler `T02` em `L003-L010`;
3. continuar ate `T12`;
4. registrar apenas drift inter-licoes, sem reabrir patch estrutural pesado sem justificativa.

Regra:
1. a varredura transversal final existe para consistencia;
2. ela nao substitui o fechamento integral por licao.

---

## 9) Definition of Ready por licao
Uma licao so entra em revisao quando:
1. arquivo correto identificado;
2. anterior e proxima abertas;
3. cerne macro preenchido;
4. matriz `001-012` preparada;
5. `experts` da sessao abertos;
6. escopo congelado;
7. houver decisao explicita sobre o que ainda e legado e o que ja e patch novo.

---

## 10) Definition of Done por licao
Uma licao so fecha quando:
1. `T00-T15` estiverem executados;
2. matriz `001-012` estiver completa;
3. fronteiras criticas estiverem auditadas;
4. `BLOCK` duro inexistente;
5. conselho de `experts` estiver respondido;
6. naming, links e semantica estiverem coerentes com o arquivo real;
7. risco residual estiver nomeado sem autoengano;
8. a licao soar como obra una, nao como colagem de correcao.

---

## 11) Formato obrigatorio de registro por topico
Usar sempre:

```md
## MV-S-00X - T0Y [Nome do topico]

### Cerne macro em jogo
- [...]

### Findings
- Critico:
- Alto:
- Medio:

### Decisao
- [...]

### Patch
- Estrutural:
- Narrativo:
- Pedagogico:
- Tecnico:
- Taste:

### Conselho experts
- Charlotte Mason:
- Jerome Bruner:
- Susan Macaulay:
- Mae Ansiosa:
- Mae Veterana:
- Beatrix Potter / Design:
- Engenharia:

### Validacao
- Passou no topico: SIM/NAO
- Gerou contradicao no todo: SIM/NAO
- Ha veto aberto: SIM/NAO

### Risco residual
- [...]

### Proximo passo
- [...]
```

Regra:
1. se um expert abrir `BLOCK`, a licao nao avanca;
2. se houver apenas `WARN`, registrar resposta, risco e motivo de manter ou patchar.

---

## 12) Gate final do lote
O lote `L003-L010` so pode ser chamado de pronto quando:
1. todas as licoes tiverem passado por fechamento integral por licao;
2. a varredura transversal `T01-T12` do lote inteiro tiver acontecido;
3. `L003-L006` tiverem sido revalidadas, nao apenas herdadas;
4. `L007-L010` tiverem sido fechadas sob o mesmo padrao;
5. o conselho de `experts` nao deixar veto aberto;
6. as fronteiras `002 -> 003` ate `010 -> 011` respirarem com clareza;
7. a Familia Rodrigues ainda seja o proximo selo, mas so depois de a IA ter feito a propria licao de casa com rigor.

---

## 13) Artefatos esperados ao final
1. `030_TASK_ROBUSTA_REAUDITORIA_TOTAL_L003_L010_POR_LICAO_COM_EXPERTS.md`
2. logs por licao e por topico
3. logs de conselho `experts` por licao, se separados
4. `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html`
5. `site/sementes/MV-S-004_A_ORDEM_DO_DIA.html`
6. `site/sementes/MV-S-005_O_ESCONDERIJO_DA_GLORIA.html` ou nome real correspondente
7. `site/sementes/MV-S-006_O_DESENHO_DO_REI.html`
8. `site/sementes/MV-S-007_A_COROA_DA_SEMANA.html`
9. `site/sementes/MV-S-008_O_PAR_PERFEITO.html`
10. `site/sementes/MV-S-009_O_CELEIRO_DE_NOE.html` ou nome real correspondente
11. `site/sementes/MV-S-010_A_FILA_DA_PROVIDENCIA.html` ou nome real correspondente
12. atualizacao coerente do quadro de status e do index canonico.

---

## 14) Proximo passo recomendado
1. reabrir `MV-S-003` sob esta `030`;
2. executar `T00-T15` em `L003`;
3. so depois seguir para `L004`;
4. manter `L005-L006` em reauditoria, nao como paginas ja fechadas;
5. entrar em `L007-L010` apenas quando o metodo estiver comprovado de novo nas quatro primeiras.
