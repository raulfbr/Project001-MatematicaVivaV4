# DISCUSSÃO: _TEMPLATE_V6.yaml — Ajustes Necessários?

**Data:** 16/01/2026 14:11
**Status:** 📋 Aguardando decisão do Maestro
**Objetivo:** Definir se o YAML fonte precisa de ajustes para ficar "impecável"

---

## 🔑 PRINCÍPIO CENTRAL

> **"Se arrumarmos o template fonte (YAML), ele fica impecável e não precisa ser mudado direito."**

Isso é **100% correto**. O YAML é a **Single Source of Truth (SSOT)**. Se ele estiver perfeito, o Jinja2 só renderiza — sem lógica condicional complexa.

---

## 📊 ANÁLISE DO TEMPLATE V6.3

### Campos que **JÁ ESTÃO OK** no YAML

| Campo | Status | Razão |
|:---|:---|:---|
| `para_familia.metodo_cpa` | ✅ | Estrutura com concreto/pictorico/abstrato/nota |
| `para_familia.principio_cm` | ✅ | Estrutura com numero/citacao/aplicacao |
| `para_familia.tgtb_conexao` | ✅ | String simples |
| `para_familia.espiral` | ✅ | Estrutura com conceito/volta_atual/proxima_volta/nota |
| `para_familia.reflexao_espiritual` | ✅ | String simples |
| `para_familia.nota_graca` | ✅ | String simples |
| `ritual_abertura.fala_portador.tom` | ✅ | Já aceita "segredo", "animado", etc. |

### Campos PROBLEMÁTICOS

| Campo | Linha | Problema | Decisão Necessária |
|:---|:---|:---|:---|
| `jornada.concreto.norte_absoluto` | 86 | Removemos do HTML. O que fazer no YAML? | 🔴 |
| `ritual_fechamento.fio_ouro` | 100 | Removemos do HTML. O que fazer no YAML? | 🔴 |
| `preparacao.materiais[].essencial` | 58 | Removemos ⭐ do HTML. Manter campo? | 🟡 |
| `navegacao_inferior` | 117-119 | Duplicação com `navegacao` (L43-45) | 🟡 |

---

## 🔴 DECISÕES CRÍTICAS

### 1. `norte_absoluto` (Linha 86)

**Situação Atual:**
```yaml
jornada:
  concreto:
    norte_absoluto: A maior parte da lição acontece aqui. Manipulação é onde a mágica vive.
```

**Problema:** Removemos do HTML porque:
- É uma instrução para o criador da lição, não para o Portador
- Já está implícito na estrutura da lição

**Opções:**

| Opção | Ação | Impacto |
|:---|:---|:---|
| A | **MANTER no YAML, NÃO RENDERIZAR** | Zero mudança no YAML. Template ignora. |
| B | **MOVER para `_meta`** | Semântica correta: é meta-informação |
| C | **REMOVER do template** | Lições existentes perdem o campo |

**Recomendação:** Opção A (menos invasivo)

---

### 2. `fio_ouro` (Linha 100)

**Situação Atual:**
```yaml
ritual_fechamento:
  fio_ouro: '[Conexão explícita com próxima jornada]'
```

**Problema:** Removemos do HTML porque:
- Duplica `linkage.proximo.gancho`
- Confunde "próxima aventura" com "próxima lição"

**Opções:**

| Opção | Ação | Impacto |
|:---|:---|:---|
| A | **MANTER no YAML, NÃO RENDERIZAR** | Zero mudança. Template ignora. |
| B | **DEPRECAR** | Adicionar `deprecated: true` |
| C | **UNIFICAR com linkage** | Usar `linkage.proximo.gancho` em vez disso |

**Recomendação:** Opção C (unificação SSOT)

---

### 3. `materiais[].essencial` (Linha 58)

**Situação Atual:**
```yaml
preparacao:
  materiais:
    - {item: nome, qtd: numero, alt: alternativa, essencial: true/false}
```

**Problema:** Removemos ⭐ do HTML por feedback visual

**Opções:**

| Opção | Ação | Impacto |
|:---|:---|:---|
| A | **MANTER campo, não usar no template** | Metadata útil para filtros futuros |
| B | **REMOVER campo** | Simplifica, perde informação |

**Recomendação:** Opção A (metadata útil)

---

### 4. `navegacao_inferior` (Linha 117-119)

**Situação Atual:**
```yaml
navegacao:          # L43
  anterior: ...
  proxima: ...

navegacao_inferior: # L117
  anterior: ...
  proxima: ...
```

**Problema:** Duplicação clara. Viola DRY.

**Opções:**

| Opção | Ação | Impacto |
|:---|:---|:---|
| A | **REMOVER `navegacao_inferior`** | SSOT: usar só `navegacao` |
| B | **MANTER ambos** | Permite navegação diferente topo/base |

**Recomendação:** Opção A (SSOT)

---

## 📝 RESUMO DAS RECOMENDAÇÕES

| Campo | Decisão Recomendada | Ação no YAML |
|:---|:---|:---|
| `norte_absoluto` | Manter, não renderizar | Nenhuma |
| `fio_ouro` | Unificar com linkage | Deprecar ou remover |
| `materiais[].essencial` | Manter como metadata | Nenhuma |
| `navegacao_inferior` | Remover (duplicação) | Remover seção |

---

## ⚠️ IMPACTO NAS LIÇÕES EXISTENTES

Se mudarmos o template fonte:

| Lição | Tem `fio_ouro`? | Tem `navegacao_inferior`? |
|:---|:---|:---|
| MV-S-001 | ✅ Sim | ✅ Sim |
| MV-S-002 | ✅ Sim | ✅ Sim |

**Risco:** Se removermos campos usados, precisamos atualizar as lições.

---

## 🎯 DECISÕES DO MAESTRO (16/01/2026 14:24)

### 1. `norte_absoluto` → ✅ OPÇÃO A (MANTER, NÃO RENDERIZAR)

**Justificativa do Maestro:**
> "Como usaremos o template Sementes para Raízes1, talvez fica de alguma informação para 'evolução' do template."

**Ação:** Nenhuma mudança no YAML. Template Jinja2 já não renderiza.

---

### 2. `fio_ouro` → ✅ OPÇÃO C (UNIFICAR COM LINKAGE)

**Ação Necessária:**
- [ ] Remover renderização de `fio_ouro` no template (já feito ✅)
- [ ] Considerar deprecar o campo no `_TEMPLATE_V6.yaml` para próximas lições
- [ ] Usar apenas `linkage.proximo.gancho` daqui em diante

---

### 3. `materiais[].essencial` → ✅ OPÇÃO A + DISCUSSÃO VISUAL

**Decisão:** Manter campo como metadata.

**Nova Discussão do Maestro:**
> "Será que temos que mudar a abordagem da renderização para dar um destaque no que é essencial e o que é opcional? Acho melhor né?"

---

## 💡 DISCUSSÃO: Destaque Visual para Materiais

### Situação Atual

**YAML:**
```yaml
materiais:
  - {item: "3 sementes", qtd: 3, essencial: true}
  - {item: "cestinho", qtd: 1, essencial: true}
  - {item: "almofada", qtd: 1, essencial: false}
```

**HTML Atual:**
```
• 3 sementes (3)
• cestinho (1)
• almofada (1)
```

Não há distinção visual.

### Proposta: Distinção Visual

**Opção 1: Ícone Diferente**
```
🔴 3 sementes (3)      ← essencial
🔴 cestinho (1)        ← essencial
⚪ almofada (1)        ← opcional
```

**Opção 2: Separação por Grupo**
```
🎯 ESSENCIAL:
  • 3 sementes (3)
  • cestinho (1)

📦 SE TIVER:
  • almofada (1)
```

**Opção 3: Estilo Diferente**
```
• 3 sementes (3)       ← normal (essencial)
• cestinho (1)         ← normal (essencial)
• almofada (1) ⁽ᵒᵖᶜⁱᵒⁿᵃˡ⁾ ← menor/cinza
```

### Recomendação

**Opção 2 (Separação por Grupo)** é a mais clara para o Portador:
- Sabe imediatamente o que PRECISA ter
- Sabe o que é "bônus" se tiver
- Alinha com UX Toca Boca (clareza)

### Implementação no Template

```jinja2
{# MATERIAIS COM SEPARAÇÃO ESSENCIAL/OPCIONAL #}
{% set essenciais = licao.para_portador.preparacao.materiais | selectattr('essencial', 'true') | list %}
{% set opcionais = licao.para_portador.preparacao.materiais | rejectattr('essencial', 'true') | list %}

{% if essenciais %}
<p><strong>🎯 Essencial:</strong></p>
<ul>
{% for mat in essenciais %}
    <li>{{ mat.item }}{% if mat.qtd %} ({{ mat.qtd }}){% endif %}</li>
{% endfor %}
</ul>
{% endif %}

{% if opcionais %}
<p><strong>📦 Se tiver:</strong></p>
<ul style="color:#6B7280;">
{% for mat in opcionais %}
    <li>{{ mat.item }}{% if mat.qtd %} ({{ mat.qtd }}){% endif %}</li>
{% endfor %}
</ul>
{% endif %}
```

---

### 4. `navegacao_inferior` → 🔍 REVISÃO

**Análise:**

| Campo | Linhas | Conteúdo |
|:---|:---|:---|
| `navegacao` | 43-45 | anterior.id/titulo, proxima.id/titulo |
| `navegacao_inferior` | 117-119 | anterior.id/titulo, proxima.id/titulo |

**Verificando o uso atual:**

O template `base.j2` usa `licao.navegacao` (L98-110).
O template **não usa** `navegacao_inferior`.

**Decisão:** 

✅ **REMOVER `navegacao_inferior` do _TEMPLATE_V6.yaml**

**Justificativa:**
1. Template não usa
2. Duplicação clara (viola DRY)
3. Se precisar navegação diferente topo/base no futuro, pode adicionar depois

---

## ✅ RESUMO FINAL DAS DECISÕES

| Campo | Decisão | Mudança no YAML | Mudança no Template |
|:---|:---|:---|:---|
| `norte_absoluto` | Manter | Nenhuma | Já não renderiza ✅ |
| `fio_ouro` | Unificar | Deprecar futuro | Já não renderiza ✅ |
| `materiais[].essencial` | Usar visualmente | Nenhuma | **Implementar separação** |
| `navegacao_inferior` | Remover | **Remover seção** | Nenhuma |

---

## 📝 PRÓXIMAS AÇÕES

1. [ ] Implementar separação visual de materiais essenciais/opcionais no `licao.j2`
2. [ ] Remover `navegacao_inferior` do `_TEMPLATE_V6.yaml`
3. [ ] Atualizar lições existentes (MV-S-001, MV-S-002) para remover `navegacao_inferior`
4. [ ] Rebuild e verificar

**Maestro, posso executar?** claras
