# 🦁 Log de Planejamento: Refinamento Sementes

**Data:** 03/02/2026
**Horário:** 13:35
**Tema:** Cirurgia Fina e Padronização - Ciclo Sementes
**Status:** 🟡 Em Planejamento (Aguardando Novos Pontos)

---

## 1. 🎯 Objetivo Central
Realizar uma revisão "impecável" nas lições do ciclo **Sementes**, garantindo:
1.  **Narrativa Limpa:** Eliminação de redundâncias visuais que quebram a imersão.
2.  **Consistência:** Padrão rigoroso de uso de Assets (Cards vs. Personas).
3.  **Excelência Visual:** Refinamentos estéticos para ampliar o "maravilhamento".

---

## 2. 🔍 Diagnóstico: MV-S-000 (O Portal do Reino)
**Problema Identificado:** Poluição Visual por Redundância do Guardião Melquior.

*   **Análise de Ocorrências:**
    *   ❌ **Linha 212 (Visualizar):** Redundante. O avatar já introduz o diálogo. -> **AÇÃO: REMOVER.**
    *   ⚠️ **Linha 252 (Convite):** Avaliar. Se o foco é o texto do convite, o card "Mostrar Card" compete com a leitura. -> **AÇÃO: PROVÁVEL REMOÇÃO.**
    *   ❌ **Linha 315 (História da Criação):** Interrupção desnecessária antes de um momento solene de fala. -> **AÇÃO: REMOVER.**
    *   ✅ **Linha 385 (Quem é Melquior):** Momento correto de identificação e "fichamento" do personagem. -> **AÇÃO: MANTER.**

**Diretriz Definida:**
> *O Card do Guardião ("Mostrar Card") deve ser usado APENAS quando a instrução for explicitamente para a criança "olhar e analisar" o personagem físico, ou na sua apresentação formal. Para diálogos, o Avatar no `script-persona-block` é suficiente.*

---

## 3. 📝 Lista de Inspeção e Tarefas
Este documento será atualizado conforme novas demandas forem inseridas.

### Fase A: MV-S-000 (O Portal)
- [ ] Remover cards redundantes do Melquior.
- [ ] Validar fluidez do texto após remoção.

### Fase B: Auditoria Sementes (S-001 a S-025)
- [ ] Verificar aplicação da "Diretriz Melquior" em todas as lições.
- [ ] Identificar outros vícios de repetição (Ex: Cards de outros guardiões).

### Fase C: Refinamentos Visuais & Estruturais (Baseado em Log 29/01)
*Pontos recuperados da revisão de Migração CSS:*
- [ ] **Navegação Superior:** Verificar integridade do bloco `<nav>` (Item A).
- [ ] **Espaçamento Topo:** Garantir que o botão "Home" não colida com o conteúdo (Item F).
- [ ] **Labels Padronizados:** Confirmar uso de `<p class="local-label">` em vez de estilos inline (Item H).
- [ ] **Alinhamento Portador:** Verificar se o ícone e título do "Portador" estão alinhados (Item B).
## 14. 🔥 Correção de Identidade Visual (Portador)
*Diagnóstico:* O ícone `ph-flashlight` (Lanterna) foi um fix técnico, mas erra no *conceito*. O correto é `ph-fire` (Chama/Zeal), representando o "Portador da Chama".

**Ações de Correção:**
1.  **Iconografia:** Substituir `ph-flashlight` por **`ph-fire`** (com classe `duotone-carmim` para tom afetivo/vivo, ou `duotone-gold` se quisermos manter a luz). *Decisão: `duotone-carmim` conforme Lab.*
2.  **CSS Global (`style.css`):**
    *   Refinar `.script-avatar-icon` para ser uma classe utilitária universal.
    *   Acrescentar regras específicas para `.portador-block .script-avatar-icon` para garantir que, se o HTML for simples, o CSS garanta a centralização e as cores corretas (Carmim/Gold) automaticamente.
## 15. 🎭 Padronização de Roteiro (Direção de Palco & Ritual)
*Objetivo:* Definir regras claras para que a IA (e o usuário) saibam exatamente como formatar falas vs. instruções.

**1. A Regra dos Colchetes (Stage Directions):**
*   Quando o Portador deve fazer uma *ação* enquanto fala (ex: olhar nos olhos, sussurrar, apontar), usamos **Colchetes**.
*   **Sintaxe:** `[Ação ou Tom]`
*   **Estilo Visual:** Texto menor, cor Dourada/Accent, dentro do próprio fluxo de fala.
*   *Exemplo:* `"Você está pronto? [Sussurrando] O Reino nos espera."`

**2. Estrutura do Ritual (O Fluxo Sagrado):**
*   **A. Bastidores (Box Amarelo):** Instruções puramente *técnicas* ou de preparação (Luz, Som, Postura Física antes de começar). O "Pai-Técnico" lê isso.
*   **B. Palco (Portador Block):** A "Entrada do Personagem". O Pai veste o Manto.
    *   *Regra de Consolidação:* Se o Portador fala vários parágrafos seguidos, **NÃO** quebre em vários blocos. Use um único `.portador-block` com múltiplos `<p>`. Só quebre se houver uma *Ação Técnica* ou *Mudança de Cena* (Narrativa) no meio.
*   **C. A Ponte (Narrative Text):** Texto corrido (`.narrative-text`) para trechos guiados ("Feche os olhos...", "Imagine..."). Isso é o Pai-Narrador, não necessariamente o Personagem Portador falando diretamente, mas conduzindo a imaginação.

**Próximo Passo:** Documentar essas regras explicitamente em `Revisao/padrao_visual_sementes.md`.

- [ ] **Estilos de Cena:** Validar renderização de `.scene-header` e `.scene-card` (Itens D e E).

---


### Fase D: Otimização do Ritual de Entrada (UX Narrativa)
*Problema:* O Ritual está fragmentado em 4 blocos desconexos (Instrução -> Transição -> Sensorial -> Fala), dificultando para o pai entender o fluxo.
- [ ] **Unificação:** Criar um fluxo contínuo.
- [ ] **Distinção Visual:** Separar claramente "Instrução ao Pai" de "Texto Narrativo".

---

## 5. 🎨 ESPECIFICAÇÃO DETALHADA: Novo Ritual de Entrada

### O Conceito Visual
Transformaremos os vários "bloquinhos" em dois momentos claros:
1.  **O Preparo (Instrução Interna):** Um card amarelo, discreto, com ícone de lâmpada. É o "bastidor". O pai lê para si.
2.  **A Imersão (Narrativa):** Um texto fluido, poético, que *começa* com a transição (fechar olhos) e *termina* com a descrição sensorial, tudo em um único bloco visual ou parágrafos conectados, sem caixas interrompendo a leitura.

### Mockup da Estrutura Proposta (Markdown Preview)

**[BLOCO 1: INSTRUÇÃO - BASTIDORES]**
> 💡 **Ritual de Entrada:**
> Diga: "Luz de fora acalma." (Diminua o ritmo).
> Diga: "Sol de dentro acende." (Acenda a Luz Amarela).
> Diga: "Respirem... Estamos no Reino."

*(Espaço em branco - Respiro)*

**[BLOCO 2: NARRATIVA - PALCO]**
> *Feche os olhos. Respire fundo.*
> *Quando você abrir os olhos, estaremos em um lugar muito especial...*
>
> **O Jardim Central do Reino Contado.**
>
> 🍃 O ar cheira a terra molhada e musgo fresco. O sol dourado aquece o rosto. Pássaros cantam ao longe.
> Em um banco de pedra antiga, sentado com as patas cruzadas, está um grande Leão de juba dourada. Ele sorri ao ver você chegar.

*(Fim do bloco narrativo -> Entra Avatar do Portador)*

---

## 6. 💅 ESPECIFICAÇÃO CSS: "Impecabilidade" (Lição 000)

Para deixar a Lição 000 visualmente robusta, aplicaremos as seguintes correções no `style.css` (ou local, se necessário, mas preferencialmente global):

### A. Tipografia & Hierarquia
*   **`.hero-quote`:** Aumentar ligeiramente o line-height e garantir itálico elegante (`Lora`).
*   **`.instruction-box`:**
    *   Remover bordas pretas pesadas se houver.
    *   Usar `background: #FEF9C3` (Amarelo suave) com `border-left: 4px solid #F59E0B` (Ouro).
    *   Fonte: `Outfit` (Sans-serif) para contraste com a narrativa.
*   **Texto Narrativo (Sensorial):**
    *   Fonte: `Lora` ou `Merriweather` (Serif).
    *   Tamanho: `1.1rem` ou `1.2rem` para leitura confortável (Leitura em voz alta exige letra maior).
    *   Cor: `#374151` (Cinza escuro, não preto puro).

### B. Elementos "Scene Card"
*   **Sombra:** `box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);` (Suave, premium).
*   **Borda:** `border-radius: 16px;` (Amigável).
*   **Header do Card:** Garantir que o ícone e o título estejam alinhados verticalmente (`display: flex; align-items: center; gap: 0.5rem;`).

### C. Alinhamentos (Correções do Log 29/01)
*   **Navegação:** O topo da página precisa ter padding suficiente para o botão "Home" não flutuar sobre o título. (`.lesson-container { padding-top: 4rem; }`).
*   **Portador da Tocha:** Forçar alinhamento flex no header do script para evitar que o ícone 🔥 fique "solto" do nome.


---

## 7. 🃏 Coreografia dos Cards (Definição Final - Lição 000)

**Decisão:** O Card do Melquior deve aparecer **apenas uma vez** como apresentação solene.
**Momento:** Imediatamente após a apresentação do LOCAL (Jardim Central).

**Fluxo Narrativo Aprovado:**
1.  **Cena:** "O Convite de Melquior" (Contexto).
2.  **Visualizar 1:** Exibir Card **LOCAL** (Jardim Central) -> *"Estamos aqui."*
3.  **Visualizar 2:** Exibir Card **MELQUIOR** (Leão) -> *"Este é quem nos recebe."*
4.  **Ação:** Avatar do Melquior inicia o diálogo ("Aproxime-se...").

**Roteiro de Limpeza (Kill List):**
- [x] 🗑️ **(FEITO MANUALMENTE)** Remover da Intro (Linha 212).
- [x] 🗑️ **(FEITO MANUALMENTE)** Remover da História (Linha 315).
- [x] 🗑️ **(FEITO MANUALMENTE)** Remover da Seção "Quem é Melquior" (Linha 385).
- [ ] ✅ **MANTER/AJUSTAR** na Cena "O Convite" (Linha 252) para garantir que venha logo após o Local.

---

## 8. ✅ Verificação Pós-Edição Manual
*Como o usuário já realizou remoções manuais, precisamos validar a integridade:*
- [ ] Verificar se sobraram tags órfãs (ex: `</div>` solto) onde os cards foram removidos.
- [ ] Confirmar se a instrução de "Mostrar Card" não ficou no texto sem o card correspondente.
- [ ] Validar se o fluxo visual na Lição 000 ficou coerente com o planejado (Apenas 1 Card do Melquior no Convite).

---


## 9. 🚀 Estratégia Consolidada para Execução (Go-Forward)
Para garantir que a implementação seja "inteligente e robusta", dividiremos o trabalho em etapas claras e verificáveis:

1.  **Auditoria HTML (Pós-Edição Manual):** Garantir que o "terreno" está limpo antes de construir.
2.  **CSS Global:** Implementar as classes de suporte global (`.instruction-box` refinado, `.scene-card` premium, correções de layout) no `style.css` ANTES de tocar no HTML. Isso garante que, ao ajustarmos o HTML, ele já "nasça" bonito.
3.  **HTML Refactoring (Lição 000):**
    *   Reconstruir a estrutura do **Ritual de Entrada** (Bloco Bastidores + Bloco Palco).
    *   Ajustar a **Coreografia dos Cards** (Snippet exato: Local -> Melquior -> Diálogo).
    *   Verificar **Navegação** (Re-inserção do header).
4.  **Auditoria Sementes:** Validar se as regras aplicadas na 000 precisam ser replicadas (anotar para tarefa futura).

Esta estratégia minimiza regressões: primeiro limpamos, depois preparamos o estilo visual, e por fim estruturamos o conteúdo.

---

## 10. 🗣️ Refinamento de Feedback (Portador da Tocha)
**Diretriz de Tom:** Impecabilidade.
*   ❌ **Proibido:** Onomatopeias infantis ("Shhh...", "Psiu").
*   ✅ **Obrigatório:** Instruções de "bastidores" (como *tom de voz*, *ação física*) devem estar estritamente dentro de **colchetes** `[ ]` e estilizadas visualmente para não se confundirem com a fala.

**Especificação do Bloco do Portador:**
*   **Ícone:** Tocha (`ph-torch duotone-gold`).
*   **Cabeçalho:** Apenas "Portador da Tocha" (Sem "Tom:" redundante).
*   **Corpo:**
    *   Texto falado em cor normal.
    *   Instrução interna: `<span style="color:var(--accent-gold); font-size:0.9em;">[Olhe nos olhos da criança]</span>`

**Ação Imediata (Lição 000):**
- [ ] Converter instruções de tom para notação `[ ]`.

---

## 11. 🛡️ Conformidade com Orchestrator v1.5 (Checagem)
*Alinhamento com Meta-Regras e Distinção de Papéis:*

1.  **Distinção de Papéis (Regra Suprema):**
    *   *Técnico (Bastidores/Pais):* Instruction Box Amarela (`.instruction-box`). **(CONFORME)**
    *   *Narrativo (Reino Contado):* Texto fluido e Portador (`.narrative-text`, `.script-persona-block`). **(CONFORME)**
    *   *Separador:* Instruções internas no diálogo usam colchetes `[ ]` e estilo diferenciado, mantendo a "Quarta Parede" intacta para a criança. **(CONFORME)**

2.  **Regent UX (Mobile First):**
    *   CSS removendo padding lateral excessivo em mobile (`style.css` atualizado). **(CONFORME)**
    *   Botão Home flutuante ajustado para não cobrir texto. **(CONFORME)**

3.  **Guardião Tom (CS Lewis/Tolkien):**
    *   Remoção de "Shhh" (infantilização) -> Adoção de tom misterioso/respeitoso. **(CONFORME)**

