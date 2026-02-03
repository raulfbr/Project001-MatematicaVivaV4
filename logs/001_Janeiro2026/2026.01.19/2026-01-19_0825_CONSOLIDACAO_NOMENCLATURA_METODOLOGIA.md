# CONSOLIDAÇÃO: Nomenclatura e Posicionamento Metodológico
**Data:** 2026-01-19 08:25
**Status:** COMPLETO

## CONTEXTO

O Maestro identificou necessidade de consolidar:
1. Distinção entre "Matemática Viva" (marca pública) e "Forja Viva" (projeto interno)
2. Posicionamento correto do método CPA como criação de Jerome Bruner (não Singapura)

## FONTES CONSULTADAS

| Arquivo | Aprendizado |
|---------|-------------|
| `README.md` | Usava "Singapore Math (CPA)" - necessitava correção |
| `LORE/north_star.yaml` | Já correto: referencia Bruner, não Singapura |
| `logs/2026.01.14/2026-01-14_1203_DELIBERACAO_CURRICULO_ESPIRAL.yaml` | Deliberação clara: "Singapura ADOTOU ideias de Bruner, não inventou" |
| `.bmad/experts/matematica/jerome_bruner.yaml` | Documenta origem correta do CPA |

## DELIBERAÇÃO ENCONTRADA (14/01/2026)

> **NÃO É o mesmo que Método Singapura:**
> - Singapura = CPA (Bruner) + Bar Models + Mastery Approach
> - Espiral = Conceito de Bruner que Singapura USA, mas não inventou

**Fonte:** `logs/2026.01.14/2026-01-14_1203_DELIBERACAO_CURRICULO_ESPIRAL.yaml`, linhas 221-223

## DECISÕES IMPLEMENTADAS

### 1. Nomenclatura (Matemática Viva vs Forja Viva)

| Contexto | Usar |
|----------|------|
| Blog, Redes Sociais, Landing Pages | **Matemática Viva** |
| README.md, Marketing, Comunicação Externa | **Matemática Viva** |
| Código fonte, Logs técnicos, BMAD | **Forja Viva** (aceitável) |

**Arquivo SSOT criado:** `.bmad/experts/comunicacao/embaixador.yaml#naming`

### 2. Posicionamento Metodológico

| ❌ NÃO Dizer | ✅ DIZER |
|-------------|----------|
| "Usamos Método Singapura" | "Usamos CPA de Jerome Bruner" |
| "Singapore Math" | "Jerome Bruner (CPA) — o método que tornou Singapura #1" |

**Razões:**
1. Bruner é o criador intelectual do CPA (1960s, Harvard)
2. Singapura apenas aplicou suas ideias com rigor
3. Honestidade intelectual — dar crédito ao autor real
4. Evita confusão com "currículos Singapura" comerciais

**Arquivo SSOT criado:** `.bmad/experts/comunicacao/embaixador.yaml#metodologia`

## ARQUIVOS ATUALIZADOS

### 1. `.bmad/experts/comunicacao/embaixador.yaml`
- ✅ Adicionada seção `naming` com convenções de nomenclatura
- ✅ Adicionada seção `metodologia` com posicionamento CPA vs Singapura

### 2. `README.md`
- ✅ Linha 39: "Singapore Math (CPA)" → "Jerome Bruner (CPA)"
- ✅ Linha 182: Créditos atualizados

### 3. Artigos de Blog (Markdown)
- ✅ `2026-01-14_por-que-seu-filho-nao-ama-matematica.md` — "Forja Viva" → "Matemática Viva"
- ✅ `2026-01-15_a-mentira-ser-de-exatas.md` — "Forja Viva" → "Matemática Viva"
- ✅ `2026-01-19_matematica-em-20-minutos.md` — "Forja Viva" → "Matemática Viva"
- ✅ `2026-01-19_para-quem-e-matematica-viva.md` — "Forja Viva" → "Matemática Viva"

### 4. Artigos de Blog (HTML)
- ✅ Todos os 5 HTMLs atualizados correspondentemente

## LOCALIZAÇÃO DAS DEFINIÇÕES (SSOT)

| Definição | Local SSOT |
|-----------|------------|
| Nomenclatura marca vs projeto | `.bmad/experts/comunicacao/embaixador.yaml#naming` |
| Posicionamento CPA/Bruner | `.bmad/experts/comunicacao/embaixador.yaml#metodologia` |
| Currículo Espiral | `LORE/curriculo_espiral.yaml` (referenciado) |
| Bruner CPA detalhado | `.bmad/experts/matematica/jerome_bruner.yaml` |
| Deliberação original | `logs/2026.01.14/2026-01-14_1203_DELIBERACAO_CURRICULO_ESPIRAL.yaml` |

## VERIFICAÇÃO

O `north_star.yaml` NÃO precisa de alteração — já está correto:
- Linha 176: `matematica: [Jerome Bruner (CPA), Lev Vygotsky (Scaffolding)]`
- Nenhuma menção a "Singapura" no arquivo

---

**Log encerrado:** 2026-01-19 08:30
**Próximos passos:** Deploy quando solicitado
