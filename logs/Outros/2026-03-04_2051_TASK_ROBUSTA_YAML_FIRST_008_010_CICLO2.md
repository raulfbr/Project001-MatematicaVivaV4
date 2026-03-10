# TASK ROBUSTA - YAML-FIRST 008-010 (CICLO 2)
Data: 2026-03-04 20:51 (America/Sao_Paulo)
Escopo: `MV-S-008`, `MV-S-009`, `MV-S-010`
Modo: Refino premium em YAML (narrativo + matematico + tecnico), mantendo encadeamento curricular.

---

## 1) Objetivo operacional
Elevar as licoes 008-010 para padrao premium no YAML, com:
1. narrativa mais imersiva e menos imperativa,
2. alinhamento explicito ao curriculo mestre (L8-L10),
3. consistencia com template V6.5 e com `Revisao/padrao_visual_sementes.md`,
4. seguranca tecnica (YAML estrito, sem armadilhas semanticas).

---

## 2) Fontes de verdade obrigatorias
1. `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md`
2. `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml`
3. `Revisao/padrao_visual_sementes.md`
4. `Revisao/framework_estrategia_mestria.md`
5. `bmad/orchestrator.yaml` (gates de revisao e veto CM/CPA/template)
6. `bmad/experts/pedagogia/charlotte_mason.yaml`

---

## 3) Regra de decisao para este ciclo
Como este ciclo e YAML-first (nao backfill fiel), aplicar melhoria editorial e pedagógica quando:
1. aumentar clareza para o Portador,
2. reforcar aprendizado matematico concreto,
3. nao quebrar o fio narrativo da trilha 008 -> 009 -> 010 -> 011,
4. nao violar tempo/preparo e principios CM.

---

## 4) Gates de qualidade (DoD do ciclo)

### Gate A - Meta/CM (Charlotte)
Checklist:
1. licao curta (15-20 min), preparo <= 5 min.
2. crianca tratada com dignidade (sem medo/culpa).
3. narrativa viva (sem "dry facts").
4. bloco de narracao presente.
5. linguagem inclusiva + adaptacao_bernardo.

### Gate B - Narrativa Premium
Checklist:
1. hook alinhado ao curriculo mestre L8/L9/L10.
2. tom gentil e nobre (reduzir caixa alta e infantilizacao).
3. continuidade dramatica entre licoes.
4. texto de condução acionavel para pais novatos.

### Gate C - Matematica/CPA
Checklist:
1. concreto domina a licao (things before signs).
2. abstrato minimo e tardio.
3. progresso conceitual claro:
   - 008: correspondencia 1:1
   - 009: quantidades 8-9
   - 010: ordinais 1o ao 5o

### Gate D - Template/YAML
Checklist:
1. parser YAML PASS.
2. sem mapas inline arriscados em blocos longos.
3. navegacao e linkage coerentes.
4. chaves principais preservadas.
5. `sementes_do_dia` com framework de 5 atividades no padrao atual.

### Gate E - Produto Premium
Checklist:
1. portador sai com acao concreta para o dia.
2. licao e memoravel (imagem + acao + frase-forca).
3. math learning e explicitamente perceptivel pela familia.

---

## 5) Plano de execucao (passo a passo)
1. Auditar 008-010 linha a linha contra os 5 gates.
2. Aplicar refino textual e estrutural nos YAML.
3. Incluir `sementes_do_dia` nas 3 licoes (5 blocos).
4. Normalizar `materiais` e `pictorico` em formato YAML estrito.
5. Atualizar metadados para versao 6.5 nas 3 licoes revisadas.
6. Rodar validacao automatica:
   - parse global `curriculo/01_SEMENTESV6/*.yaml`,
   - auditoria semantica de `materiais`,
   - sanity check de navegacao.
7. Registrar log de execucao com PASS/WARN por gate.
8. Commit seletivo e push.

---

## 6) Riscos e mitigacoes
1. Risco: tom excessivamente performatico e menos pratico.
   Mitigacao: manter instrucoes curtas e acionaveis para o Portador.
2. Risco: mudanca editorial distanciar do HTML publicado.
   Mitigacao: registrar claramente que e ciclo YAML-first (fonte para proxima geracao HTML).
3. Risco: erro YAML silencioso.
   Mitigacao: parse automatizado de todos os arquivos e checagem de mapas.

---

## 7) Entregaveis do ciclo
1. YAML 008-010 revisados.
2. Log de execucao detalhado do ciclo 2.
3. Commit com mensagem tecnica detalhada.
