# TASK ROBUSTA - IMPLANTACAO DO SISTEMA DE FEEDBACK DE MAES REAIS
Data: 2026-03-12
Status: concluida nesta rodada
Escopo: criar a trilha operacional de feedback de maes reais e rodar o caso piloto `Marina x L003`

---

## 1) Objetivo
1. impedir que feedback real de maes se perca em conversa ou log solto;
2. impedir que feedback bruto suba cedo demais para o `North Star`;
3. criar uma trilha clara de:
   a. evidencia bruta;
   b. leitura critica;
   c. sintese transversal;
   d. canonizacao seletiva;
4. usar `Marina x L003` como caso piloto real.

---

## 2) Decisao desta task
Nesta rodada, a melhor decisao e:
1. criar a pasta `logs/FEEDBACK_MAES_REAIS/`;
2. criar README, template, lista viva e indice de promocao;
3. migrar `Marina x L003` para o novo formato de caso;
4. criar uma primeira sintese transversal a partir desse caso;
5. NAO editar ainda o `008_NORTH_STAR_OPERACIONAL.md`;
6. deixar o `North Star` para uma fase seguinte, ja apoiada em evidencia organizada.

---

## 3) Arquivos em escopo
### Criar
1. `logs/FEEDBACK_MAES_REAIS/000_README.md`
2. `logs/FEEDBACK_MAES_REAIS/001_TEMPLATE_CASO_FEEDBACK_MAE_REAL.md`
3. `logs/FEEDBACK_MAES_REAIS/002_LISTA_VIVA_CANDIDATOS_NORTH_STAR.md`
4. `logs/FEEDBACK_MAES_REAIS/INDEX_PROMOCAO_CANONICA.md`
5. `logs/FEEDBACK_MAES_REAIS/CASOS/2026/2026-03-12_MARINA_MV-S-003.md`
6. `logs/FEEDBACK_MAES_REAIS/SINTESIS/2026-03-12_SINTESIS_INICIAL_PADROES_MARINA_L003.md`

### Atualizar
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/000_INDEX_SISTEMA_REVISAO.md`

### Base de decisao
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/033_PLANO_SISTEMA_FEEDBACK_MAES_REAIS_E_CANONIZACAO_NORTH_STAR.md`
2. `logs/2026.03.12/2026-03-12_ANALISE_FEEDBACK_MARINA_L003.md`
3. `logs/2026.03.12/2026-03-12_EXECUCAO_INCREMENTAL_L003_POS_FEEDBACK_MARINA.md`

---

## 4) Regras desta implantacao
1. feedback bruto deve permanecer reconhecivel como voz real da mae;
2. leitura critica nao pode apagar a evidencia;
3. sintese transversal deve separar o que e local do que e duravel;
4. `North Star` so recebe principio duravel, nao historico de caso;
5. a nova trilha deve ficar simples o suficiente para ser usada de verdade.

---

## 5) Passo a passo executado
### Fase 1 - Estrutura
1. criar a pasta-base `logs/FEEDBACK_MAES_REAIS/`;
2. criar `000_README.md`;
3. criar `001_TEMPLATE_CASO_FEEDBACK_MAE_REAL.md`;
4. criar `002_LISTA_VIVA_CANDIDATOS_NORTH_STAR.md`;
5. criar `INDEX_PROMOCAO_CANONICA.md`.

### Fase 2 - Caso piloto
1. migrar o caso `Marina x L003` para o formato novo;
2. registrar:
   a. feedback bruto;
   b. leitura;
   c. decisoes;
   d. o que foi aplicado;
   e. o que o sistema aprendeu;
   f. status de promocao.

### Fase 3 - Sintese inicial
1. criar uma primeira sintese transversal do caso;
2. separar:
   a. heuristicas locais;
   b. heuristicas transversais;
   c. candidatos futuros ao `North Star`.

### Fase 4 - Integracao minima
1. atualizar o index canonico para que a trilha nova nao fique invisivel.

### Fase 5 - Refino pos-auditoria
1. reforcar o README com:
   a. convencao de nomes;
   b. checklist minimo;
   c. anti-patterns;
2. evoluir o template para capturar:
   a. criticas e validacoes;
   b. risco de overcorrection;
   c. fechamento do caso;
   d. status do caso e status de promocao atual;
3. alinhar o caso piloto ao template refinado;
4. tornar o indice de promocao mais explicito sobre o proximo gate.

---

## 6) Resultado esperado
Ao fim desta task, o projeto passa a ter:
1. um lugar oficial para feedback real de maes;
2. um formato padrao para novos casos;
3. um piloto real ja documentado;
4. uma camada inicial de sintese;
5. uma lista viva de candidatos ao `North Star`;
6. uma ponte clara para futura canonizacao.
7. uma estrutura que diferencia critica, validacao e fechamento do caso.

---

## 7) Definition of Done
1. a pasta `logs/FEEDBACK_MAES_REAIS/` existe;
2. ha README e template utilizaveis;
3. o caso `Marina x L003` esta migrado;
4. a sintese inicial existe;
5. a lista viva de candidatos ao `North Star` existe;
6. o index canonico aponta para a nova trilha;
7. o `North Star` ainda nao foi poluido com feedback bruto.
8. o template captura tambem feedback positivo e risco de overcorrection.
9. o caso piloto termina com `o que realmente fizemos` e `o que ficou importante`.

---

## 8) Proximo passo recomendado
1. usar o template em todo novo feedback real de mae;
2. acumular mais 2 ou 3 casos;
3. reabrir a decisao sobre:
   a. nova transversal `009_EMPATIA_OPERACIONAL_E_TESTE_DA_MAE_REAL.md`;
   b. ajustes seletivos no `008_NORTH_STAR_OPERACIONAL.md`.
