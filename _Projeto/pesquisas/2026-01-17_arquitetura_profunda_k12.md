# 🔬 PESQUISA PROFUNDA: Arquitetura K-12 (Tabula Rasa)

**Data:** 17/01/2026
**Contexto:** O usuário solicitou um "Reinício Completo" da pesquisa arquitetural após considerar o plano anterior (Atlas Pattern) confuso.
**Objetivo:** Encontrar a arquitetura mais simples, explícita e robusta para sustentar 13 anos de currículo (K-12).

---

## 1. O Problema Fundamental: "Cada Ano é Diferente"

A análise do currículo de Legado 1 (`009_MAPA...md`) confirma que as diferenças não são cosméticas:
*   **Sementes**: Veta pictórico, requer assets locais.
*   **Raízes**: Requer oficinas phygital.
*   **Legado**: Requer "Protocolo Dual Printing", Alinhamento Khan, e Hooks Doxológicos complexos.

Uma arquitetura única ("One Driver to Rule Them All") exigiria tantos `if/else` que se tornaria inmanutenível.

---

## 2. As 3 Opções Arquiteturais (Stress Test)

### Opção A: Hierarquia Explícita (13 Classes Reais)
Cada ano tem seu próprio arquivo Python.
*   `build/fases/raizes/ano1.py`
*   `build/fases/raizes/ano2.py`
*   `build/fases/legado/ano10.py`

| Critério | Avaliação |
| :--- | :--- |
| **Cognitive Load** | **Baixo**. "O que você vê é o que é". Se quero mudar o Ano 1, abro `ano1.py`. |
| **Debug** | **Excelente**. O stack trace aponta exatamente para o arquivo do ano. |
| **Boilerplate** | **Alto**. Repetição de código (class Raizes2(Base): ...). |
| **Flexibilidade** | **Infinita**. Posso reescrever o Ano 9 do zero sem tocar no Ano 8. |

### Opção B: O "Atlas" (Registry Pattern - Tentativa Anterior)
Um arquivo central (`atlas.py`) define configurações, drivers genéricos leem isso.
*   `build/core/atlas.py`

| Critério | Avaliação |
| :--- | :--- |
| **Cognitive Load** | **Médio/Alto**. Exige entender como o Atlas injeta configs no Driver. |
| **Debug** | **Médio**. Erros podem estar no Atlas ou no Driver genérico. |
| **Boilerplate** | **Mínimo**. Zero arquivos novos. |
| **Flexibilidade** | **Alta**, mas exige "Adapters" para casos complexos. |

### Opção C: O "Manifesto" (Configuração YAML Pura)
Um arquivo `k12_manifest.yaml` define as regras. O Python é "burro" e apenas obedece.

| Critério | Avaliação |
| :--- | :--- |
| **Cognitive Load** | **Baixo**. Ler YAML é mais fácil que ler Python. |
| **Debug** | **Difícil**. Se o YAML estiver errado, o erro no Python pode ser críptico. |
| **Flexibilidade** | **Limitada**. Difícil codar lógica complexa (ex: validação Legado) em YAML. |

---

## 3. Veredito da Engenharia (Consulta aos Princípios)

Consultando `engenharia.yaml`:
1.  **"Explicit is better than implicit"**: A Opção A (Classes Explícitas) ganha de lavada. Não há mágica.
2.  **"Bounded Contexts"**: A Opção A cria fronteiras físicas (arquivos).
3.  **"Simplicity"**: A Opção A é "burra", mas simples. A Opção B é "esperta", mas complexa.

### A Escolha: Opção A (Refinada - "Hierarquia Pragmática")

Não precisamos de 13 arquivos *agora*. Precisamos da **liberdade** de tê-los.
Podemos começar com:
*   `fases/raizes.py` (Define `RaizesBase` e `Raizes1`)
*   Se Raízes 2 for igual, ele usa `RaizesBase` configurada.
*   Se o ano divergir, cria-se a classe.

---

## 4. O Mapa Definitivo (K-12 Directory Structure)

Esta é a estrutura física proposta para atender o requisito "Cada ano muda":

```text
build/
  fases/
     sementes.py (Driver Sementes)
     raizes.py   (Contém RaizesBase + Raizes1..5)
     logica.py   (Contém LogicaBase + Logica6..9)
     legado.py   (Contém LegadoBase + Legado10..12)

site/
  raizes/
     ano1/
     templates/ano1/ (Visual exclusivo do Ano 1)
  legado/
     ano10/
     templates/ano10/ (Visual "High School" exclusivo)
```

## 5. Conclusão da Pesquisa Profunda

A tentativa anterior (Atlas) falhou por "over-engineering".
A solução correta, alinhada com a mentalidade do usuário e com a engenharia robusta, é a **Programação Explícita**.

**Recomendação:**
Implementar classes Python reais. É mais código para escrever, mas **zero custo cognitivo** para entender depois.
Para o usuário (Maestro), isso significa que ele pode pedir "Mude a regra do 9º ano" e saberemos exatamente onde ir (`legado.py` -> `Legado9Driver`), sem medo de quebrar o 1º ano.
