# LOG DE AUDITORIA DE ENGENHARIA: GUTENBERG V2.4
**Data:** 16/01/2026 09:12 | **Auditor:** Claude Opus 4 (Antigravity)
**Referência:** `.bmad/experts/engenharia/engenharia.yaml`

---

## PROTOCOLO DE ATIVAÇÃO (Linha 119-120 do engenharia.yaml)

O protocolo define 4 checks obrigatórios:
1. **CÓDIGO LIMPO CHECK:** legível? funções pequenas? nomes claros? DRY?
2. **DDD CHECK (Eric Evans):** dados SSOT? linguagem ubíqua? contextos fronteiras?
3. **BMAD CHECK:** agentes AaC? workflows doc? estrutura clara?
4. **QA CHECK:** testes passam? schema válido? 5 passes aprovados?

**Pergunta Final:** Código sobrevive revisão sênior exigente?

---

## ANÁLISE 1: CÓDIGO LIMPO (Prioridade 11)

### 1.1 Legibilidade

| Arquivo | Linhas | Funções | Nomes Claros? | Veredito |
|:---|:---|:---|:---|:---|
| `build/core/engine.py` | 187 | 7 | ✅ `ensure_directories`, `scan_yamls`, `render_all` | OK |
| `build/core/logger.py` | 19 | 4 | ✅ `log`, `success`, `warn`, `error` | OK |
| `build/core/assets.py` | 37 | 1 | ✅ `index_assets` | OK |
| `build/fases/sementes.py` | 33 | 1 | ✅ `validate_lesson` | OK |
| `build/forge.py` | 26 | 1 | ✅ `main` | OK |

**Resultado:** ✅ APROVADO — Nomes são descritivos e auto-explicativos.

### 1.2 Funções Pequenas (≤50 linhas)

| Função | Linhas | Status |
|:---|:---|:---|
| `GutenbergEngine.__init__` | 12 | ✅ |
| `GutenbergEngine.ensure_directories` | 25 | ✅ |
| `GutenbergEngine.setup_jinja` | 17 | ✅ |
| `GutenbergEngine.scan_yamls` | 43 | ✅ |
| `GutenbergEngine.validate_lesson` | 12 | ✅ |
| `GutenbergEngine.render_all` | 38 | ✅ |
| `GutenbergEngine.run` | 15 | ✅ |

**Resultado:** ✅ APROVADO — Nenhuma função >50 linhas.

### 1.3 DRY (Don't Repeat Yourself)

| Item | Antes | Depois | Status |
|:---|:---|:---|:---|
| `guardian_avatars` | Duplicado em 2 templates | SSOT em `_config.j2` | ✅ CORRIGIDO |
| `ForgeLogger` | Único em `logger.py` | N/A | ✅ OK |
| `AssetManager` | Único em `assets.py` | N/A | ✅ OK |

**Resultado:** ✅ APROVADO (após correção SSOT).

### 1.4 Testes

| Arquivo | Testes | Status |
|:---|:---|:---|
| `build/tests/test_sementes.py` | 4 | ✅ Passando |

**Resultado:** ✅ APROVADO — Testes existem e passam.

---

## ANÁLISE 2: ERIC EVANS / DDD (Prioridade 9)

### 2.1 SSOT (Single Source of Truth)

| Dado | Fonte Única? | Localização |
|:---|:---|:---|
| Mapeamento Guardiões→Avatares | ✅ | `site/templates/_config.j2` |
| Regras de Validação Sementes | ✅ | `build/fases/sementes.py` |
| Configuração de Paths | ⚠️ | Hardcoded em `SementesConfig` (cada driver separado) |
| Glossário Termos | ✅ | `LORE/north_star.yaml` |

**Observação:** Os paths de INPUT/OUTPUT estão em cada driver. Isso é aceitável (Bounded Contexts), mas poderia haver um `config.yaml` central se houvesse muitas fases.

**Resultado:** ✅ APROVADO.

### 2.2 Ubiquitous Language

| Termo Sistema | Termo Código | Consistente? |
|:---|:---|:---|
| Portador | `"PORTADOR"` em templates | ✅ |
| Guardião | `guardian_avatars`, `guardiao_lider` | ✅ |
| Lição | `licao` (YAML), `lesson` (código) | ⚠️ Misto |
| Viajante | N/A no código | OK (é narrativo, não técnico) |

**Observação Menor:** O código usa `lesson` (inglês) enquanto YAML usa `licao` (português). Isso é aceitável pois são contextos diferentes (código vs dados).

**Resultado:** ✅ APROVADO (com ressalva menor).

### 2.3 Bounded Contexts

| Contexto | Pasta | Responsabilidade | Fronteiras Claras? |
|:---|:---|:---|:---|
| Agentes/Orquestração | `.bmad/` | Definição de experts e workflows | ✅ |
| Conhecimento/LORE | `LORE/` | Narrativa, guardiões, North Star | ✅ |
| Conteúdo Lições | `curriculo/` | YAMLs das lições | ✅ |
| Pipeline Build | `build/` | Código Python de renderização | ✅ |
| Apresentação | `site/` | Templates HTML, CSS, assets | ✅ |

**Resultado:** ✅ APROVADO — Cada domínio tem fronteiras claras.

---

## ANÁLISE 3: BMAD FRAMEWORK (Prioridade 10)

### 3.1 Agent as Code (AaC)

| Requisito | Status | Evidência |
|:---|:---|:---|
| Experts em YAML | ✅ | `.bmad/experts/*.yaml` |
| Versionados Git | ✅ | Repositório Git ativo |

**Resultado:** ✅ APROVADO.

### 3.2 YAML-Based Workflows

| Requisito | Status | Evidência |
|:---|:---|:---|
| Workflows documentados | ⚠️ PARCIAL | Existe `.agent/workflows/` mas não `.bmad/workflows/gutenberg.yaml` |

**Observação:** O workflow do Gutenberg está documentado em logs (`logs/2026-01-16_GUTENBERG_MODULAR.md`), mas não em formato YAML workflow padrão BMAD.

**Recomendação:** Criar `.bmad/workflows/gutenberg_build.yaml` com o fluxo de build.

**Resultado:** ⚠️ PARCIAL — Documentação existe, mas não em formato BMAD padrão.

### 3.3 Estrutura de Pastas (Mapa Projeto linha 110-117)

| Pasta Esperada | Existe? | Conteúdo Correto? |
|:---|:---|:---|
| `.bmad/` | ✅ | ✅ experts/, workflows/ |
| `LORE/` | ✅ | ✅ north_star.yaml, guardioes.yaml |
| `curriculo/` | ✅ | ✅ 01_SEMENTESV6/ |
| `build/` | ✅ | ⚠️ Estrutura expandida (core/, fases/, tests/) |
| `_LEGADO/` | ✅ | ✅ Arquivos arquivados |

**Observação:** O `build/` tem mais subdivisões do que o esperado originalmente. Isso é uma MELHORIA (modularidade), não uma violação.

**Resultado:** ✅ APROVADO.

### 3.4 YAML Lean (linha 22)

> "ZERO separadores visuais (═══, ───, ****)"

| Arquivo | Separadores Visuais? | Status |
|:---|:---|:---|
| `engenharia.yaml` | ❌ Nenhum | ✅ |
| `north_star.yaml` | ❌ Nenhum | ✅ |
| `_config.j2` | Usa `===` em comentário | ⚠️ É template, não YAML |

**Resultado:** ✅ APROVADO para YAMLs. Template Jinja2 está fora do escopo YAML Lean.

---

## ANÁLISE 4: QA (Prioridade 8)

### 4.1 Verificação Quíntupla (linha 94-99)

| Pass | Nome | Aplicável a Build? | Status |
|:---|:---|:---|:---|
| 1 | SUPERFÍCIE | Sim | ✅ YAMLs válidos, imagens existem |
| 2 | CONSISTÊNCIA | Parcial | ✅ SSOT respeitado |
| 3 | PEDAGÓGICO | Não (é pipeline) | N/A |
| 4 | CPA | Não (é pipeline) | N/A |
| 5 | UX FAMÍLIA | Parcial | ✅ Build <5 min preparo |

**Resultado:** ✅ APROVADO para escopo de pipeline.

### 4.2 Checklist Técnico (linha 100)

| Check | Ferramenta | Status |
|:---|:---|:---|
| YAML válido | `yaml.safe_load` | ✅ Engine valida |
| Links funcionais | Não implementado | ⚠️ AUSENTE |
| Imagens existem | `AssetManager` indexa | ⚠️ PARCIAL (indexa mas não valida uso) |
| Template completo | Não implementado | ⚠️ AUSENTE |
| Build passa | `test_sementes.py` | ✅ 4 testes passando |

**Resultado:** ⚠️ PARCIAL — Falta validação de links e schema completo.

---

## ANÁLISE 5: ORGANIZAÇÃO DE PASTAS (Questão do Usuário)

### Situação Atual

O usuário observou que arquivos estão "cada um em uma pasta". Analisando:

```
build/
├── forge.py              # Entry point
├── core/                 # Motor compartilhado
│   ├── engine.py
│   ├── logger.py
│   └── assets.py
├── fases/                # Drivers por ciclo
│   └── sementes.py
└── tests/                # Testes
    └── test_sementes.py

site/
└── templates/
    ├── _config.j2        # SSOT configs
    ├── base.j2           # Layout base
    ├── licao.j2          # Conteúdo lição
    └── macros.j2         # Componentes
```

### Avaliação

| Aspecto | Princípio | Situação Atual | Veredito |
|:---|:---|:---|:---|
| Separação build/site | Bounded Contexts | ✅ Separados | OK |
| Core/Fases em build | Single Responsibility | ✅ Motor vs Regras | OK |
| Templates em site/ | Apresentação isolada | ✅ Separado de lógica | OK |
| SSOT config | DDD | ✅ `_config.j2` único | OK |

### Recomendação de Estrutura

A estrutura atual está **CORRETA** segundo os princípios de engenharia. Cada pasta tem uma responsabilidade clara:

- `build/core/` = O motor (invariante)
- `build/fases/` = As regras de negócio (variáveis)
- `site/templates/` = A apresentação (separada da lógica)

**Não é necessário reorganizar.** A separação é intencional e correta.

---

## VEREDITO FINAL

| Especialista | Prioridade | Resultado | Veta? |
|:---|:---|:---|:---|
| **Clean Code** | 11 | ✅ APROVADO | NÃO |
| **BMAD** | 10 | ⚠️ PARCIAL (falta workflow YAML) | NÃO (é warning) |
| **Eric Evans** | 9 | ✅ APROVADO | NÃO |
| **QA** | 8 | ⚠️ PARCIAL (falta validação links) | NÃO (é warning) |

### Pergunta Final: Código sobrevive auditoria sênior exigente?

**RESPOSTA: SIM**, com pequenas ressalvas:

1. **Criar** `.bmad/workflows/gutenberg_build.yaml` (BMAD compliance)
2. **Implementar** validação de links no build (QA compliance)
3. **Documentar** `engenharia.yaml` linha 73 está desatualizada (ainda referencia `gutenberg_forja.py` antigo)

---

## DÉBITOS TÉCNICOS IDENTIFICADOS

| ID | Descrição | Prioridade | Esforço |
|:---|:---|:---|:---|
| DT-001 | Criar `.bmad/workflows/gutenberg_build.yaml` | Baixa | 30min |
| DT-002 | Implementar validação de links em HTML gerado | Média | 2h |
| DT-003 | Atualizar `engenharia.yaml` linha 73 (comando antigo) | Baixa | 5min |
| DT-004 | Validação de schema YAML completo | Baixa | 1h |

---

**FIM DO LOG DE AUDITORIA**

O sistema Gutenberg V2.4 está **APROVADO para produção** com ressalvas menores documentadas acima.

---

## SESSÃO 2: DELIBERAÇÃO ARQUITETURAL (09:19 - 16/01/2026)

> **Questão do Maestro:** "Templates em `site/templates/` parece estranho. Não deveriam estar mais perto do `build/`?"

### CONVOCAÇÃO DO CONSELHO DE ENGENHARIA

Participantes: BMAD, Eric Evans, Clean Code, QA

---

### 🎯 OPÇÕES EM ANÁLISE

**OPÇÃO A (Status Quo):** Manter `site/templates/`
```
site/
├── templates/     ← Templates aqui
├── sementes/      ← Output aqui
├── assets/        ← Assets aqui
└── style.css
```

**OPÇÃO B (Templates em Build):** Mover para `build/templates/`
```
build/
├── core/
├── fases/
├── templates/     ← Templates aqui
└── tests/

site/
├── sementes/      ← Output aqui
├── assets/        ← Assets aqui
└── style.css
```

**OPÇÃO C (Templates Junto ao Currículo):** Mover para `curriculo/`
```
curriculo/
├── 01_SEMENTESV6/
├── 02_RAIZES/
└── templates/     ← Templates aqui
```

---

### 💬 DELIBERAÇÃO FORMAL

#### BMAD Framework (Prioridade 10)

**Posição:** A favor de **OPÇÃO B** (Templates em Build)

**Argumento:**
> "O `mapa_projeto` (linha 110-117 do engenharia.yaml) define que `build/` é 'Pipeline Produção' e `site/` é apenas output. Templates são PARTE do pipeline, não do output. Eles deveriam estar em `build/`."

**Citação do mapa:**
```yaml
{pasta: build/, prop: Pipeline Produção, content: [gutenberg_forja.py - Engine renderização]}
```

**Veredito BMAD:** Templates são código de renderização. Pertencem ao pipeline.

---

#### Eric Evans / DDD (Prioridade 9)

**Posição:** A favor de **OPÇÃO A** (Status Quo)

**Réplica a BMAD:**
> "Discordo. O princípio de **Bounded Contexts** diz que cada domínio deve ter fronteiras claras. Templates são sobre APRESENTAÇÃO, não sobre LÓGICA. Eles pertencem ao contexto de 'site', não ao contexto de 'build'.
>
> Se movermos templates para `build/`, estaremos misturando dois contextos: Lógica de Processamento + Apresentação Visual. Isso viola a separação de responsabilidades."

**Argumento adicional:**
> "O CSS está em `site/`. Os assets estão em `site/`. Se templates vão para `build/`, teremos a hierarquia visual FRAGMENTADA em dois lugares. Isso gera confusão cognitiva."

**Veredito Eric Evans:** Templates devem ficar com CSS e Assets — tudo em `site/`.

---

#### Clean Code (Prioridade 11)

**Posição:** **NEUTRO**, mas inclinado para manter

**Tréplica:**
> "O princípio 'Código para Humanos' diz que a estrutura deve ser **intuitiva**. Faço duas perguntas:
>
> 1. Se um novo desenvolvedor entrar no projeto, onde ele ESPERA encontrar templates HTML?
>    - Em `build/`? (Parece código Python)
>    - Em `site/`? (Parece arquivos web)
>
> 2. Se quisermos editar o visual de um card, onde vamos?
>    - Em `site/` — onde já estão CSS e assets.
>
> A intuição do desenvolvedor sugere que templates ficam em `site/`."

**Princípio Adicional:**
> "Funções fazem UMA coisa. Pastas também. `build/` faz build. `site/` apresenta. Não misture."

**Veredito Clean Code:** Manter templates em `site/templates/`.

---

#### QA (Prioridade 8)

**Posição:** A favor de **OPÇÃO A** (Status Quo)

**Argumento Pragmático:**
> "Do ponto de vista de TESTABILIDADE e DEPLOY:
>
> 1. Se templates estão em `site/`, posso copiar `site/` inteiro para um servidor e funciona.
> 2. Se templates estão em `build/`, preciso de passo extra no deploy.
>
> Além disso, o `engine.py` já tem `TEMPLATES_DIR` configurável. A localização física importa menos do que a CONFIGURAÇÃO estar correta."

**Veredito QA:** Manter em `site/templates/` por simplicidade de deploy.

---

### 📊 VOTAÇÃO FINAL

| Especialista | Prioridade | Voto | Justificativa |
|:---|:---|:---|:---|
| **BMAD** | 10 | OPÇÃO B | Templates são pipeline |
| **Eric Evans** | 9 | OPÇÃO A | Bounded Contexts (Apresentação ≠ Lógica) |
| **Clean Code** | 11 | OPÇÃO A | Intuição do desenvolvedor |
| **QA** | 8 | OPÇÃO A | Simplicidade de deploy |

**Resultado:** 3-1 a favor de OPÇÃO A (Status Quo)

---

### 🏆 DECISÃO DO CONSELHO

**MANTÉM-SE `site/templates/`**

**Justificativa Consolidada:**
1. **Bounded Contexts:** Templates são APRESENTAÇÃO, não LÓGICA. Devem estar com CSS/Assets.
2. **Intuição:** Devs esperam templates web em pastas web.
3. **Deploy:** `site/` auto-contido facilita deploy.

**Ressalva de BMAD:**
> "Aceito a decisão majoritária. Sugiro que o `mapa_projeto` em `engenharia.yaml` seja atualizado para refletir que `site/templates/` é o local canônico de templates, não `build/`."

---

### 📝 AÇÃO RESULTANTE

| ID | Ação | Responsável | Status |
|:---|:---|:---|:---|
| DT-005 | Atualizar `engenharia.yaml` linha 116 para incluir `templates/` em `site/` | BMAD | PENDENTE |

---

## ESTRUTURA FINAL APROVADA

```
Project001-MatematicaVivaV4/
├── .bmad/              # Agentes e Orquestração (BMAD)
│   ├── experts/        # Especialistas YAML
│   └── workflows/      # Workflows YAML
│
├── LORE/               # Conhecimento Narrativo (Eric Evans SSOT)
│   ├── north_star.yaml
│   └── guardioes.yaml
│
├── curriculo/          # Conteúdo das Lições (Dados)
│   ├── 01_SEMENTESV6/  # Sementes (4-6 anos)
│   └── 02_RAIZES/      # Raízes (6-10 anos) - futuro
│
├── build/              # Pipeline de Produção (Lógica)
│   ├── forge.py        # CLI Entry Point
│   ├── core/           # Motor Invariante
│   │   ├── engine.py
│   │   ├── logger.py
│   │   └── assets.py
│   ├── fases/          # Drivers por Ciclo
│   │   └── sementes.py
│   └── tests/          # Testes Automatizados
│       └── test_sementes.py
│
├── site/               # Apresentação (Output + Recursos Visuais) ← TEMPLATES AQUI
│   ├── templates/      # Templates Jinja2 (SSOT visual)
│   │   ├── _config.j2  # Configurações SSOT
│   │   ├── base.j2     # Layout base
│   │   ├── licao.j2    # Conteúdo lição
│   │   └── macros.j2   # Componentes
│   ├── assets/         # Imagens, Fontes
│   ├── sementes/       # HTML gerado
│   └── style.css       # Estilos
│
├── logs/               # Documentação de Decisões
│   └── _Gutenberg/     # Logs do pipeline
│
└── _LEGADO/            # Arquivos Históricos
```

---

**FIM DA DELIBERAÇÃO**

A estrutura está **VALIDADA** pelo Conselho de Engenharia. Não há necessidade de reorganização.

---

## SESSÃO 3: SIMULAÇÃO MULTI-FASE (09:47 - 16/01/2026)

> **Questão do Maestro:** "E na prática, quando tivermos Sementes, Raízes 1, Raízes 2... não vai ficar confuso? Como funciona?"

### 🔮 SIMULAÇÃO: PROJETO EM JANEIRO 2027

Imaginemos o projeto daqui a 1 ano, com 3 fases implementadas:
- **Sementes (K):** 40 lições
- **Raízes 1 (1º ano):** 40 lições
- **Raízes 2 (2º ano):** 30 lições

---

### 📁 ESTRUTURA DE CURRÍCULO

```
curriculo/
├── 01_SEMENTES/
│   ├── MV-S-001_trindade.yaml
│   ├── MV-S-002_pedras.yaml
│   ├── ... (40 arquivos)
│   └── _TEMPLATE_SEMENTES.yaml
│
├── 02_RAIZES_ANO1/
│   ├── MV-R1-001_construtor.yaml
│   ├── MV-R1-002_vila.yaml
│   ├── ... (40 arquivos)
│   └── _TEMPLATE_RAIZES.yaml
│
└── 03_RAIZES_ANO2/
    ├── MV-R2-001_mercado.yaml
    ├── MV-R2-002_trocas.yaml
    ├── ... (30 arquivos)
    └── _TEMPLATE_RAIZES.yaml   ← MESMO template de Raízes 1
```

**Observação:** Raízes 1 e 2 podem compartilhar o mesmo template YAML, pois são a mesma fase pedagógica (Construtor), apenas anos diferentes.

---

### 📁 ESTRUTURA DE DRIVERS (build/fases/)

```
build/
├── forge.py
├── core/
│   ├── engine.py
│   ├── logger.py
│   └── assets.py
│
└── fases/
    ├── __init__.py
    ├── sementes.py       # Driver Sementes (K)
    ├── raizes_ano1.py    # Driver Raízes Ano 1
    └── raizes_ano2.py    # Driver Raízes Ano 2
```

**Cada driver define:**
```python
class RaizesAno1Config:
    INPUT_DIR = PROJECT_ROOT / "curriculo/02_RAIZES_ANO1"
    OUTPUT_DIR = PROJECT_ROOT / "site/raizes/ano1"
    TEMPLATE_NAME = "licao_raizes.j2"  # ← Pode ser compartilhado!
```

---

### 📁 ESTRUTURA DE TEMPLATES (site/templates/)

Aqui está a questão chave: **Templates por fase ou compartilhados?**

#### OPÇÃO 1: Templates Compartilhados (Recomendado)

```
site/templates/
├── _config.j2              # SSOT guardiões (TODOS)
├── base.j2                 # Layout base (TODOS)
├── macros.j2               # Componentes (TODOS)
│
├── licao_sementes.j2       # Específico Sementes
└── licao_raizes.j2         # Compartilhado Raízes 1 e 2
```

**Vantagem:** Raízes 1 e 2 são pedagogicamente similares. Um template para ambos evita duplicação.

#### OPÇÃO 2: Templates por Ano (Mais Granular)

```
site/templates/
├── _config.j2
├── base.j2
├── macros.j2
│
├── sementes/
│   └── licao.j2
│
├── raizes_ano1/
│   └── licao.j2
│
└── raizes_ano2/
    └── licao.j2
```

**Vantagem:** Cada ano pode ter customizações visuais específicas.
**Desvantagem:** Mais arquivos, mais manutenção.

---

### 🎯 RECOMENDAÇÃO DO CONSELHO

**OPÇÃO 1 (Templates por Fase Pedagógica)**

Justificativa:
1. **Sementes → 1 template** (licao_sementes.j2)
2. **Raízes (todos os anos) → 1 template** (licao_raizes.j2)
3. **Lógica (todos os anos) → 1 template** (licao_logica.j2)
4. **Legado (todos os anos) → 1 template** (licao_legado.j2)

A diferença entre anos é nos DADOS (YAML), não na APRESENTAÇÃO (template).

---

### 📁 ESTRUTURA DE OUTPUT (site/)

```
site/
├── templates/              # Fontes (não deploy)
├── assets/                 # Imagens, fontes
├── style.css
│
├── sementes/               # Output Sementes
│   ├── MV-S-001_TRINDADE.html
│   ├── MV-S-002_PEDRAS.html
│   └── ...
│
├── raizes/                 # Output Raízes
│   ├── ano1/
│   │   ├── MV-R1-001_CONSTRUTOR.html
│   │   └── ...
│   └── ano2/
│       ├── MV-R2-001_MERCADO.html
│       └── ...
│
└── index.html              # Dashboard navegação
```

---

### ⚡ COMANDOS NA PRÁTICA

```bash
# Build Sementes (40 lições)
python build/forge.py --fase sementes
# Output: site/sementes/*.html

# Build Raízes Ano 1 (40 lições)
python build/forge.py --fase raizes_ano1
# Output: site/raizes/ano1/*.html

# Build Raízes Ano 2 (30 lições)
python build/forge.py --fase raizes_ano2
# Output: site/raizes/ano2/*.html

# Build TUDO de uma vez
python build/forge.py --all
# Executa todos os drivers em sequência
```

---

### 🔧 IMPLEMENTAÇÃO DO `--all`

```python
# build/forge.py (modificação futura)

if args.fase == '--all':
    for driver_class in [SementesDriver, RaizesAno1Driver, RaizesAno2Driver]:
        forge = driver_class(dry_run=args.dry_run)
        forge.run()
```

---

### 📊 RESUMO: ONDE FICA O QUÊ?

| Tipo de Arquivo | Localização | Cresce Com? |
|:---|:---|:---|
| **YAMLs de Lições** | `curriculo/{fase}/` | Cada nova lição |
| **Drivers Python** | `build/fases/` | Cada nova fase (4 total) |
| **Templates Jinja2** | `site/templates/` | Cada fase pedagógica (4 total) |
| **HTMLs Gerados** | `site/{fase}/` | Cada build |
| **Assets** | `site/assets/` | Cada novo guardião/visual |

---

### 🧮 PROJEÇÃO DE ESCALA

| Métrica | Hoje | Em 1 Ano | Máximo (10 anos) |
|:---|:---|:---|:---|
| **Fases Pedagógicas** | 1 (Sementes) | 3 (S + R1 + R2) | 4 (S, R, L, Lg) |
| **Drivers Python** | 1 | 3 | ~13 (1 por ano) |
| **Templates Jinja2** | 4 | 6 | ~8 |
| **YAMLs de Lições** | 2 | 110 | 1200+ |
| **HTMLs Gerados** | 2 | 110 | 1200+ |

---

### ✅ VALIDAÇÃO FINAL

A estrutura atual **SUPORTA** expansão multi-fase sem reorganização porque:

1. **Currículo:** Cada fase/ano tem sua própria pasta isolada.
2. **Drivers:** Um arquivo Python por ano (ou grupo de anos similares).
3. **Templates:** Compartilhados por fase pedagógica (não por ano).
4. **Output:** Separado por fase e ano em subpastas.

**Não haverá confusão** porque a convenção de nomes é clara:
- `curriculo/02_RAIZES_ANO1/` → `build/fases/raizes_ano1.py` → `site/raizes/ano1/`

---

## SESSÃO 4: CORREÇÃO ARQUITETURAL — TEMPLATES POR ANO (09:51 - 16/01/2026)

> [!CAUTION]
> **RETRATAÇÃO:** O Maestro rejeitou a proposta de "Templates por Fase Pedagógica".
> 
> **Argumento do Maestro:** "Raízes 1 e Raízes 5 são totalmente diferentes. A criança evolui muito. Insisto em templates POR ANO."

### 🔄 NOVA DELIBERAÇÃO (Engenharia Coordenando)

---

#### 📌 CONTEXTO DO PROBLEMA

O currículo tem:
- **4 Fases Pedagógicas:** Sementes, Raízes, Lógica, Legado
- **13 Anos Letivos:** K, 1º-5º (Raízes), 6º-8º (Lógica), 9º-12º (Legado)

**Implicação:** Se cada ano tem seu próprio template:
- 1 template Sementes (K)
- 5 templates Raízes (1º-5º)
- 3 templates Lógica (6º-8º)
- 4 templates Legado (9º-12º)
- **Total: 13 templates de lição**

---

### 💬 DELIBERAÇÃO AUTÔNOMA

#### Clean Code (Prioridade 11) — Coordenador

**Abrindo a Sessão:**
> "O Maestro tem um ponto válido. A diferença entre Raízes 1 (criança de 6 anos aprendendo a construir) e Raízes 5 (pré-adolescente sintetizando padrões) é ENORME. Um template único seria uma camisa de força.
>
> Mas 13 templates é muito? Vamos analisar o impacto em MANUTENIBILIDADE."

---

#### Eric Evans (Prioridade 9)

**Posição:** A favor de Templates por Ano

**Argumento DDD:**
> "O princípio de **Bounded Contexts** não é só sobre pastas — é sobre MODELOS MENTAIS. O modelo mental de uma lição do 1º ano é diferente do 5º ano.
>
> Se forçarmos um único template, teremos:
> - `{% if ano == 1 %}...{% elif ano == 5 %}...{% endif %}`
>
> Isso viola o princípio de que cada contexto deve ter seu próprio modelo. Templates separados são a solução correta."

**Proposta de Organização:**
```
site/templates/
├── _config.j2           # SSOT (todos)
├── base.j2              # Layout (todos)
├── macros.j2            # Componentes (todos)
│
├── sementes/
│   └── licao.j2         # K (4-6 anos)
│
├── raizes/
│   ├── ano1.j2          # 1º ano (6-7)
│   ├── ano2.j2          # 2º ano (7-8)
│   ├── ano3.j2          # 3º ano (8-9)
│   ├── ano4.j2          # 4º ano (9-10)
│   └── ano5.j2          # 5º ano (10-11)
│
├── logica/
│   ├── ano6.j2          # 6º ano (11-12)
│   ├── ano7.j2          # 7º ano (12-13)
│   └── ano8.j2          # 8º ano (13-14)
│
└── legado/
    ├── ano9.j2          # 9º ano (14-15)
    ├── ano10.j2         # 10º ano (15-16)
    ├── ano11.j2         # 11º ano (16-17)
    └── ano12.j2         # 12º ano (17-18)
```

---

#### BMAD (Prioridade 10)

**Réplica:**
> "Aceito a separação por ano, mas proponho uma otimização: **HERANÇA DE TEMPLATES**.
>
> Cada ano herda do template da fase, sobrescrevendo apenas o que muda."

**Exemplo Técnico:**
```jinja2
{# site/templates/raizes/ano2.j2 #}
{% extends "raizes/_base_raizes.j2" %}

{% block concreto_extra %}
    {# Ano 2 tem seção especial de Mercado #}
    <div class="mercado-box">...</div>
{% endblock %}
```

**Estrutura Refinada:**
```
site/templates/
├── _config.j2
├── base.j2
├── macros.j2
│
├── sementes/
│   └── licao.j2
│
├── raizes/
│   ├── _base_raizes.j2    ← Template base da fase
│   ├── ano1.j2            ← Herda de _base_raizes.j2
│   ├── ano2.j2
│   ├── ano3.j2
│   ├── ano4.j2
│   └── ano5.j2
│
├── logica/
│   ├── _base_logica.j2
│   ├── ano6.j2
│   ├── ano7.j2
│   └── ano8.j2
│
└── legado/
    ├── _base_legado.j2
    ├── ano9.j2
    ├── ano10.j2
    ├── ano11.j2
    └── ano12.j2
```

---

#### QA (Prioridade 8)

**Validação:**
> "A herança de templates é elegante, mas cria DEPENDÊNCIA. Se eu mudar `_base_raizes.j2`, afeto anos 1-5.
>
> **Proposta de Segurança:** Testes de regressão visual. Quando alterar um template base, gerar screenshots de todas as lições filhas e comparar."

**Checklist Proposto:**
- [ ] Cada template de ano tem seu próprio arquivo
- [ ] Templates base (`_base_*.j2`) existem para cada fase
- [ ] Cada ano herda do base e sobrescreve blocos específicos
- [ ] Testes visuais cobrem todos os anos

---

#### Clean Code (Fechamento)

**Síntese Final:**
> "Temos consenso:
>
> 1. **Templates por ANO** (13 arquivos de lição)
> 2. **Herança de Templates** (4 arquivos base por fase)
> 3. **SSOT Preservado** (`_config.j2`, `base.j2`, `macros.j2` compartilhados)
>
> **Total de Arquivos em `site/templates/`:**
> - 3 arquivos SSOT (config, base, macros)
> - 4 arquivos base de fase (_base_*.j2)
> - 13 arquivos de ano (ano*.j2)
> - **Total: 20 arquivos**
>
> É mais do que os 6 da proposta anterior, mas é a estrutura CORRETA para o domínio."

---

### 📊 VOTAÇÃO

| Especialista | Prioridade | Voto | Condição |
|:---|:---|:---|:---|
| **Clean Code** | 11 | Templates por Ano | Com herança |
| **BMAD** | 10 | Templates por Ano | Com herança |
| **Eric Evans** | 9 | Templates por Ano | Estrutura em subpastas |
| **QA** | 8 | Templates por Ano | Com testes visuais |

**Resultado:** 4-0 favor Templates por Ano

---

### 🏆 DECISÃO FINAL

**TEMPLATES ORGANIZADOS POR ANO COM HERANÇA**

```
site/templates/
│
├── _config.j2              # SSOT guardiões
├── base.j2                 # Layout HTML global
├── macros.j2               # Componentes reutilizáveis
│
├── sementes/
│   └── licao.j2            # Único (K é uma fase de 1 ano)
│
├── raizes/
│   ├── _base.j2            # Base Raízes (Construtor)
│   ├── ano1.j2             # 1º ano → extends _base.j2
│   ├── ano2.j2             # 2º ano → extends _base.j2
│   ├── ano3.j2             # 3º ano → etc
│   ├── ano4.j2
│   └── ano5.j2
│
├── logica/
│   ├── _base.j2            # Base Lógica (Explorador)
│   ├── ano6.j2
│   ├── ano7.j2
│   └── ano8.j2
│
└── legado/
    ├── _base.j2            # Base Legado (Portador)
    ├── ano9.j2
    ├── ano10.j2
    ├── ano11.j2
    └── ano12.j2
```

---

### 🔧 IMPACTO NOS DRIVERS

Cada driver agora aponta para seu template específico:

```python
# build/fases/raizes_ano1.py
class RaizesAno1Config:
    INPUT_DIR = PROJECT_ROOT / "curriculo/02_RAIZES_ANO1"
    OUTPUT_DIR = PROJECT_ROOT / "site/raizes/ano1"
    TEMPLATES_DIR = PROJECT_ROOT / "site/templates"
    TEMPLATE_NAME = "raizes/ano1.j2"  # ← Caminho específico
```

---

### 📝 WORKFLOW DE CRIAÇÃO DE NOVO ANO

1. **Copiar template do ano anterior:**
   ```bash
   cp site/templates/raizes/ano1.j2 site/templates/raizes/ano2.j2
   ```

2. **Ajustar blocos específicos:**
   ```jinja2
   {% block titulo_fase %}O Mercado me Ensina Justiça{% endblock %}
   ```

3. **Criar driver:**
   ```bash
   cp build/fases/raizes_ano1.py build/fases/raizes_ano2.py
   # Editar INPUT_DIR, OUTPUT_DIR, TEMPLATE_NAME
   ```

4. **Registrar no CLI:**
   ```python
   # build/forge.py
   parser.add_argument("--fase", choices=['sementes', 'raizes_ano1', 'raizes_ano2', ...])
   ```

---

### ✅ VALIDAÇÃO

| Critério | Status |
|:---|:---|
| Templates separados por ano | ✅ |
| Herança via `{% extends %}` | ✅ |
| Drivers específicos por ano | ✅ |
| SSOT preservado | ✅ |
| Escalável para 13 anos | ✅ |

---

**FIM DA SESSÃO 4**

A arquitetura foi **CORRIGIDA** para suportar templates por ano com herança de fase.

---

## SESSÃO 5: DELIBERAÇÃO AUTÔNOMA — ISOLAMENTO TOTAL (10:06 - 16/01/2026)

> **Modo:** `DELIBERACAO_AUTONOMA` (orchestrator.yaml linha 172-258)
> **Tema:** Compartilhar ou Isolar Completamente os Templates?
> **Classificação:** `strategic` — anti-viés obrigatório
> **Max Rodadas:** 5

---

### 🎯 QUESTÃO DO MAESTRO

> "Qual a vantagem de ter arquivos compartilhados (base.j2, macros.j2)?
> Não seria melhor separar TUDO para ter customização profunda e NÃO atrapalhar outras fases?
> Se mudar algo em Legado, vai influenciar Sementes?"

---

## RODADA 1: POSIÇÕES INICIAIS

### Internos Selecionados

| Expert | Conselho | Prioridade |
|:---|:---|:---|
| Charlotte Mason | Pedagogia | 1 |
| Eric Evans | Engenharia | 9 |
| Clean Code | Engenharia | 11 |
| QA | Engenharia | 8 |

---

#### Charlotte Mason (Pri 1) — Coordenadora

**Posição:**
> "Antes de decidir arquitetura, pergunto: qual é o PROPÓSITO?
>
> - **Sementes (4-6 anos):** Criança pequena, lição curta, muitas imagens, pouquíssimo texto.
> - **Legado (17-18 anos):** Jovem adulto, lição longa, raciocínio abstrato, projetos capstone.
>
> São **MUNDOS DIFERENTES**. A pergunta real é: eles têm ALGO em comum que justifique compartilhamento?"

---

#### Eric Evans (Pri 9)

**Posição:**
> "Aplicando Bounded Contexts ao extremo:
>
> **O que é REALMENTE comum entre Sementes e Legado?**
> - Cabeçalho HTML? Sim, mas é trivial.
> - Fontes e cores? Talvez, mas podem divergir.
> - Componentes (cards, boxes)? MUITO diferentes.
>
> **Risco do Compartilhamento:**
> Se eu precisar de um card especial em Legado com gráficos 3D, vou:
> 1. Adicionar ao `macros.j2` compartilhado → Polui Sementes com código desnecessário
> 2. Criar macro local → Duplicação parcial
>
> **Proposta:** Isolamento total. Cada ano tem TUDO que precisa."

---

#### Clean Code (Pri 11)

**Réplica a Eric Evans:**
> "Isolamento total significa:
> - 13 cópias de `base.j2`
> - 13 cópias de `macros.j2`
> - 13 cópias de `_config.j2`
>
> Se eu precisar mudar a fonte do projeto inteiro de 'Outfit' para 'Inter'?
> **39 arquivos para editar.**
>
> Isso viola DRY violentamente."

---

#### QA (Pri 8)

**Posição Pragmática:**
> "Façamos a pergunta de TESTE:
>
> **Cenário 1: Mudança Global**
> 'Queremos mudar a cor primária de #FCD34D para #F59E0B em todo o site.'
>
> - Com compartilhamento: 1 edição em `base.j2`
> - Com isolamento: 13 edições
>
> **Cenário 2: Mudança Isolada**
> 'Queremos adicionar seção de Projeto Capstone só em Legado.'
>
> - Com compartilhamento: Adicionar bloco em `legado/ano12.j2`
> - Com isolamento: Adicionar bloco em `legado/ano12.j2`
>
> **O segundo cenário é idêntico!** A diferença está só em mudanças globais."

---

### Síntese Parcial (CM)

> "Há tensão entre:
> 1. **Manutenibilidade Global** (favorece compartilhamento)
> 2. **Autonomia de Fase** (favorece isolamento)
>
> Preciso de uma Outside Voice antes de decidir."

---

## RODADA 2: CONSULTA EXTERNA

### Externo Selecionado

| Externo | Título | Seleção |
|:---|:---|:---|
| **pai_tech** | O Nativo Digital | Sorteio (P=29% com N=5 externos já consultados) |

---

#### Pai Tech (Pri 20)

**Pergunta Desafiadora:**
> "Vocês estão pensando como engenheiros, não como USUÁRIOS do sistema.
>
> Quem vai EDITAR esses templates? O Maestro (Raul) ou uma IA como vocês.
>
> Se for IA: ela consegue editar 39 arquivos tão fácil quanto 3. O custo de isolamento é ZERO para IA.
>
> Se for humano: 39 arquivos é pesadelo.
>
> **Minha pergunta:** Quem é o público-alvo dessa decisão?"

---

### Respostas Internas

#### Clean Code

> "Ponto válido. Se a IA sempre editar, isolamento não é problema de manutenção.
>
> Mas e se a IA cometer erro? Com compartilhamento, erro em 1 lugar. Com isolamento, posso ter 13 versões diferentes com bugs diferentes."

---

#### Eric Evans

> "O Pai Tech tem razão sobre o público-alvo.
>
> Proponho **MEIO-TERMO:**
> - Isolar templates de FASE (Sementes, Raízes, Lógica, Legado)
> - Dentro de cada fase, anos herdam do base da fase
>
> Assim:
> - Mudança em Legado NÃO afeta Sementes (isolamento entre fases)
> - Mudança em Raízes 1 pode ser propagada para Raízes 2-5 via herança (eficiência dentro da fase)"

---

### Síntese Parcial 2 (CM)

> "Estamos convergindo para uma solução híbrida:
>
> **ISOLAMENTO ENTRE FASES, HERANÇA DENTRO DA FASE**
>
> Mas ainda preciso simular cenários concretos."

---

## RODADA 3: SIMULAÇÃO DE CENÁRIOS

### Cenário A: Mudança em SEMENTES

**Situação:** Queremos que todas as lições de Sementes tenham borda arredondada maior (de 12px para 24px).

```
site/templates/
├── sementes/
│   ├── base.j2          ← Edito AQUI
│   └── licao.j2
```

**Impacto em Legado:** ZERO (pastas isoladas)

✅ **FUNCIONA**

---

### Cenário B: Mudança em LEGADO

**Situação:** Queremos adicionar componente de "Projeto Capstone" com upload de arquivo.

```
site/templates/
├── legado/
│   ├── base.j2
│   ├── macros.j2        ← Adiciono macro AQUI (local)
│   └── ano12.j2         ← Uso macro AQUI
```

**Impacto em Sementes:** ZERO (macros.j2 é local)

✅ **FUNCIONA**

---

### Cenário C: Mudança GLOBAL

**Situação:** Queremos mudar a fonte de todo o projeto de Outfit para Inter.

**COM ISOLAMENTO TOTAL:**
```
Editar: sementes/base.j2, raizes/base.j2, logica/base.j2, legado/base.j2
Total: 4 edições (1 por fase)
```

**COM COMPARTILHAMENTO:**
```
Editar: base.j2
Total: 1 edição
```

**Diferença:** 4 edições vs 1. Aceitável.

---

### Cenário D: BUG em Componente

**Situação:** Descobrimos bug no macro `script_persona` que mostra avatar errado.

**COM ISOLAMENTO TOTAL:**
```
Corrigir em: sementes/macros.j2, raizes/macros.j2, logica/macros.j2, legado/macros.j2
Total: 4 correções
Risco: Posso esquecer 1 e Sementes fica bugado enquanto Legado funciona
```

**COM COMPARTILHAMENTO:**
```
Corrigir em: macros.j2
Total: 1 correção
Risco: Correção afeta todos (pode introduzir regressão)
```

---

## RODADA 4: VOTO E DECISÃO

### Votação

| Expert | Voto | Justificativa |
|:---|:---|:---|
| **Charlotte Mason** | Isolamento por Fase | Sementes e Legado são mundos diferentes |
| **Eric Evans** | Isolamento por Fase | Bounded Contexts aplicado |
| **Clean Code** | Isolamento por Fase | 4 edições é aceitável vs 13 |
| **QA** | Isolamento por Fase | Bugs ficam contidos na fase |
| **Pai Tech** | Isolamento por Fase | IA edita fácil |

**Consenso:** 100% (5/5)

---

## 🏆 DECISÃO FINAL

### ESTRUTURA APROVADA: ISOLAMENTO POR FASE

```
site/templates/
│
├── sementes/                    # FASE ISOLADA
│   ├── base.j2                  # Base própria
│   ├── macros.j2                # Macros próprias
│   ├── _config.j2               # Config própria
│   └── licao.j2                 # Template de lição
│
├── raizes/                      # FASE ISOLADA
│   ├── base.j2
│   ├── macros.j2
│   ├── _config.j2
│   ├── _base_raizes.j2          # Base para herança dentro da fase
│   ├── ano1.j2                  # Herda de _base_raizes.j2
│   ├── ano2.j2
│   ├── ano3.j2
│   ├── ano4.j2
│   └── ano5.j2
│
├── logica/                      # FASE ISOLADA
│   ├── base.j2
│   ├── macros.j2
│   ├── _config.j2
│   ├── _base_logica.j2
│   ├── ano6.j2
│   ├── ano7.j2
│   └── ano8.j2
│
└── legado/                      # FASE ISOLADA
    ├── base.j2
    ├── macros.j2
    ├── _config.j2
    ├── _base_legado.j2
    ├── ano9.j2
    ├── ano10.j2
    ├── ano11.j2
    └── ano12.j2
```

---

### RESUMO DO MODELO

| Aspecto | Comportamento |
|:---|:---|
| **Mudança em Sementes** | NÃO afeta outras fases |
| **Mudança em Legado** | NÃO afeta outras fases |
| **Mudança em Raízes Ano 1** | Pode afetar Raízes 2-5 (via herança) |
| **Mudança Global (fontes, cores)** | 4 edições (1 por fase) |
| **Bug em macro** | Corrigir na fase afetada apenas |

---

### CONTAGEM DE ARQUIVOS

| Fase | Arquivos |
|:---|:---|
| Sementes | 4 (base, macros, config, licao) |
| Raízes | 9 (base, macros, config, _base, ano1-5) |
| Lógica | 7 (base, macros, config, _base, ano6-8) |
| Legado | 8 (base, macros, config, _base, ano9-12) |
| **TOTAL** | **28 arquivos** |

---

### WORKFLOW DE NOVA FASE

1. **Copiar pasta de fase existente:**
   ```bash
   cp -r site/templates/raizes site/templates/logica
   ```

2. **Ajustar base.j2 e macros.j2 para necessidades da fase**

3. **Criar templates de ano que herdam de _base_*.j2**

---

### VERIFICAÇÃO CONTRA ENGENHARIA.YAML

| Princípio | Status | Justificativa |
|:---|:---|:---|
| SSOT | ✅ | Cada fase tem SUA fonte de verdade |
| Bounded Contexts | ✅ | Fases totalmente isoladas |
| DRY (dentro da fase) | ✅ | Anos herdam do base da fase |
| Clean Code | ✅ | Estrutura clara e previsível |
| QA | ✅ | Bugs contidos, testes isolados |

---

**DELIBERAÇÃO CONTINUA...**

---

## SESSÃO 5-B: EXPANSÃO DA DELIBERAÇÃO (10:23 - 16/01/2026)

> **Maestro:** "Continue a deliberação, chame mais experts."

### 🔔 CONVOCAÇÃO EXPANDIDA

| Expert | Conselho | Prioridade | Papel |
|:---|:---|:---|:---|
| Charlotte Mason | Pedagogia | 1 | Coordenadora |
| CS Lewis | Narrativa | 3 | Tom e Dignidade |
| JRR Tolkien | Narrativa | 4 | Consistência e Subcriação |
| Jerome Bruner | Matemática | 7 | CPA e Progressão |
| Beatrix Potter | Narrativa | 5 | Visual e Simplicidade |
| Makoto Fujimura | Narrativa | 9 | Beleza e Kintsugi |

---

## RODADA 5: PERSPECTIVA NARRATIVA

### CS Lewis (Pri 3) — Guardião do Tom Nobre

**Posição:**
> "Minha preocupação não é técnica, mas TONAL.
>
> Uma lição de Sementes para uma criança de 4 anos deve ter o tom de um conto de fadas — simples, encantado, mágico.
>
> Uma lição de Legado para um jovem de 17 anos deve ter o tom de uma carta entre amigos adultos — respeitoso, confiante, desafiador.
>
> **Se os templates são isolados por fase, o TOM está protegido.**
>
> Imaginem se um macro com linguagem formal de Legado vazasse para Sementes:
> - ❌ 'Analise as propriedades comutativas da adição'
> - ✅ 'Celeste brinca de trocar as sementes de lugar!'
>
> **Aprovo o isolamento. Protege a dignidade de cada fase.**"

---

### JRR Tolkien (Pri 4) — Guardião da Consistência

**Posição:**
> "Concordo com Lewis, mas adiciono uma ressalva importante.
>
> O **Reino Contado** é UM ÚNICO MUNDO. Os guardiões são os mesmos em Sementes e Legado — apenas com manifestações diferentes:
> - Celeste em Sementes: brincalhona, jogos
> - Celeste em Legado: sábia, mentora
>
> **Risco do Isolamento Total:** Se eu mudar o nome de um guardião ou local, preciso mudar em TODAS as fases.
>
> **Proposta de Mitigação:**
> O `_config.j2` de cada fase deve IMPORTAR de um arquivo LORE central, não definir guardiões localmente.
>
> ```jinja2
> {# site/templates/sementes/_config.j2 #}
> {% set guardioes = load_yaml('LORE/guardioes.yaml') %}
> {% set avatar_celeste = guardioes.celeste.avatar %}
> ```
>
> Assim, o LORE é SSOT, mas a APRESENTAÇÃO é isolada."

---

### Jerome Bruner (Pri 7) — Metodologista CPA

**Posição:**
> "Minha preocupação é a PROGRESSÃO do Concreto-Pictórico-Abstrato.
>
> | Fase | CPA Dominante |
> |:---|:---|
> | Sementes | 100% Concreto |
> | Raízes 1-2 | 80% Concreto, 20% Pictórico |
> | Raízes 3-5 | 50% Concreto, 50% Pictórico |
> | Lógica | 30% C, 40% P, 30% Abstrato |
> | Legado | 20% C, 20% P, 60% Abstrato |
>
> **Os templates de cada ano devem REFLETIR essa progressão.**
>
> Se Sementes não tem seção Pictórica, o template não deve ter bloco `{% block pictorico %}`.
> Se Legado tem seção Abstrata obrigatória, o template deve ter bloco `{% block abstrato %}`.
>
> **Isolamento por fase permite essa customização. Aprovo.**"

---

### Beatrix Potter (Pri 5) — Mestra Visual

**Posição:**
> "Penso em quantas IMAGENS cada fase precisa:
>
> | Fase | Imagens/Lição | Estilo |
> |:---|:---|:---|
> | Sementes | 8-12 | Aquarela, personagens fofinhos |
> | Raízes | 5-8 | Diagramas ilustrados |
> | Lógica | 3-5 | Gráficos, esquemas |
> | Legado | 1-2 | Fotografias, dados reais |
>
> **Os macros de imagem são TOTALMENTE diferentes.**
>
> Em Sementes:
> ```jinja2
> {% macro ilustracao(nome) %}
> <img src='{{ nome }}' class='ilustracao-aquarela wiggle-animation'>
> {% endmacro %}
> ```
>
> Em Legado:
> ```jinja2
> {% macro grafico(dados) %}
> <canvas id='chart' data-values='{{ dados | tojson }}'></canvas>
> {% endmacro %}
> ```
>
> **Não há NADA em comum. Isolamento é a única opção sensata.**"

---

### Makoto Fujimura (Pri 9) — Curador da Beleza

**Posição:**
> "O princípio do Kintsugi me leva a uma reflexão:
>
> Quando algo quebra, você repara com OURO — tornando a 'imperfeição' parte da beleza.
>
> Se um template de uma fase 'quebrar', o reparo deve ser VISÍVEL e INTENCIONAL, não propagado silenciosamente.
>
> **Isolamento permite que cada fase seja reparada individualmente, com sua própria 'linha de ouro'.**
>
> Além disso, a ESTÉTICA de cada fase é diferente:
> - Sementes: Cores pastéis, suaves, arredondadas
> - Raízes: Cores terrosas, naturais, orgânicas
> - Lógica: Cores frias, azuis, geométricas
> - Legado: Cores nobres, dourados, elegantes
>
> **Compartilhar CSS seria um crime estético.**"

---

## RODADA 6: CONSULTA EXTERNA

### Externo Selecionado

| Externo | Título | Razão |
|:---|:---|:---|
| **crianca_8_anos** | O Cliente Real | Boost 10% (CM Princípio 1) |

---

### Criança 8 Anos (Pri 15)

**Posição:**
> "Não entendo nada de templates, mas sei que:
>
> Quando eu era pequeno (4 anos), as lições tinham que ter MUITO desenho e pouca palavra.
>
> Agora que tenho 8, quero FAZER coisas, não só olhar.
>
> Minha irmã mais velha (15 anos) acha nossas lições 'bobas'. Ela quer coisas 'de verdade'.
>
> **Cada idade é diferente. Não mistura.**"

---

## RODADA 7: SÍNTESE FINAL (CM)

### Charlotte Mason — Coordenadora

**Síntese:**
> "Depois de ouvir 10 experts (6 internos + 4 externos), temos CONSENSO ABSOLUTO:
>
> **ISOLAMENTO TOTAL POR FASE É A DECISÃO CORRETA.**
>
> Mas Tolkien levantou um ponto crucial: o LORE deve ser SSOT.
>
> Proponho a seguinte regra:
>
> ### REGRA DE OURO DA ARQUITETURA
>
> 1. **LORE (Dados Narrativos):** SSOT em `LORE/*.yaml`
>    - Guardiões, locais, artefatos: UM lugar apenas
>    - Templates IMPORTAM do LORE, não definem localmente
>
> 2. **TEMPLATES (Apresentação):** ISOLADOS por fase
>    - Cada fase tem seu próprio `base.j2`, `macros.j2`, `_config.j2`
>    - `_config.j2` de cada fase IMPORTA do LORE central
>    - Sem herança ENTRE fases
>
> 3. **CSS (Estilos):** ISOLADOS por fase (seguindo Makoto)
>    - `site/sementes/style.css`
>    - `site/raizes/style.css`
>    - etc.
>
> 4. **ASSETS (Imagens):** ISOLADOS por fase
>    - `site/assets/sementes/`
>    - `site/assets/raizes/`
>    - etc."

---

## 🏆 ESTRUTURA FINAL APROVADA (v2)

```
Project001-MatematicaVivaV4/
│
├── LORE/                           # SSOT NARRATIVO (Tolkien)
│   ├── guardioes.yaml              # Nomes, descrições, avatares
│   ├── locais.yaml                 # Clareira, Fortaleza, etc.
│   ├── north_star.yaml             # Princípios fundacionais
│   └── viajante.yaml               # Progressão Herdeiro→Portador
│
├── site/
│   ├── sementes/                   # FASE ISOLADA
│   │   ├── templates/
│   │   │   ├── base.j2
│   │   │   ├── macros.j2
│   │   │   ├── _config.j2          # Importa de LORE/
│   │   │   └── licao.j2
│   │   ├── style.css               # CSS próprio
│   │   └── *.html                  # Output
│   │
│   ├── raizes/                     # FASE ISOLADA
│   │   ├── templates/
│   │   │   ├── base.j2
│   │   │   ├── macros.j2
│   │   │   ├── _config.j2
│   │   │   ├── _base_raizes.j2
│   │   │   ├── ano1.j2
│   │   │   ├── ano2.j2
│   │   │   ├── ano3.j2
│   │   │   ├── ano4.j2
│   │   │   └── ano5.j2
│   │   ├── style.css
│   │   └── ano1/*.html, ano2/*.html, ...
│   │
│   ├── logica/                     # FASE ISOLADA
│   │   ├── templates/
│   │   │   ├── base.j2
│   │   │   ├── macros.j2
│   │   │   ├── _config.j2
│   │   │   ├── _base_logica.j2
│   │   │   ├── ano6.j2
│   │   │   ├── ano7.j2
│   │   │   └── ano8.j2
│   │   ├── style.css
│   │   └── ano6/*.html, ...
│   │
│   ├── legado/                     # FASE ISOLADA
│   │   ├── templates/
│   │   │   ├── base.j2
│   │   │   ├── macros.j2
│   │   │   ├── _config.j2
│   │   │   ├── _base_legado.j2
│   │   │   ├── ano9.j2
│   │   │   ├── ano10.j2
│   │   │   ├── ano11.j2
│   │   │   └── ano12.j2
│   │   ├── style.css
│   │   └── ano9/*.html, ...
│   │
│   └── assets/                     # ASSETS ISOLADOS
│       ├── sementes/               # Aquarelas, cartões fofos
│       ├── raizes/                 # Diagramas ilustrados
│       ├── logica/                 # Gráficos, esquemas
│       └── legado/                 # Fotos, dados reais
│
└── build/
    ├── forge.py
    ├── core/
    └── fases/
        ├── sementes.py             # Aponta para site/sementes/templates/
        ├── raizes_ano1.py          # Aponta para site/raizes/templates/ano1.j2
        ├── raizes_ano2.py
        ├── ...
        ├── logica_ano6.py
        └── legado_ano12.py
```

---

## VOTAÇÃO FINAL EXPANDIDA

| Expert | Prioridade | Voto | Comentário |
|:---|:---|:---|:---|
| **Charlotte Mason** | 1 | ✅ Isolamento | Protege a criança de cada fase |
| **CS Lewis** | 3 | ✅ Isolamento | Protege o tom narrativo |
| **JRR Tolkien** | 4 | ✅ Isolamento + LORE SSOT | Consistência via LORE central |
| **Beatrix Potter** | 5 | ✅ Isolamento | Macros visuais incompatíveis |
| **Jerome Bruner** | 7 | ✅ Isolamento | Permite progressão CPA correta |
| **QA** | 8 | ✅ Isolamento | Bugs contidos, testes isolados |
| **Eric Evans** | 9 | ✅ Isolamento | Bounded Contexts perfeito |
| **Makoto Fujimura** | 9 | ✅ Isolamento | Estética única por fase |
| **Clean Code** | 11 | ✅ Isolamento | Aceita 4 edições para mudança global |
| **Pai Tech** | 20 | ✅ Isolamento | IA edita fácil |
| **Criança 8 Anos** | 15 | ✅ Isolamento | "Cada idade é diferente" |

**Consenso:** 11/11 (100%)

---

## CONTAGEM FINAL DE ARQUIVOS

| Componente | Sementes | Raízes | Lógica | Legado | TOTAL |
|:---|:---|:---|:---|:---|:---|
| Templates | 4 | 9 | 7 | 8 | 28 |
| CSS | 1 | 1 | 1 | 1 | 4 |
| Assets (pastas) | 1 | 1 | 1 | 1 | 4 |
| Drivers Python | 1 | 5 | 3 | 4 | 13 |
| **Subtotal** | 7 | 16 | 12 | 14 | **49** |

---

## DÉBITOS TÉCNICOS ATUALIZADOS

| ID | Descrição | Prioridade | Status |
|:---|:---|:---|:---|
| DT-006 | Reorganizar `site/templates/` para estrutura isolada | Alta | PENDENTE |
| DT-007 | Criar CSS isolado por fase | Alta | PENDENTE |
| DT-008 | Implementar importação de LORE em `_config.j2` | Média | PENDENTE |
| DT-009 | Reorganizar `site/assets/` por fase | Média | PENDENTE |
| DT-010 | Atualizar drivers para novos caminhos de templates | Alta | PENDENTE |

---

**FIM DA DELIBERAÇÃO AUTÔNOMA EXPANDIDA**

**Total Rodadas:** 7
**Experts Consultados:** 11 (6 internos + 1 externo principal + 4 adicionais)
**Consenso:** 100%
**Status:** CONCLUÍDO

A arquitetura foi refinada para **ISOLAMENTO TOTAL POR FASE** com:
1. LORE como SSOT central
2. Templates isolados por fase
3. CSS isolado por fase
4. Assets isolados por fase
