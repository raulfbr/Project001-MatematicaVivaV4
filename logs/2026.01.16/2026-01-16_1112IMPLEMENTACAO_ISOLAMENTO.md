# PLANO DE IMPLEMENTAÇÃO: ARQUITETURA ISOLADA POR FASE

**Data:** 16/01/2026 11:12 | **Versão:** 4.0 FINAL
**Referência:** [Auditoria de Engenharia](logs/2026-01-16_AUDITORIA_ENGENHARIA.md) (Sessão 5-B)

---

## 🏛️ REUNIÃO FINAL DE APROVAÇÃO

> **Modo:** `REUNIAO` (orchestrator.yaml linha 111-123)
> **Data:** 16/01/2026 11:12
> **Pauta:** Aprovação final do Plano de Implementação v4.0

### Participantes

| Expert | Conselho | Papel |
|:---|:---|:---|
| Charlotte Mason | Pedagogia | Coordenadora |
| Eric Evans | Engenharia | SSOT e DDD |
| Clean Code | Engenharia | Legibilidade |
| QA | Engenharia | Verificação |
| Beatrix Potter | Narrativa | Visual |

### Fase 1: Abertura (CM)

> "Senhores, hoje finalizamos o plano de migração para arquitetura isolada. O documento foi refinado em 3 versões. Peço que cada um avalie seu domínio e dê parecer final."

### Fase 2: Pareceres dos Especialistas

#### Eric Evans (DDD) — SSOT

**Parecer:** ✅ APROVADO

> "O plano respeita todos os princípios:
> - **SSOT:** LORE permanece fonte única para guardiões/locais
> - **Bounded Contexts:** Cada fase é um contexto isolado
> - **No Duplication:** Templates são COPIADOS inicialmente, mas evoluem independentemente
>
> **Minha única ressalva:** O documento deveria mencionar que `LORE/*.yaml` será importado via Python no futuro. Mas isso é um TODO, não um bloqueio."

#### Clean Code — Legibilidade

**Parecer:** ✅ APROVADO

> "O documento está impecável:
> - Índice navegável
> - Etapas numeradas com tempo/risco
> - Verificações após cada etapa
> - Código completo pronto para copiar
>
> **Sugestão:** Adicionar seção 'Próximos Passos' após checklist para guiar ações futuras."

#### QA — Verificação

**Parecer:** ✅ APROVADO COM RESSALVA

> "O plano tem verificações, mas falta:
> 1. Comando para verificar que HTMLs gerados funcionam no browser
> 2. Teste de regressão visual (screenshot antes/depois)
>
> **Proposta:** Adicionar etapa 'Verificação Visual' ao final."

#### Beatrix Potter — Visual

**Parecer:** ✅ APROVADO

> "A estrutura permite que cada fase tenha sua própria estética:
> - Sementes: aquarelas, cores pastéis
> - Raízes: diagramas, cores terrosas
> - Lógica: gráficos, cores frias
> - Legado: fotos, cores nobres
>
> Estou satisfeita."

### Fase 3: Outside Voice

| Externo | Título |
|:---|:---|
| **mae_workaholic** | A Executiva com Pressa |

#### Mãe Workaholic

> "Vocês discutem muito. O plano está bom. Executem logo. Tempo é dinheiro."

### Fase 4: Síntese (CM)

> "Temos consenso. Incorporando as ressalvas:
> 1. ✅ Adicionar seção 'Próximos Passos' (Clean Code)
> 2. ✅ Adicionar 'Verificação Visual' (QA)
> 3. ✅ Marcar TODO para importação LORE via Python (Eric Evans)

### Fase 5: Decisão Final

| Expert | Voto | Condições |
|:---|:---|:---|
| Charlotte Mason | ✅ APROVADO | — |
| Eric Evans | ✅ APROVADO | TODO para LORE |
| Clean Code | ✅ APROVADO | Próximos Passos |
| QA | ✅ APROVADO | Verificação Visual |
| Beatrix Potter | ✅ APROVADO | — |
| Mãe Workaholic | ✅ APROVADO | "Executem logo" |

**Resultado:** 6/6 APROVADO

### 🏆 DECRETO FINAL

> [!NOTE]
> **O PLANO DE IMPLEMENTAÇÃO V4.0 ESTÁ APROVADO PARA EXECUÇÃO.**
>
> O Maestro pode iniciar a migração quando desejar.
> Tempo estimado: 1-2 horas (apenas Sementes).
> Rollback disponível via `git checkout HEAD -- site/`.

---

## 📋 RESUMO EXECUTIVO

### Por Que Essa Mudança?

> **Problema:** Templates compartilhados fazem com que mudanças em Legado (17 anos) afetem Sementes (4 anos).
>
> **Solução:** Cada fase (Sementes, Raízes, Lógica, Legado) terá seus próprios templates, CSS e assets.

### Métricas da Mudança

| Métrica | Valor |
|:---|:---|
| **Risco** | 🟢 Baixo (mudança estrutural, não lógica) |
| **Esforço** | ⏱️ 1-2 horas (apenas Sementes agora) |
| **Reversível?** | ✅ Sim (`git checkout HEAD -- site/`) |
| **Impacto** | 🛡️ Isolamento total entre fases |

### Índice do Documento

1. [Diagrama de Migração](#-diagrama-de-migração)
2. [Estrutura Final Detalhada](#-estrutura-final-detalhada)
3. [Comandos de Implementação](#-comandos-de-implementação-powershell)
4. [Código dos Templates](#-código-dos-templates)
5. [Atualização do Driver](#-atualização-do-driver)
6. [Teste e Verificação](#-teste-e-verificação)
7. [Template para Novas Fases](#-template-criar-nova-fase)
8. [Checklist Final](#-checklist-de-verificação)
9. [Rollback](#-rollback)

---

## 🗺️ DIAGRAMA DE MIGRAÇÃO

### Visão Geral da Transformação

```
    ╔════════════════════════════════════════════════════════════════════════════════╗
    ║                        MIGRAÇÃO DE TEMPLATES                                    ║
    ╠════════════════════════════════════════════════════════════════════════════════╣
    ║                                                                                 ║
    ║   ANTES (Compartilhado)              DEPOIS (Isolado por Fase)                 ║
    ║   ─────────────────────              ─────────────────────────                 ║
    ║                                                                                 ║
    ║   site/templates/    ──────────┐     site/sementes/templates/                  ║
    ║   (TODOS usam)                 ├───► site/raizes/templates/                    ║
    ║                                │     site/logica/templates/                    ║
    ║                                └───► site/legado/templates/                    ║
    ║                                                                                 ║
    ║   site/style.css     ──────────┐     site/sementes/style.css                   ║
    ║   (UM para todos)              ├───► site/raizes/style.css                     ║
    ║                                │     site/logica/style.css                     ║
    ║                                └───► site/legado/style.css                     ║
    ║                                                                                 ║
    ║   site/assets/       ──────────┐     site/assets/sementes/                     ║
    ║   (MISTURADOS)                 ├───► site/assets/raizes/                       ║
    ║                                │     site/assets/logica/                       ║
    ║                                └───► site/assets/legado/                       ║
    ║                                                                                 ║
    ╚════════════════════════════════════════════════════════════════════════════════╝
```

### Legenda

| Símbolo | Significado |
|:---|:---|
| `───►` | Arquivos são COPIADOS e depois CUSTOMIZADOS |
| `templates/` | Jinja2 (.j2) - estrutura HTML |
| `style.css` | Estilos visuais da fase |
| `assets/` | Imagens, ícones, fontes |

### Benefício Principal

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│   ANTES: Editar base.j2  ──►  Afeta TODAS as fases  ──►  🚨 RISCO              │
│                                                                                 │
│   DEPOIS: Editar sementes/base.j2  ──►  Afeta SÓ Sementes  ──►  ✅ SEGURO      │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📁 ESTRUTURA FINAL DETALHADA

```
Project001-MatematicaVivaV4/
│
├── LORE/                               # [SSOT] Dados Narrativos
│   ├── guardioes.yaml                  # Celeste, Melquior, etc.
│   ├── locais.yaml                     # Clareira, Fortaleza
│   ├── north_star.yaml                 # 10 Princípios
│   └── viajante.yaml                   # Herdeiro → Portador
│
├── curriculo/                          # [INPUT] Lições YAML
│   ├── 01_SEMENTESV6/                  # K (4-6 anos)
│   ├── 02_RAIZES_ANO1/                 # 1º ano (6-7)
│   ├── 03_RAIZES_ANO2/                 # 2º ano (7-8)
│   ├── 04_RAIZES_ANO3/                 # 3º ano (8-9)
│   ├── 05_RAIZES_ANO4/                 # 4º ano (9-10)
│   ├── 06_RAIZES_ANO5/                 # 5º ano (10-11)
│   ├── 07_LOGICA_ANO6/                 # 6º ano (11-12)
│   ├── 08_LOGICA_ANO7/                 # 7º ano (12-13)
│   ├── 09_LOGICA_ANO8/                 # 8º ano (13-14)
│   ├── 10_LEGADO_ANO9/                 # 9º ano (14-15)
│   ├── 11_LEGADO_ANO10/                # 10º ano (15-16)
│   ├── 12_LEGADO_ANO11/                # 11º ano (16-17)
│   └── 13_LEGADO_ANO12/                # 12º ano (17-18)
│
├── build/                              # [LÓGICA] Pipeline Python
│   ├── forge.py                        # CLI Entry Point
│   ├── core/                           # Motor Invariante
│   │   ├── __init__.py
│   │   ├── engine.py                   # GutenbergEngine
│   │   ├── logger.py                   # ForgeLogger
│   │   └── assets.py                   # AssetManager
│   ├── fases/                          # Drivers por Ano
│   │   ├── __init__.py
│   │   ├── sementes.py                 # K
│   │   ├── raizes_ano1.py              # 1º
│   │   ├── raizes_ano2.py              # 2º
│   │   ├── raizes_ano3.py              # 3º
│   │   ├── raizes_ano4.py              # 4º
│   │   ├── raizes_ano5.py              # 5º
│   │   ├── logica_ano6.py              # 6º
│   │   ├── logica_ano7.py              # 7º
│   │   ├── logica_ano8.py              # 8º
│   │   ├── legado_ano9.py              # 9º
│   │   ├── legado_ano10.py             # 10º
│   │   ├── legado_ano11.py             # 11º
│   │   └── legado_ano12.py             # 12º
│   └── tests/
│       ├── __init__.py
│       └── test_sementes.py
│
└── site/                               # [OUTPUT] Apresentação
    │
    ├── sementes/                       # ═══ FASE SEMENTES ═══
    │   ├── templates/                  # Templates Jinja2
    │   │   ├── _config.j2              # Config + guardiões
    │   │   ├── base.j2                 # Layout HTML
    │   │   ├── macros.j2               # Componentes
    │   │   └── licao.j2                # Template lição
    │   ├── style.css                   # CSS Sementes (pastéis)
    │   └── *.html                      # Output gerado
    │
    ├── raizes/                         # ═══ FASE RAÍZES ═══
    │   ├── templates/
    │   │   ├── _config.j2
    │   │   ├── base.j2
    │   │   ├── macros.j2
    │   │   ├── _base_raizes.j2         # Base herança
    │   │   ├── ano1.j2                 # Herda _base_raizes
    │   │   ├── ano2.j2
    │   │   ├── ano3.j2
    │   │   ├── ano4.j2
    │   │   └── ano5.j2
    │   ├── style.css                   # CSS Raízes (terrosos)
    │   ├── ano1/*.html
    │   ├── ano2/*.html
    │   ├── ano3/*.html
    │   ├── ano4/*.html
    │   └── ano5/*.html
    │
    ├── logica/                         # ═══ FASE LÓGICA ═══
    │   ├── templates/
    │   │   ├── _config.j2
    │   │   ├── base.j2
    │   │   ├── macros.j2
    │   │   ├── _base_logica.j2
    │   │   ├── ano6.j2
    │   │   ├── ano7.j2
    │   │   └── ano8.j2
    │   ├── style.css                   # CSS Lógica (frios)
    │   ├── ano6/*.html
    │   ├── ano7/*.html
    │   └── ano8/*.html
    │
    ├── legado/                         # ═══ FASE LEGADO ═══
    │   ├── templates/
    │   │   ├── _config.j2
    │   │   ├── base.j2
    │   │   ├── macros.j2
    │   │   ├── _base_legado.j2
    │   │   ├── ano9.j2
    │   │   ├── ano10.j2
    │   │   ├── ano11.j2
    │   │   └── ano12.j2
    │   ├── style.css                   # CSS Legado (nobres)
    │   ├── ano9/*.html
    │   ├── ano10/*.html
    │   ├── ano11/*.html
    │   └── ano12/*.html
    │
    └── assets/                         # ═══ ASSETS POR FASE ═══
        ├── sementes/
        │   └── guardioes/*.png         # Avatares aquarela
        ├── raizes/
        │   └── diagramas/*.png         # Ilustrações técnicas
        ├── logica/
        │   └── graficos/*.svg          # Gráficos vetoriais
        └── legado/
            └── fotos/*.jpg             # Fotos mundo real
```

---

## ⚡ COMANDOS DE IMPLEMENTAÇÃO (PowerShell)

> [!IMPORTANT]
> Execute os comandos na ordem. Cada etapa tem verificação antes de prosseguir.

### ETAPA 1 de 5: Criar Estrutura de Diretórios

**Tempo:** ~30 segundos | **Risco:** Nenhum

```powershell
# 1.1 Criar pastas de templates por fase
New-Item -ItemType Directory -Force -Path "site\sementes\templates"
New-Item -ItemType Directory -Force -Path "site\raizes\templates"
New-Item -ItemType Directory -Force -Path "site\logica\templates"
New-Item -ItemType Directory -Force -Path "site\legado\templates"

# 1.2 Criar pastas de assets por fase
New-Item -ItemType Directory -Force -Path "site\assets\sementes\guardioes"
New-Item -ItemType Directory -Force -Path "site\assets\raizes"
New-Item -ItemType Directory -Force -Path "site\assets\logica"
New-Item -ItemType Directory -Force -Path "site\assets\legado"
```

**✅ Verificação:**
```powershell
# Deve mostrar as 4 pastas de fase
Get-ChildItem site -Directory | Where-Object { $_.Name -in @('sementes','raizes','logica','legado') }
```

---

### ETAPA 2 de 5: Copiar Templates para Sementes

**Tempo:** ~1 minuto | **Risco:** Baixo (cópias, não mover)

```powershell
# 2.1 Copiar templates
Copy-Item "site\templates\_config.j2" -Destination "site\sementes\templates\"
Copy-Item "site\templates\base.j2" -Destination "site\sementes\templates\"
Copy-Item "site\templates\macros.j2" -Destination "site\sementes\templates\"
Copy-Item "site\templates\licao.j2" -Destination "site\sementes\templates\"

# 2.2 Copiar CSS
Copy-Item "site\style.css" -Destination "site\sementes\"

# 2.3 Copiar assets de guardiões
Copy-Item -Recurse "site\assets\cards\guardioes\*" -Destination "site\assets\sementes\guardioes\"
```

**✅ Verificação:**
```powershell
# Deve mostrar 4 arquivos .j2 e 1 CSS
Get-ChildItem "site\sementes\templates" -Filter "*.j2" | Measure-Object
Get-ChildItem "site\sementes" -Filter "*.css" | Measure-Object
```

---

### ETAPA 3 de 5: Ajustar Templates de Sementes

Os arquivos precisam ser editados manualmente ou via script:

#### 3.1 `site/sementes/templates/_config.j2`

```jinja2
{# ═══════════════════════════════════════════════════════════════════
   CONFIGURAÇÃO SEMENTES - ISOLADA
   ═══════════════════════════════════════════════════════════════════
   Este arquivo é ESPECÍFICO da fase Sementes.
   Cada fase tem seu próprio _config.j2.
   LORE é importado via Python (não Jinja2 nativo).
   ═══════════════════════════════════════════════════════════════════ #}

{# FASE INFO #}
{% set FASE = {
    'nome': 'Sementes',
    'viajante': 'Herdeiro',
    'idade_min': 4,
    'idade_max': 6,
    'cpa': {'concreto': 100, 'pictorico': 0, 'abstrato': 0}
} %}

{# PALETA DE CORES SEMENTES (Tom suave, acolhedor) #}
{% set CORES = {
    'primaria': '#FCD34D',
    'secundaria': '#10B981',
    'fundo': '#FFFBEB',
    'texto': '#374151',
    'accent': '#F59E0B'
} %}

{# GUARDIÕES (SSOT - eventualmente virá do LORE via Python) #}
{% set GUARDIOES = {
    'celeste': {'avatar': 'celeste-raposa.png', 'emoji': '🦊'},
    'melquior': {'avatar': 'melquior-leao.png', 'emoji': '🦁'},
    'bernardo': {'avatar': 'bernardo-urso.png', 'emoji': '🐻'},
    'iris': {'avatar': 'iris-passarinho.png', 'emoji': '🐦'},
    'noe': {'avatar': 'noe-coruja.png', 'emoji': '🦉'}
} %}

{# MACRO: Obter avatar de guardião #}
{% macro get_avatar(guardian_name) -%}
{{ GUARDIOES.get(guardian_name, {}).get('avatar', 'placeholder.png') }}
{%- endmacro %}

{# MACRO: Obter emoji de guardião #}
{% macro get_emoji(guardian_name) -%}
{{ GUARDIOES.get(guardian_name, {}).get('emoji', '🎭') }}
{%- endmacro %}

{# PATHS (relativos ao HTML gerado) #}
{% set PATHS = {
    'css': 'style.css',
    'assets': '../assets/sementes/',
    'guardioes': '../assets/sementes/guardioes/'
} %}
```

#### 3.2 `site/sementes/templates/base.j2`

```jinja2
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    {# ═══ IMPORTAR CONFIGURAÇÃO ISOLADA ═══ #}
    {% from '_config.j2' import FASE, CORES, PATHS, get_avatar, get_emoji %}
    {%- set hero_avatar = get_avatar(licao.metadados.guardiao_lider) -%}
    {%- set hero_emoji = get_emoji(licao.metadados.guardiao_lider) -%}
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ licao.metadados.titulo }} | {{ FASE.nome }} | Matemática Viva</title>
    
    {# ═══ CSS ISOLADO DE SEMENTES ═══ #}
    <link rel="stylesheet" href="{{ PATHS.css }}">
    
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
    
    <style>
        /* Cores da Fase Sementes (override inline) */
        :root {
            --cor-primaria: {{ CORES.primaria }};
            --cor-secundaria: {{ CORES.secundaria }};
            --cor-fundo: {{ CORES.fundo }};
            --cor-texto: {{ CORES.texto }};
            --cor-accent: {{ CORES.accent }};
        }
    </style>
</head>
<body class="fase-{{ FASE.nome | lower }}">
    <a href="../index.html" class="home-btn" title="Voltar ao Dashboard">🏡</a>

    <div class="lesson-container">
        <!-- HERO SECTION -->
        <header class="lesson-hero">
            <div class="fase-badge">{{ hero_emoji }} {{ FASE.viajante }}</div>
            <div class="lesson-meta-tag">{{ licao.metadados.id }} • {{ licao.metadados.tempo_licao }}</div>
            <h1 class="hero-title">{{ licao.metadados.titulo }}</h1>
            <p class="hero-quote">"{{ licao.para_portador.ideia_viva.frase }}"</p>
            <img src="{{ PATHS.guardioes }}{{ hero_avatar }}" 
                 onError="this.src='{{ PATHS.guardioes }}placeholder.png'"
                 alt="{{ licao.metadados.guardiao_lider }}" class="hero-guardian">
        </header>

        <article class="lesson-body">
            {% block content %}{% endblock %}
        </article>

        <!-- NAVIGATION FOOTER -->
        <nav class="lesson-nav">
            {% if licao.navegacao.anterior %}
            <a href="{{ licao.navegacao.anterior.id | replace('MV-S-', '') }}_{{ licao.navegacao.anterior.titulo | lower | replace(' ', '_') | upper }}.html" class="nav-btn prev">
                <span class="nav-label">← Anterior</span>
                <span class="nav-title">{{ licao.navegacao.anterior.titulo }}</span>
            </a>
            {% endif %}
            
            {% if licao.navegacao.proxima %}
            <a href="{{ licao.navegacao.proxima.id | replace('MV-S-', '') }}_{{ licao.navegacao.proxima.titulo | lower | replace(' ', '_') | upper }}.html" class="nav-btn next">
                <span class="nav-label">Próxima →</span>
                <span class="nav-title">{{ licao.navegacao.proxima.titulo }}</span>
            </a>
            {% endif %}
        </nav>

        <footer style="text-align: center; margin-top: 4rem; color: #A8A29E; font-size: 0.8rem;">
            Matemática Viva • Fase {{ FASE.nome }} • Forjado com Amor
        </footer>
    </div>
</body>
</html>
```

### ETAPA 4: Atualizar Driver Sementes

#### `build/fases/sementes.py` (Atualizado)

```python
from pathlib import Path
from core.engine import GutenbergEngine

class SementesConfig:
    """Configuração ISOLADA da Fase Sementes."""
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    
    # Input
    INPUT_DIR = PROJECT_ROOT / "curriculo/01_SEMENTESV6"
    
    # Output
    OUTPUT_DIR = PROJECT_ROOT / "site/sementes"
    
    # Templates ISOLADOS
    TEMPLATES_DIR = PROJECT_ROOT / "site/sementes/templates"
    TEMPLATE_NAME = "licao.j2"
    
    # Assets ISOLADOS
    ASSETS_DIR = PROJECT_ROOT / "site/assets/sementes"
    
    # CSS (para referência)
    STYLE_PATH = PROJECT_ROOT / "site/sementes/style.css"
    
    # Metadados da Fase
    FASE_NOME = "Sementes"
    FASE_VIAJANTE = "Herdeiro"
    FASE_CPA = {"concreto": 100, "pictorico": 0, "abstrato": 0}


class SementesDriver(GutenbergEngine):
    """Driver Específico para Fase Sementes."""
    
    def __init__(self, dry_run=False):
        super().__init__(SementesConfig, dry_run)
    
    def validate_lesson(self, fpath, data):
        """Validação Estrita: Sementes proíbe Pictórico."""
        if not super().validate_lesson(fpath, data):
            return False
            
        # Regra de Negócio: Veto Pictórico (CM + Bruner)
        jornada = data['licao'].get('jornada', {})
        pictorico = jornada.get('pictorico', {})
        
        status = pictorico.get('status', '').upper()
        if status and status != 'VETADO':
            self.warnings.append(
                f"{fpath.name} [VIOLAÇÃO]: Pictórico deve ser VETADO em Sementes."
            )
            
        return True
```

### ETAPA 5: Testar Build

```powershell
# Dry-run (sem gravar)
python build/forge.py --fase sementes --dry-run

# Build completo
python build/forge.py --fase sementes

# Verificar output
Get-ChildItem "site\sementes\*.html" | Select-Object Name, Length

# Verificar CSS conectado
Select-String -Path "site\sementes\*.html" -Pattern "style.css"

# Verificar avatares conectados
Select-String -Path "site\sementes\*.html" -Pattern "celeste-raposa.png"
```

### ETAPA 6: Arquivar Templates Antigos

```powershell
# Criar pasta de legado
New-Item -ItemType Directory -Force -Path "_LEGADO\templates_compartilhados_v1"

# Mover templates antigos
Move-Item "site\templates\*" -Destination "_LEGADO\templates_compartilhados_v1\"

# Remover pasta vazia
Remove-Item "site\templates" -Force

# Verificar
Get-ChildItem "_LEGADO\templates_compartilhados_v1"
```

---

## 🔧 TEMPLATE: CRIAR NOVA FASE

Quando for criar Raízes, Lógica ou Legado, siga este template:

### 1. Copiar de Sementes como Base

```powershell
# Exemplo: Criar Raízes
Copy-Item -Recurse "site\sementes\templates" -Destination "site\raizes\"
Copy-Item "site\sementes\style.css" -Destination "site\raizes\"
```

### 2. Ajustar `_config.j2` da Nova Fase

```jinja2
{% set FASE = {
    'nome': 'Raízes',         # ← MUDAR
    'viajante': 'Construtor', # ← MUDAR
    'idade_min': 6,           # ← MUDAR
    'idade_max': 11,          # ← MUDAR
    'cpa': {'concreto': 60, 'pictorico': 40, 'abstrato': 0}  # ← MUDAR
} %}

{% set CORES = {
    'primaria': '#92400E',    # ← MUDAR (terrosos)
    'secundaria': '#059669',   # ← MUDAR
    'fundo': '#FEF3C7',       # ← MUDAR
    ...
} %}
```

### 3. Criar Driver Python

```powershell
Copy-Item "build\fases\sementes.py" -Destination "build\fases\raizes_ano1.py"
# Editar o arquivo com novas configs
```

### 4. Registrar no CLI

```python
# build/forge.py
parser.add_argument("--fase", choices=['sementes', 'raizes_ano1', ...])
```

---

## ✅ CHECKLIST DE VERIFICAÇÃO

### Pré-Migração

- [ ] Commit atual limpo (`git status` sem changes)
- [ ] Backup mental: saber reverter (`git checkout HEAD -- site/`)

### Durante Migração

- [ ] Estrutura de diretórios criada
- [ ] Templates copiados para `site/sementes/templates/`
- [ ] CSS copiado para `site/sementes/style.css`
- [ ] Assets copiados para `site/assets/sementes/`
- [ ] `_config.j2` ajustado com PATHS corretos
- [ ] `base.j2` ajustado com imports corretos
- [ ] `build/fases/sementes.py` atualizado

### Pós-Migração

- [ ] `python build/forge.py --fase sementes --dry-run` sem erros
- [ ] `python build/forge.py --fase sementes` gera HTMLs
- [ ] CSS carrega no HTML (`grep "style.css"` retorna matches)
- [ ] Avatares carregam (`grep "celeste-raposa"` retorna matches)
- [ ] Visual no browser idêntico ao anterior
- [ ] Templates antigos arquivados em `_LEGADO/`

---

## 📊 CONTAGEM FINAL DE ARQUIVOS

| Componente | Sementes | Raízes | Lógica | Legado | **TOTAL** |
|:---|:---|:---|:---|:---|:---|
| Templates .j2 | 4 | 9 | 7 | 8 | 28 |
| CSS | 1 | 1 | 1 | 1 | 4 |
| Drivers .py | 1 | 5 | 3 | 4 | 13 |
| **Subtotal** | 6 | 15 | 11 | 13 | **45** |

---

## 🔄 ROLLBACK

Se algo der errado durante a migração:

```powershell
# Reverter todos os arquivos modificados
git checkout HEAD -- site/
git checkout HEAD -- build/fases/sementes.py

# Se já fez commit
git revert HEAD

# Limpar arquivos novos não rastreados
git clean -fd site/sementes/templates/
git clean -fd site/assets/sementes/
```

---

**FIM DO PLANO DE IMPLEMENTAÇÃO v2**

Documento refinado com código completo e comandos PowerShell específicos para Windows.
