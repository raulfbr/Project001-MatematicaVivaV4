# Log de Planejamento: Protocolo de Escala 3x3 (Segurança Máxima)
**Data:** 29/01/2026
**Horário:** 12:45
**Escopo:** 23 Arquivos (Lições 003 a 025)
**Estratégia:** Micro-Lotes de 3 lições ("Trindade de Segurança").

## 1. O Conceito: "Segurança Impecável"
Atendendo à diretriz de risco zero, abandonamos os grandes lotes.
Adotaremos o **Ciclo 3x3**:
1.  **Refatorar** 3 arquivos.
2.  **Validar** 1 arquivo do grupo visualmente.
3.  **Commitar** o micro-lote.

*Benefício:* Se um erro ocorrer, ele estará confinado a apenas 3 arquivos, facilitando a reversão instantânea.

## 2. Definição dos Micro-Lotes (Batches)

| Lote | Lições Alvo | Status |
| :--- | :--- | :--- |
| **Batch 01 (Piloto)** | `003`, `004`, `005` | ⏳ Pendente |
| **Batch 02** | `006`, `007`, `008` | ⏳ Pendente |
| **Batch 03** | `009`, `010`, `011` | ⏳ Pendente |
| **Batch 04** | `012`, `013`, `014` | ⏳ Pendente |
| **Batch 05** | `015`, `016`, `017` | ⏳ Pendente |
| **Batch 06** | `018`, `019`, `020` | ⏳ Pendente |
| **Batch 07** | `021`, `022`, `023` | ⏳ Pendente |
| **Batch 08 (Final)**| `024`, `025` | ⏳ Pendente |

## 3. Especificação Técnica (O "Pente Fino")

### A. Substituição Estrutural (Regex Seguro)
Estas mudanças são idênticas em todos os arquivos e podem ser aplicadas com confiança:

1.  **Navegação Semântica**
    *   *Busca:* `<div class="lesson-header-nav">` ... (conteúdo) ... `</div>`
    *   *Substituição:* `<nav class="lesson-nav-grid" aria-label="Navegação da Lição">` ... (conteúdo ajustado) ... `</nav>`

2.  **Materiais Semânticos**
    *   *Busca:* `<div class="materials-box">`
    *   *Substituição:* `<aside class="materials-box" aria-label="Lista de Materiais">` (fechando com `</aside>`)

### B. Tratamento Visual de Imagens (Cirúrgico)
Como cada imagem tem um `style` inline diferente, o agente fará:
1.  **Remoção:** Deletar atributos `style="..."` das tags `<img>`.
2.  **Aplicação:** Adicionar `class="card-visual-asset rotate-left hover-float"`.
3.  **Variação:** Alternar para `rotate-right` em imagens pares do mesmo arquivo para dar "efeito bagunçado/natural".

## 4. Protocolo de Reversão (Rollback)
Caso a validação visual falhe em qualquer lote:
1.  Não tentar consertar "por cima".
2.  Executar: `git checkout .` (Desfaz alterações não commitadas do lote atual).
3.  Reavaliar a estratégia para aquele lote específico.

---
**Status:** PRONTO PARA INICIAR O LOTE PILOTO (003-005).
