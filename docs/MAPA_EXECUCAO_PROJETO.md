# Mapa de Execucao do Projeto (Sementes AI-First)

- Data de referencia: 2026-02-26
- Escopo desta fase: Sementes (L000 + L001..L120)
- Objetivo: transformar o estado atual em pipeline contrato-first com qualidade publish

---

## 1) Snapshot rapido do estado atual

### 1.1 Arquitetura que esta rodando hoje

- Build principal em Python + YAML + Jinja:
  - `build/forge.py`
  - `build/core/engine.py`
  - `build/fases/sementes.py`
  - `build/fases/raizes.py`
  - `build/fases/landing.py`
- Saida estatica em `site/` com deploy Vercel via rewrite para `/site/*`.
- Conteudo atual:
  - Sementes: 27 YAML (25 validos no dry-run atual por erro em L000)
  - Sementes: 28 HTML em `site/sementes` (inclui extras como `lab_icones.html`)
  - Raizes: 1 YAML e 2 HTML
  - Blog: 5 MD e 5 HTML

### 1.2 Estrategia e governanca ja existentes

- PRD mestre da fase AI-first: `PRD_MESTRE_AI_FIRST_SEMENTES.md`
- Task oficial de execucao iterativa: `logs/TASK_IMPECABILIDADE_PRD_SEMENTES.md`
- Base narrativa/cultural: `LORE/north_star.yaml`
- Camada metodologica multi-agent ativa: `.bmad/`

---

## 2) Arquitetura alvo da fase (definida, nao concluida)

O alvo oficial desta fase e migrar para contrato unico de licao, com variacoes controladas e gates fortes de qualidade.

### 2.1 Entregaveis estruturais obrigatorios (Fase B)

- `contracts/lesson_contract.sementes.yaml`
- `contracts/variant_rules.yaml`
- `contracts/schema_lesson_v1.yaml`

### 2.2 Capacidades obrigatorias do pipeline alvo

- Validacao de contrato e licoes (preview/publish)
- Render HTML mobile-first por contrato
- Print A4 funcional (`print.css`)
- PDF unitario e PDF caderno
- Relatorios obrigatorios por lote:
  - `pending_report.json`
  - `quality_report.json`
  - `variant_report.json`
  - `pdf_report.json`
  - `family_seal_report.json`

---

## 3) Gaps tecnicos confirmados agora

## 3.1 Bloqueadores imediatos (P0)

1. L000 com YAML invalido
- Arquivo: `curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml`
- Impacto: quebra parse e derruba teste de dry-run sem erros.

2. Logger quebra em terminal Windows CP1252 por emoji
- Arquivo: `build/core/logger.py`
- Impacto: `forge.py` pode falhar sem `PYTHONIOENCODING=utf-8`.

3. Bug potencial no driver de Sementes
- Arquivo: `build/fases/sementes.py`
- Problema: uso de `self.logger.warning` sem `self.logger` definido.
- Impacto: caminho de erro pode quebrar com `AttributeError`.

## 3.2 Gaps de produto/arquitetura (P1)

1. Contratos da Fase B ainda inexistentes (`contracts/` nao existe).
2. Estrutura `content/`, `templates/`, `styles/`, `dist/` do PRD ainda nao foi materializada.
3. Relatorios de qualidade no formato da TASK ainda nao existem no pipeline principal.
4. Pipeline de PDF existe (`build/pdf_forge.py`), mas ainda nao esta acoplado ao fluxo contrato-first definido no PRD.

## 3.3 Gaps de qualidade operacional (P2)

1. Testes dependem de `pytest`, que nao esta instalado no ambiente atual.
2. Testes existentes cobrem baseline tecnico, mas ainda nao cobrem gates de publish por score/variant/PDF.
3. Coexistencia de pipelines legados (`tools/*.py`) e pipeline atual (`build/*`) sem consolidacao formal de ownership.

---

## 4) Priorizacao recomendada (execucao real)

## Sprint P0 - Estabilizacao basica (1 a 2 dias)

1. Corrigir YAML da licao L000.
2. Tornar logger resiliente a encoding em Windows.
3. Corrigir `self.logger.warning` para `ForgeLogger.warn` (ou equivalente).
4. Rodar dry-run Sementes e Raizes sem erro.

## Sprint P1 - Fundacao contrato-first (3 a 5 dias)

1. Criar `contracts/lesson_contract.sementes.yaml`.
2. Criar `contracts/variant_rules.yaml`.
3. Criar `contracts/schema_lesson_v1.yaml`.
4. Implementar validadores de contrato/licao em modo `preview` e `publish`.
5. Gerar primeiro `contract_validation_report.json`.

## Sprint P2 - Render + print + PDF + relatorios (5 a 8 dias)

1. Adaptar renderer para ler contrato (sem regra estrutural hardcoded no template).
2. Separar estilo de tela e print (`screen.css` e `print.css`).
3. Integrar PDF no fluxo por escopo (`single`, `bundle`, `full-sementes`).
4. Gerar relatorios obrigatorios da TASK por lote piloto.

## Sprint P3 - Gate real de publicacao (2 a 3 dias)

1. Implementar fluxo de states da licao (`AI_DRAFT` -> `PUBLISHED`).
2. Integrar `family_seal_report.json` como gate final.
3. Definir criterio de bloqueio automatico em `publish`.

---

## 5) Runbook minimo para o time

## 5.1 Comandos atuais (pipeline em producao hoje)

```bash
# Sementes dry-run
python build/forge.py --fase sementes --dry-run

# Raizes dry-run
python build/forge.py --fase raizes --dry-run

# Build completo atual
python build/forge.py --fase all
```

## 5.2 Comandos alvo (apos Fase B/C/D)

```bash
python tools/validate_contract.py
python tools/validate_lessons.py --mode preview
python tools/render_lessons.py --mode preview
python tools/render_pdf.py --scope single --id MV-S-001
python tools/pipeline.py --mode publish
```

---

## 6) Definicao de pronto da fase atual

Esta fase pode ser considerada pronta quando:

1. As licoes Sementes passarem validacao estrutural por contrato.
2. As 3 variantes (`standard`, `portal`, `celebration`) estiverem operacionais em HTML + print + PDF.
3. `publish` bloquear erros estruturais, lore critica e PDF invalido.
4. Relatorios obrigatorios existirem por lote.
5. Gate final por selo familiar estiver ativo no fluxo.

---

## 7) Donos e manutencao do documento

- Dono primario: Engenharia de pipeline (`build/` + futuros `tools/contrato`).
- Dono secundario: Governanca de produto (PRD + TASK).
- Cadencia de atualizacao: semanal ou a cada mudanca de contrato.

## Regra de atualizacao

Sempre que houver mudanca em contrato, validadores, renderizacao, print/PDF ou gate de publish, atualizar este mapa no mesmo PR.
