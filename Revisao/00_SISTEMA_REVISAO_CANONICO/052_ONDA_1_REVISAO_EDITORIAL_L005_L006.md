# ONDA 1 - REVISAO EDITORIAL L005 E L006
Data: 2026-03-25
Task base: `050_TASK_ROBUSTA_REVISAO_EDITORIAL_INTELIGENTE_L005_L015.md`

---

## Licao 005 - `MV-S-005_O_ESCONDERIJO_DA_GLORIA.html`
### Findings
- Alto: `Navegacao entre licoes` sem acento no `aria-label`.
- Alto: `Lista de Materiais para a Preparacao do Portador` sem acento no `aria-label`.

### Patch
- Ajustado `aria-label` da navegacao superior para `Navegação entre lições`.
- Ajustado `aria-label` da lista de materiais para `Lista de Materiais para a Preparação do Portador`.

### Veredito
- Matriz `001-012`: NAO reavaliada nesta passagem.
- Fronteiras: sem regressao observada.
- Encoding: sem regressao observada.
- Status editorial: bom, com acabamento melhorado.

### Risco residual
- Pode haver outros microajustes de acento ou naming em ondas posteriores, mas nada estrutural apareceu aqui.

## Licao 006 - `MV-S-006_O_DESENHO_DO_REI.html`
### Findings
- Alto: `Navegacao entre licoes` sem acento no `aria-label`.
- Alto: `Lista de Materiais para a Preparacao do Portador` sem acento no `aria-label`.
- Alto: `recognoscível` era uma grafia incorreta; o correto e `reconhecível`.

### Patch
- Ajustado `aria-label` da navegacao superior para `Navegação entre lições`.
- Ajustado `aria-label` da lista de materiais para `Lista de Materiais para a Preparação do Portador`.
- Corrigido `reconhecível` na lista de descoberta da crianca.

### Veredito
- Matriz `001-012`: NAO reavaliada nesta passagem.
- Fronteiras: sem regressao observada.
- Encoding: sem regressao observada.
- Status editorial: melhorado e mais limpo.

### Risco residual
- Vale revisar ondas seguintes com o mesmo olhar para labels auxiliares, mas o bloco principal permaneceu coerente.

## Consolidacao
- A Fase 0 da task editorial ja existia e continuava valida.
- A Onda 1 trouxe ganho real sem abrir reconstrucao.
- A melhor leitura atual e seguir para `MV-S-007` e `MV-S-008` com o mesmo criterio cirurgico.



