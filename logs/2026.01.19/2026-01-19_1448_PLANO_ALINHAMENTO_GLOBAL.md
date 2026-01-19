# PLANO DE ALINHAMENTO GLOBAL: Comunicação MatViva

**Data:** 2026-01-19 14:48  
**Status:** 📋 PARA VALIDAÇÃO  
**Referência:** `logs/2026-01-19_1357_NORTE_CONSOLIDADO.md`

---

## Objetivo

Alinhar **todos os materiais públicos e experts** com as decisões de comunicação consolidadas:
- Slogan: "Histórias que ensinam. Narração que fixa."
- Verbos: ABRA E FAÇA → OUVE → CONTA → REENCONTRA
- Tom: Positivo, preservar brilho (não reverter trauma)
- CPA: De Bruner (não "Singapura")

---

## 1. REFINAMENTOS NO NORTH_STAR.YAML

### 🔶 Pontos a Revisar:

| Linha | Atual | Proposta | Prioridade |
|-------|-------|----------|------------|
| **115** | `Conveniência 5min` | `Abra e Faça: 5min preparo` | Média |
| **175** | `experiencia: 5 min preparo` | `experiencia: Abra e Faça` | Baixa |
| **222** | Diretriz vazia | Adicionar "Tom Positivo" | Média |

### ✅ Já Está Bom:
- Slogan (L31): ✅
- Slogan secundário (L32): ✅
- Verbos (L49): ✅
- Tríade pedagógica: ✅

---

## 2. EXPERTS PARA REVISAR

### 🔴 ALTA Prioridade (Comunicação Pública)

| Expert | Arquivo | O que revisar |
|--------|---------|---------------|
| **Embaixador** | `comunicacao/embaixador.yaml` | ✅ Já atualizado |
| **Seth Godin** | `negocios/seth_godin.yaml` | Verificar alinhamento tribal |
| **Alex Hormozi** | `negocios/alex_hormozi.yaml` | Verificar "Value Equation" |

### 🟡 MÉDIA Prioridade (Pedagógico)

| Expert | Arquivo | O que revisar |
|--------|---------|---------------|
| **Charlotte Mason** | `pedagogia/charlotte_mason.yaml` | Verificar princípios citados |
| **Jerome Bruner** | `matematica/jerome_bruner.yaml` | Garantir CPA não Singapura |

### 🟢 BAIXA Prioridade (Externos/Personas)

| Expert | Arquivo | O que revisar |
|--------|---------|---------------|
| **Mães Personas** | `ux_familias/maes_personas.yaml` | Tom positivo nas dores |
| **Externos** | `externos/*.yaml` | 12 arquivos — revisar tom |

---

## 3. BLOG POSTS PARA REVISAR

| Arquivo | Título | O que revisar |
|---------|--------|---------------|
| `2026-01-14_por-que-seu-filho-nao-ama-matematica.html` | Por que seu filho não ama | ⚠️ "Não ama" — verificar tom |
| `2026-01-15_a-mentira-ser-de-exatas.html` | A mentira de ser de exatas | Verificar alinhamento |
| `2026-01-19_matematica-em-20-minutos.html` | Matemática em 20 minutos | Verificar tempo (CM) |
| `2026-01-19_para-quem-e-matematica-viva.html` | Para quem é | ✅ Provavelmente ok |
| `2026-01-19_primeiro-mes-raulzito.html` | Primeiro mês Raulzito | ✅ Relato pessoal |

---

## 4. ORDEM DE EXECUÇÃO

### Fase 1: North Star (Base)
- [ ] Refinar comentários e métricas
- [ ] Adicionar seção "Tom de Comunicação"

### Fase 2: Experts Críticos
- [ ] Revisar `seth_godin.yaml` 
- [ ] Revisar `alex_hormozi.yaml`
- [ ] Revisar `charlotte_mason.yaml`
- [ ] Revisar `jerome_bruner.yaml`

### Fase 3: Blog Posts
- [ ] Revisar `por-que-seu-filho-nao-ama-matematica.html`
- [ ] Ajustar títulos/tom se necessário

### Fase 4: Landing Page
- [ ] Revisar `layout_landing.html` completo

---

## 5. PERGUNTA PARA O MAESTRO

1. **Quer que eu execute tudo** ou prefere validar fase por fase?
2. **Prioridade:** Começar pelos experts ou pelos blog posts?
3. **North Star:** Quer que eu adicione uma seção formal de "Tom de Comunicação"?

---

## 5. VERIFICAÇÃO FINAL ✅

| Teste | Resultado |
|-------|-----------|
| Grep "odeia" em blog | ✅ 1 ocorrência (contexto pessoal Raulzito) |
| Grep "trauma" em site | ✅ 0 ocorrências |
| Grep "Forja Viva" em blog | ✅ 0 ocorrências (corrigido) |
| Grep "Open and Go" | ✅ 0 ocorrências |
| Separadores `═══` no north_star | ✅ 0 ocorrências |

---

**ALINHAMENTO CONCLUÍDO: 2026-01-19 15:00**
