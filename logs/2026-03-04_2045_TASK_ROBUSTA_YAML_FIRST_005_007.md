# TASK ROBUSTA V1 — FASE YAML-FIRST (005-007)
Data: 2026-03-04 20:45 (America/Sao_Paulo)
Escopo inicial: `MV-S-005` a `MV-S-007`
Objetivo: elevar a qualidade editorial/técnica das lições a partir do YAML (fonte de verdade), mantendo compatibilidade com o HTML publicado.

---

## 1) Contexto consolidado
1. Backfill 000-004 foi concluído e validado.
2. `_TEMPLATE_V6.yaml` foi atualizado para V6.5 (YAML estrito + alinhamento com padrão real).
3. Precheck 005 foi concluído e indicou base estável para iniciar fase YAML-first.

Referências obrigatórias:
1. `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml`
2. `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md`
3. `Revisao/padrao_visual_sementes.md`
4. `logs/2026-03-04_2040_CONTINUACAO_POS_BACKFILL_005_PRECHECK.md`

---

## 2) Princípios da fase YAML-first
1. YAML é a fonte primária de decisão.
2. HTML é referência de consistência visual e narrativa, não autoridade de conteúdo nesta fase.
3. Não quebrar rotas/links já publicados.
4. Evitar deriva de schema: só evoluir estrutura com justificativa e registro.
5. Toda mudança deve passar em cinco gates (`Narrativa`, `Matemática`, `Curricular`, `Técnica`, `Template`).

---

## 3) Ordem de execução inteligente
1. `MV-S-005` (posição espacial — transição pós 000-004).
2. `MV-S-006` (continuidade direta de 005).
3. `MV-S-007` (consolidação de progressão para 008+).

---

## 4) Protocolo operacional por lição
### Passo A — Diagnóstico YAML (fonte primária)
1. Ler YAML completo da lição.
2. Marcar aderência ao template V6.5:
- chaves obrigatórias presentes,
- campos opcionais usados com consistência,
- linguagem e tom adequados.
3. Marcar riscos:
- inconsistência de narrativa,
- objetivos matemáticos vagos,
- linkage fraco,
- campos com sintaxe frágil.

Saída A:
1. Matriz `OK/AJUSTAR/BLOCK` por bloco.

### Passo B — Verificação de consistência com HTML
1. Conferir Hero, Jornada, Narração, Fechamento, Navegação.
2. Identificar divergências materiais (não cosméticas).
3. Decidir:
- manter YAML (se estiver melhor e fiel ao currículo),
- ou ajustar YAML para corrigir desvio.

Saída B:
1. Lista de divergências e decisão por item.

### Passo C — Refino pedagógico (CM + CPA + Currículo Mestre)
1. Confirmar fase concreta dominante.
2. Verificar progressão da estação.
3. Checar linguagem de acolhimento do Portador.
4. Garantir fio de ouro para a próxima lição.

Saída C:
1. Ajustes pedagógicos aplicados.

### Passo D — Higiene técnica YAML
1. Validar parser.
2. Buscar inline maps frágeis (valores com vírgula sem aspas).
3. Confirmar ausência de campos críticos vazios.

Comandos padrão:
```powershell
@'
import pathlib, yaml
yaml.safe_load(pathlib.Path('curriculo/01_SEMENTESV6/00X_*.yaml').read_text(encoding='utf-8'))
print('PASS')
'@ | python -
```

Saída D:
1. `PASS` ou `BLOCK` técnico.

### Passo E — Registro de decisão
1. Resumo objetivo.
2. Risco residual.
3. Próxima ação da sequência.

Formato:
`L00X | Narrativa: PASS/BLOCK | Matematica: PASS/BLOCK | Curricular: PASS/BLOCK | Tecnica: PASS/BLOCK | Template: PASS/BLOCK | Status: APROVADA/BLOCK`

---

## 5) Critérios de aprovação por lição
1. Objetivo matemático claro e operacional.
2. Jornada com ações executáveis por adulto.
3. Narrativa coesa com guardião/local/virtude.
4. Navegação e linkage corretos.
5. YAML estrito e semanticamente limpo.
6. Template V6.5 respeitado.

---

## 6) Regra para `sementes_do_dia` nesta fase
1. Se existir no HTML e fizer sentido pedagógico: manter/adicionar no YAML.
2. Se não existir no HTML:
- não inventar automaticamente;
- decidir por inclusão apenas se houver ganho pedagógico claro e sem ruptura de tom.
3. Toda inclusão deve ser registrada com justificativa.

---

## 7) Entregáveis desta fase (005-007)
1. YAMLs 005, 006 e 007 revisados e validados.
2. Relatório de execução por lição.
3. Quadro de bordo consolidado 005-007.
4. Decisão formal sobre adoção de `sementes_do_dia` como opcional ou padrão.

---

## 8) Quadro de bordo (preencher durante execução)
```md
| Licao | Narrativa | Matematica | Curricular | Tecnica | Template | Status |
|------|-----------|------------|------------|---------|----------|--------|
| 005  | PASS      | PASS       | PASS       | PASS    | PASS     | APROVADA |
| 006  | PASS      | PASS       | PASS       | PASS    | PASS     | APROVADA |
| 007  | PASS      | PASS       | PASS       | PASS    | PASS     | APROVADA |
```
