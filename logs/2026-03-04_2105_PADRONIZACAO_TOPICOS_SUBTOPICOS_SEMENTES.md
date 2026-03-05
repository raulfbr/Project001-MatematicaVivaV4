# PADRONIZACAO DE TOPICOS E SUBTOPICOS - SEMENTES
Data: 2026-03-04 21:05 (America/Sao_Paulo)
Motivacao: consolidar um padrao unico para identificar topico/subtopico em todas as licoes.

---

## 1) Decisao de arquitetura
1. Manter `Revisao/padrao_visual_sementes.md` como SSOT principal.
2. Transformar a secao de estrutura em contrato auditavel com IDs (T0-T9).
3. Manter `Revisao/topicos_licao_revisao.md` como checklist operacional subordinado ao SSOT.

---

## 2) Alteracoes aplicadas
1. `Revisao/padrao_visual_sementes.md`
   - adicionada secao 18.1: contrato canonico de topicos/subtopicos (T0-T9);
   - adicionada secao 18.2: nomenclatura fixa dos titulos de secao;
   - adicionada secao 18.3: regra objetiva de completude (PASS/FAIL estrutural);
   - atualizacao do path de compliance para `bmad/orchestrator.yaml`.

2. `Revisao/topicos_licao_revisao.md`
   - adicionada nota de prioridade normativa (em conflito, vence `padrao_visual_sementes.md`);
   - checklist rapido passou a exigir contrato T0-T9;
   - snippet de header superior atualizado para formato canonico (anterior | sementes | proxima).

---

## 3) Ganho pratico
1. Revisao deixa de ser subjetiva: cada licao agora pode ser auditada por IDs (T0-T9).
2. Topico e subtopico ficam unificados em um contrato claro e repetivel.
3. Reducao de retrabalho por ambiguidade entre documentos de revisao.

---

## 4) Proximo passo recomendado
1. Rodar auditoria estrutural 001-010 usando T0-T9 e gerar matriz PASS/FAIL por licao.
2. Corrigir primeiro as licoes com FAIL em T0 (header superior) e T4/T7 (conexao/sementes do dia).
