# ⏸️ STATUS: Landing Page (Pause)

**Data:** 2026-01-19 21:40
**Estado Atual:** `site/landingpage.html` v2.0 (Design Moderno + Paleta Potter em progresso)

---

## 🔍 Análise Profunda (Auditoria Visual)

Revisão detalhada contra `north_star.yaml` e princípios de design.

### ✅ O Que Está Alinhado
1.  **Tipografia:** `Playfair Display` (Títulos) e `Inter` (Corpo) respeitam a meta-regra de "Nobreza e Clareza".
2.  **Estrutura:** As 8 seções seguem o fluxo de persuasão planejado.
3.  **Variáveis Base:** Paleta Potter (`#3D2E1E`, `#2D5A41`, `#D4A574`, `#FAF6F0`) corretamente definida.

### ⚠️ Dissonâncias Identificadas (CORREÇÃO IMEDIATA PRÓXIMA SESSÃO)

**1. Legibilidade Crítica (Pricing)**
*   **Problema:** O preço grande (`.preco-grande`) usa `background: linear-gradient(135deg, #fff, var(--gold))`.
*   **Impacto:** Texto **BRANCO** sobre fundo **CREME** (`#FAF6F0`). Invisível/Ileǵível.
*   **Correção:** Mudar gradiente para `var(--green)` → `var(--gold)`.

**2. Estética "Glass" (Vidro)**
*   **Problema:** Cards usam `rgba(61, 46, 30, 0.06)` (Escuro).
*   **Impacto:** Em fundo creme, vidro escuro parece "sujo" ou queimado.
*   **Correção:** Mudar para **Vidro Pergaminho** (`rgba(255, 255, 255, 0.5)`) para manter o ar leve e premium.

**3. Resquícios Neon**
*   **Problema:** Badge de economia usa `#3dc5a8` (Verde Neon Cyberpunk).
*   **Impacto:** Quebra a imersão "floresta/magia".
*   **Correção:** Mudar para um verde sálvia ou manter o `var(--green)` sólido.

---

## 🛠️ Micro-Checklist de Retomada

Ao iniciar a próxima sessão, execute estas mudanças CSS exatas:

- [ ] **CSS Variáveis:** Alterar `--glass` para `rgba(255, 255, 255, 0.4)` e `--glass-border` para `rgba(255, 255, 255, 0.6)`.
- [ ] **CSS Pricing:** Alterar gradiente de `.preco-grande` para `linear-gradient(135deg, var(--primary), var(--green))`.
- [ ] **CSS Badge:** Alterar `.preco-economia` para `background: var(--green)` (sem neon).
- [ ] **CSS Solução:** Garantir que ícones tenham contraste suficiente.

---

## 🦁 Contexto Emocional do Usuário
O usuário pediu para "não perder a identidade visual" e fazer "por partes". A ansiedade é com a descaracterização (virar um site genérico de SaaS). **A estética deve gritar "Matemática Viva" (Acolhimento + Magia), não "Tech Startup".**
