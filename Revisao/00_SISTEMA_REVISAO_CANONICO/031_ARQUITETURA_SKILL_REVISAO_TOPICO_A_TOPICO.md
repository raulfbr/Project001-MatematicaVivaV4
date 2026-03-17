# ARQUITETURA DA SKILL - REVISAO TOPICO A TOPICO
Data: 2026-03-10
Status: proposta detalhada para aprovacao antes da implementacao
Escopo: desenhar uma skill reutilizavel para executar a revisao canonica `html-first`, por licao e topico a topico, nas paginas `MV-S-*`

---

## 1) Decisao
Sim, vale criar uma skill dedicada.

Razao central:
1. o metodo ja esta suficientemente estavel para sair do formato "prompt gigante repetido" e virar workflow reutilizavel;
2. a revisao atual depende de ordem de leitura, gates, logs, checks e veredito padronizados;
3. sem skill, cada sessao corre risco de drift metodologico, omissao de topico ou resumao apressado;
4. com skill, o agente passa a herdar o ritual correto antes de tocar no HTML.

---

## 2) O que a skill deve resolver
### Problema atual
1. o operador precisa repetir um prompt longo;
2. a IA pode esquecer parte da ordem canonica;
3. a estrutura do log pode variar entre sessoes;
4. a revisao pode escorregar para patch por impulso;
5. a consulta aos `experts` pode virar retorica solta em vez de gate real.
6. a licao pode ficar correta por fora, mas fria, pesada ou pouco redentora para a mae;
7. a narrativa pode soar bonita, mas nao realmente util para a familia na vida real.

### Resultado desejado
1. um comando curto do usuario deve ativar um fluxo longo e seguro;
2. a skill deve obrigar a leitura do curriculo mestre e do protocolo antes do patch;
3. a skill deve padronizar o log operacional da licao;
4. a skill deve manter a revisao no trilho `001-012`;
5. a skill deve produzir veredito final honesto, sem chamar de premium o que ainda esta em risco.
6. a skill deve proteger o `North Star`: aliviar o adulto, encantar a crianca e manter a matematica como descoberta e nao como peso;
7. a skill deve empurrar a escrita para um nivel mais `premium`, mais `tasteful`, mais empatico e mais imersivo sem perder funcionalidade.

---

## 3) Nome sugerido da skill
Nome tecnico sugerido:
1. `revisao-sementes-topico-a-topico`

Outras opcoes aceitaveis:
1. `revisao-canonica-sementes`
2. `html-first-revisao-por-licao`

Preferencia:
1. usar `revisao-sementes-topico-a-topico`, porque o nome ja comunica escopo, dominio e metodo.

---

## 4) Regra de ouro da skill
**A licao nao pode sair mais arrumada, porem menos verdadeira ao seu tema central.**

Essa regra deve aparecer explicitamente na skill.

Corolario:
1. a licao tambem nao pode sair mais bonita, porem mais pesada para a mae;
2. a licao nao pode soar mais literaria, porem menos usavel;
3. a licao nao pode aliviar por fora e culpar por dentro.

---

## 5) O que a skill faz
### Funcao principal
Executar uma revisao canonica, `html-first`, por licao, com patch incremental topico a topico, respeitando:
1. o curriculo mestre;
2. o protocolo canonico;
3. os contratos `011_TOPICOS/`;
4. as regras `012_TRANSVERSAIS/`;
5. os gates dos `experts`;
6. o veredito final com `PASS`, `GAP`, `BLOCK`.

### Funcao secundaria
Gerar e manter um log detalhado de revisao da licao, para:
1. rastreabilidade;
2. reabertura futura;
3. auditoria posterior;
4. validacao humana posterior.

---

## 6) O que a skill nao deve fazer
1. nao deve reescrever a licao inteira por padrao;
2. nao deve tratar outras licoes como template cego;
3. nao deve improvisar opinioes de `experts` sem ler os arquivos reais;
4. nao deve chamar de "impecavel" uma licao sem reauditoria local;
5. nao deve pular do curriculo direto para patch sem montar o cerne macro;
6. nao deve transformar a revisao em limpeza tecnica sem julgamento pedagogico e narrativo;
7. nao deve abrir commit ou push automaticamente.
8. nao deve endurecer a copy ao ponto de a mae sentir mais cobranca do que ajuda;
9. nao deve confundir "premium" com texto rebuscado ou ornamental;
10. nao deve permitir que narrativa e instrucao parecam linguagens concorrentes.

---

## 7) Quando a skill deve ser usada
### Gatilhos explicitos
1. `revise a licao 007 topico a topico`
2. `faça a revisao canonica html-first da licao 010`
3. `rode o protocolo de revisao por licao`
4. `reaudite a licao 005 com experts`
5. `revise MV-S-008 pelo contrato 001-012`

### Gatilhos implicitos
1. quando o usuario pedir revisao de uma `MV-S-*` seguindo o protocolo;
2. quando o usuario pedir verificar se uma licao esta realmente premium;
3. quando o usuario pedir reauditoria estrutural e narrativa de uma licao especifica;
4. quando o usuario pedir julgamento por `experts` aplicado ao HTML de uma licao.

### Quando nao usar
1. pedido de simples leitura sem revisao;
2. pedido de traducao, resumo ou conversa conceitual sem tocar o workflow;
3. alteracao isolada fora do escopo da revisao canonica.

---

## 8) Entradas esperadas da skill
### Entrada minima
1. numero da licao, por exemplo `007`;

### Entrada ideal
1. numero da licao;
2. eventual foco extra, por exemplo `reauditar narrativa` ou `confirmar se esta impecavel`;
3. opcionalmente, limite operacional, por exemplo `nao faça commit`.

### Assuncoes padrao
Se o usuario nao disser o contrario, a skill deve assumir:
1. revisar a licao inteira;
2. abrir licao anterior e proxima;
3. criar ou atualizar log em `logs/`;
4. nao fazer commit;
5. nao fazer push.

---

## 9) Saidas obrigatorias da skill
1. diagnostico inicial;
2. extracao explicita do tema principal a partir do curriculo mestre;
3. revisao `001-012` com status por topico;
4. log criado ou atualizado;
5. veredito final honesto;
6. lista de arquivos lidos;
7. lista de arquivos alterados;
8. riscos residuais.
9. leitura editorial final: `isso ajuda a mae ou pesa a mae?`
10. leitura narrativa final: `isso chama a crianca para dentro da historia e da matematica ao mesmo tempo?`

Formato de veredito recomendado:
1. `passou`
2. `passou com riscos`
3. `precisa de nova passada`
4. `bloqueada`

---

## 10) Ordem canonica de leitura que a skill deve impor
Antes de qualquer patch, a skill deve seguir esta ordem:

1. localizar o arquivo real da licao em `site/sementes/MV-S-XXX_*.html`;
2. localizar e abrir a licao anterior;
3. localizar e abrir a licao seguinte;
4. abrir o bloco correspondente da licao em `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md`;
5. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/000_README.md`;
6. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`;
7. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`;
8. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`;
9. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/002_REGRAS_DE_HTML_E_ANTI_PATTERNS.md`;
10. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/003_TOM_NARRATIVO_E_DIRECAO_DO_PORTADOR.md`;
11. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/005_CRITERIOS_PEDAGOGICOS_CM_CPA_TGTB.md`;
12. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/006_ENCODING_E_SANITY_CHECK.md`;
13. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`;
14. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md` quando houver criacao, reescrita profunda, imagem dominante frouxa ou duvida de ancora concreta;
15. abrir os `experts` obrigatorios definidos para a passada.

Regra:
1. a skill nao pode tocar o HTML antes de montar o cerne macro da licao.
2. a skill nao pode fechar a licao como premium sem aplicar o `North Star` como gate final.
3. se o principal problema da licao for abstracao, distancia ou ausencia de revelacao concreta, a skill deve consultar a `TX10` antes do patch narrativo.

---

## 11) Cerne macro que a skill deve extrair antes do patch
Antes de revisar qualquer topico, a skill deve registrar:
1. `TGTB ref`
2. tema principal / ideia viva
3. guardiao
4. imagem dominante
5. promessa pedagogica
6. risco de descaracterizacao
7. fronteira com a licao anterior
8. fronteira com a licao seguinte

Esse bloco deve aparecer no log antes da matriz `001-012`.

---

## 12) Workflow operacional da skill
### Fase A - Preparacao
1. localizar a licao real;
2. localizar vizinhas;
3. ler o curriculo mestre;
4. ler o protocolo base;
5. ler os transversais minimos;
6. ler os `experts`;
7. criar ou atualizar o log da licao.

### Fase B - Diagnostico inicial
1. auditar o HTML atual sem patchar ainda;
2. preencher matriz inicial `001-012`;
3. marcar cada topico como `PASS`, `GAP` ou `BLOCK`;
4. registrar anti-patterns, drift curricular, risco narrativo, risco pedagogico e risco tecnico.

### Fase C - Revisao topico a topico
Para cada topico, na ordem:
1. abrir o arquivo `.md` do topico;
2. auditar o bloco correspondente no HTML;
3. registrar findings concretos;
4. patchar apenas o necessario;
5. reauditar o topico corrigido;
6. reauditar os vizinhos imediatos;
7. registrar o que foi confirmado, tensionado e alterado.

### Fase D - Releitura integral
1. reler a licao inteira como experiencia unica;
2. validar se a pagina continua fiel ao cerne macro;
3. verificar se o patch local nao matou atmosfera, ritmo ou imagem dominante.

### Fase E - Conselho de experts
Aplicar o conselho minimo:
1. `Charlotte Mason`
2. `Jerome Bruner`
3. `Susan Macaulay`
4. `Beatrix Potter`
5. `Mae Ansiosa`
6. `Mae Veterana`
7. `Engenharia`
8. `Design`

Aplicar tambem uma sintese editorial obrigatoria:
1. `Charlotte + Susan + Mae Ansiosa`: o texto consola, orienta e respeita?
2. `Beatrix + North Star`: a imagem dominante esta viva, coerente e bela sem artificialidade?
3. `Mae Veterana + Design`: uma mae real conseguiria conduzir isso sem releitura tecnica e sem perder a paz?

### Fase F - Sanity checks
1. encoding;
2. anti-patterns;
3. links e nomes reais;
4. estrutura HTML;
5. presenca dos blocos canonicos;
6. ordem correta dos blocos.

### Fase G - Veredito
1. dizer o que ficou impecavel;
2. dizer o que ainda ficou em risco;
3. dizer se passou ou precisa de nova passada;
4. listar arquivos lidos, alterados e log gerado.
5. dizer explicitamente se a licao ficou mais leve ou mais pesada para a mae.

---

## 13) Ordem fixa dos topicos dentro da skill
1. `001_BASE_E_HERO.md`
2. `002_HEADER_SUPERIOR.md`
3. `003_PREPARACAO_DO_PORTADOR.md`
4. `004_RITUAL_DE_ENTRADA.md`
5. `005_A_JORNADA.md`
6. `006_O_CONCRETO.md`
7. `007_NARRAMOS_JUNTOS.md`
8. `008_RITUAL_DE_FECHAMENTO.md`
9. `009_CONEXAO_DA_JORNADA.md`
10. `010_SEMENTES_PARA_O_DIA.md`
11. `011_FORMACAO_DO_PORTADOR.md`
12. `012_NAVEGACAO_INFERIOR.md`

Regra:
1. a skill nao deve pular topico;
2. a skill nao deve mudar a ordem;
3. a skill nao deve fechar a licao sem revisar `010` e `011`, que sao zonas frequentes de regressao.

---

## 14) Politica de status por topico
### `PASS`
1. topico alinhado ao contrato;
2. sem risco relevante aberto;
3. sem necessidade de patch ou com patch minimo ja estabilizado.

### `GAP`
1. topico funcional, mas com perda de nitidez, fidelidade ou acabamento;
2. pode ser resolvido sem reabrir a pagina toda.

### `BLOCK`
1. topico em desacordo material com o contrato;
2. risco pedagogico, narrativo ou tecnico forte;
3. nao pode seguir para o proximo topico sem resposta.

Regra:
1. a skill nao avanca com `BLOCK` aberto.

---

## 15) Regras de patch da skill
1. patch incremental;
2. mexer apenas no necessario;
3. proteger os vizinhos do bloco tocado;
4. nao importar texto de outra licao por analogia cega;
5. nao trocar a voz do guardiao;
6. nao achatar a imagem dominante;
7. nao limpar markup a ponto de empobrecer a narrativa;
8. preferir correcao localizada antes de reescrita ampla;
9. permitir reescrita ampla apenas quando a pagina estiver em `BLOCK` estrutural de verdade.
10. quando o bloco for estrategico, priorizar clareza, fluidez e usabilidade;
11. quando o bloco for narrativo, priorizar atmosfera, imagem dominante e imersao;
12. em qualquer bloco, eliminar culpa, pressa, comparacao toxica e professoralismo;
13. tratar "premium" como combinacao de beleza, precisao, empatia e conducão suave.

---

## 16) Fronteiras que a skill deve sempre proteger
1. `preparacao -> ritual`
2. `ritual -> jornada`
3. `jornada -> o concreto`
4. `o concreto -> narramos juntos`
5. `ritual de fechamento -> conexao da jornada`
6. `conexao da jornada -> sementes para o dia`
7. `sementes para o dia -> formacao do portador`

Razao:
1. grande parte das regressões aparece nas transicoes, nao apenas dentro dos blocos.

---

## 17) Uso dos experts dentro da skill
### Regra de uso
1. a skill deve ler os arquivos reais dos `experts`;
2. a skill deve usar perguntas, vetos e gatilhos desses arquivos;
3. a skill nao deve fingir conselho de expert sem base documental.

### Funcao de cada grupo
1. `Charlotte Mason`: dignidade, narracao, licao viva, tom sem culpa;
2. `Jerome Bruner`: concreto antes do abstrato, descoberta, espiral;
3. `Susan Macaulay`: teste da casa real;
4. `Mae Ansiosa`: ansiedade e culpa;
5. `Mae Veterana`: sustentabilidade no mundo real;
6. `Beatrix Potter`: imagem dominante, atmosfera, beleza natural;
7. `Design`: calma visual, clareza em celular, hierarquia;
8. `Engenharia`: naming, links, markup, SSOT, drift.

### Mandatos editoriais que a skill deve herdar dos experts
1. de `Charlotte Mason`: a crianca deve ser tratada como pessoa capaz; a licao nao pode soar mecânica, seca ou punitiva;
2. de `Jerome Bruner`: a matematica deve ser descoberta encarnada, nao explicacao abstrata disfarcada de historia;
3. de `Susan Macaulay`: a mae leiga deve entender na primeira leitura e conseguir fazer com bebe no colo e feijao no fogo;
4. de `Mae Ansiosa`: o texto deve diminuir comparacao, culpa e panico de atraso;
5. de `Mae Veterana`: a promessa precisa soar verdadeira, sustentavel e honesta para o primeiro mes;
6. de `Beatrix Potter`: a atmosfera deve ser natural, delicada e coerente com a imagem dominante da licao;
7. de `Design`: a experiencia precisa ser usavel em casa real, inclusive em leitura corrida no celular;
8. do `North Star`: a escrita deve consolar o adulto, encantar a crianca e preservar a identidade viva do Reino.

### Politica de veto
1. `Charlotte`, `Bruner` e `Engenharia` podem gerar `BLOCK`;
2. `Susan`, `Maes`, `Beatrix` e `Design` podem gerar `WARN` duro;
3. a skill nao deve chamar de premium uma licao com `WARN` duro aberto sem explicitar o risco.
4. o `North Star` pode gerar `BLOCK` final mesmo quando a estrutura passou.

### Perguntas editoriais obrigatorias
1. isto ajuda a mae a conduzir com mais paz ou a deixa mais pressionada?
2. a crianca esta sendo convidada para uma descoberta ou apenas conduzida por instrucoes?
3. a narrativa e as instrucoes parecem partes do mesmo produto?
4. a licao continua reconhecivelmente Matematica Viva?
5. ha beleza redentora ou apenas acabamento bonito?

---

## 18) Estrutura documental minima da skill
### Obrigatorio
1. `SKILL.md`

### Recomendado
1. `references/fluxo-canonico.md`
2. `references/matriz-topicos.md`
3. `references/formato-log.md`
4. `references/checklist-veredito.md`

### Opcional na versao 1
1. `scripts/bootstrap_review_log.ps1`
2. `scripts/run_review_sanity.ps1`

Decisao recomendada:
1. comecar sem scripts;
2. criar primeiro uma skill procedural forte;
3. so adicionar scripts depois que o metodo textual estiver aprovado.

---

## 19) Formato ideal do `SKILL.md`
O `SKILL.md` da skill deve ser curto, firme e operacional.

Estrutura sugerida:
1. objetivo da skill;
2. quando usar;
3. entradas esperadas;
4. ordem obrigatoria de leitura;
5. montagem do cerne macro;
6. execucao `001-012`;
7. uso dos `experts`;
8. sanity checks;
9. formato do log;
10. formato da resposta final;
11. limites e proibicoes.

Regra:
1. o `SKILL.md` deve apontar para referencias locais, em vez de repetir tudo longamente.

---

## 20) Formato ideal do log produzido pela skill
Nome sugerido:
1. `logs/YYYY-MM-DD_REVISAO_LXXX_TOPICO_A_TOPICO.md`

Secoes obrigatorias:
1. cabecalho da revisao;
2. cerne macro;
3. fronteiras curriculares;
4. matriz inicial `001-012`;
5. revisao topico a topico;
6. conselho de `experts`;
7. sanity checks;
8. veredito final;
9. proximos passos.
10. leitura `North Star`;
11. nota editorial sobre peso percebido pela mae.

---

## 21) Sanity checks que a skill deve sempre rodar
1. buscar residuos legados como `Ritual de Abertura`, `Atividade Concreta`, `Para a Familia`, `[Foco:]`, `div onclick`;
2. buscar sinais comuns de encoding quebrado;
3. verificar nomes reais de arquivos nos `href`;
4. verificar presenca dos blocos canonicos;
5. verificar ordem dos blocos;
6. fazer ao menos uma checagem estrutural minima do HTML;
7. confirmar que `Conexao da Jornada` usa link semantico;
8. confirmar separacao entre `Sementes para o Dia` e `Formacao do Portador`.
9. confirmar que nao ha linguagem de medo, culpa, comparacao ou peso desnecessario;
10. confirmar que narrativa e instrucao mantem uma voz compatível;
11. confirmar que a imagem dominante da licao nao se perdeu no meio do patch.

---

## 22) Riscos de uma skill mal desenhada
1. virar prompt empacotado sem forca real de governanca;
2. reforcar padronizacao cega entre licoes;
3. incentivar reescrita total por conveniencia;
4. reduzir o papel dos `experts` a floreio retorico;
5. esconder conflitos reais entre curriculo, HTML e protocolo.
6. produzir licoes corretas, mas emocionalmente pesadas;
7. trocar imersao por enfeite e empatia por infantilizacao;
8. chamar de `premium` algo que esta apenas polido.

---

## 23) Recomendacao de implementacao em duas fases
### Fase 1 - Skill textual
Entregar:
1. `SKILL.md`
2. referencias minimas
3. gatilhos e workflow completos

Objetivo:
1. validar se a skill conduz revisoes boas de verdade.

### Fase 2 - Automacao leve
Entregar, se fizer sentido:
1. script de bootstrap de log;
2. script de sanity checks;
3. template de saida final.

Objetivo:
1. ganhar velocidade sem perder criterio.

---

## 24) Veredito desta proposta
Criar a skill e uma boa decisao, desde que:
1. ela seja uma skill de metodo, nao de texto pronto;
2. ela proteja o cerne curricular antes do patch;
3. ela imponha o trilho `001-012`;
4. ela trate `experts` como gate real;
5. ela produza log e veredito rastreaveis.
6. ela trate o `North Star` como gate editorial e espiritual final;
7. ela empurre cada revisao para uma escrita mais calma, mais bela, mais usavel e mais redentora para a familia;
8. ela ajude a tirar peso da matematica, nao colocar mais peso.

Proximo passo recomendado:
1. aprovar esta arquitetura;
2. implementar a versao 1 da skill com `SKILL.md` + referencias, sem scripts;
3. testar a skill em uma licao real antes de expandir automacao.
