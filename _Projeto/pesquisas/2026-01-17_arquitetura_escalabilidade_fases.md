# 🔬 PESQUISA: Escalabilidade da Arquitetura (Raízes, Lógica, Legado)

**Data**: 2026-01-17 04:59
**Pesquisador**: Antigravity
**Commit**: (Latest local state)
**Branch**: main

---

## Questão de Pesquisa
> "Isso [a separação de templates e driver] seria replicado para raizes 2 3 4 e 5, logica 6 7 8 9 e legado 10 11 e 12?"

---

## Resumo Executivo
Replicar **Drivers e Templates** para cada *Ano* (ex: `Raizes2Driver`, `Raizes3Driver`) seria excessivo e violaria princípios de simplicidade. A arquitetura atual de **Drivers por Fase** (`RaizesDriver` cobrindo anos 1-5, `LogicaDriver` cobrindo 6-9) é mais robusta e escala melhor, desde que os templates suportem variação interna se necessário.

---

## Descobertas Detalhadas

### 1. Estrutura do Currículo (Mapeamento K-12)
Confronto entre Arquivos e Diretriz do Usuário:
- **Sementes**: K (000)
- **Raízes**: Anos 1, 2, 3, 4, 5.
- **Lógica**: Anos 6, 7, 8, 9*. (*Nota: Arquivo 009 está nomeado LEGADO-1, mas usuário definiu como Lógica. Seguiremos o Usuário).
- **Legado**: Anos 10, 11, 12.

**Total**: 13 Anos/Séries.

### 2. O Padrão de Drivers (Arquitetura "Projeto Completo")
Para atender à necessidade de "Mudança total a cada ano" sem perder a sanidade, a arquitetura será:

#### Camada 1: Bases (Principais Fases)
Classes abstratas que definem o comportamento geral daquela fase (Navigation, Logging, diretórios base).
1. `SementesDriver` (Standalone)
2. `RaizesBaseDriver` (Abstrata)
3. `LogicaBaseDriver` (Abstrata)
4. `LegadoBaseDriver` (Abstrata)

#### Camada 2: Concretas (Ano a Ano)
Classes que definem apenas os caminhos de Input/Output e Templates específicos.

| Driver (Classe) | Herda de | Input (Curriculo) | Output (Site) | Templates |
|---|---|---|---|---|
| **SementesDriver** | GutenbergEngine | `01_SEMENTESV6` | `site/sementes` | `site/sementes/templates` |
| **Raizes1Driver** | RaizesBase | `01_RAIZES_I` | `site/raizes/ano1` | `site/raizes/templates/ano1` |
| **Raizes2Driver** | RaizesBase | `02_RAIZES_II` | `site/raizes/ano2` | `site/raizes/templates/ano2` |
| **Raizes3Driver** | RaizesBase | `03_RAIZES_III` | `site/raizes/ano3` | `site/raizes/templates/ano3` |
| **Raizes4Driver** | RaizesBase | `04_RAIZES_IV` | `site/raizes/ano4` | `site/raizes/templates/ano4` |
| **Raizes5Driver** | RaizesBase | `05_RAIZES_V` | `site/raizes/ano5` | `site/raizes/templates/ano5` |
| **Logica6Driver** | LogicaBase | `06_LOGICA_I` | `site/logica/ano6` | `site/logica/templates/ano6` |
| **Logica7Driver** | LogicaBase | `07_LOGICA_II` | `site/logica/ano7` | `site/logica/templates/ano7` |
| **Logica8Driver** | LogicaBase | `08_LOGICA_III` | `site/logica/ano8` | `site/logica/templates/ano8` |
| **Logica9Driver** | LogicaBase | `09_LOGICA_IV` | `site/logica/ano9` | `site/logica/templates/ano9` |
| **Legado10Driver** | LegadoBase | `10_LEGADO_I` | `site/legado/ano10` | `site/legado/templates/ano10` |
| **Legado11Driver** | LegadoBase | `11_LEGADO_II` | `site/legado/ano11` | `site/legado/templates/ano11` |
| **Legado12Driver** | LegadoBase | `12_LEGADO_III` | `site/legado/ano12` | `site/legado/templates/ano12` |

### 3. O Padrão de Templates
Cada pasta `templates/anoX` conterá sua própria versão de `licao.j2`, `base.j2` e `_config.j2`.
Isso garante isolamento total. Se o 7º ano decidir usar React e o 2º ano usar Planilhas de Papel, o sistema suporta.


### 3. O Padrão de Templates (A Divergência)
A análise de `001_1ANO_RAIZES-1` vs `005_5ANO_RAIZES-5` revelou divergências profundas:
- **Raízes 1 (Fundação)**: Concreto, sensorial, contagem visual. Exige templates "lúdicos".
- **Raízes 5 (Domínio)**: Abstrato, gráficos, equações. Exige templates "laboratoriais" (Chart.js, layouts densos).

**Correção de Rumo**:
Tentar usar um único `site/raizes/templates/licao.j2` para o 1º e 5º ano criaria um "Monólito Cheio de Ifs".
A estrutura visual PRECISA ser segregada, mesmo que o Driver seja o mesmo.

---

## Mapa de Arquivos Relevantes (Refinado)

| Componente | Escopo Proposto | Justificativa |
|------------|-----------------|---------------|
| `RaizesDriver` | Fase (Anos 1-5) | O processo de build (YAML->HTML) é o mesmo. |
| `site/raizes/templates/ano1` | Ano 1 | Identidade visual "Fundação". |
| `site/raizes/templates/ano5` | Ano 5 | Identidade visual "Laboratório". |
| `site/logica/templates` | Fase (Anos 6-9) | Identidade dialética. |

O driver deve ser inteligente o suficiente para escolher `template_dir` baseado no metadado `ano` do YAML.

---

## Experts BMAD Relevantes

| Expert | Conselho | Por quê? |
|--------|----------|----------|
| `engenharia` | "Separation of Concerns" | Não misture visual de criança (1º) com pré-adolescente (5º). |
| `charlotte_mason` | "Atmosphere is Discipline" | A atmosfera visual deve amadurecer com a criança. |

---

O driver `Base` cuida do scan de arquivos e parsing do YAML. O driver `Concreto` apenas configura os caminhos.

---

## Experts BMAD Relevantes

| Expert | Conselho | Por quê? |
|--------|----------|----------|
| `engenharia` | "Explicit is better than implicit" | Mapear cada ano explicitamente evita "mágicas" de adivinhação de pasta. |
| `charlotte_mason` | "Cada idade tem sua glória" | Respeita a identidade única de cada série. |

---

## Questões Abertas
1. [ ] Como o `RaizesDriver` sabe qual template usar? (Solução: Metadado `contexto: { ano: 5 }` no YAML ou inferência pelo caminho do arquivo).
2. [ ] Devemos criar `site/raizes/ano1`, `site/raizes/ano5` ou manter tudo em `site/raizes`? (Decisão de Engenharia: Manter em `site/raizes` mas com prefixos ou pastas seria melhor para deploy, mas URLs mudariam).

---

## Conclusão da Pesquisa (Projeto Completo)
A arquitetura final K-12 está definida na tabela acima.
- **Total de Drivers**: 13 (1 Standalone + 12 Herdeiros).
- **Total de Bases**: 3 (`RaizesBase`, `LogicaBase`, `LegadoBase`).
- **Isolamento**: 100% (Cada ano tem seus templates).
- **Reuso**: Alto (Lógica Python centralizada nas Bases).


---

## 🔎 Verificação Tripla (Protocolo de Impecabilidade)
*Referência: `.bmad/orchestrator.yaml` e `logs/_Guterberg/GUTENBERG_MODULAR_2026-01-16.md`*

### 1. Verificação Técnica (Engenharia)
*   **Princípio**: "Explicit is better than implicit" (Zen of Python) e "Bounded Contexts" (DDD).
*   **Análise**: A criação de 13 Drivers Herdeiros (`Raizes1Driver`, etc.) aumenta a complexidade inicial, mas reduz drasticamente a complexidade acidental (cyclomatic complexity) dentro dos templates.
*   **Veredito**: ✅ Aprovado. O custo de criar 13 arquivos Python é menor que o custo de manter 130 `if/else` dentro de templates Jinja compartilhados.
*   **Refinamento**: `RaizesBase` deve herdar de `GutenbergEngine` e implementar métodos comuns (Navigation), enquanto `Raizes1Driver` apenas define constantes `INPUT`, `OUTPUT` e `TEMPLATES`.

### 2. Verificação Pedagógica (Charlotte Mason)
*   **Princípio**: "A criança é uma pessoa" e respeita fases de desenvolvimento.
*   **Análise**: Uma criança de 6 anos (Raízes 1) precisa de "Atmosphere" (templates) focados no concreto/lúdico. Uma de 10 anos (Raízes 5) precisa de "Discipline" (organizadores gráficos, tabelas).
*   **Veredito**: ✅ Aprovado. A separação física dos templates protege a "Atmosfera" de cada idade contra contaminação visual de outras fases.

### 3. Verificação do Maestro (Usuário)
*   **Diretriz**: "Cada ano muda... as fases são totalmente diferentes".
*   **Análise**: O mapa proposto cobre exaustivamente K-12 (000 a 012).
*   **Veredito**: ✅ Aprovado. A arquitetura "Projeto Completo" entrega a granularidade exigida.

---

## Próximo Passo Recomendado
Iniciar o **Plano de Implementação K-12**, começando pela prova de conceito:
1. Refatorar `RaizesDriver` para `RaizesBaseDriver` (Abstrata).
2. Implementar `Raizes1Driver` (Concreta).
3. Validar se L001 continua operando perfeitamente.
sses**:

1.  **Classe Base Abstrata**: `RaizesBaseDriver` (Contém a lógica core: Navigation, Jinja Loader, Assets).
2.  **Classes Concretas por Ano**:
    *   `Raizes1Driver(RaizesBaseDriver)` -> `site/raizes/ano1`, `Input: raizes/ano1`
    *   `Raizes5Driver(RaizesBaseDriver)` -> `site/raizes/ano5`

**Benefícios**:
- **Granularidade Total**: O usuário pode mudar TUDO no ano 5 sem afetar o ano 1.
- **Organização**: Cada ano tem sua "pasta reino" (`site/raizes/anoX`).
- **Documentação**: Como pedido, manteremos tudo bem documentado.

Esta estrutura será replicada para Lógica (Logica1..4) e Legado (Legado1..3).

