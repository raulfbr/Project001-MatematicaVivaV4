# README REVISAO - Fase de Revisão Premium

Este arquivo é o ponto de entrada da fase de revisão.

## Ordem de Leitura (obrigatória)
1. `README.md` (visão geral e contexto do projeto).
2. `Revisao/RadmeRevisao.md` (este arquivo).
3. `Revisao/TASK_ROBUSTA_SISTEMA_REVISAO_HTML_FIRST.md` (decisão de escopo e arquitetura do sistema).
4. `Revisao/ESQUELETO_GERAL_LICAO_SEMENTES.md` (contrato canônico da lição padrão).
5. `Revisao/PROTOCOLO_REVISAO_POR_LICAO.md` (fluxo operacional de revisão).
6. `Revisao/RUBRICA_PREMIUM_REVISAO.md` (PASS/BLOCK e nota premium).
7. `Revisao/transversais/TX08_NORTH_STAR_OPERACIONAL.md` (tradução operacional do North Star para a revisão).
8. `Revisao/STATUS_REVISAO_SEMENTES.md` (quadro de bordo).
9. `Revisao/padrao_visual_sementes.md` (fonte principal de padrão visual).
10. `Revisao/topicos_licao_revisao.md` (referência histórica/checklist legado).
11. `Revisao/framework_estrategia_mestria.md` (estratégia narrativa/pedagógica premium).
12. `Revisao/TASK_ROBUSTA_PILOTO_001_003.md` (plano detalhado de validação antes de tocar nas lições).
13. `Revisao/TEMPLATE_RELATORIO_PILOTO_001_003.md` (molde do diagnóstico do piloto).

## SSOT da Revisão
1. `ESQUELETO_GERAL_LICAO_SEMENTES.md` = contrato macro da lição padrão.
2. `PROTOCOLO_REVISAO_POR_LICAO.md` = ordem oficial da revisão.
3. `RUBRICA_PREMIUM_REVISAO.md` = critério de PASS/BLOCK.
4. `TX08_NORTH_STAR_OPERACIONAL.md` = filtro de fidelidade ao espírito da obra.
5. `padrao_visual_sementes.md` = padrão visual/estrutural detalhado.
6. `framework_estrategia_mestria.md` = profundidade narrativa e intenção pedagógica.
7. `topicos_licao_revisao.md` = apoio legado; não é mais a fonte primária.

## Objetivo da Fase Atual
1. Padronizar lições no nível premium (estrutura + narrativa + pedagogia).
2. Garantir progressão clara da revisão (sem retrabalho circular).
3. Fechar cada lição com evidência objetiva de PASS/FAIL.

## Regra Crítica (Encoding)
Para não quebrar textos HTML/YAML/MD:

1. Salvar sempre em UTF-8.
2. Não converter encoding durante edição.
3. Após mudanças em lições HTML, rodar sanity check:
`rg -n "Ã|Â|â|\\b\\w+\\?\\w+\\b" site/sementes/MV-S-00[1-3]*.html`
4. Qualquer ocorrência deve ser corrigida antes de encerrar.

## Estado Atual da Revisão
1. L001-L003 seguem como lote piloto oficial para validar o novo sistema.
2. O sistema canônico de revisão HTML-first foi estruturado com arquivos centrais, `topicos/`, `transversais/` e gate explícito de North Star.
3. O piloto `001-003` já tem task própria e template de relatório.
4. Próximo ciclo: validar o sistema no piloto e então entrar em cadência.

## Próxima Sessão (anotado)
Vamos executar a estratégia que você definiu:

1. Aplicar o sistema em `MV-S-001`, `MV-S-002` e `MV-S-003`.
2. Registrar findings reais de cobertura dos guias por tópico.
3. Registrar PASS/BLOCK de North Star por lição.
4. Ajustar qualquer ambiguidade do sistema antes da escala.
5. Iniciar lote `004-006` se o piloto ficar verde.

Arquivos de apoio já criados:
1. `Revisao/TASK_ROBUSTA_SISTEMA_REVISAO_HTML_FIRST.md`
2. `Revisao/ESQUELETO_GERAL_LICAO_SEMENTES.md`
3. `Revisao/PROTOCOLO_REVISAO_POR_LICAO.md`
4. `Revisao/RUBRICA_PREMIUM_REVISAO.md`
5. `Revisao/STATUS_REVISAO_SEMENTES.md`

## Arquivos Históricos
Conteúdos antigos/contextuais estão em:
`logs/Outros/Revisao_Legado/`
