# 📐 PLANO: Arquitetura da Fase Raízes e Refatoração Core

**Data**: 2026-01-17 04:54
**Baseado em**: Análise in-loco dos drivers (`build/fases/*.py`) e templates (`site/sementes/templates`)
**Classificação**: `medium` (Mudança arquitetural moderada)
**Aprovador requerido**: Humano

---

## Visão Geral
Este plano define a estratégia para estabelecer a infraestrutura independente ("Bounded Context") para a fase **Raízes (1º Ano)**, garantindo desacoplamento visual (Templates) enquanto mantém a base de código limpa (DRY) através da extração de lógica comum para um novo módulo Core.

A arquitetura atual duplica lógica de navegação dentro dos drivers (`SementesDriver`, `RaizesDriver`) e força o compartilhamento de templates, o que inibe a evolução visual distinta necessária para materiais de 1º Ano (ex: numeração de versículos, layouts de cópia).

---

## Análise do Estado Atual

### Pontos-chave:
- **Duplicação de Código (Violação DRY)**: A classe `NavigationService` está implementada de forma idêntica em `sementes.py` e `raizes.py`.
- **Acoplamento de Templates**: A configuração atual de Raízes aponta para `site/sementes/templates`, impedindo que Raízes tenha sua própria identidade visual e estrutura HTML.
- **Risco de Manutenção**: Alterações no algoritmo de navegação exigiriam edições em múltiplos lugares.

---

## Estado Desejado

### Critérios de Sucesso:
- [ ] **Templates Desacoplados**: Existência de `site/raizes/templates/` com cópia base funcional de Sementes, permitindo divergência futura.
- [ ] **Lógica Centralizada**: `build/core/navigation.py` contendo a lógica de cálculo de links, consumida por ambos os drivers.
- [ ] **Drivers Limpos**: `SementesDriver` e `RaizesDriver` delegando o cálculo para o módulo core.
- [ ] **Build Funcional**: `python build/forge.py` executando com sucesso para ambas as fases.

---

## O que NÃO Estamos Fazendo
> ⛔ Escopo explícito do que está FORA deste plano

- [ ] **Redesign Visual de Raízes**: Não vamos alterar o CSS ou layout agora; apenas criar a *capacidade* de alterá-lo (infraestrutura). O visual será idêntico a Sementes inicialmente.
- [ ] **Refatoração do GutenbergEngine**: O motor de renderização principal (`engine.py`) permanece intocado.

---

## Experts Consultados

| Expert | Posição | Veto? | Justificativa |
|--------|---------|-------|---------------|
| `engenharia` | "Clean Code (DRY) exige extração. Bounded Contexts exige templates separados." | ❌ Não | Alinhado com princípios 1 e 3. |
| `qa` | "Separação facilita testes de regressão visual." | ❌ Não | Reduz risco de quebrar Sementes ao mexer em Raízes. |

---

## Fase 1: Refatoração Core (Extração)

### Objetivo
Centralizar a lógica de navegação para eliminar duplicação de código.

### Arquivos Afetados

| Arquivo | Ação | Descrição |
|---------|------|-----------|
| `build/core/navigation.py` | CREATE | Novo módulo com `NavigationService` agnóstico. |
| `build/fases/sementes.py` | MODIFY | Remover classe interna, importar de core. |
| `build/fases/raizes.py` | MODIFY | Remover classe interna, importar de core. |

### Mudanças Específicas

#### `build/core/navigation.py`
```python
# [New File]
class NavigationService:
    @staticmethod
    def _generate_filename(lid, titulo):
        # ... lógica extraída ...
    
    @staticmethod
    def calculate_links(lessons_data):
        # ... lógica extraída ...
```

#### `build/fases/sementes.py` (e `raizes.py`)
```python
# ANTES
class NavigationService: ...

# DEPOIS
from core.navigation import NavigationService
```

### Verificação Automatizada
- [ ] `python build/forge.py --dry-run` — Sem erros de import.

### ⏸️ Checkpoint
> **PAUSAR AQUI para verificação humana antes da Fase 2**

---

## Fase 2: Infraestrutura de Templates (Separação)

### Objetivo
Criar o "reino" visual independente para Raízes.

### Arquivos Afetados

| Arquivo | Ação | Descrição |
|---------|------|-----------|
| `site/raizes/templates/` | CREATE | Diretório de templates. |
| `site/raizes/templates/*.j2` | CREATE | Cópias de `_config.j2`, `base.j2`, `licao.j2`, `macros.j2`. |
| `build/fases/raizes.py` | MODIFY | Atualizar `RaizesConfig.TEMPLATES_DIR`. |

### Mudanças Específicas

#### `build/fases/raizes.py`
```python
class RaizesConfig:
    # ...
    TEMPLATES_DIR = PROJECT_ROOT / "site/raizes/templates" # Apontando para próprio reino
```

### Verificação Manual
- [ ] Verificar se HTML gerado em `site/raizes/` usa o template correto (pode-se adicionar um comentário HTML oculto no template novo para provar).

---

## Estratégia de Testes

### Testes Automáticos
| Teste | Comando | Critério |
|-------|---------|----------|
| Dry Run Sementes | `python build/forge.py --fase sementes --dry-run` | Execução limpa, log "Navegação injetada" |
| Dry Run Raízes | `python build/forge.py --fase raizes --dry-run` | Execução limpa, log "Navegação injetada" |

---

## Plano de Rollback
> 🔙 Como reverter se algo der errado

1. [ ] Reverter edições em `sementes.py` e `raizes.py` (voltar classe interna).
2. [ ] Deletar `build/core/navigation.py`.
3. [ ] Reverter `TEMPLATES_DIR` em `raizes.py` para apontar para `sementes`.
4. [ ] Deletar pasta `site/raizes/templates`.

---

## Riscos Identificados

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Quebra de Imports | Baixa | Alto | Teste `dry-run` imediato. |
| Divergência de Templates | Média | Baixo | Aceitável (feature, not bug). Manter `base.j2` sincronizado manualmente se houver mudanças globais. |
