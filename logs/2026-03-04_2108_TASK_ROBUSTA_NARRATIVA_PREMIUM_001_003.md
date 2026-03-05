# TASK ROBUSTA - NARRATIVA PREMIUM (001-003)
Data: 2026-03-04 21:08 (America/Sao_Paulo)
Escopo: `MV-S-001`, `MV-S-002`, `MV-S-003` em `curriculo/01_SEMENTESV6/`

---

## 1) Objetivo
Elevar a narrativa e a imersão das lições 001-003 sem perder rigor matemático e pedagógico.

Resultado esperado:
1. texto mais nobre e cristalino (Lewis),
2. mundo interno coerente e sem furos (Tolkien),
3. criança tratada como pessoa, com concreto dominando a experiência (Charlotte Mason + CPA).

---

## 2) Critérios de revisão por expert

### CS Lewis (Dignidade Narrativa)
1. remover tom condescendente, exagero infantilizado e comandos agressivos;
2. preservar mistério e convite, evitando moralização pesada;
3. manter texto legível para criança e agradável para adulto.

### Tolkien (Consistência do Reino)
1. locais e climas coerentes com `LORE/locais.yaml` e `LORE/climas.yaml`;
2. guardiões agem conforme sua identidade narrativa;
3. evitar contradições internas de cenário/voz.

### Charlotte Mason (Pedagogia Viva)
1. concreto antes de pictórico/abstrato;
2. narração presente e curta;
3. lição aplicável em 15-20 min, com preparo <= 5 min;
4. linguagem de respeito e inclusão (adaptação Bernardo).

---

## 3) Estratégia de implementação
1. atualizar metadados para revisão V6.5 nos 3 YAML;
2. revisar blocos centrais:
   - `para_portador`
   - `ritual_abertura`
   - `jornada.narrativa_principal`
   - `narracao`
   - `ritual_fechamento`
   - `para_familia`
3. normalizar campos técnicos para YAML estrito (evitar mapas inline críticos);
4. manter e qualificar `sementes_do_dia` em framework de 5 atividades.

---

## 4) Gates de aceite
1. Gate Narrativo: tom nobre, imersivo e convidativo.
2. Gate Pedagógico: matemática concreta explícita + narração CM.
3. Gate Técnico: parse YAML global sem erro.
4. Gate de Continuidade: encadeamento 001->002->003->004 preservado.

---

## 5) Entregáveis
1. 3 YAML revisados.
2. Log de execução com justificativas e status por gate.
3. Base pronta para escalar lote 004-006.
