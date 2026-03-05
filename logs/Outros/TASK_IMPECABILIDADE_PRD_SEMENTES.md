# TASK Robusta - Impecabilidade do PRD e Execucao Sementes

- Versao: `v1.0`
- Data: `2026-02-26`
- Documento alvo: `PRD_MESTRE_AI_FIRST_SEMENTES.md`
- Objetivo: elevar o sistema para padrao premium operacional com revisao iterativa ate satisfacao maxima

---

## 1) Objetivo da TASK

Executar um ciclo continuo de melhoria do PRD e da implementacao com:

1. Clareza total de regras.
2. Eliminacao de ambiguidades.
3. Estrutura unificada para 121 licoes.
4. Saida mobile + impressao + PDF funcional.
5. Qualidade controlada por score e gates.

---

## 2) Definicao de Sucesso

Esta TASK e concluida quando:

1. PRD mestre estabilizado sem pendencias criticas.
2. Contrato estrutural implementado e versionado.
3. Pipeline gera HTML/PDF com qualidade minima validada.
4. Variantes `standard`, `portal`, `celebration` operacionais.
5. Relatorios de qualidade implementados.
6. Fluxo de Selo Familia Rodrigues funcionando.

---

## 3) Ciclo de Trabalho (Loop Impecabilidade)

Cada ciclo deve seguir:

1. Diagnosticar
2. Corrigir
3. Expandir
4. Validar
5. Registrar
6. Decidir proximo ciclo

Regra:

1. Nunca acumular mudancas sem relatorio de impacto.
2. Nunca publicar com erro estrutural.

---

## 4) Fase A - Auditoria Estrutural do PRD

### A.1 Checklist

- [ ] Verificar consistencia entre secoes (sem contradicao de regra).
- [ ] Validar nomenclatura padrao (`publish`, `preview`, `overrides`, `variant`).
- [ ] Confirmar precedencia documental e SSOT.
- [ ] Confirmar que todo requisito tem criterio de validacao.
- [ ] Confirmar que todos os gates estao mensuraveis.

### A.2 Saida obrigatoria

- `reports/prd_audit_report.md`

### A.3 Critico bloqueador

- Contradicao entre gate e fluxo de publish.

---

## 5) Fase B - Contrato de Licao (Implementacao)

### B.1 Entregaveis

- [ ] `contracts/lesson_contract.sementes.yaml`
- [ ] `contracts/variant_rules.yaml`
- [ ] `contracts/schema_lesson_v1.yaml`

### B.2 Checklist

- [ ] Blocos obrigatorios definidos.
- [ ] Ordem global definida.
- [ ] Alias/deprecacao definidos.
- [ ] Regras de print por bloco definidas.
- [ ] Politica de bloqueio em `publish` definida.

### B.3 Saida obrigatoria

- `reports/contract_validation_report.json`

---

## 6) Fase C - Normalizacao das 121 Licoes

### C.1 Checklist

- [ ] Mapear L000..L120.
- [ ] Garantir `meta`, `lore`, `blocks`, `review` em todas.
- [ ] Aplicar `variant` inicial.
- [ ] Registrar pendencias por bloco.
- [ ] Resolver campos obrigatorios faltantes para lote piloto.

### C.2 Saidas obrigatorias

- `reports/pending_report.json`
- `reports/variant_report.json`

### C.3 Critico bloqueador

- Qualquer licao sem `id`, `titulo`, `variant`, `status`.

---

## 7) Fase D - Renderer Mobile-First

### D.1 Checklist

- [ ] Template base funcional.
- [ ] Blocos renderizando por contrato.
- [ ] Variantes aplicadas sem hardcode por licao.
- [ ] Sem overflow horizontal em 360px.
- [ ] Navegacao clara entre licoes.

### D.2 Saida obrigatoria

- `reports/mobile_qa_report.json`

---

## 8) Fase E - Impressao A4 + PDF

### E.1 Checklist Print

- [ ] `styles/print.css` ativo e funcional.
- [ ] Presets `print_standard` e `print_compact`.
- [ ] Sem cortes/sobreposicoes.
- [ ] Texto completo preservado.

### E.2 Checklist PDF

- [ ] PDF unitario por licao.
- [ ] PDF caderno por faixa.
- [ ] PDF caderno completo.
- [ ] Qualidade minima aprovada no checklist.

### E.3 Saida obrigatoria

- `reports/pdf_report.json`

### E.4 Critico bloqueador

- PDF com texto ilegivel.

---

## 9) Fase F - QA Narrativo e Selo Familiar

### F.1 Checklist

- [ ] Revisao de falas por Raul/Marina.
- [ ] Aplicacao real com filho.
- [ ] Registro da classificacao (`aprovado`, `aprovado_com_ajustes`, `reprovado`).
- [ ] Ajustes reaplicados quando necessario.

### F.2 Saida obrigatoria

- `reports/family_seal_report.json`

### F.3 Critico bloqueador

- Ausencia de selo em licao candidata a publish.

---

## 10) Fase G - Publish e Rollback

### G.1 Checklist publish

- [ ] Todos os gates verdes.
- [ ] Score por licao >= 90.
- [ ] Score medio do lote >= 90.
- [ ] Nenhuma licao < 80.
- [ ] Relatorios consolidados arquivados.

### G.2 Checklist rollback

- [ ] Snapshot do ultimo build estavel.
- [ ] Procedimento de rollback testado.
- [ ] Causa raiz registrada quando rollback ocorrer.

---

## 11) Matriz de Severidade

1. `error`: bloqueia publish.
2. `warning`: nao bloqueia preview; regra de publish definida no contrato.
3. `info`: informativo.

---

## 12) Cadencia Recomendada

1. Diaria: executar preview + corrigir pendencias novas.
2. Semanal: fechar lote de melhoria (estrutura + qualidade).
3. Quinzenal: revisao profunda de contrato e variantes.
4. Mensal: auditoria de produto premium com selo familiar ampliado.

---

## 13) Indicadores de Progresso

1. `% licoes com contrato valido`
2. `% licoes com variant definida`
3. `% licoes com score >= 90`
4. `% licoes com selo aprovado`
5. `% licoes com PDF aprovado`

---

## 14) Comandos Operacionais (Referencia)

```bash
python tools/validate_contract.py
python tools/validate_lessons.py --mode preview
python tools/render_lessons.py --mode preview
python tools/render_pdf.py --scope single --id MV-S-001
python tools/render_pdf.py --scope bundle --from MV-S-001 --to MV-S-010
python tools/render_pdf.py --scope full-sementes
python tools/pipeline.py --mode publish
```

---

## 15) Ordem Inteligente de Execucao (Recomendada)

1. A -> B -> C (base estrutural)
2. D -> E (entrega para mae: mobile + papel)
3. F -> G (qualidade real e publicacao)
4. Repetir ciclo com foco em pendencias e score

---

## 16) Regra Final de Impecabilidade

Se houver duvida entre velocidade e qualidade:

1. priorizar qualidade estrutural e clareza para a familia
2. publicar menos, porem melhor
3. manter consistencia do Reino em todas as licoes

---

## 17) Priorizacao Inteligente (WSJF simplificado)

Ao escolher o proximo ajuste, priorizar:

1. Impacto alto no usuario (mae/pai/crianca)
2. Risco alto se nao corrigir
3. Esforco baixo ou medio

Ordem recomendada:

1. Quebra estrutural
2. Problema de impressao/PDF
3. Problema de legibilidade mobile
4. Ajuste de narrativa
5. Refino estético

---

## 18) Gatilhos de Escalacao

Escalar imediatamente quando ocorrer:

1. Falha repetida de PDF em 2 ciclos seguidos.
2. Reprovacao familiar repetida da mesma licao.
3. Queda de score medio do lote abaixo de 90.
4. Aumento de pendencias criticas apos mudanca de contrato.

---

## 19) Template de Revisao por Licao

Para cada licao revisada, registrar:

1. `id`
2. `variant`
3. `score_total`
4. `status_gate` (pass/fail)
5. `principais_ajustes`
6. `decisao_familia` (aprovado/aprovado_com_ajustes/reprovado)
7. `proximo_passo`

---

## 20) Encerramento da TASK

A TASK entra em modo manutencao quando:

1. pipeline estabilizado por 3 ciclos consecutivos
2. score medio >= 90 por 3 ciclos
3. 0 erros criticos em publish por 3 ciclos
4. taxa de selo aprovado no lote piloto em nivel satisfatorio
