# PROJETO: AI Search & Replace Protocol (Icon Standardization)
DATA: 2026-01-29
HORA: 16:15
STATUS: **REVISION CYCLE 2.2 (Planning)**

## Contexto
O protocolo inicial foi bom, mas o User identificou melhorias semânticas essenciais ("Cycle 2.2"). Precisamos ajustar as metáforas visuais e garantir que a linguagem seja acessível ("Ritual de Entrada").

## Refinamentos Visuais (Feedback do User)

### 1. Persona: Portador da Tocha
*   **Antes:** `ph-lantern` (Parece um abajur/lampião).
*   **Agora:** Precisamos de uma **TOCHA** real.
*   **Candidato:** `ph-torch` (Se existir) ou `ph-flame` (com estilo distinto).

### 2. Ritual de Entrada (Ambiente/Preparação)
*   **Contexto:** O texto "Tapete estendido...", "Luzes diminuídas...".
*   **Ação:** Padronizar título para **"Ritual de Entrada"**.
*   **Ícone:** Aqui sim cabe o **Abajur/Lampião** (`ph-lamp` ou `ph-lantern`) para simbolizar "luz de casa/aconchego".

### 3. Símbolos Específicos
*   **Charlotte Mason:** `ph-columns` ficou muito "acadêmico".
    *   *Ideias:* `ph-feather` (Pena/Natureza), `ph-leaf` (Vida), `ph-open-book` (Livros Vivos).
*   **Preparação do Portador:** Ícone atual não agradou.
    *   *Ideias:* `ph-armchair` (Lugar do Pai), `ph-coffee` (Pausa), `ph-list-checks` (Checklist).

## Plano de Execução Incremental (Task Strategy)

Para não quebrar o contexto, faremos em blocos pequenos:

### Fase A: Definição (Lab Icones)
1.  **Investigar Ícones:** Verificar existência de `ph-torch`, `ph-lamp`, etc. no Lab.
2.  **Validação Visual:** Apresentar as novas escolhas no `lab_icones.html` para o User.

### Fase B: Retrofit (L000, L001, L002)
*Como já padronizamos L000-L002, precisamos "re-padronizar" antes de escalar.*
1.  **Lote 1 (L000):** Aplicar Tocha, Abajur, CM e Preparação. Revisar Texto "Ritual de Entrada".
2.  **Lote 2 (L001):** Replicar.
3.  **Lote 3 (L002):** Replicar.

### Fase C: Atualização do Protocolo AI
1.  Atualizar o JSON em `lab_icones.html` COM AS NOVAS REGRAS FINAIS.
2.  Só então liberar para L003+.

## Tabela de Substituição (Rascunho v2.2)

| Contexto | Busca (Antigo) | Alvo (Novo) | Obs |
| :--- | :--- | :--- | :--- |
| **Persona** | `ph-lantern` (Portador) | `ph-torch` | Se houver |
| **Ritual** | "Tapete...", `ph-wind`? | `ph-lamp` + Texto "Ritual de Entrada" | Padronizar Texto |
| **Pedagogia** | `ph-columns` (CM) | `ph-feather` (Pena) | Testar |
| **Header** | Preparação | `ph-coffee`? | Discutir |

---
*Aguardando validação dos ícones no Lab.*
