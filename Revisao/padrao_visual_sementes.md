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

## 4. O Ritual de Entrada (Estrutura Unificada)
Abertura com **Voz Única**. O Portador não "entra e sai" de cena.

1.  🟡 **Preparo (Bastidores):** Use a **Instruction Box** amarela.
    *   **Contém:** Ações físicas prévias (ex: "Prepare a Luz Amarela", "Respire fundo").
    *   **Quem lê:** O pai, em silêncio, *antes* de iniciar a cena.

2.  🔥 **O Palco (Monobloco do Portador):** Use UM único `.portador-block`.
    *   **Contém TUDO:** As falas iniciais ("Luz de fora...") E a condução da imaginação ("Feche os olhos...").
    *   **Voz:** O pai assume o manto e narra tudo como Personagem.
    *   **Imersão:** Se precisar descrever o cenário, o Portador descreve. Não use bloco de texto solto fora do avatar.

> **Regra de Ouro:** "Uma vez acesa a luz, o Portador não sai de cena até o fim do Ritual."

---

## 4.1 Regra de Separação: Ritual = Local / Jornada = Guardião

O **Ritual de Entrada** transporta a criança para o LOCAL da lição (ex: Jardim Central).
Nenhum Guardião deve ser *mencionado* ou *mostrado* até a seção "A Jornada".

*   **Ritual de Entrada:**
    *   Foco: Imersão sensorial pura no LUGAR.
    *   Fluxo: "Feche os olhos..." -> [CARD DO LOCAL] -> Descrição sensorial.
    *   Encerramento: "Alguém especial espera por você. Pronto?"

*   **A Jornada:**
    *   Foco: Encontro com o GUARDIÃO do dia.
    *   Fluxo: [CARD DO GUARDIÃO] -> "— Bem-vindo, Viajante."
    *   Impacto: O reveal visual do Guardião acontece AQUI.

> **Por quê?** Mencionar o Leão antes de mostrar seu card quebra a surpresa. O "reveal" precisa ser visual e imediato.

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

---

## 10. Estilo de Texto (Writing Style) ✍️
Regras para garantir clareza, fluidez e imersão no texto das lições.

### 10.1 Evitar "Quote Clutter" (Excesso de Aspas)
*   **Problema:** Cada frase entre aspas (`"..."`) cria poluição visual.
*   **Regra:** Use aspas APENAS em diálogos diretos do Guardião (personagem).
*   **Narrativa do Portador:** Sem aspas (é instrução/condução, não fala literal de personagem).

**Exemplo Errado:**
```html
<p>"Luz de fora acalma."</p>
<p>"Sol de dentro acende."</p>
```

**Exemplo Correto:**
```html
<p>Luz de fora acalma.</p>
<p>Sol de dentro acende.</p>
```

### 10.2 Capitalização de Nomes Próprios
*   **Guardiões:** Sempre iniciados com maiúscula em TODOS os contextos.
    *   ❌ `melquior` → ✅ `Melquior`
    *   ❌ `noé` → ✅ `Noé`
    *   ❌ `celeste` → ✅ `Celeste`
*   **Headers:** `<span class="script-name">Melquior</span>` (Capitalizado).
*   **Auditoria:** Buscar por `script-name` e verificar capitalização.

### 10.3 Evitar Repetição de Frases-Chave
*   **Regra:** Cada frase marcante deve aparecer **UMA ÚNICA VEZ** na lição.
*   **Exemplos de repetição comum:**
    *   "lugar muito especial" (aparece 2x)
    *   "alguém especial espera" (aparece 2x)
*   **Fix:** Reescrever ocorrências duplicadas com variações criativas.

### 10.4 Tom do Primeiro Ritual (Lição 000)
A Lição 000 é a **PORTA DE ENTRADA**. O tom deve ser:
*   **Acolhedor:** Como um convite gentil, não uma sequência de comandos.
*   **Fluido:** Menos frases curtas e staccato, mais narrativa contínua.
*   **Misterioso:** Criar suspense sobre os Guardiões (sem revelar antes da hora).
*   **Sem Infantilização:** Proibido "Shhh...", "Psiu..." — usar tom de mistério/nobreza.

> "O medo acaba em você. O encantamento começa neles." — North Star

---

## 11. Labels Obrigatórios (Visual Cues) 🏷️
Regras para uso consistente de labels nas lições.

### 11.1 Label "Mostrar Card"
*   **Uso:** SEMPRE antes de exibir um card visual (Guardião ou Local).
*   **Classe:** `<p class="local-label">Mostrar Card</p>`
*   **Posição:** Imediatamente antes da tag `<img>`.

**Exemplo:**
```html
<div class="card-container">
    <p class="local-label">Mostrar Card</p>
    <img src="../assets/cards/locais/local-jardim-central.png" ...>
</div>
```

### 11.2 Centralização de Títulos de Local
*   Títulos como "✨ O Jardim Central ✨" devem estar:
    *   Centralizados (`text-align: center`)
    *   Com tamanho destacado (`font-size: 1.1rem`)
    *   Cor primária (`color: var(--primary)`)
    *   Peso bold (`font-weight: 700`)

---

## 12. Checklist de Auditoria para IA 🤖
Use este checklist ao revisar QUALQUER lição do ciclo Sementes.

| # | Regra | Verificação |
|---|-------|-------------|
| 1 | **Portador Icon** | Usa `ph-fire duotone-carmim`? |
| 2 | **Navigation Icon** | Usa `ph-plant duotone-forest`? |
| 3 | **Quote Clutter** | Narrativa sem excesso de aspas? |
| 4 | **Capitalização** | Nomes dos Guardiões capitalizados? |
| 5 | **Repetição** | Nenhuma frase-chave repetida? |
| 6 | **Local Label** | "Mostrar Card" antes de todos os cards? |
| 7 | **Ritual Structure** | Ritual = Local only, Guardião na Jornada? |
| 8 | **Instruction Box** | Auto-suficiente para pais novatos? |
| 9 | **Acting Cues** | Instruções de ação em `[ ]`? |
| 10 | **Card Centerização** | `.card-container` centralizado? |
| 11 | **Sinal de Início** | "Dica do Coração" menciona Sinal (não "luzes baixas")? |
| 12 | **Segredo do Maravilhamento** | Usa "maravilhamento" (não "encantamento pressão")? |
| 13 | **Sementes para o Dia** | Seção com 5 atividades opcionais presente? |
| 14 | **CPA Foco Concreto** | Bloco CPA enfatiza CONCRETO para Sementes? |
| 15 | **Sementes Continuam** | Explicação do "porquê" das atividades presente? |

---

## 13. Sinal de Início (Ritual Entry) 🔔
O início de cada lição deve ser marcado por um **Sinal de Início** — escolhido pela família.

### 13.1 Conceito
*   **O que é:** Um sinal físico que marca a entrada no "tempo sagrado" da lição.
*   **Não é:** Apagar luzes ou criar escuridão (❌ "luzes baixas").

### 13.2 Exemplos de Sinal
*   Luminária amarela
*   Baú especial com os cards
*   Tapete específico
*   Abrir o "livro" (tablet/celular)
*   Sino ou campainha

### 13.3 Regra de Ouro
> "O ritual começa quando vocês decidem que começa. **Você é a voz de Melquior.**"

**Exemplo de Dica do Coração:**
```html
<strong>Dica do Coração:</strong> Hoje não há matemática. Só <strong>maravilhamento</strong>.
Seu único trabalho é criar o <strong>Sinal de Início</strong> — acenda a luminária amarela,
abra o baú dos cards, estenda o tapete, ou simplesmente abra este "livro" junto com seu filho.
```

---

## 14. Segredo do Maravilhamento 🌟
O termo-chave é **maravilhamento**, não "encantamento" ou "protocolo".

### 14.1 Princípio
*   **Não force compreensão.** O maravilhamento vem primeiro.
*   **Responda com mistério:** "Você vai descobrir..."
*   **Tom gentil:** Não usar caixa alta ou imperativo (❌ "NÃO EXPLIQUE NADA").

### 14.2 Padrão HTML
```html
<p><strong><i class="ph-duotone ph-sparkle duotone-magic"></i> Segredo do Maravilhamento:</strong>
    Não precisa explicar nada. Apenas <strong>viva a narrativa</strong>. Se a criança perguntar,
    sorria e diga: "Você vai descobrir...". O <strong>maravilhamento</strong> é mais importante
    que a compreensão — por enquanto.
</p>
```

---

## 15. Sementes para o Dia (Framework Padronizado) 🌱

### 15.1 Princípios
| Princípio | Descrição |
|-----------|-----------|
| **Opcional** | A lição já está completa. Isto é extensão. |
| **Independência** | Criança pode fazer sozinha ou com pais. |
| **Lúdico** | Brincadeira, não dever de casa. |
| **Conexão** | Reforça vínculo com o Reino ao longo do dia. |
| **Dignidade** | Sem infantilização. Trata a criança como Herdeiro. |

### 15.2 Tipos de Atividades (5 categorias)
| Tipo | Descrição | Sozinha? | Com Pais? |
|------|-----------|----------|-----------|
| 🎭 **Dramatização** | Brincar de "ser" alguém do Reino | ✅ | ✅ |
| 🔎 **Exploração** | Encontrar/organizar elementos físicos | ✅ | ✅ |
| ✏️ **Criação** | Desenhar, colorir, construir | ✅ | ⚠️ Ajuda menor |
| 💬 **Narração** | Recontar a história (CM) | ⚠️ Precisa ouvinte | ✅ |
| 🌙 **Reflexão** | Perguntas para hora de dormir | ❌ | ✅ Ritual noturno |

### 15.3 Template por Lição
Cada lição deve ter **5 atividades** seguindo o framework:
1. 🔎 Exploração (baseada no tema)
2. 🎭 Dramatização (personagens do dia)
3. ✏️ Criação (desenho/construção)
4. 💬 Narração (recontar para alguém)
5. 🌙 Reflexão (pergunta noturna)

### 15.4 Padrão HTML
```html
<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-shooting-star duotone-forest" style="font-size:1.5rem; margin-right:0.5rem;"></i>
        ✨ Sementes para o Dia
    </div>

    <div class="instruction-box" style="background-color: #F0FDF4; border-left-color: #166534;">
        <!-- 5 atividades aqui -->
    </div>
</div>
```

---

## 16. CPA — Foco no Concreto (Sementes) 🧱

### 16.1 Regra
No ciclo **Sementes**, quase tudo é **CONCRETO**:
*   Tocar, sentir, manipular, vivenciar.
*   Os cards físicos são essenciais.
*   A voz do Portador é experiência sensorial.

### 16.2 Progressão CPA
| Fase | Concreto | Pictórico | Abstrato |
|------|----------|-----------|----------|
| **Sementes** | ✅ Foco principal | ⚠️ Cards ilustrados | ❌ Ainda não |
| **Raízes** | ✅ Manipuláveis | ✅ Desenhos | ⚠️ Início |
| **Lógica** | ⚠️ Revisão | ✅ Diagramas | ✅ Símbolos |

### 16.3 Padrão HTML (Box CPA)
```html
<div class="bruner-box">
    <strong><i class="ph-duotone ph-brain duotone-terra"></i> Método CPA (Jerome Bruner):</strong><br>
    <ul>
        <li><strong>Concreto:</strong> ✅ O foco de Sementes. Experiência sensorial completa.</li>
        <li><strong>Pictórico:</strong> Será introduzido no momento oportuno.</li>
        <li><strong>Abstrato:</strong> Virá nas próximas fases.</li>
    </ul>
    <span style="color:#6B7280; font-size:0.9rem;">
        No Ciclo Sementes, quase tudo é <strong>concreto</strong>.
    </span>
</div>
```

---

## 17. Sementes Continuam (Para a Família) 🌻
Explicação do "porquê" as atividades de continuação funcionam.

### 17.1 Propósito
*   Reforço natural (sem "estudar")
*   Desejo próprio (criança QUER mais)
*   Conexão familiar (memórias)
*   **Restauração do Pai** (ao brincar junto, o pai também é transformado)

### 17.2 Citações Chave
> "O medo acaba em você. O encantamento começa neles." — North Star

> "A cada lição, o filho aprende e o pai é restaurado." — Matemática Viva

### 17.3 Padrão HTML
```html
<div class="instruction-box" style="background-color: #FEF3C7; border-left-color: #F59E0B;">
    <i class="ph-duotone ph-sun duotone-gold"></i>
    <div>
        <strong>🌱 As Sementes Continuam:</strong><br>
        Acima, você encontrou sugestões de "Sementes para o Dia"...
        <ul>
            <li><strong>Reforço Natural:</strong> ...</li>
            <li><strong>Desejo Próprio:</strong> ...</li>
            <li><strong>Conexão Familiar:</strong> ...</li>
            <li><strong>Restauração do Pai:</strong> ...</li>
        </ul>
    </div>
</div>
```

---

## 18. Estrutura Narrativa — Ordem das Seções 📐
Ordem correta das seções na Jornada (após Ritual de Entrada):

### 18.1 Regra de Ordenação
1. **O Convite de [Guardião]** — Card + acolhimento inicial
2. **Quem é [Guardião]** — Apresentação detalhada (juba, olhos, rugido etc.)
3. **A História da Criação** — Cosmogonia do Reino (se aplicável)
4. **Outros Guardiões** — Apresentação dos demais
5. **O Concreto** — Atividade principal
6. **Sementes para o Dia** — Atividades de continuação
7. **Narramos Juntos** — Reflexão
8. **Ritual de Fechamento** — Despedida

### 18.2 Erro Comum
❌ "A História da Criação" vindo ANTES de "Quem é [Guardião]"
✅ Primeiro conhecemos o Guardião, DEPOIS ele conta a história.

---

*Atualizado em: 03/02/2026 — Fase 11 (Lesson 000 Final)*
