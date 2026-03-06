# TASK ROBUSTA - SISTEMA CANONICO DE REVISAO HTML-FIRST
Data: 2026-03-06 (America/Sao_Paulo)
Base imediata: `Revisao/99_HISTORICO_E_TRANSICAO/ESQUELETO_GERAL_PLANO_PROXIMA_SESSAO.md`
Escopo operacional: `site/sementes/MV-S-000..025`
Prioridade: critica
Status: planejamento estruturado; pronto para piloto

---

## Progresso desta sessao
Executado:
1. `002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
2. `003_PROTOCOLO_REVISAO_POR_LICAO.md`
3. `004_RUBRICA_PREMIUM_REVISAO.md`
4. `005_STATUS_REVISAO_SEMENTES.md`
5. pasta `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/` com 12 guias
6. pasta `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/` com 8 regras

Estado resultante:
1. a fase de planejamento deixou de ser conceitual;
2. o sistema de revisao ja pode ser testado no piloto `001-003`.

---

## 0) Decisao oficial desta fase
1. Congelar a frente `Next/V5` como trabalho de fase futura.
2. Tratar os HTMLs publicados em `site/sementes/` como produto operacional atual.
3. Focar a energia da equipe em revisao premium das licoes iniciais, porque ja existem familias usando o material.
4. Nao revisar em massa antes de fechar um sistema de revisao canonico, modular e reutilizavel.
5. Tratar `MV-S-000` como excecao oficial de Portal.
6. Tratar `MV-S-001+` como licao padrao do ciclo Sementes.

Racional:
1. O gargalo real agora nao e tecnologia nova; e consistencia editorial, estrutural e pedagogica no HTML que ja esta em uso.
2. Sem sistema canonico, revisar 2 licoes por dia vai gerar drift, retrabalho e contradicoes entre IA e humano.

---

## 1) Contexto operacional real
1. Ja existem pelo menos 3 familias usando o material.
2. Elas ja passaram da licao 001.
3. As licoes iniciais precisam de revisao urgente e confiavel.
4. A meta de throughput desejada e `2 licoes por dia`, mas isso so e seguro depois que o metodo de revisao estiver fechado.
5. O sistema atual de revisao ja tem conteudo forte, mas ainda nao tem forma modular suficiente para escala diaria.

---

## 2) Problema real que esta task resolve
Hoje o conhecimento esta espalhado, misturado e parcialmente ambiguo:

1. `Revisao/01_REFERENCIAS_DE_APOIO/padrao_visual_sementes.md` esta forte, mas concentra contrato estrutural, regras de escrita, iconografia, anti-patterns e filosofia em um unico documento.
2. `Revisao/01_REFERENCIAS_DE_APOIO/topicos_licao_revisao.md` ainda preserva exemplos legados e trechos que conflitam com o padrao alvo.
3. `Revisao/99_HISTORICO_E_TRANSICAO/ESQUELETO_GERAL_PLANO_PROXIMA_SESSAO.md` define a intencao, mas ainda nao define o sistema operacional final.
4. Os HTMLs reais 000-025 mostram padroes importantes que ainda nao foram totalmente promovidos a contrato documental.
5. A IA ainda nao tem um arquivo por topico com instrucao clara sobre:
   - o que precisa existir tecnicamente;
   - o que precisa existir narrativamente;
   - o que caracteriza PASS/FAIL;
   - como escrever em nivel premium.
6. Ainda nao havia um protocolo diario de revisao que permitisse executar rapido sem reabrir todo o contexto do projeto.

Consequencia antes desta rodada:
1. Cada nova sessao de revisao precisa "reaprender" o sistema.
2. A tendencia natural e misturar correcoes estruturais, narrativas, pedagogicas e visuais sem ordem clara.
3. Isso reduz velocidade e aumenta o risco de incoerencia entre licoes.

---

## 3) Gaps confirmados agora
Gaps observados nos documentos e HTMLs reais:

1. `Conexao da Jornada` aparece nos HTMLs publicados 000-025 e no template legado, mas nao esta incluida no contrato `T0-T9` atual de `padrao_visual_sementes.md`.
2. `Momento de Conexao` e o nome alvo, mas a maior parte do acervo ainda usa `O Concreto` / `Atividade Concreta`.
3. `Hero`, `head`, `body`, `home button` e container geral existem de fato nas licoes, mas ainda nao estao tratados como uma camada documental propria no plano por topicos.
4. Existem regras transversais demais para ficarem embutidas em arquivos de topico:
   - icones e paleta;
   - cards e reveal de local/guardiao;
   - voz do Portador;
   - qualidade pedagogica;
   - encoding/sanity check;
   - anti-patterns de HTML.

Interpretacao pratica:
1. Antes de criar 1 arquivo por topico, precisamos fechar a arquitetura do sistema documental.
2. O sistema precisa separar `estrutura`, `topicos` e `regras transversais`.

---

## 4) Decisoes canonicas propostas por esta task
Estas decisoes existem para reduzir ambiguidade antes da execucao:

### 4.1 Camadas do sistema de revisao
1. Camada A - `Base da pagina`: estrutura geral do HTML.
2. Camada B - `Topicos da licao`: fluxo da experiencia da licao.
3. Camada C - `Regras transversais`: regras que atravessam varios topicos.
4. Camada D - `Protocolo operacional`: como revisar uma licao do inicio ao fim.

### 4.2 Contrato da licao padrao
Para `MV-S-001+`, a estrutura canonica proposta passa a ser:

1. Base do Documento (`head`, `body`, `home-btn`, `lesson-container`)
2. Hero
3. Header Superior Canonico
4. Preparacao do Portador
5. Ritual de Entrada
6. A Jornada
7. Momento de Conexao
8. Narramos Juntos
9. Ritual de Fechamento
10. Conexao da Jornada
11. Sementes para o Dia
12. Formacao do Portador
13. Navegacao Inferior

### 4.3 Regras de nomenclatura
1. Nome alvo da secao: `Momento de Conexao`.
2. Alias temporario aceitavel no acervo atual: `O Concreto` / `Atividade Concreta`.
3. `Conexao da Jornada` volta a ser tratada como secao canonica, nao como detalhe opcional.
4. `MV-S-000` tera arquivo de excecao propria e nao deve ditar sozinha a regra da licao padrao.

### 4.4 Estrategia de migracao editorial
1. Primeiro documentar o sistema.
2. Depois rodar piloto pequeno.
3. So entao escalar para 2 licoes por dia.
4. Renomes globais e limpezas amplas so entram depois que o protocolo estiver validado.

---

## 5) Fontes obrigatorias (ordem de leitura)
Para construir e usar o sistema:

1. `README.md`
2. `Revisao/RadmeRevisao.md`
3. `Revisao/01_REFERENCIAS_DE_APOIO/padrao_visual_sementes.md`
4. `Revisao/01_REFERENCIAS_DE_APOIO/topicos_licao_revisao.md`
5. `Revisao/01_REFERENCIAS_DE_APOIO/framework_estrategia_mestria.md`
6. `Revisao/99_HISTORICO_E_TRANSICAO/ESQUELETO_GERAL_PLANO_PROXIMA_SESSAO.md`
7. `site/sementes/MV-S-000_O_PORTAL_DO_REINO.html`
8. `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html`
9. `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`
10. `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html`
11. `site/sementes/style.css`
12. `site/sementes/lab_icones.html`

Se houver conflito:
1. HTML publicado vence exemplos desatualizados.
2. `padrao_visual_sementes.md` vence `topicos_licao_revisao.md`.
3. O novo `ESQUELETO_GERAL` canonico, quando criado, passara a vencer exemplos legados.
4. Regras transversais novas nao podem contradizer HTML real sem justificativa explicita.

---

## 6) Entregaveis canonicos desta fase
Esta task so estara concluida quando existirem os seguintes ativos:

1. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
5. Pasta `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/`
6. Pasta `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/`
7. Arquivo de excecao `MV-S-000`

---

## 7) Arquitetura documental alvo

### 7.1 Arquivos centrais
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
   - ordem final da licao padrao;
   - obrigatorio vs recomendado vs legado;
   - definicao curta de cada bloco;
   - relacao entre blocos;
   - mapa de leitura da pasta `Revisao`.

2. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
   - fluxo executavel para revisar 1 licao;
   - checklist pre-flight;
   - ordem dos gates;
   - validacao final;
   - formato de log.

3. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
   - score estrutural;
   - score narrativo;
   - score pedagogico;
   - score de UX para Portador;
   - criterio PASS/BLOCK.

4. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
   - quadro de bordo do lote;
   - qual licao esta pronta, bloqueada ou em revisao;
   - backlog e prioridade real.

### 7.2 Pasta de topicos
Proposta de arquivos:

1. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/001_BASE_E_HERO.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/002_HEADER_SUPERIOR.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/003_PREPARACAO_DO_PORTADOR.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/004_RITUAL_DE_ENTRADA.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/005_A_JORNADA.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/006_MOMENTO_DE_CONEXAO.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/007_NARRAMOS_JUNTOS.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/008_RITUAL_DE_FECHAMENTO.md`
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/009_CONEXAO_DA_JORNADA.md`
10. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/010_SEMENTES_PARA_O_DIA.md`
11. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/011_FORMACAO_DO_PORTADOR.md`
12. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/012_NAVEGACAO_INFERIOR.md`

### 7.3 Pasta de regras transversais
Proposta de arquivos:

1. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/001_ICONES_CORES_E_ASSETS.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/002_REGRAS_DE_HTML_E_ANTI_PATTERNS.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/003_TOM_NARRATIVO_E_DIRECAO_DO_PORTADOR.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/004_GUARDIOES_CARDS_E_REVEAL.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/005_CRITERIOS_PEDAGOGICOS_CM_CPA_TGTB.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/006_ENCODING_E_SANITY_CHECK.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/007_EXCECAO_L000_PORTAL.md`

---

## 8) Contrato obrigatorio de cada arquivo de topico
Cada arquivo em `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/` deve seguir a mesma anatomia:

1. Missao do topico
   - o que esta secao faz dentro da experiencia da licao.

2. Posicao no fluxo
   - o que vem antes;
   - o que vem depois;
   - que transicao precisa acontecer.

3. Contrato tecnico
   - tags HTML esperadas;
   - classes obrigatorias;
   - icones canonicos;
   - assets esperados;
   - regras mobile-first;
   - erros tecnicos proibidos.

4. Contrato narrativo
   - tom da escrita;
   - papel do Portador;
   - papel do Guardiao;
   - nivel de imersao desejado;
   - tipo de frase que funciona;
   - tipo de frase que degrada o premium.

5. Contrato pedagogico
   - objetivo da secao;
   - relacao com CPA;
   - relacao com narracao;
   - o que a crianca deve viver, nao apenas ouvir.

6. Anti-patterns
   - exemplos do que reprova;
   - fragmentacao indevida;
   - repeticao;
   - quebra de reveal;
   - imperativo duro;
   - texto burocratico.

7. PASS estrutural e BLOCK estrutural
   - criterio objetivo do que aprova ou reprova a secao.

8. Ambiguidades resolvidas
   - decisoes que nao devem ser reabertas sem motivo forte.

9. Prompt operacional para IA
   - instrucoes curtas para revisar ou reescrever so aquele topico sem contaminar o resto.

---

## 9) Contrato obrigatorio dos arquivos transversais
Cada arquivo em `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/` deve resolver uma familia de decisoes que afeta varios topicos.

Regras:
1. Nao repetir o conteudo completo dentro de cada topico.
2. Cada topico deve apontar para as transversais relevantes.
3. O objetivo e reduzir contexto e acelerar a revisao.

Estrutura minima de cada transversal:
1. Quando consultar este arquivo
2. Regra canonica
3. Casos de PASS
4. Casos de FAIL
5. Impacto no premium
6. Observacoes de migracao do legado

---

## 10) Fases de execucao recomendadas

### Fase 1 - Canonizacao do sistema
Objetivo:
1. fechar a estrutura alvo da licao padrao;
2. resolver conflitos documentais antes da fragmentacao.

Entregas:
1. decidir definitivamente:
   - `Conexao da Jornada` = obrigatoria;
   - `Momento de Conexao` = nome alvo;
   - `O Concreto` = alias legado;
   - `MV-S-000` = excecao.
2. definir o indice final dos arquivos.

Criterio de saida:
1. zero ambiguidade sobre quais secoes compoem a licao padrao.

### Fase 2 - Criacao dos arquivos centrais
Objetivo:
1. criar o esqueleto geral;
2. criar o protocolo por licao;
3. criar a rubrica premium;
4. criar o quadro de status do lote.

Criterio de saida:
1. uma IA consegue entender o fluxo geral sem abrir os HTMLs.

### Fase 3 - Criacao das transversais
Objetivo:
1. retirar do documento principal tudo o que e regra compartilhada;
2. deixar o esqueleto limpo e navegavel.

Criterio de saida:
1. cada topico consegue apontar para as transversais certas sem duplicar conhecimento.

### Fase 4 - Criacao dos arquivos por topico
Objetivo:
1. transformar cada secao da licao em unidade de revisao autonoma.

Prioridade de criacao:
1. `001_BASE_E_HERO`
2. `002_HEADER_SUPERIOR`
3. `003_PREPARACAO_DO_PORTADOR`
4. `004_RITUAL_DE_ENTRADA`
5. `005_A_JORNADA`
6. `006_MOMENTO_DE_CONEXAO`
7. `007_NARRAMOS_JUNTOS`
8. `008_RITUAL_DE_FECHAMENTO`
9. `011_FORMACAO_DO_PORTADOR`
10. `009_CONEXAO_DA_JORNADA`
11. `010_SEMENTES_PARA_O_DIA`
12. `012_NAVEGACAO_INFERIOR`

Racional:
1. primeiro fechar shell, entrada e nucleo da experiencia;
2. depois fechamento, formacao e extensoes.

### Fase 5 - Piloto de validacao
Objetivo:
1. testar o sistema documental em licoes reais;
2. identificar lacunas antes da escala.

Lote piloto:
1. `MV-S-001`
2. `MV-S-002`
3. `MV-S-003`

O que validar:
1. se os topicos cobrem o HTML real;
2. se a IA consegue revisar sem reabrir todo o projeto;
3. se os criterios PASS/FAIL estao objetivos;
4. se a escrita premium melhora de forma consistente.

### Fase 6 - Cadencia de producao
Objetivo:
1. entrar em ritmo de revisao diaria sem perder qualidade.

Cadencia alvo:
1. `2 licoes por dia`

Ordem sugerida:
1. Dia 1 de producao: `001 + 002`
2. Dia 2 de producao: `003 + 004`
3. Dia 3 de producao: `005 + 006`
4. Dia 4 de producao: `007 + 008`
5. Dia 5 de producao: `009 + 010`

Regra:
1. so avancar para a cadencia `2/dia` depois que o piloto estiver verde.

---

## 11) Protocolo diario de revisao (proposta operacional)
Cada licao deve passar por 5 passos, nesta ordem:

1. Pre-auditoria estrutural
   - abrir licao atual, anterior e proxima;
   - abrir esqueleto geral;
   - abrir os topicos relevantes;
   - marcar faltas ou conflitos.

2. Patch estrutural
   - corrigir ordem das secoes;
   - corrigir header/nav;
   - corrigir classes, icons, cards, labels;
   - remover quebra estrutural evidente.

3. Patch narrativo e pedagogico
   - refinar tom;
   - reforcar imersao;
   - limpar imperativos secos;
   - reforcar concreto e reconto.

4. Validacao final
   - PASS/FAIL estrutural;
   - PASS/FAIL narrativo;
   - PASS/FAIL pedagogico;
   - PASS/FAIL navegacao;
   - sanity check de encoding.

5. Registro
   - salvar log da licao;
   - atualizar quadro `STATUS_REVISAO_SEMENTES`.

---

## 12) Definition of Ready para revisar uma licao
Uma licao so entra em revisao quando:

1. o esqueleto geral estiver disponivel;
2. os topicos da licao estiverem documentados;
3. a licao anterior e a proxima estiverem acessiveis;
4. o protocolo de revisao estiver definido;
5. o criterio PASS/FAIL estiver claro;
6. o sanity check de encoding estiver lembrado.

---

## 13) Definition of Done por licao
Uma licao so pode ser marcada como pronta quando:

1. todas as secoes obrigatorias estiverem presentes;
2. a ordem da experiencia estiver correta;
3. a navegacao anterior/proxima estiver correta;
4. o texto estiver em tom premium, imersivo e digno;
5. o concreto estiver claro e aplicavel;
6. a Formacao do Portador estiver forte e limpa;
7. nao houver erro estrutural critico;
8. nao houver encoding quebrado;
9. houver log de fechamento com risco residual explicito.

---

## 14) Rubrica minima de qualidade premium
Proposta de eixos:

1. Estrutura (0-5)
   - ordem correta;
   - secoes presentes;
   - classes e icones coerentes;
   - navegacao valida.

2. Narrativa (0-5)
   - imersao;
   - voz do Portador;
   - voz do Guardiao;
   - ritmo;
   - continuidade.

3. Pedagogia (0-5)
   - concreto real;
   - narracao significativa;
   - respeito a crianca;
   - aplicabilidade em casa;
   - espiral.

4. UX do Portador (0-5)
   - clareza;
   - leveza;
   - tempo realista;
   - texto escaneavel;
   - instrucoes acionaveis.

Meta:
1. nenhuma licao fecha com nota baixa em estrutura;
2. nenhuma licao fecha com tom burocratico ou seco;
3. nenhuma licao fecha com concreto fraco.

---

## 15) Regras de escopo: o que nao fazer agora
Para proteger foco e velocidade, esta fase nao deve:

1. retomar migracao para Next;
2. redesenhar o pipeline V5;
3. fazer refactor grande de CSS sem necessidade de revisao;
4. reescrever 25 licoes de uma vez;
5. fazer busca-e-substituicao global sem piloto validado;
6. misturar de novo HTML, YAML e pipeline na mesma sessao sem motivo claro.

---

## 16) Riscos principais e mitigacao
1. Risco: criar documentacao bonita, mas lenta demais para usar.
   - Mitigacao: cada topico precisa ter checklist objetivo e prompt curto para IA.

2. Risco: documentar teoria que nao bate com HTML real.
   - Mitigacao: sempre validar 001-003 no piloto antes de escalar.

3. Risco: cair em refactor estrutural demais e perder urgencia das familias.
   - Mitigacao: separar claramente `sistema de revisao` de `revisao das licoes`.

4. Risco: abrir ambiguidade entre `O Concreto` e `Momento de Conexao`.
   - Mitigacao: nome alvo fixado + alias legado aceito temporariamente.

5. Risco: esquecer a excecao de `MV-S-000`.
   - Mitigacao: criar arquivo transversal proprio de excecao.

---

## 17) Modelo de saida esperado da IA ao revisar uma licao
Ao finalizar uma licao, a IA deve responder em formato consistente:

1. Findings
   - criticos;
   - altos;
   - medios.

2. Decisoes
   - o que foi padronizado;
   - o que foi preservado;
   - o que ficou como legado aceito.

3. Patch
   - resumo tecnico;
   - resumo narrativo;
   - resumo pedagogico.

4. Validacao
   - Estrutura: PASS/BLOCK
   - Narrativa: PASS/BLOCK
   - Pedagogia: PASS/BLOCK
   - Navegacao: PASS/BLOCK
   - Encoding: PASS/BLOCK

5. Risco residual
   - se houver.

6. Proximo passo
   - acao objetiva e pequena.

---

## 18) Ordem recomendada de implementacao desta task
Para nao abrir varias frentes ao mesmo tempo:

1. Criar `002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
2. Criar `003_PROTOCOLO_REVISAO_POR_LICAO.md`
3. Criar `004_RUBRICA_PREMIUM_REVISAO.md`
4. Criar `005_STATUS_REVISAO_SEMENTES.md`
5. Criar pasta `transversais/`
6. Criar pasta `topicos/`
7. Criar `007_EXCECAO_L000_PORTAL.md`
8. Criar `001_BASE_E_HERO.md`
9. Criar `002_HEADER_SUPERIOR.md`
10. Criar `003_PREPARACAO_DO_PORTADOR.md`
11. Criar `004_RITUAL_DE_ENTRADA.md`
12. Criar `005_A_JORNADA.md`
13. Criar `006_MOMENTO_DE_CONEXAO.md`
14. Criar `007_NARRAMOS_JUNTOS.md`
15. Criar `008_RITUAL_DE_FECHAMENTO.md`
16. Criar `009_CONEXAO_DA_JORNADA.md`
17. Criar `010_SEMENTES_PARA_O_DIA.md`
18. Criar `011_FORMACAO_DO_PORTADOR.md`
19. Criar `012_NAVEGACAO_INFERIOR.md`
20. Rodar piloto em `001-003`
21. Ajustar sistema
22. Entrar em cadencia `2/dia`

---

## 19) Criterio de aceite final desta task
Esta task so podera ser considerada concluida quando:

1. o sistema de revisao estiver modularizado;
2. existir um esqueleto geral canonico;
3. existir um arquivo por topico;
4. existirem regras transversais separadas;
5. existir um protocolo claro por licao;
6. existir um quadro de status do lote;
7. o sistema tiver sido validado no piloto `001-003`;
8. a equipe puder revisar licoes sem depender de memoria difusa do projeto.

---

## 20) Proximo movimento recomendado
Nao sair revisando licoes ainda.

Proximo passo correto:
1. criar o `002_ESQUELETO_GERAL_LICAO_SEMENTES.md` ja com as decisoes acima;
2. em seguida criar `003_PROTOCOLO_REVISAO_POR_LICAO.md`;
3. depois montar os arquivos transversais e os topicos.

Sequencia certa:
1. fechar o metodo;
2. validar o metodo;
3. escalar a revisao.
