# 🦁 Padrão Visual e Estrutural: Ciclo Sementes
> **Fonte da Verdade:** Lição 000 (O Portal do Reino)
> **Última Atualização:** Mar/2026 (Header Canônico + Ordem Completa)

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

## 2. Header de Navegação (Menu Superior) — Padrão Canônico
Toda lição deve ter o "norte" claro para o usuário no topo da página.

### 2.1 Regra Oficial (Fonte: Lição 003)
O header superior deve ter **3 zonas fixas**:
1. **Esquerda:** link para a lição anterior.
2. **Centro:** ícone `ph-plant` + label `Sementes`.
3. **Direita:** link para a lição seguinte.

Regras:
* **Posição:** topo do `.lesson-body`.
* **Centro visual:** o label `Sementes` deve ficar centralizado no bloco do meio, com `margin-left: 0.5rem`.
* **Navegação lateral:** usar links para lições adjacentes (`MV-S-XXX`), não "Voltar" genérico para `index.html` nas lições 001+.
* **Exceção:** Lição 000 pode manter comportamento de entrada/portal.

```html
<div class="lesson-header-nav">
    <div style="width: 33%;">
        <a href="MV-S-002_AS_PEDRAS_DA_FORTALEZA.html" class="nav-mini-link">
            <span>←</span> <span>As Pedras da Fortaleza</span>
        </a>
    </div>

    <div style="width: 33%; text-align: center;">
        <i class="ph-duotone ph-plant duotone-forest" style="font-size: 1.5rem;"></i>
        <span style="font-family: var(--font-heading); font-weight: 700; color: var(--primary); font-size: 0.9rem; margin-left: 0.5rem;">
            Sementes
        </span>
    </div>

    <div style="width: 33%; text-align: right;">
        <a href="MV-S-004_A_ORDEM_DO_DIA.html" class="nav-mini-link"
           style="justify-content: flex-end;">
            <span>A Ordem do Dia</span> <span>→</span>
        </a>
    </div>
</div>
```

### 2.2 Diagnóstico Rápido (001–003)
* **L003:** PASS (canônico para header superior).
* **L001:** FAIL no topo (usa "Voltar", sem anterior/próxima no header superior).
* **L002:** FAIL no topo (usa "Voltar", sem anterior/próxima no header superior).

### 2.3 Mapa Obrigatório de Links no Topo
* `MV-S-001`: esquerda `MV-S-000`, direita `MV-S-002`
* `MV-S-002`: esquerda `MV-S-001`, direita `MV-S-003`
* `MV-S-003`: esquerda `MV-S-002`, direita `MV-S-004`

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

1.  📜 **Regras & Estrutura:** `Revisao/01_REFERENCIAS_DE_APOIO/padrao_visual_sementes.md` (Este arquivo).
2.  💎 **Bíblia de Assets & Ícones:** `site/sementes/lab_icones.html` (Consulte a seção "AI Protocol" no final do arquivo).
3.  🧱 **Enforcer Visual (CSS):** `site/sementes/style.css` (Contém as regras de `width: auto` e cores `duotone-*`).
---

## 9. Conformidade com Orchestrator v1.5 (Compliance) 🛡️
Este padrão de design respeita a "Distinção de Papéis" definida em `bmad/orchestrator.yaml`:

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

### 10.2 Capitalização de Nomes Próprios
*   **Guardiões:** Sempre iniciados com maiúscula em TODOS os contextos.
    *   ❌ `melquior` → ✅ `Melquior`
    *   ❌ `noé` → ✅ `Noé`
    *   ❌ `celeste` → ✅ `Celeste`
*   **Headers:** `<span class="script-name">Melquior</span>` (Capitalizado).
*   **Auditoria:** Buscar por `script-name` e verificar capitalização.

### 10.3 Evitar Repetição de Frases-Chave
*   **Regra:** Cada frase marcante deve aparecer **UMA ÚNICA VEZ** na lição.
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
| 6 | **Formação Portador** | Usa `ph-graduation-cap` e boxes padronizadas? |
| 7 | **Sementes Box** | Usa `.sementes-box` (verde) e sem ícones duplicados? |
| 8 | **Instruction Box** | Auto-suficiente para pais novatos? |
| 9 | **Acting Cues** | Instruções de ação em `[ ]`? |
| 10 | **Card Centerização** | `.card-container` centralizado? |
| 15 | **Sementes Continuam** | Explicação e boxes corretas? |

---

## 13. Sinal de Início (Ritual Entry) 🔔
O início de cada lição deve ser marcado por um **Sinal de Início** — escolhido pela família.

### 13.1 Conceito
*   **O que é:** Um sinal físico que marca a entrada no "tempo sagrado" da lição.
*   **Não é:** Apagar luzes ou criar escuridão (❌ "luzes baixas").

### 13.2 Regra de Ouro
> "O ritual começa quando vocês decidem que começa. **Você é a voz de Melquior.**"

---

## 14. Segredo do Maravilhamento 🌟
O termo-chave é **maravilhamento**, não "encantamento" ou "protocolo".

### 14.1 Princípio
*   **Não force compreensão.** O maravilhamento vem primeiro.
*   **Responda com mistério:** "Você vai descobrir..."
*   **Tom gentil:** Não usar caixa alta ou imperativo (❌ "NÃO EXPLIQUE NADA").

---

## 15. Sementes para o Dia (Framework Padronizado) 🌱

### 15.1 Template por Lição
Cada lição deve ter **5 atividades** seguindo o framework:
1. 🔎 Exploração (baseada no tema)
2. 🎭 Dramatização (personagens do dia)
3. ✏️ Criação (desenho/construção)
4. 💬 Narração (recontar para alguém)
5. 🌙 Reflexão (pergunta noturna)

### 15.2 Padrão HTML
*   **Header:** Sem ícone emoji duplicado. Apenas `ph-plant` (ou similar temático) + Texto.
*   **Container:** `instruction-box` verde (`#F0FDF4`).

```html
<div class="scene-header">
    <i class="ph-duotone ph-plant duotone-forest" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Sementes para o Dia
</div>

<div class="instruction-box" style="background-color: #F0FDF4; border-left-color: #166534;">
    <!-- 5 atividades aqui -->
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
| **Sementes** | ✅ Foco principal (80-100%) | ⚠️ Cards ilustrados | ❌ Não |

---

## 17. Sementes Continuam (Extensão) 🌻
Explicação do "porquê" as atividades de continuação funcionam.

### 17.1 Nova Classe CSS
*   **Classe:** `.sementes-box`
*   **Cores:** Fundo `#ECFDF5` (verde claro), Borda `#10B981` (esmeralda).
*   **Visual:** Limpo, sem ícones duplicados no header.

### 17.2 Padrão HTML
```html
<div class="sementes-box">
    <strong><i class="ph-duotone ph-plant duotone-forest"></i> As Sementes Continuam:</strong>
    
    <p style="margin-top: 0.5rem;">
        Texto explicativo...
    </p>

    <p style="margin-top: 0.75rem;"><strong>Por que isso funciona?</strong></p>
    <ul style="margin: 0.5rem 0 0 1.5rem; line-height: 1.6;">
        <li><strong>Reforço Natural:</strong> ...</li>
        <li><strong>Desejo Próprio:</strong> ...</li>
    </ul>
</div>
```

---

## 18. Estrutura Narrativa & Ordem (Tópicos Obrigatórios) 📐
Toda lição Sementes (001–025) deve seguir esta ordem mínima:

1. **Header Superior Canônico** (anterior | Sementes central | próxima)
2. **Preparação do Portador**
3. **Ritual de Entrada**
4. **A Jornada (Guardiões)**
5. **Momento de Conexão** (atividade concreta fluida)
6. **Narramos Juntos**
7. **Ritual de Fechamento**
8. **🌱 Sementes para o Dia** (recomendado no padrão atual)
9. **🎓 Formação do Portador** (antigo "Para a Família")
10. **Navegação Inferior** (`.lesson-nav` com `nav-btn prev/next`)

Regra de auditoria:
* Se faltar item estrutural obrigatório, a lição recebe **FAIL estrutural**.

### 18.1 Contrato Canônico de Tópicos e Subtópicos
Use os IDs abaixo para revisão técnica e editorial. Cada lição deve mapear 1:1 com este contrato.

| ID | Tópico | Subtópicos mínimos | Status |
|---|---|---|---|
| T0 | Header Superior Canônico | anterior (esq), selo Sementes (centro), próxima (dir) | Obrigatório |
| T1 | Preparação do Portador | foco da lição, dica do coração, materiais, filho descobre, protocolo, nota de graça | Obrigatório |
| T2 | Ritual de Entrada | bastidores, Portador em monobloco, card do local com label | Obrigatório |
| T3 | A Jornada | H2 da jornada, cenas narrativas, card do guardião, instrução de ação, fala/persona | Obrigatório |
| T4 | Momento de Conexão | objetivo concreto, instrução prática, adaptação de acesso | Obrigatório |
| T5 | Narramos Juntos | instrução de escuta, pergunta principal, perguntas do coração | Obrigatório |
| T6 | Ritual de Fechamento | fala final, fio de ouro, transição de volta | Obrigatório |
| T7 | Sementes para o Dia | introdução, 5 atividades (Exploração/Dramatização/Criação/Narração/Reflexão), frase final | Recomendado |
| T8 | Formação do Portador | porque importa, método CPA, princípio CM, conexão TGTB, espiral, nota de graça | Obrigatório |
| T9 | Navegação Inferior | botão anterior, botão próxima | Obrigatório |

### 18.2 Nomenclatura Fixa (Título de Seção)
Para evitar variação desnecessária entre lições, usar estes títulos exatamente:

1. `Preparação do Portador`
2. `Ritual de Entrada`
3. `A Jornada`
4. `Momento de Conexão`
5. `Narramos Juntos`
6. `Ritual de Fechamento`
7. `Sementes para o Dia`
8. `Formação do Portador`

Regra de migração:
* Legado aceitável temporário: `O Concreto` como alias de `Momento de Conexão`.
* Padrão alvo de todas as lições: `Momento de Conexão`.

### 18.3 Regra de Completude por Lição
Critério objetivo para aprovar estrutura:

* **PASS Estrutural:** todos os itens `T0, T1, T2, T3, T4, T5, T6, T8, T9` presentes.
* **PASS Premium:** PASS Estrutural + `T7` completo com 5 atividades.
* **FAIL Estrutural:** ausência de qualquer tópico obrigatório.

---

## 19. Atividade Concreta: Momento de Conexão 🧱
A "Atividade Concreta" foi renomeada para **Momento de Conexão** na Lição 000, para refletir seu objetivo.

### 19.1 Ícones de Atividades (Sementes do Dia)
Para a seção "Sementes do Dia", usamos ícones que representam o **tipo de interação**:

| Tipo | Emoji Antigo | Ícone Phosphor | Cor |
|------|--------------|----------------|-----|
| **Investigação** (Caça, Busca) | 🔎 | `ph-magnifying-glass` | `duotone-forest` |
| **Dramatização** (Teatro, Bonecos) | 🎭 | `ph-mask-happy` | `duotone-indigo` |
| **Criação** (Desenho, Construção) | ✏️ | `ph-pencil-simple` | `duotone-terra` |
| **Narração** (Conversa, Reconto) | 💬 | `ph-chat-circle` | `duotone-carmim` |
| **Reflexão** (Noite, Pensamento) | 🌙 | `ph-moon-stars` | `duotone-sky` |

### 19.2 Regras de Ouro
1.  **Objetivo:** Criar conexão, não cumprir tarefa.
2.  **Tom:** Sugestivo ("Se você tiver..."), nunca imperativo ("Faça agora").
3.  **Fluidez:** Texto corrido, parágrafos curtos, transição suave para a próxima seção.
4.  **Não Repetição:** Se foi feito na história, faça diferente aqui.

---

## 20. Formação do Portador (Standard) 🎓
Seção dedicada à educação dos pais. O símbolo é o **Chapéu de Graduação** (`ph-graduation-cap`).

### 20.1 Boxes Padronizadas
Todas as caixas devem seguir a estrutura `<p>` com `margin-top`, **sem usar `<br>`**.

| Box | Classe | Ícone Usual | Cor |
|-----|--------|-------------|-----|
| CM | `.cm-box` | `ph-feather` | Roxo |
| TGTB | `.tgtb-box` | `ph-link` | Amarelo |
| Bruner | `.bruner-box` | `ph-spiral` / `ph-brain` | Azul |
| Espiritual | `.espiritual-box` | `ph-sparkle` | Verde |
| Graça | `.graca-box` | `ph-heart` | Cinza |

### 20.2 Exemplo de Código (Box Universal)
```html
<div class="cm-box">
    <strong><i class="ph-duotone ph-feather duotone-forest"></i> Princípio Charlotte Mason:</strong>
    
    <!-- Parágrafo 1: Citação Original (Inglês) -->
    <p style="margin-top: 0.5rem; font-style: italic; color: #4B5563;">
        "Education is an atmosphere, a discipline, a life."
    </p>

    <!-- Parágrafo 2: Tradução (Destaque) -->
    <p style="margin-top: 0.25rem; font-weight: 600; color: #5B21B6; font-size: 0.95rem;">
        "A educação é uma atmosfera, uma disciplina, uma vida."
    </p>
    
    <!-- Parágrafo 3: Explicação -->
    <p style="margin-top: 0.5rem; color: #6B7280;">
        A atmosfera vem primeiro...
    </p>
</div>
```

---

*Atualizado em: 04/03/2026 — Canonização do Header Superior (L003) + Ordem Completa de Tópicos*

---

## 21. 🧠 Protocolo de Consciência da IA (Leia Isto Sempre)
> **De:** Maestro Fundador
> **Para:** Você (Agente IA)
> **Assunto:** Como pensar ao auditar uma lição.

Se você está lendo isso, sua missão é garantir a **Integridade do Reino**. Não execute tarefas de forma mecânica. Entenda o espírito da lei:

### 21.1 O "Mindset" do Auditor
1.  **Impeccability (Impecabilidade):** Não aceite "bom o suficiente". Se um ícone está duplicado, se um espaçamento está estranho, se uma cor não bate com a paleta → **Corrija**.
2.  **Soberania da Família:** O pai/mãe (Portador) é a autoridade máxima. Nós servimos a eles. Não use linguagem acadêmica fria. Acolha.
3.  **Dignidade Visual:** O site deve parecer um aplicativo premium de $100/mês, não um blog amador.

### 21.2 Nuances Críticas (O que a IA costuma esquecer)
*   🚫 **North Star:** Nunca use este termo no texto final. Use **"Matemática Viva"**.
*   🚫 **Caixa Alta:** Não grite nos títulos. Use *Title Case* ("Sementes para o Dia"), não *UPPERCASE* ("SEMENTES PARA O DIA").
*   🚫 **Banalização do Portador:** O Portador não é um rodapé. Ele é o **Narrador**. Sua caixa (fogo carmim) é sagrada.
*   ✅ **Mobile First (UX Regente):** O pai está segurando o celular com uma mão e a criança com a outra. O texto deve ser legível, botões grandes, scroll suave.
*   ✅ **Sinal de Início:** O ritual físico (luz, baú) é mais importante que o digital. Garanta que a "Dica do Coração" sugira isso.

### 21.3 O Teste de "Sanity Check" Final
Antes de dizer "Terminei", pergunte-se:

1.  **Consistência de Ícones:** O ícone "Para a Família" virou `ph-graduation-cap`? O ícone Sementes Box é único?
2.  **CPA Review:** Estou sugerindo algo abstrato (2+2=4) no ciclo Sementes (4-6 anos)? Se sim, **VETO**. Deve ser concreto (duas pedras + duas pedras).
3.  **Fluidez:** O texto do "Momento de Conexão" parece uma ordem militar ("Faça isso") ou um convite gentil ("Convide a criança...")?
4.  **Estética:** As boxes (.cm-box, .bruner-box) estão limpas, sem `<br>` quebrados, com parágrafos elegantes?

> **Lembrete Final:** Você não está apenas editando código HTML. Você está construindo a catedral onde memórias entre pai e filho serão forjadas. Trabalhe com reverência.

---

## 22. O Arsenal do Mestre (Obrigatório) 🧠
> **Substitui:** Dicas soltas, sugestões pedagógicas genéricas.
> **Local:** Dentro de `Formação do Portador`, antes das boxes teóricas.

### 22.1 O Princípio da Variedade Tática
Toda lição deve ter uma box `Estratégia do Mestre` que resolva um **Problema Crítico Específico** daquela lição.

> **Fonte da Verdade:** Consulte o [Framework de Mestria](Revisao/01_REFERENCIAS_DE_APOIO/framework_estrategia_mestria.md) para a lista atualizada de arquétipos (Espelho, Termostato, Eco do Reino, etc.).
> **Não invente:** Use apenas os arquétipos definidos no Framework.

### 22.2 Padrão HTML
*   **Ícone:** `ph-strategy duotone-forest`
*   **Cor de Fundo:** `#F0FDF4`
*   **Borda:** `#15803D`

```html
<div class="instruction-box" style="background-color: #F0FDF4; border-left-color: #15803D;">
    <i class="ph-duotone ph-strategy duotone-forest" style="font-size:1.5rem;"></i>
    <div>
        <strong>Estratégia do Mestre:</strong> [Nome do Arquétipo: O Espelho / A Ponte / A Tribo...]
        <p style="margin-top:0.5rem; color:#374151;">
            [O DIAGNÓSTICO: Qual problema estamos resolvendo ou qual cultura estamos criando?]
        </p>
        <p style="margin-top:0.5rem; color:#374151;">
            [A INTERVENÇÃO CIRÚRGICA: O algoritmo de ação <strong>sem dar a resposta</strong>.]
        </p>
    </div>
</div>
```
