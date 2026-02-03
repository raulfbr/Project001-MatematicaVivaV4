# 🦁 Padrão Visual e Estrutural: Ciclo Sementes
> **Fonte da Verdade:** Lição 000 (O Portal do Reino)
> **Última Atualização:** Fev/2026 (Impeccable Release)

Este documento é a **Bíblia de Auditoria**. Qualquer desvio deste padrão nas lições 000-025 deve ser corrigido imediatamente.

---

## 1. Identidade do Portador da Tocha (Avatar)
O Portador não é um rodapé; ele é um Personagem com dignidade visual.

*   **Ícone Sagrado:** `ph-fire` (Chama da Verdade/Zeal).
*   **Cor Litúrgica:** `duotone-carmim` (`#960018`).
*   ** Estrutura HTML (Lei Universal):**
    *   Proibido usar `span` solto ou estilos inline.
    *   Obrigatório usar `.script-avatar-icon` flutuando à esquerda.

```html
<!-- ✅ CORRETO: Padrão Avatar-Icon -->
<div class="script-persona-block portador-block">
    <div class="script-avatar-icon">
        <i class="ph-duotone ph-fire duotone-carmim"></i>
    </div>
    <div class="script-content">
        <div class="script-header">
            <span class="script-name">Portador da Tocha</span>
        </div>
        <div class="script-text">
            <p>"Sua fala aqui..."</p>
        </div>
    </div>
</div>
```

---

---

## 2. Header de Navegação (Menu Superior)
Toda lição deve ter o "norte" claro para o usuário.

*   **Posição:** Topo absoluto do `.lesson-container`.
*   **Ícone Sementes:** Use **`ph-plant`** (`duotone-forest`). *Proibido* usar imagens PNG quebradas.

```html
<div class="lesson-header-nav">
    <!-- Link Voltar -->
    <a href="../index.html" class="nav-back-link">
        <i class="ph-duotone ph-arrow-left"></i> Voltar
    </a>
    <!-- Identificador de Ciclo -->
    <div style="display: flex; align-items: center; gap: 0.5rem;">
        <i class="ph-duotone ph-plant duotone-forest" style="font-size: 1.5rem;"></i>
        <span style="font-family: var(--font-heading); font-weight: 700; color: var(--primary); font-size: 0.9rem;">Sementes</span>
    </div>
</div>
```

---

## 3. Centralização dos Cards (CSS)
Os Guardiões não podem "cair" para a esquerda. A simetria é fundamental.

*   **Audit CSS:** Verifique se esta regra existe em `style.css`:

```css
.card-container {
    display: flex;
    flex-direction: column;
    align-items: center; /* ALINHAMENTO CENTRAL OBRIGATÓRIO */
    text-align: center;
    width: 100%;
    margin: 1.5rem 0.5rem;
}
```

---

## 4. O Ritual de Entrada (Estrutura Sagrada)
Não misture o "Técnico" com o "Mágico".

1.  🟡 **Bastidores (Instruction Box):** Instruções de preparo (Luz, Som, Postura). O pai lê para si mesmo.
2.  🔥 **Palco (Portador Block):** A "Entrada em Cena". As 3 frases rituais.
3.  🌿 **Narrativa (Texto Corrido):** A condução da imaginação ("Feche os olhos..."). Sem quebras bruscas.

---

---

## 5. Roteiro & Direção de Palco 🎭
Regras para formatar falas e instruções de atuação (Acting Cues). A diferença entre "O que falar" e "Como agir".

*   **A "Voz do Diretor" (Acting Cues):**
    *   Use **colchetes `[ ]`** para indicar *como* o pai deve agir ou falar.
    *   **Onde:** *Dentro* do bloco do Portador, misturado ao texto ou em linha separada.
    *   **Estilo:** O CSS renderiza automaticamente em dourado/itálico.
    *   **Exemplo:**
        > "Hoje vamos visitar um lugar muito especial."
        >
        > `[Olhe nos olhos da criança]`
        >
        > "Você está pronto para conhecê-los?"

*   **A "Voz do Técnico" (Instruction Box):**
    *   Use a **Caixa Amarela de Bastidores** para ações físicas pesadas ou preparação de ambiente.
    *   *Não confunda:* Se é sobre "Luz/Som/Material", use Yellow Box. Se é sobre "Entonação/Olhar", use `[ ]`.

*   **Consolidação de Blocos:**
    *   Não fragmente a fala do Portador em vários blocos `.script-persona-block` seguidos.
    *   Use **um único bloco** com vários parágrafos `<p>`, a menos que haja uma mudança de cena técnica no meio.

---

## 6. Coreografia dos Guardiões (Cards) 🃏
*Objetivo:* Evitar poluição visual. O card físico só aparece quando é **essencial**.

*   **Regra de Ouro:** Apresente o Guardião (Card) **UMA ÚNICA VEZ** por lição, no momento de sua introdução formal.
*   **Nos Diálogos:** Use apenas o **Avatar** (`.script-avatar`) no bloco de fala. *NÃO* coloque o card grande novamente.
*   **Fluxo Padrão:**
    1.  **Cena:** Contexto/Local.
    2.  **Visualizar:** Card do Local (Onde estamos).
    3.  **Apresentar:** Card do Guardião (Quem nos recebe).
    4.  **Agir:** Avatar inicia o diálogo.

---

## 7. Ícones Técnicos e Paleta de Cores 🎨

### Cores Litúrgicas (`duotone-*`)
Use estas classes para manter a consistência semântica:
*   🔥 **Carmim:** `.duotone-carmim` (`#960018`) → Portador, Paixão, Zeal.
*   🥇 **Gold:** `.duotone-gold` (`#F59E0B`) → Melquior, Luz, Glória, Instruções Importantes.
*   🌲 **Forest:** `.duotone-forest` (`#166534`) → Sementes, Vida, Natureza.
*   🦉 **Terra:** `.duotone-terra` (`#92400E`) → Noé, Sabedoria, Base, Bastidores.

### Ícones de Instrução
*   **Tamanho:** Ícones dentro de `.instruction-box` devem ter tamanho natural (~24px).
*   **Fix CSS:** A classe `.instruction-box i` possui `width: auto` para evitar distorção (bug do 80px).

---

## 8. Arquivos de Referência (Source of Truth)
A IA deve consultar estes arquivos nesta ordem de prioridade:

1.  📜 **Regras & Estrutura:** `Revisao/padrao_visual_sementes.md` (Este arquivo).
2.  💎 **Bíblia de Assets & Ícones:** `site/sementes/lab_icones.html` (Consulte a seção "AI Protocol" no final do arquivo).
3.  🧱 **Enforcer Visual (CSS):** `site/sementes/style.css` (Contém as regras de `width: auto` e cores `duotone-*`).
---

## 9. Conformidade com Orchestrator v1.5 (Compliance) 🛡️
Este padrão de design respeita a "Distinção de Papéis" definida em `.bmad/orchestrator.yaml`:

1.  **Papel Técnico (Bastidores):** Representado pela **Instruction Box Amarela**.
    *   *Regra Orchestrator:* "Instruções puramente técnicas ou de preparação."
2.  **Papel Narrativo (Reino Contado):** Representado pelo **Portador Block (Carmim)** e **Texto Narrativo**.
    *   *Regra Orchestrator:* "Texto fluido e Portador."
3.  **Quarta Parede:** O uso de colchetes `[ ]` dentro do roteiro protege a imersão da criança, separando a "voz do personagem" da "voz do diretor".
