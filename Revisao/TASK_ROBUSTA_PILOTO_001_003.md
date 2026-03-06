# TASK ROBUSTA - PILOTO DE VALIDACAO DO SISTEMA DE REVISAO (001-003)
Data: 2026-03-06
Escopo: `MV-S-001`, `MV-S-002`, `MV-S-003`
Regra desta fase: nao editar licoes antes do precheck estrutural completo
Status: pronto para execucao futura

---

## 0) Decisao desta task
1. O piloto `001-003` sera a primeira validacao real do sistema de revisao.
2. Esta task nao autoriza edicao imediata; ela estrutura a execucao.
3. Cada licao sera usada para testar:
   - cobertura do esqueleto;
   - clareza dos topicos;
   - utilidade das transversais;
   - objetividade da rubrica;
   - fidelidade ao North Star.
4. O objetivo do piloto nao e "terminar rapido", mas provar que o metodo aguenta escala sem drift.

---

## 1) Missao do piloto
Validar se o sistema documental criado em `Revisao/` e suficiente para revisar licoes reais sem depender de memoria difusa do projeto.

Pergunta central:
1. uma IA ou humano consegue revisar `001-003` usando apenas o sistema canônico atual?

---

## 2) O que este piloto precisa provar
1. O esqueleto cobre a estrutura real das licoes.
2. Os topicos são claros o bastante para orientar patch por secao.
3. As transversais evitam contradicao e duplicacao.
4. A rubrica premium consegue separar licao boa de licao realmente pronta.
5. O gate North Star impede revisao tecnicamente correta e espiritualmente errada.
6. O processo cabe numa cadencia futura de `2/dia`.

---

## 3) Nao-escopo
1. Nao revisar `004+` nesta fase.
2. Nao fazer busca-e-substituicao global.
3. Nao refatorar templates gerais antes do piloto.
4. Nao reabrir migracao para Next/V5.
5. Nao mexer no YAML nesta task.

---

## 4) Fontes obrigatorias
1. `LORE/north_star.yaml`
2. `Revisao/RadmeRevisao.md`
3. `Revisao/TASK_ROBUSTA_SISTEMA_REVISAO_HTML_FIRST.md`
4. `Revisao/TASK_ROBUSTA_ALINHAMENTO_NORTH_STAR_NA_REVISAO.md`
5. `Revisao/ESQUELETO_GERAL_LICAO_SEMENTES.md`
6. `Revisao/PROTOCOLO_REVISAO_POR_LICAO.md`
7. `Revisao/RUBRICA_PREMIUM_REVISAO.md`
8. `Revisao/STATUS_REVISAO_SEMENTES.md`
9. `Revisao/topicos/`
10. `Revisao/transversais/`
11. `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html`
12. `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`
13. `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html`
14. licoes adjacentes de contexto:
   - `MV-S-000`
   - `MV-S-004`

---

## 5) Papel de cada licao no piloto

### MV-S-001
Funcao no piloto:
1. validar licao padrao mais precoce;
2. testar nomenclatura alvo `Momento de Conexao`;
3. testar transicao Portal -> licao padrao.

### MV-S-002
Funcao no piloto:
1. testar robustez estrutural no miolo inicial do ciclo;
2. testar concreto, organizacao visual e progressao.

### MV-S-003
Funcao no piloto:
1. testar consistencia de guardiao, clima e forma viva;
2. testar coexistencia de legado estrutural e padrao novo.

---

## 6) Ordem oficial do piloto
1. Precheck do sistema
2. Precheck por licao
3. Diagnostico sem patch
4. Matriz de cobertura dos topicos
5. Matriz de vetos North Star
6. Plano de patch por licao
7. Validacao de cadencia
8. Consolidacao do sistema

Regra:
1. nenhuma licao deve ser editada antes de completar as fases 1 a 5 para o lote piloto inteiro.

---

## 7) Fase 1 - Precheck do sistema
Objetivo:
1. garantir que o aparato documental esta realmente pronto.

Checklist:
1. `ESQUELETO_GERAL_LICAO_SEMENTES.md` presente e estavel?
2. `PROTOCOLO_REVISAO_POR_LICAO.md` cobre a ordem real da revisao?
3. `RUBRICA_PREMIUM_REVISAO.md` tem nota e veto suficientes?
4. `TX08_NORTH_STAR_OPERACIONAL.md` esta acionavel?
5. todos os 12 topicos existem?
6. todas as transversais necessarias existem?

Saida:
1. `PASS SISTEMA` ou `BLOCK SISTEMA`

---

## 8) Fase 2 - Precheck por licao
Objetivo:
1. preparar o lote sem editar nada.

Para cada licao:
1. abrir a licao atual;
2. abrir a anterior e a proxima;
3. listar guardiao, local, clima, objetivo concreto e teaser;
4. mapear nome real das secoes;
5. marcar uso de alias legado.

Saida:
1. ficha de precheck por licao.

---

## 9) Fase 3 - Diagnostico sem patch
Objetivo:
1. descobrir os problemas antes de propor solucao.

Para cada licao:
1. identificar findings estruturais;
2. identificar findings narrativos;
3. identificar findings pedagogicos;
4. identificar findings de UX do Portador;
5. identificar findings North Star.

Severidade:
1. Critico
2. Alto
3. Medio
4. Baixo

Saida:
1. lista de findings por licao.

---

## 10) Fase 4 - Matriz de cobertura dos topicos
Objetivo:
1. testar se os 12 guias de topico cobrem mesmo o HTML real.

Modelo por licao:
1. `00_BASE_E_HERO` -> cobre / cobre parcial / nao cobre
2. `01_HEADER_SUPERIOR` -> cobre / cobre parcial / nao cobre
3. `02_PREPARACAO_DO_PORTADOR` -> cobre / cobre parcial / nao cobre
4. `03_RITUAL_DE_ENTRADA` -> cobre / cobre parcial / nao cobre
5. `04_A_JORNADA` -> cobre / cobre parcial / nao cobre
6. `05_MOMENTO_DE_CONEXAO` -> cobre / cobre parcial / nao cobre
7. `06_NARRAMOS_JUNTOS` -> cobre / cobre parcial / nao cobre
8. `07_RITUAL_DE_FECHAMENTO` -> cobre / cobre parcial / nao cobre
9. `08_CONEXAO_DA_JORNADA` -> cobre / cobre parcial / nao cobre
10. `09_SEMENTES_PARA_O_DIA` -> cobre / cobre parcial / nao cobre
11. `10_FORMACAO_DO_PORTADOR` -> cobre / cobre parcial / nao cobre
12. `11_NAVEGACAO_INFERIOR` -> cobre / cobre parcial / nao cobre

Saida:
1. matriz de cobertura por licao;
2. gaps do sistema documental.

---

## 11) Fase 5 - Matriz de vetos North Star
Objetivo:
1. testar se o gate North Star pega desvios reais.

Perguntas por licao:
1. a familia esta no centro?
2. o tom e redentor?
3. a crianca e tratada com dignidade?
4. o concreto domina?
5. a beleza redentora foi preservada?
6. a identidade tribal esta viva?

Saida:
1. PASS/BLOCK North Star por licao;
2. pontos de veto por licao;
3. padrao de falha recorrente, se houver.

---

## 12) Fase 6 - Plano de patch por licao
Objetivo:
1. so depois do diagnostico completo, definir a ordem de edicao futura.

Ordem interna de patch:
1. estrutural
2. navegacao
3. narrativa
4. pedagogia
5. acabamento premium

Regra:
1. gerar plano minimo viavel por licao;
2. evitar reescrita total quando um patch localizado resolve.

Saida:
1. mini-plano de patch por licao.

---

## 13) Fase 7 - Validacao de cadencia
Objetivo:
1. testar se a equipe pode mesmo revisar `2/dia`.

Perguntas:
1. o sistema reduz contexto o suficiente?
2. o numero de ambiguidades ainda e alto?
3. o topico mais lento do fluxo esta bem especificado?
4. o gate North Star atrasa por ser vago ou ajuda por ser claro?

Saida:
1. `PRONTO PARA 2/DIA` ou `AINDA NAO`

---

## 14) Fase 8 - Consolidacao do sistema
Objetivo:
1. melhorar o sistema antes da escala.

Possiveis acoes:
1. refinar topico com baixa cobertura;
2. refinar transversal vaga;
3. simplificar rubrica;
4. endurecer veto recorrente;
5. criar nota de migracao para legados.

Saida:
1. backlog curto de melhorias do sistema.

---

## 15) Entregaveis do piloto
1. precheck do sistema
2. 3 fichas de precheck de licao
3. 3 listas de findings
4. 3 matrizes de cobertura dos topicos
5. 3 matrizes North Star
6. 3 mini-planos de patch
7. 1 decisao de cadencia
8. 1 consolidado final do sistema

---

## 16) Definition of Ready do piloto
O piloto so comeca quando:
1. todos os docs centrais existirem;
2. os topicos estiverem completos;
3. as transversais estiverem completas;
4. a task North Star estiver integrada;
5. as licoes 001-003 e adjacentes estiverem acessiveis.

---

## 17) Definition of Done do piloto
O piloto so fecha quando:
1. as 3 licoes tiverem sido diagnosticadas;
2. a cobertura dos topicos tiver sido medida;
3. o gate North Star tiver sido testado;
4. houver plano de patch por licao;
5. houver decisao sobre cadencia `2/dia`;
6. o sistema tiver sido ajustado ou declarado pronto para escala.

---

## 18) Modelo de saida por licao
Usar:

```md
## MV-S-XXX - [Titulo]

### Precheck
- Guardiao:
- Local:
- Clima:
- Conceito concreto:
- Alias legado:

### Findings
- Critico:
- Alto:
- Medio:
- Baixo:

### Cobertura dos topicos
- 00_BASE_E_HERO:
- 01_HEADER_SUPERIOR:
- 02_PREPARACAO_DO_PORTADOR:
- 03_RITUAL_DE_ENTRADA:
- 04_A_JORNADA:
- 05_MOMENTO_DE_CONEXAO:
- 06_NARRAMOS_JUNTOS:
- 07_RITUAL_DE_FECHAMENTO:
- 08_CONEXAO_DA_JORNADA:
- 09_SEMENTES_PARA_O_DIA:
- 10_FORMACAO_DO_PORTADOR:
- 11_NAVEGACAO_INFERIOR:

### Gate North Star
- Familia no centro: PASS/BLOCK
- Tom redentor: PASS/BLOCK
- Dignidade: PASS/BLOCK
- Descoberta concreta: PASS/BLOCK
- Beleza redentora: PASS/BLOCK
- Identidade tribal: PASS/BLOCK

### Plano de patch futuro
- Estrutural:
- Narrativo:
- Pedagogico:
- Premium:
```

---

## 19) Proximo passo recomendado
1. nao editar licoes ainda;
2. usar esta task para fazer o diagnostico puro do piloto;
3. so depois autorizar patch.

