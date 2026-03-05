# Revisão LORE L003 — Histórico Completo & Referência 📜

> **Data Final:** 05/02/2026  
> **Status:** CONCLUÍDO (ROUNDS 1-3)  
> **Responsável:** Gravity (Agente IA)  
> **Validador:** Raul (Maestro Fundador)

Esta documentação serve como **referência histórica** para a evolução da Lição 003 e como **modelo de revisão** para futuras lições (L004+).

---

## 🏆 Resultado Final (O que buscamos)
A Lição 003 ("A Estrela do Reino") agora é um exemplo de **Impecabilidade Visual e Narrativa**. Ela transita perfeitamente do concreto (pedras da L002) para o imaginário (flor/estrela), usando:
*   **LORE Canônica:** Íris no Ninho Mirante (local correto), não "Jardim Secreto".
*   **Metáfora Viva:** Objetos físicos são "pedras", mas na narrativa são "pétalas" e "coração".
*   **Visual Intencional:** Ícones rotacionados para guiar o olhar.
*   **Encantamento:** O "Segredo do Maravilhamento" protege a magia contra explicações excessivas.

---

## 📅 Histórico de Evolução (Incremental)

### ROUND 1: A Fundação Narrativa 🏰
*Foco: Corrigir o "Hook" Narrativo e alinhar com o Currículo Master.*

| # | Item | Problema Anterior | Solução Impecável |
|---|------|-------------------|-------------------|
| 1 | **Foco da Lição** | "Estrela" (genérico) | **"Números 4-5 \| A Flor que Vira Estrela"** (Canonical Hook) |
| 2 | **Dica do Coração** | Texto genérico | Conexão com a "fileira do Bernardo" (L002) |
| 3 | **Sensory Box** | Descrição simples | Adicionado **"flor roxa de cinco pétalas"** (elemento-chave) |
| 4 | **Material** | Apenas "flores" | Especificado: **Violeta, Jasmim ou Pervinca** |

---

### ROUND 2: Imersão & LORE 🌸
*Foco: Consistência de LORE e refinamento da metáfora.*

| # | Item | Problema Anterior | Solução Impecável |
|---|------|-------------------|-------------------|
| 1 | **Local da Cena** | "Jardim Secreto" (Não existe na LORE) | **"Ninho Mirante"** (Lar canônico da Íris - `guardioes.yaml`) |
| 2 | **Título da Cena** | "As Folhas de Pedra" | **"As Pétalas da Flor"** (Reforço da metáfora) |
| 3 | **Metáfora Íris** | "olha essas folhas de pedra" | **"olha essas pétalas de flor!"** |
| 4 | **Contagem** | "1, 2, 3 pedras" | **"1, 2, 3 pétalas..."** (Na voz da Íris) |
| 5 | **Estrutura** | Instrução "Seu filho vai saber" solta | **"Segredo do Maravilhamento"** adicionado para proteger a magia |
| 6 | **Imagem** | `local-jardim-secreto.png` | **`local-ninho-mirante.png`** |

> **Aprendizado Chave:** Quando o Guardião fala, ele vê a magia (Flor). Quando damos instrução técnica, usamos o material (Pedra).

---

### ROUND 3: O Concreto & Refinamento Visual 🧱✨
*Foco: A experiência tátil ("O Concreto") e detalhes visuais sutis.*

| # | Item | Problema Anterior | Solução Impecável |
|---|------|-------------------|-------------------|
| 1 | **Ícone Apontando** | `ph-hand-pointing` apontava para cima (☝️) | - [x] **Visual:** Ícone `ph-hand-pointing` rotacionado (90º) para apontar para a direita.
- [x] **O Concreto (Imersão Total):** Substituição de termos "pedra" por metáforas vivas.
    - "Separe 4 pedras para criar as pétalas..."
    - "Aponte para o centro vazio: o coração da flor."
    - "Coloque a 5ª pedra (pétala) no centro..."
    - "Conte cada pétala..." |
| 2 | **Instrução Concreta** | "Pegue 4 pedras..." (Frio) | **"Separe 4 pedras para criar as pétalas..."** (Intencional) |
| 3 | **Instrução Concreta** | "Mostre o espaço vazio" | **"Aponte para o centro vazio: o coração da flor."** (Poético) |
| 4 | **Instrução Concreta** | "Coloque a 5ª pedra" | **"Coloque a 5ª pedra (pétala) no centro..."** (Fusão Concreto/Abstrato) |
| 5 | **Contagem** | "Conte as pedras" | **"Conte cada pétala tocando nelas."** |

---

### ROUND 3.1: Fix Global (CSS) 🛠️
*Foco: Solução sistêmica em vez de correção local.*

| # | Item | Problema Anterior | Solução Impecável |
|---|------|-------------------|-------------------|
| 1 | **Rotação do Ícone** | Estilo `inline` na L003 era frágil | **Regra Global CSS** em `style.css`: `.instruction-box .ph-hand-pointing { transform: rotate(90deg); }` |
| 2 | **Escalabilidade** | Teria que corrigir manualmente em L001, L002... | **Correção Automática** para TODAS as lições que usam esse componente. |

---

## 🧠 Checklist de Verificação (Para Futuras Lições)

Ao revisar L004 (Noé) e seguintes, verificar:

1.  **Local LORE:** O local indicado no card existe em `locais.yaml`? É o local correto do Guardião?
2.  **Metáfora vs. Material:**
    *   Instrução Técnica (Pai): "Pegue o material..."
    *   Fala do Guardião/Imaginação: "Veja a [metáfora]..."
    *   **O Concreto:** A fusão dos dois ("Toque na pedra e sinta a pétala").
3.  **Visual Cues:** Ícones estão apontando para onde devem? (Use rotação se necessário).
4.  **Proteção da Magia:** Existe o "Segredo do Maravilhamento" para impedir explicações excessivas?

---

> **Status:** Referência congelada. Usar como "Gold Standard" para revisão.

---

### ROUND 4: Estratégias de Resgate & Semântica (08/02/2026) 🛟
*Foco: Preparar a lição para teste real. Adicionar contingências (Learning Billionaire).*

| # | Item | Problema Anterior | Solução Impecável |
|---|------|-------------------|-------------------|
| 1 | **"Dica do Coração"** | Mantido na Preparação (sugestão afetiva) | **"Estratégia de Mestria"** adicionada ao final (profundidade) |
| 2 | **Protocolo de Impecabilidade** | Texto genérico ("joias") | Específico: "como se cada pedra fosse uma joia do jardim da Íris" |
| 3 | **Contingência** | Nenhuma estratégia se criança travar | **"Estratégias de Resgate"** com 4 cenários |

#### Estratégia de Mestria (Novo Elemento):
Inserido na seção "Formação do Portador", focando no **Loss Function Loop**:
> "Se ele montar a estrela torta, **não corrija com as mãos**. Ajuste o ambiente (coloque a flor real ao lado) e pergunte: 'O que a sua estrela tem de parecido com essa aqui?'"

#### Estratégias de Resgate Adicionadas:
1. **Se não quiser montar a flor:** Deixe explorar livremente
2. **Se dispersar:** Use a voz da Íris para reconectar
3. **Se cansar:** Encurte para 3 pétalas
4. **Se quiser do jeito dele:** Celebre a criatividade


> **Aprendizado Chave:** Learning Billionaire — "Estratégia > Dica" + Contingências preparadas = Confiança do Portador.
