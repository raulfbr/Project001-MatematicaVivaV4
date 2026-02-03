# PLANO: Migração HTML → Templates Jinja2

**Data:** 16/01/2026 13:52
**Status:** 📋 PLANEJAMENTO (não executar ainda)
**Origem:** Refinamentos validados em `MV-S-001_A_TRINDADE_NA_PALMA.html`

---

## 📋 RESUMO

| Item | Valor |
|:---|:---|
| **Objetivo** | Migrar refinamentos do HTML para templates Gutenberg |
| **Arquivos Alvo** | 4 templates + 1 CSS |
| **Risco** | 🟡 Médio (afeta todas as lições Sementes) |
| **Previsão** | ~1h de trabalho |

---

## 📁 ARQUIVOS A MODIFICAR

| # | Arquivo | Tipo | Mudanças |
|:---|:---|:---|:---|
| 1 | `site/sementes/templates/licao.j2` | Jinja2 | Portador, Local, Para Família |
| 2 | `site/sementes/templates/macros.j2` | Jinja2 | Novos macros |
| 3 | `site/sementes/templates/base.j2` | Jinja2 | Meta tag |
| 4 | `site/sementes/style.css` | CSS | Novas classes |
| 5 | `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml` | YAML | Ajustes estruturais |

---

## 🎯 MUDANÇAS DETALHADAS

### 1. `style.css` — Novas Classes CSS

```css
/* === CORES POR AUTOR === */
.bruner-box {
    background: #DBEAFE;
    border-left: 4px solid #3B82F6;
    padding: 1rem;
    border-radius: 0 8px 8px 0;
    margin-top: 1rem;
}

.cm-box {
    background: #EDE9FE;
    border-left: 4px solid #8B5CF6;
    padding: 1rem;
    border-radius: 0 8px 8px 0;
    margin-top: 1rem;
}

.tgtb-box {
    background: #FEF3C7;
    border-left: 4px solid #F59E0B;
    padding: 1rem;
    border-radius: 0 8px 8px 0;
    margin-top: 1rem;
}

.espiritual-box {
    background: #DCFCE7;
    border-left: 4px solid #22C55E;
    padding: 1rem;
    border-radius: 0 8px 8px 0;
    margin-top: 1rem;
}

.graca-box {
    background: #F9FAFB;
    border-left: 4px solid #9CA3AF;
    padding: 1rem;
    border-radius: 0 8px 8px 0;
    margin-top: 1rem;
}

/* === PORTADOR === */
.portador-icon {
    font-size: 2.5rem;
    margin-right: 0.75rem;
}

/* === LOCAL CARD === */
.local-card {
    text-align: center;
    margin: 1.5rem 0;
}

.local-card img {
    max-width: 480px;
    width: 100%;
    border-radius: 16px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    border: 4px solid white;
    transform: rotate(-1deg);
}

.local-label {
    font-size: 0.9rem;
    color: #9CA3AF;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}
```

### 2. `macros.j2` — Novos Macros

```jinja2
{# MACRO: Portador da Tocha #}
{% macro portador_block(tom, texto) %}
<div class="script-persona-block portador-block">
    <span class="portador-icon">🔥</span>
    <div class="script-content">
        <div class="script-header">
            <span class="script-name">Portador da Tocha</span>
            {% if tom %}<span class="script-tone">(tom: {{ tom }})</span>{% endif %}
        </div>
        <div class="script-text">{{ texto | safe }}</div>
    </div>
</div>
{% endmacro %}

{# MACRO: Local Card #}
{% macro local_card(nome, imagem) %}
<div class="local-card">
    <p><strong>📍 Local:</strong> {{ nome }}</p>
    <p class="local-label">Visualizar</p>
    <img src="../assets/cards/locais/{{ imagem }}" alt="{{ nome }}">
</div>
{% endmacro %}

{# MACRO: Box por Autor #}
{% macro author_box(tipo, titulo, conteudo) %}
<div class="{{ tipo }}-box">
    <strong>{{ titulo }}</strong><br>
    {{ conteudo | safe }}
</div>
{% endmacro %}
```

### 3. `licao.j2` — Mudanças no Template

| Seção | Mudança |
|:---|:---|
| Portador | Substituir `<img>` por `{{ portador_block(tom, texto) }}` |
| Local | Substituir `<p>📍 Local:</p>` por `{{ local_card(nome, imagem) }}` |
| Norte Absoluto | **REMOVER** (não renderizar) |
| Fio de Ouro | **REMOVER** (não renderizar) |
| Para Família | Usar macros `author_box()` |
| Navegação | "Última Aventura" / "Próxima Aventura" |

### 4. `base.j2` — Meta Tag

```jinja2
{# ANTES #}
<div class="lesson-meta-tag">{{ licao.metadados.id }} • {{ licao.metadados.tempo_licao }} • {{ loop.index }}</div>

{# DEPOIS #}
<div class="lesson-meta-tag">Lição {{ loop.index | default('01') }} • {{ licao.metadados.titulo }} • ⏱️ 20 min</div>
```

### 5. `_TEMPLATE_V6.yaml` — Ajustes Estruturais

| Campo | Ação |
|:---|:---|
| `ritual_fechamento.fio_ouro` | Avaliar remoção ou unificação com linkage |
| `jornada.concreto.norte_absoluto` | Avaliar remoção ou mover para para_portador |

---

## ⏱️ ORDEM DE EXECUÇÃO

```
1. CSS PRIMEIRO
   └── Adicionar classes em style.css
   └── Testar build (sem quebrar)

2. MACROS
   └── Adicionar macros em macros.j2
   └── Testar importação

3. LICAO.J2
   └── Substituir Portador
   └── Substituir Local
   └── Remover Norte Absoluto
   └── Remover Fio de Ouro
   └── Atualizar Para Família

4. BASE.J2
   └── Atualizar meta tag

5. BUILD & VERIFICAÇÃO
   └── python build/forge.py --fase sementes
   └── Verificar TODAS as lições
   └── Comparar com HTML original

6. YAML (OPCIONAL)
   └── _TEMPLATE_V6.yaml ajustes
```

---

## ⚠️ CUIDADOS

1. **Backup:** Antes de modificar, fazer cópia dos templates atuais
2. **Build Incremental:** Testar após cada mudança
3. **Não perder funcionalidades:** Verificar se tudo que funcionava continua
4. **Mobile:** Testar `max-width: 480px` em telas pequenas

---

## ✅ CHECKLIST PRÉ-EXECUÇÃO

- [ ] Maestro aprovou este plano?
- [ ] Backup dos templates feito?
- [ ] Entendi cada mudança?
- [ ] Posso reverter se der errado?

---

## 📊 VALIDAÇÃO DO PLANO

**Engenharia (Clean Code):**
> ✅ Classes CSS reutilizáveis seguem DRY
> ✅ Macros Jinja2 são funções que fazem UMA coisa
> ✅ Estrutura clara e documentada

**Design:**
> ✅ Cores seguem paleta definida
> ✅ Componentes visuais padronizados
> ✅ `max-width: 480px; width: 100%` para responsividade (Toca Boca)

---

**Status:** 📋 AGUARDANDO APROVAÇÃO DO MAESTRO
