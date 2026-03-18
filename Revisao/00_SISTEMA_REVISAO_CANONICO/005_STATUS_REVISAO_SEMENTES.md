# STATUS DA REVISAO SEMENTES
Data base: 2026-03-17
Status geral: protocolo central consolidado em `023`; `Manual do Portador`, `MV-S-001` e `MV-S-002` seguem prontos para validacao humana; `MV-S-003` e `MV-S-004` passaram por rodadas profundas com feedback real; por decisao operacional de `2026-03-17`, a trilha publicada foi cortada em `MV-S-015`, `MV-S-016` virou pagina de continuidade em construcao e `MV-S-017+` sairam da trilha publicada ate reconstrucao com protocolo premium endurecido

---

## 1) Objetivo deste quadro
Este arquivo e o quadro de bordo da fase atual.

Ele serve para:
1. mostrar em que estado o sistema de revisao esta;
2. indicar quais licoes ja passaram pelo protocolo central;
3. registrar qual trilha esta realmente publicada;
4. registrar o proximo passo seguro sem recontar toda a historia do projeto.

Regra:
1. este arquivo mostra o estado atual;
2. memoria detalhada fica nas tasks e auditorias historicas;
3. se uma regra procedural mudar, ela deve mudar primeiro no `023`, nao aqui.

---

## 2) Estado atual da fase
Fase ativa:
1. protocolo topico a topico centralizado em fonte unica;
2. `MV-S-001` e `MV-S-002` revisitadas contra esse protocolo e mantidas prontas para selo humano;
3. `Manual do Portador` reescrito na abertura para alinhar `Licao 000`, mobile-first e impressao opcional;
4. `MV-S-003` e `MV-S-004` passaram por rodada profunda com recalibragem via feedback real;
5. a task `029` segue como trilho do lote estruturado `MV-S-003` ate `MV-S-010`;
6. a task `030` segue como reauditoria criteriosa por licao com conselho `experts`;
7. a validacao humana da Familia Rodrigues segue adiada para depois do fechamento do lote, salvo se aparecer `BLOCK` duro que exija retorno imediato;
8. a experiencia publica do site agora vai de `MV-S-000` ate `MV-S-015`;
9. `MV-S-016` permanece acessivel apenas como pagina de continuidade em construcao;
10. `MV-S-017+` aguardam reconstrucao sob protocolo premium mais robusto para criacao e revisao.

Antes de fechar o lote atual:
1. preservar `MV-S-003` e `MV-S-004` como referencias fechadas desta rodada, salvo novo feedback relevante;
2. migrar `MV-S-005` ate `MV-S-010` ao contrato canonico atual;
3. executar a reauditoria por licao e por `experts` descrita na `030`;
4. fechar auditoria transversal do bloco `003-010`;
5. sustentar o protocolo endurecido na revisao de `MV-S-005` ate `MV-S-010`;
6. so depois levar o conjunto para validacao humana posterior e decidir a volta de `MV-S-016+`.

---

## 3) Fontes canonicas desta camada

| Camada | Fonte atual | Funcao |
|---|---|---|
| Ativacao do protocolo | `023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md` | Ordem de leitura, cerne macro, algoritmo e anti-duplicacao |
| Execucao da revisao | `003_PROTOCOLO_REVISAO_POR_LICAO.md` | Patch, reauditoria, gates e formato de log |
| Veredito | `004_RUBRICA_PREMIUM_REVISAO.md` | Pontuacao e bloqueios objetivos |
| Registro da sessao | `010_TEMPLATE_SESSAO_DIARIA_REVISAO.md` | Template preenchivel para cada rodada |
| Contratos dos blocos | `011_TOPICOS/` | Regras topico por topico |
| Regras transversais | `012_TRANSVERSAIS/` | HTML, tom, pedagogia, taste, encoding e North Star |
| Quadro de bordo | `005_STATUS_REVISAO_SEMENTES.md` | Estado atual e proximo passo seguro |

---

## 4) Estado dos ativos principais

| Ativo | Status | Observacao |
|---|---|---|
| `023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md` | Canonico | Fonte unica de ativacao e anti-duplicacao |
| `003_PROTOCOLO_REVISAO_POR_LICAO.md` | Canonico | Execucao do patch e reauditoria alinhadas ao `023` |
| `004_RUBRICA_PREMIUM_REVISAO.md` | Canonico | Rubrica depende da matriz topica e das fronteiras |
| `010_TEMPLATE_SESSAO_DIARIA_REVISAO.md` | Canonico | Template de sessao alinhado ao fluxo atual |
| `011_TOPICOS/` | Canonico | Contratos ativos `001-012` consolidados |
| `012_TRANSVERSAIS/` | Canonico | Pacote minimo transversal ativo |
| Trilha publicada do site | Ativa ate `MV-S-015` | `MV-S-016` em construcao; `MV-S-017+` fora da trilha publicada |
| `024_TASK_ROBUSTA_EXECUCAO_PROTOCOLO_CENTRAL_L001_L002.md` | Feito | Rodada principal de reaplicacao nas licoes `001` e `002` |
| `025_AUDITORIA_FINAL_L001_L002_PROTOCOLO_CENTRAL.md` | Feito | Auditoria final das duas licoes registrada |
| `026_TASK_ROBUSTA_REVISAO_MANUAL_PORTADOR_E_AUDITORIA_FINAL.md` | Feito | Rodada atual documentada |
| `027_DISCUSSAO_MUDANCA_E_MELHORIA_MANUAL_PORTADOR_L000_MOBILE.md` | Feito | Base de decisao para a revisao do manual |
| `028_AUDITORIA_FINAL_GERAL_PROTOCOLO_MANUAL_L001_L002.md` | Feito | Auditoria final consolidada desta rodada |
| `029_TASK_ROBUSTA_REVISAO_IMPECAVEL_L003_L010.md` | Ativa | Task canonica do lote atual `L003-L010` |
| `030_TASK_ROBUSTA_REAUDITORIA_TOTAL_L003_L010_POR_LICAO_COM_EXPERTS.md` | Ativa | Reauditoria rigorosa do lote por licao e com conselho `experts` |
| `048_TASK_ROBUSTA_ENDURECIMENTO_PROTOCOLO_PREMIUM_E_CORTE_PUBLICADO_L015.md` | Feito | Registrou o corte publicado em `L015` e o endurecimento do protocolo de criacao/revisao |
| `049_TASK_ROBUSTA_AUDITORIA_SISTEMICA_REENTRADA_E_COERENCIA_DOCUMENTAL.md` | Feito | Consolidou a ordem canonica de retomada, limpou drift entre `README`, `AI_CONTEXT` e docs vivos, e reforcou escrita interna pratica |
| `MV-S-001` | PASS PREMIUM por IA | Pronta para validacao humana |
| `MV-S-002` | PASS PREMIUM por IA | Pronta para validacao humana |
| `Manual do Portador` | PASS PREMIUM por IA | Abertura mobile-first e anatomia real do metodo consolidadas |

---

## 5) Licoes auditadas e em lote ativo

| Licao | Estado | Observacao |
|---|---|---|
| `MV-S-001_A_TRINDADE_NA_PALMA.html` | Passou pela matriz topica e fronteiras | Pronta para selo humano, com validacao adiada |
| `MV-S-002_AS_PEDRAS_DA_FORTALEZA.html` | Passou pela matriz topica e fronteiras | Pronta para selo humano, com validacao adiada |
| `MV-S-003_A_ESTRELA_DO_REINO.html` | Rodada profunda + feedback real aplicado | Fechada para a rodada atual; reabrir apenas se surgir novo feedback relevante |
| `MV-S-004_A_ORDEM_DO_DIA.html` | Rodada profunda + feedback real aplicado | Fechada para a rodada atual; reabrir apenas se surgir novo feedback relevante |
| `MV-S-005_O_ESCONDERIJO_DA_GLORIA.html` | Em fila de revisao profunda | Entra na Onda 2 da `029` |
| `MV-S-006_O_DESENHO_DO_REI.html` | Em fila de revisao profunda | Entra na Onda 2 da `029` |
| `MV-S-007_A_COROA_DA_SEMANA.html` | Em fila de revisao profunda | Entra na Onda 3 da `029` |
| `MV-S-008_O_PAR_PERFEITO.html` | Em fila de revisao profunda | Entra na Onda 3 da `029` |
| `MV-S-009_O_CELEIRO_DE_NOE.html` | Em fila de revisao profunda | Entra na Onda 4 da `029` |
| `MV-S-010_A_FILA_DA_PROVIDENCIA.html` | Em fila de revisao profunda | Entra na Onda 4 da `029` |

---

## 6) Trilha publicada neste momento
1. o site publicado deve expor somente `MV-S-000` ate `MV-S-015`;
2. `MV-S-016` funciona como pagina de continuidade em construcao, com retorno seguro para `MV-S-015` e para a home;
3. `MV-S-017+` nao entram em cards, navegacao publica nem promessa de continuidade ate nova reconstrucao.

---

## 7) Proximo passo seguro
1. executar a `029_TASK_ROBUSTA_REVISAO_IMPECAVEL_L003_L010.md`;
2. executar a `030_TASK_ROBUSTA_REAUDITORIA_TOTAL_L003_L010_POR_LICAO_COM_EXPERTS.md`;
3. revisar `L005-L010` sob o mesmo metodo e fechar a auditoria transversal;
4. sustentar o protocolo endurecido com passada premium antecipada, radiacao local e passada premium final;
5. so depois encaminhar o bloco para validacao humana posterior da Familia Rodrigues e decidir a volta de `MV-S-016+`.

---

## 8) Regra de manutencao deste quadro
Ao final de cada sessao:
1. atualizar apenas o estado atual;
2. mover memoria detalhada para tasks e auditorias;
3. evitar manter aqui snapshots contraditorios de fases antigas.
