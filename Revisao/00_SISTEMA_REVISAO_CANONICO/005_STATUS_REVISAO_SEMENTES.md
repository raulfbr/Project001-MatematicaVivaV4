# STATUS DA REVISAO SEMENTES
Data base: 2026-03-10
Status geral: protocolo central consolidado em `023`; `Manual do Portador`, `MV-S-001` e `MV-S-002` passaram pela rodada profunda atual e estao prontos para validacao humana da Familia Rodrigues

---

## 1) Objetivo deste quadro
Este arquivo e o quadro de bordo da fase atual.

Ele serve para:
1. mostrar em que estado o sistema de revisao esta;
2. indicar quais licoes ja passaram pelo protocolo central;
3. registrar o proximo passo seguro sem recontar toda a historia do projeto.

Regra:
1. este arquivo mostra o estado atual;
2. memoria detalhada fica nas tasks e auditorias historicas;
3. se uma regra procedural mudar, ela deve mudar primeiro no `023`, nao aqui.

---

## 2) Estado atual da fase
Fase ativa:
1. protocolo topico a topico centralizado em fonte unica;
2. `MV-S-001` e `MV-S-002` revisitadas contra esse protocolo;
3. `Manual do Portador` reescrito na abertura para alinhar `Licao 000`, mobile-first e impressao opcional;
4. preparacao para validacao humana final da Familia Rodrigues.

Antes de escalar revisao em lote:
1. colher o selo humano da Familia Rodrigues sobre `MV-S-001` e `MV-S-002`;
2. registrar qualquer ajuste real de uso que aparecer;
3. so depois decidir a entrada de `MV-S-003` e do piloto mais amplo.

---

## 3) Fontes canonicas desta camada

| Camada | Fonte atual | Funcao |
|---|---|---|
| Ativacao do protocolo | `023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md` | Ordem de leitura, cerne macro, algoritmo e anti-duplicacao |
| Execucao da revisao | `003_PROTOCOLO_REVISAO_POR_LICAO.md` | Patch, reauditoria, gates e formato de log |
| Veredito | `004_RUBRICA_PREMIUM_REVISAO.md` | Pontuacao e bloqueios objetivos |
| Registro da sessao | `010_TEMPLATE_SESSAO_DIARIA_REVISAO.md` | Template preenchivel para cada rodada |
| Contratos dos blocos | `011_TOPICOS/` | Regras topico por topico |
| Regras transversais | `012_TRANSVERSAIS/` | HTML, tom, pedagogia, encoding e North Star |
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
| `024_TASK_ROBUSTA_EXECUCAO_PROTOCOLO_CENTRAL_L001_L002.md` | Feito | Rodada principal de reaplicacao nas licoes `001` e `002` |
| `025_AUDITORIA_FINAL_L001_L002_PROTOCOLO_CENTRAL.md` | Feito | Auditoria final das duas licoes registrada |
| `026_TASK_ROBUSTA_REVISAO_MANUAL_PORTADOR_E_AUDITORIA_FINAL.md` | Feito | Rodada atual documentada |
| `027_DISCUSSAO_MUDANCA_E_MELHORIA_MANUAL_PORTADOR_L000_MOBILE.md` | Feito | Base de decisao para a revisao do manual |
| `028_AUDITORIA_FINAL_GERAL_PROTOCOLO_MANUAL_L001_L002.md` | Feito | Auditoria final consolidada desta rodada |
| `MV-S-001` | PASS PREMIUM por IA | Pronta para validacao humana |
| `MV-S-002` | PASS PREMIUM por IA | Pronta para validacao humana |
| `Manual do Portador` | PASS PREMIUM por IA | Abertura mobile-first e anatomia real do metodo consolidadas |

---

## 5) Licoes auditadas neste estado

| Licao | Estado | Observacao |
|---|---|---|
| `MV-S-001_A_TRINDADE_NA_PALMA.html` | Passou pela matriz topica e fronteiras | Pronta para selo humano |
| `MV-S-002_AS_PEDRAS_DA_FORTALEZA.html` | Passou pela matriz topica e fronteiras | Pronta para selo humano |
| `MV-S-003` | Ainda nao entrou em rodada final | Espera validacao humana de `001` e `002` |

---

## 6) Proximo passo seguro
1. colher validacao humana da Familia Rodrigues;
2. registrar qualquer ajuste real de uso;
3. atualizar o status com o que a validacao humana confirmar;
4. so depois decidir a entrada de `MV-S-003`.

---

## 7) Regra de manutencao deste quadro
Ao final de cada sessao:
1. atualizar apenas o estado atual;
2. mover memoria detalhada para tasks e auditorias;
3. evitar manter aqui snapshots contraditorios de fases antigas.
