# CONTINUACAO POS-BACKFILL (PRECHECK 005)
Data: 2026-03-04 20:40 (America/Sao_Paulo)
Contexto: após conclusão e push do backfill 000-004.

---

## 1) Verificacao rapida da licao 005
Arquivos:
1. HTML: `site/sementes/MV-S-005_O_ESCONDERIJO_DA_GLÓRIA.html`
2. YAML: `curriculo/01_SEMENTESV6/005_O_ESCONDERIJO_DA_GLORIA.yaml`

Resultado:
1. YAML `PASS` em parser PyYAML.
2. Navegacao coerente:
- anterior: `MV-S-004`
- proxima: `MV-S-006`
3. Blocos principais presentes no HTML:
- Hero, Preparacao, Jornada, Narracao, Fechamento, Conexao, Formacao do Portador, Nav.
4. Observacao:
- HTML 005 nao expoe secao explicita `Sementes para o Dia` (diferente de 000-003).
- YAML 005 tambem nao possui `sementes_do_dia` atualmente.

Decisao de continuidade:
1. Nao inventar `sementes_do_dia` em 005 sem fonte no HTML (mantido o principio de backfill fiel).
2. Levar 005+ para fase YAML-first (onde decidir padronizacao total de blocos opcionais/obrigatorios).

---

## 2) Proxima frente recomendada
1. Iniciar fase YAML-first em 005-007 com gates:
- Narrativa
- Matematica
- Curricular (CM/CPA)
- Tecnica
- Template
2. Definir regra formal para `sementes_do_dia`:
- opcional por licao, ou
- obrigatoria para todo ciclo Sementes.
3. Se obrigatoria, aplicar migracao controlada em 004+ (sem perder fidelidade do HTML publicado).

