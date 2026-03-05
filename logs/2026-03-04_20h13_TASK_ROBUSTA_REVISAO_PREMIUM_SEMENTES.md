# TASK ROBUSTA - REVISAO PREMIUM SEMENTES (PLAYBOOK PARA IA)
Data: 2026-03-04 20:13 (America/Sao_Paulo)
Escopo inicial: L000 a L003
Projeto: Project001-MatematicaVivaV4
Objetivo: padronizar revisao, elevar qualidade premium e escalar para S004+ sem perder narrativa nem rigor matematico.

---

## 1) Missao desta task
Criar um processo executavel por IA, repetivel e auditavel, para:
1. alinhar cada licao com Orchestrator + Curriculo Mestre;
2. padronizar estrutura HTML (produto premium);
3. fortalecer narrativa (imersao) e matematica concreta (aprendizagem real);
4. gerar evidencias objetivas de qualidade antes de publicar.

---logs\2026-03-04_19h56_Padronizar

## 2) Fontes obrigatorias (ordem de leitura)
1. `bmad/orchestrator.yaml`
2. `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md`
3. `Revisao/padrao_visual_sementes.md`
4. `Revisao/topicos_licao_revisao.md`
5. `Revisao/framework_estrategia_mestria.md`
6. `logs/2026-03-04_19h56_Padronizar`
7. `site/sementes/MV-S-000..003_*.html`
8. `site/sementes/style.css`

Se houver conflito entre documentos:
1. Orchestrator (meta-regras) vence.
2. Curriculo Mestre vence em objetivo pedagogico.
3. Esqueleto canonico de revisao define HTML final.

---

## 3) Regras nao-negociaveis (produto premium)
1. L000 e excecao oficial de "Portal" (liturgica/narrativa).
2. L001+ seguem esqueleto unico canonico.
3. Sem script duplicado.
4. Sem `<br>` para layout em blocos pedagogicos (usar `<p>`).
5. `instruction-box` textual multi-paragrafo deve usar wrapper interno `<div>`.
6. `Sementes para o Dia` sempre com 5 atividades (Exploracao, Dramatizacao, Criacao, Narracao, Reflexao).
7. Formacao do Portador deve iniciar com "Estrategia do Mestre".
8. Mobile-first: leitura limpa, sem friccao.

---

## 4) Gates de revisao (obrigatorios em toda licao)

### Gate A - Meta (Orchestrator)
Checklist:
1. Unidade familiar preservada?
2. Soberania intelectual preservada (sem medo como estrategia)?
3. Regent UX respeitada (simples para pai/mae no celular)?
4. Distincao de papeis respeitada (narrativo vs tecnico)?

Saida obrigatoria: `PASS` ou `BLOCK`.

### Gate B - Charlotte Mason
Checklist:
1. Crianca tratada como pessoa capaz?
2. Licao curta e respiravel (15-20 min)?
3. Narracao presente e significativa?
4. Ideia viva domina a licao?
5. Pais conseguem aplicar com preparo leve?

Saida obrigatoria: `PASS` ou `BLOCK`.

### Gate C - Bruner (CPA)
Checklist:
1. Concreto e o nucleo da experiencia?
2. Pictorico nao antecipa o concreto?
3. Abstrato aparece como reconhecimento, sem forca?
4. Objetivo matematico da licao esta concretamente executado?

Saida obrigatoria: `PASS` ou `BLOCK`.

### Gate D - Engenharia
Checklist:
1. Estrutura HTML consistente e sem quebrar layout?
2. Classes e icones padronizados?
3. Sem duplicacao tecnica (script, blocos conflitantes)?
4. Navegacao anterior/proxima valida?

Saida obrigatoria: `PASS` ou `BLOCK`.

Nenhuma licao pode ser marcada como pronta com algum `BLOCK`.

---

## 5) Matriz curricular minima (S000-S003)

### S000 - Portal (Intro)
Expectativa: liturgica, sem conteudo matematico formal.
Foco: pertencimento, atmosfera, apresentacao dos guardioes.

### S001 - 000-L1 Numbers 1 to 3
Expectativa: contagem 1-3 com correspondencia 1-a-1 real/tatil.

### S002 - 000-L2 Ten Frames
Expectativa: organizacao visual para base de ten frame.
Regra premium: nao parar em fileira de 5; incluir transicao concreta para 5+5 no nucleo (ou explicitar preparacao para isso de modo forte e pratico).

### S003 - 000-L3 Numbers 4 to 5
Expectativa: 4/5 em forma viva (moldura + estrela), com matematica concreta e narrativa coerente.

---

## 6) Protocolo operacional por licao (passo a passo para IA)

### Passo 0 - Preparacao
1. Ler YAML da licao em `curriculo/01_SEMENTESV6`.
2. Ler HTML correspondente em `site/sementes`.
3. Ler secao equivalente no Curriculo Mestre.

Entregavel: mini-resumo "promessa curricular vs estado atual".

### Passo 1 - Diagnostico com evidencias
1. Listar findings por severidade: Critico, Alto, Medio, Baixo.
2. Cada finding deve incluir arquivo + linha.
3. Separar em 3 colunas: Estrutura, Narrativa, Matematica.

Entregavel: tabela de findings com impacto.

### Passo 2 - Plano de patch minimo (menor risco)
1. Aplicar primeiro correcoes de risco tecnico (layout, script, markup).
2. Depois consistencia estrutural (secoes, icones, naming).
3. Por fim refinamento pedagogico/narrativo.

Entregavel: plano com ordem de execucao e justificativa.

### Passo 3 - Edicao
1. Editar HTML com mudancas pequenas e verificaveis.
2. Manter texto fiel ao hook curricular da licao.
3. Nao introduzir blocos novos sem motivo pedagogico claro.

Entregavel: diff limpo.

### Passo 4 - Validacao pos-patch
1. Re-rodar checklist dos 4 gates.
2. Verificar coerencia de navegacao.
3. Verificar coerencia com licao anterior e proxima.

Entregavel: relatorio PASS/BLOCK final da licao.

### Passo 5 - Registro
1. Registrar em log:
- o que foi ajustado;
- por que foi ajustado;
- quais riscos foram removidos;
- quais pendencias ficaram.
2. Atualizar backlog da rodada seguinte.

Entregavel: entrada de log pronta para historico.

---

## 7) Ordem recomendada de execucao (lote inicial)
1. L002 (maior gap tecnico + curricular).
2. L003 (higiene tecnica + padrao de estrutura).
3. L001 (ajustes finos de consistencia visual/editorial).
4. L000 (apenas ajustes nao invasivos; preservar identidade de portal).

---

## 8) Rubrica premium de narrativa (0-5)
Avaliar cada licao:
1. Imersao sensorial (cheiro, textura, luz, som sem excesso).
2. Voz dos guardioes (consistente e memoravel).
3. Direcao para Portador (clara, aplicavel, sem ambiguidade).
4. Continuidade de jornada (gancho anterior/proxima).
5. Equilibrio (poesia + instrucoes praticas).

Meta premium: media >= 4.2.

---

## 9) Rubrica premium de matematica (0-5)
Avaliar cada licao:
1. Clareza do objetivo matematico.
2. Dominio do concreto no corpo da licao.
3. Correspondencia entre narrativa e conceito.
4. Transferencia (a crianca consegue recontar o conceito).
5. Escada espiral (prepara a proxima licao sem atropelo).

Meta premium: media >= 4.3.

---

## 10) Indicadores de produto premium (Definition of Premium)
Uma licao so pode ser "impecavel" quando:
1. 4 gates = PASS.
2. Rubrica narrativa >= 4.2.
3. Rubrica matematica >= 4.3.
4. Sem debt tecnico aberto de severidade Critica/Alta.
5. Pais conseguem aplicar sem friccao em ambiente real.

---

## 11) Modelo de saida padrao para IA (usar sempre)
Ao finalizar cada licao, a IA deve responder no formato:
1. `Findings` (prioridade + linha).
2. `Decisao` (o que padronizou e por que).
3. `Patch` (resumo tecnico objetivo).
4. `Validacao` (A/B/C/D PASS ou BLOCK).
5. `Risco residual` (se houver).
6. `Proximo passo` (acao objetiva de menor risco).

---

## 12) Backlog por rodadas (execucao recomendada)

### Rodada 1 - Higiene critica
1. L002: corrigir wrapper interno em `Sementes para o Dia`.
2. L003: remover script Phosphor duplicado.
3. L002/L003: limpar anti-patterns graves de markup.

### Rodada 2 - Padrao estrutural
1. L002: migrar para nomenclatura/estrutura canonica.
2. L003: unificar header nav com padrao L001+.
3. L003: mover Estrategia do Mestre para Formacao.

### Rodada 3 - Pedagogia premium
1. L002: reforcar ten frame no nucleo concreto.
2. L002/L003: refinar narracao para aumentar reconto e transfer.
3. Ajustar perguntas do coracao para melhorar fixacao.

### Rodada 4 - Escala
1. Criar checklist automatizavel para HTML de Sementes.
2. Rodar no lote S004+.
3. Publicar relatorios de conformidade por lote.

---

## 13) Politica de commit para esta revisao
1. Um commit por licao, quando possivel.
2. Commit separado para "documentacao/task/log".
3. Mensagem deve conter:
- licao afetada;
- tipo de ajuste (estrutura/narrativa/matematica);
- impacto esperado.

---

## 14) Nota final para IA executora
Nao otimizar para "terminar rapido". Otimizar para:
1. consistencia;
2. clareza para pais;
3. aprendizado real da crianca;
4. beleza narrativa sustentavel.

Produto premium e resultado de padrao + rigor + continuidade.
