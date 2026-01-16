# LOG DE DELIBERAÇÃO: GUTENBERG V2.4 (ARQUITETURA MODULAR)
**Data:** 16/01/2026 | **Versão:** 2.4 | **Status:** IMPLEMENTADO
**Prerrequisito:** Leia primeiro `logs/2026-01-15_GUTENBERGV6.md` (seções 1-10) para contexto completo.

---

## RESUMO EXECUTIVO

O que mudou de V2.3 para V2.4:

| Aspecto | V2.3 (Anterior) | V2.4 (Atual) |
|:---|:---|:---|
| **Estrutura** | Script único `gutenberg_forja.py` | Pacote modular `build/{forge, core/, fases/}` |
| **Escalabilidade** | 1 fase (Sementes) | 4 fases (Sementes, Raízes, Lógica, Legado) |
| **Comando** | `python build/gutenberg_forja.py` | `python build/forge.py --fase sementes` |
| **Validação** | Genérica | Específica por fase |

**Motivação:** O currículo Matemática Viva cobre dos 4 aos 18 anos em 4 ciclos pedagógicos distintos. Cada ciclo tem regras de negócio contraditórias (ex: Sementes veta pictórico, Raízes exige pictórico). Um único script com `if/else` seria um desastre de manutenção.

---

## PARTE 1: O QUE FOI PRESERVADO DA V2.3

> [!IMPORTANT]
> Todas as otimizações documentadas no `logs/2026-01-15_GUTENBERGV6.md` continuam ativas.

| Componente | Localização V2.4 | Referência V2.3 |
|:---|:---|:---|
| **Single-Pass Asset Scan** | `build/core/assets.py` | Seção 5 do V6 log |
| **Escrita Atômica** (`.tmp` → `.html`) | `build/core/engine.py` | Seção 2 do V6 log |
| **Logs com Timestamps** | `build/core/logger.py` | Seção 3 do V6 log |
| **Filtro Typogrify** | `build/core/engine.py` | Seção 2 do V6 log |
| **Mapeamento de Avatares** | Templates inalterados | Seção 6 do V6 log |

---

## PARTE 2: NOVA ESTRUTURA DE ARQUIVOS

```text
build/
├── forge.py              # 🟢 CLI (ponto de entrada único)
│
├── core/                 # 🟡 MOTOR (código invariante)
│   ├── engine.py         #    GutenbergEngine: Jinja2, IO, validação base
│   ├── logger.py         #    ForgeLogger: timestamps, emojis
│   └── assets.py         #    AssetManager: single-pass scan
│
└── fases/                # 🔵 DRIVERS (regras por ciclo)
    ├── sementes.py       #    ✅ Implementado
    ├── raizes.py         #    🚧 A criar
    ├── logica.py         #    🚧 A criar
    └── legado.py         #    🚧 A criar
```

---

## PARTE 3: REGRAS DE NEGÓCIO POR CICLO

| Ciclo | Viajante | Idade | Regra CPA | Validação Técnica |
|:---|:---|:---|:---|:---|
| **Sementes** | Herdeiro | 4-6 | Concreto ONLY | `pictorico.status == 'VETADO'` |
| **Raízes** | Construtor | 6-10 | Concreto + Pictórico | `oficina` obrigatório |
| **Lógica** | Explorador | 10-14 | C + P + Abstrato | `demonstracao` obrigatório |
| **Legado** | Portador | 14-18 | Abstrato + Aplicação | `projeto_capstone` obrigatório |

### Por que essas regras?

**Sementes (Veto Pictórico):** Charlotte Mason + Bruner dizem que crianças pequenas devem manipular objetos reais antes de ver representações. A imaginação é mais poderosa que qualquer desenho.

**Raízes (Pictórico Permitido):** A criança já tem base concreta. Diagramas e esquemas agora são ferramentas de construção, não atalhos.

**Lógica (Abstração Obrigatória):** O adolescente está pronto para provas formais. Deve haver demonstração matemática.

**Legado (Aplicação Real):** O jovem adulto aplica conhecimento a problemas do mundo real. Projetos capstone são obrigatórios.

---

## PARTE 4: COMO IMPLEMENTAR UMA NOVA FASE

### Passo 1: Criar o Driver

```python
# build/fases/raizes.py
from pathlib import Path
from core.engine import GutenbergEngine

class RaizesConfig:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    INPUT_DIR = PROJECT_ROOT / "curriculo/02_RAIZES"      # Ajustar
    OUTPUT_DIR = PROJECT_ROOT / "site/raizes"             # Ajustar
    TEMPLATES_DIR = PROJECT_ROOT / "site/templates"
    ASSETS_DIR = PROJECT_ROOT / "site/assets"
    TEMPLATE_NAME = "licao.j2"                            # Pode ser específico

class RaizesDriver(GutenbergEngine):
    def __init__(self, dry_run=False):
        super().__init__(RaizesConfig, dry_run)
    
    def validate_lesson(self, fpath, data):
        if not super().validate_lesson(fpath, data):
            return False
        
        # Regra de Raízes: exige seção 'oficina'
        jornada = data['licao'].get('jornada', {})
        if 'oficina' not in jornada:
            self.warnings.append(f"{fpath.name}: Raízes exige bloco 'oficina'.")
        
        return True
```

### Passo 2: Registrar no CLI

```python
# build/forge.py (adicionar)
from fases.raizes import RaizesDriver

# No argparse, adicionar 'raizes' às choices
parser.add_argument("--fase", choices=['sementes', 'raizes'], ...)

# No main(), adicionar
if args.fase == 'raizes':
    forge = RaizesDriver(dry_run=args.dry_run)
    forge.run()
```

### Passo 3: Criar Pasta de Currículo

```bash
mkdir curriculo\02_RAIZES
```

### Passo 4: Executar

```bash
python build/forge.py --fase raizes
```

---

## PARTE 5: DÉBITOS TÉCNICOS CONHECIDOS

| Item | Prioridade | Status |
|:---|:---|:---|
| Adicionar `__init__.py` em `core/` e `fases/` | Média | 🚧 Pendente |
| Mover documentação para `build/README.md` | Baixa | 🚧 Pendente |
| Criar `test_build.py` automatizado | Média | 🚧 Pendente |
| Variável `ASSET_BASE_PATH` dinâmica | Baixa | 🚧 Pendente |

---

## REFERÊNCIA RÁPIDA (COPIE ISTO)

```
PROJETO:  Matemática Viva - Pipeline Gutenberg V2.4
BUILD:    python build/forge.py --fase sementes
INPUT:    curriculo/01_SEMENTESV6/*.yaml
OUTPUT:   site/sementes/*.html
TEMPS:    site/templates/{base.j2, licao.j2, macros.j2}
ASSETS:   site/assets/cards/guardioes/*.png
TIME:     ~0.10s para 2 lições

FASES DISPONÍVEIS: sementes (✅), raizes (🚧), logica (🚧), legado (🚧)
```

---

**FIM DO LOG V2.4.** Este documento é complementar ao `2026-01-15_GUTENBERGV6.md`. Juntos, eles formam a documentação completa do sistema de build.
