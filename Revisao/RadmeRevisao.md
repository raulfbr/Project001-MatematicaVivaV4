# README REVISAO - Fase de Revisao Premium

Este arquivo e o ponto de entrada da fase de revisao.

## Navegacao da Pasta
1. `Revisao/000_COMECAR_AQUI.md` = entrada curta para leitura humana.
2. `Revisao/001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md` = handoff detalhado da proxima sessao.
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md` = leitura profunda de onde o projeto esta de verdade.
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/` = sistema oficial numerado.
5. `Revisao/01_REFERENCIAS_DE_APOIO/` = apoio visual, narrativo e legado.
6. `Revisao/99_HISTORICO_E_TRANSICAO/` = materiais de origem e transicao.

## Ordem de Leitura (obrigatoria)
1. `README.md` (visao geral e contexto do projeto).
2. `Revisao/RadmeRevisao.md` (este arquivo).
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md` (estado real do projeto, frente ativa e limites da trilha tecnica paralela).
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/000_INDEX_SISTEMA_REVISAO.md` (mapa curto de navegacao do sistema).
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/001_TASK_ROBUSTA_SISTEMA_REVISAO_HTML_FIRST.md` (decisao de escopo e arquitetura do sistema).
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md` (contrato canonico da licao padrao).
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md` (fluxo operacional de revisao).
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md` (PASS/BLOCK e nota premium).
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md` (traducao operacional do North Star para a revisao).
10. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md` (quadro de bordo).
11. `Revisao/01_REFERENCIAS_DE_APOIO/padrao_visual_sementes.md` (fonte principal de padrao visual).
12. `Revisao/01_REFERENCIAS_DE_APOIO/topicos_licao_revisao.md` (referencia historica/checklist legado).
13. `Revisao/01_REFERENCIAS_DE_APOIO/framework_estrategia_mestria.md` (estrategia narrativa e pedagogica premium).
14. `Revisao/00_SISTEMA_REVISAO_CANONICO/007_TASK_ROBUSTA_PILOTO_001_003.md` (plano detalhado de validacao antes de tocar nas licoes).
15. `Revisao/00_SISTEMA_REVISAO_CANONICO/008_TEMPLATE_RELATORIO_PILOTO_001_003.md` (molde do diagnostico do piloto).
16. `Revisao/00_SISTEMA_REVISAO_CANONICO/009_TASK_ROBUSTA_CADENCIA_2_LICOES_DIA.md` (governanca operacional da cadencia).
17. `Revisao/00_SISTEMA_REVISAO_CANONICO/010_TEMPLATE_SESSAO_DIARIA_REVISAO.md` (template de sessao e handoff).

## SSOT da Revisao
1. `002_ESQUELETO_GERAL_LICAO_SEMENTES.md` = contrato macro da licao padrao.
2. `003_PROTOCOLO_REVISAO_POR_LICAO.md` = ordem oficial da revisao.
3. `004_RUBRICA_PREMIUM_REVISAO.md` = criterio de PASS/BLOCK.
4. `008_NORTH_STAR_OPERACIONAL.md` = filtro de fidelidade ao espirito da obra.
5. `015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md` = leitura canonica do momento real do projeto.
6. `01_REFERENCIAS_DE_APOIO/padrao_visual_sementes.md` = padrao visual e estrutural detalhado.
7. `01_REFERENCIAS_DE_APOIO/framework_estrategia_mestria.md` = profundidade narrativa e intencao pedagogica.
8. `01_REFERENCIAS_DE_APOIO/topicos_licao_revisao.md` = apoio legado; nao e mais a fonte primaria.

## Objetivo da Fase Atual
1. padronizar licoes no nivel premium (estrutura + narrativa + pedagogia);
2. garantir progressao clara da revisao (sem retrabalho circular);
3. fechar cada licao com evidencia objetiva de PASS/FAIL.

## Regra Critica (Encoding)
Para nao quebrar textos HTML/YAML/MD:

1. salvar sempre em UTF-8;
2. nao converter encoding durante edicao;
3. apos mudancas em licoes HTML, rodar sanity check:
`rg -n "Ãƒ|Ã‚|Ã¢|\\b\\w+\\?\\w+\\b" site/sementes/MV-S-00[1-3]*.html`
4. qualquer ocorrencia deve ser corrigida antes de encerrar.

## Estado Atual da Revisao
1. L001-L003 seguem como lote piloto oficial para validar o novo sistema.
2. O sistema canonico de revisao HTML-first foi estruturado com arquivos centrais, `topicos/`, `transversais/` e gate explicito de North Star.
3. O piloto `001-003` ja tem task propria e template de relatorio.
4. A cadencia `2/dia` ja tem task e template proprios, mas continua bloqueada ate o piloto ficar verde.
5. O documento `015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md` agora consolida a leitura profunda do projeto e da fase ativa.
6. Proximo ciclo: validar o sistema no piloto e entao entrar em cadencia.

## Proxima Sessao (anotado)
Vamos executar a estrategia que voce definiu:

1. aplicar o sistema em `MV-S-001`, `MV-S-002` e `MV-S-003`;
2. registrar findings reais de cobertura dos guias por topico;
3. registrar PASS/BLOCK de North Star por licao;
4. ajustar qualquer ambiguidade do sistema antes da escala;
5. iniciar lote `004-006` se o piloto ficar verde.

Arquivos de apoio ja criados:
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/001_TASK_ROBUSTA_SISTEMA_REVISAO_HTML_FIRST.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md`

## Arquivos Historicos
Conteudos antigos e contextuais estao em:
`logs/Outros/Revisao_Legado/`
