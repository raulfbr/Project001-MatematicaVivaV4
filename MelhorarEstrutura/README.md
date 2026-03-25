# MelhorarEstrutura

Esta pasta guarda um nucleo inicial de discussao sobre como melhorar a estrutura de revisao das licoes sem mexer ainda no runtime, no deploy ou no pipeline principal.

## Ponto de entrada rapido

Se voce quiser entender esta pasta com o minimo de atrito, comece por:

1. `ENTENDA_MELHORAR_ESTRUTURA.md`
2. `TASK_ROBUSTA_EXECUCAO_FASEADA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`
3. `TASK_ROBUSTA_CONVERGENCIA_SUGESTAO_SEMENTES.md`
4. `TASK_ROBUSTA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`
5. `discussoes/2026-03-19_2228_FLUXO_EDITORIAL_SEMENTES.md`

O recorte desta fase e deliberadamente pequeno:

- discutir, nao implementar
- usar linguagem BMAD em YAML
- funcionar como satelite do BMAD atual, sem alterar `bmad/`
- manter Vercel como default inicial
- atacar a dor real de revisao de licoes longas

Pergunta central:

Como tornar a revisao de licoes escalavel sem depender de HTML longo, mantendo Vercel como base inicial e preservando a continuidade curricular?

Estado atual reconhecido:

Hoje a revisao operacional real ainda acontece diretamente no HTML. Esta pasta nao nega isso; ela existe justamente para discutir se devemos continuar assim ou criar uma estrutura melhor sem perder o que hoje funciona.

## O que existe aqui

- `ENTENDA_MELHORAR_ESTRUTURA.md`: contexto resumido, status do experimento e ponto de retomada
- `TASK_ROBUSTA_MELHORAR_ESTRUTURA.md`: task curta e operacional
- `TASK_ROBUSTA_APLICACAO_EXPERTS.md`: task de conducao para sair da discussao e chegar a uma decisao aplicavel
- `TASK_ROBUSTA_EXECUCAO_FASEADA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`: task-mae oficial com todas as fases da execucao
- `TASK_ROBUSTA_SUPERFICIES_CONSTRUCAO_SEMENTES.md`: task-filha oficial para as superficies de construcao de `Sementes`
- `TASK_ROBUSTA_CONVERGENCIA_SUGESTAO_SEMENTES.md`: task detalhada para sair da exploracao e chegar a uma recomendacao final com embasamento
- `TASK_ROBUSTA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`: task faseada para aplicar a mudanca na superficie publica de `Sementes`
- `orchestrator_melhorar_estrutura.yaml`: orquestrador local desta conversa
- `experts/`: cinco experts com papeis distintos
- `rodadas/`: rodadas escritas para leitura humana e deliberacao guiada
- `discussoes/`: discussoes datadas por tema, para nao perder contexto entre sessoes
- `sinteses/`: hipoteses iniciais consolidadas

## Como usar os experts para discussoes de verdade

Toda rodada boa nesta pasta deve seguir estas regras:

1. abrir com uma pergunta clara
2. listar evidencias reais do repo usando tags como `E1`, `E2`, `E3`
3. fazer cada expert argumentar citando ao menos uma evidencia
4. separar fato observado de inferencia
5. registrar tensoes reais, nao apenas consenso educado
6. fechar com decisao provisoria e a pergunta da rodada seguinte

Se uma rodada nao tiver evidencia rastreavel, ela nao esta madura o bastante.

## Convencao para novas discussoes

Sempre que surgir uma nova conversa relevante nesta pasta, criar um arquivo novo em:

- `discussoes/YYYY-MM-DD_HHMM_TEMA.md`

Regras:

- usar data e hora local
- usar tema em ASCII e com `_`
- registrar fontes de evidencia
- fechar com recomendacao e proximo tema sugerido

## O que esta pasta nao tenta fazer

- nao cria um segundo sistema completo
- nao define toda a arquitetura 0-18
- nao troca a fonte de verdade do projeto hoje
- nao mexe em `apps/web`, `build/` ou `bmad/`

## Base de evidencia usada

As discussoes desta pasta se apoiam em fatos reais do repo:

- `docs/MAPA_EXECUCAO_PROJETO.md`
- `build/fases/sementes.py`
- `apps/web/lib/content/loader.ts`
- `apps/web/lib/contracts/lesson-structure.ts`
- `vercel.json`

## Ordem de leitura recomendada

1. `TASK_ROBUSTA_MELHORAR_ESTRUTURA.md`
2. `TASK_ROBUSTA_APLICACAO_EXPERTS.md`
3. `TASK_ROBUSTA_EXECUCAO_FASEADA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`
4. `TASK_ROBUSTA_CONVERGENCIA_SUGESTAO_SEMENTES.md`
5. `TASK_ROBUSTA_PRODUTO_PUBLICADO_E_SUPERFICIES.md`
6. `rodadas/ROUND_00_DIAGNOSTICO.md`
7. `experts/arquitetura/estrategista_estrutura.yaml`
8. `experts/arquitetura/vercel_first.yaml`
9. `experts/conteudo/contrato_licao.yaml`
10. `experts/operacao/revisao_escalavel.yaml`
11. `experts/externos/mae_regente_real.yaml`
12. `rodadas/ROUND_01_DISCUSSAO_INICIAL.md`
13. `rodadas/ROUND_02_BLOCO_MINIMO.md`
14. `discussoes/2026-03-19_2204_SEMENTES_PRODUTO_PADRAO_E_REVISAO_INTELIGENTE.md`
15. `discussoes/2026-03-19_2223_CONTRATO_CANONICO_SEMENTES.md`
16. `discussoes/2026-03-19_2225_ANATOMIA_DO_REVIEW_PACK_POR_BLOCO.md`
17. `discussoes/2026-03-19_2228_FLUXO_EDITORIAL_SEMENTES.md`
18. `discussoes/2026-03-20_1440_PRODUTO_PUBLICADO_SEMENTES.md`
19. `discussoes/2026-03-25_1631_FASE_0_INVENTARIO_SUPERFICIES.md`
20. `discussoes/2026-03-25_1633_FASE_1_CONTRATO_SUPERFICIE_PUBLICA.md`
21. `discussoes/2026-03-25_1635_FASE_2_ENTRADA_SEMENTES.md`
22. `discussoes/2026-03-25_1637_FASE_3_SUPERFICIE_DA_LICAO.md`
23. `discussoes/2026-03-25_1638_FASE_4_ARCOS_E_PROGRESSAO.md`
24. `discussoes/2026-03-25_1640_FASE_5_PILOTO_MINIMO.md`
25. `discussoes/2026-03-25_1639_FASE_6_CONSOLIDACAO_E_DECISAO.md`
26. `discussoes/2026-03-25_1641_PILOTO_MINIMO_APLICADO_MV_S_005.md`
27. `discussoes/2026-03-25_1643_APLICACAO_MANUAL_PORTADOR.md`
28. `discussoes/2026-03-25_1645_APLICACAO_HOME_PRINCIPAL.md`
29. `discussoes/2026-03-25_1646_APLICACAO_MV_S_004.md`
30. `discussoes/2026-03-25_1647_APLICACAO_MV_S_006.md`
31. `discussoes/2026-03-25_1648_APLICACAO_MV_S_007_E_008.md`
32. `discussoes/2026-03-25_1649_APLICACAO_MV_S_009.md`
33. `discussoes/2026-03-25_1650_APLICACAO_MV_S_010.md`
34. `discussoes/2026-03-25_1651_APLICACAO_MV_S_011_E_012.md`
35. `discussoes/2026-03-25_1652_APLICACAO_MV_S_013_E_014.md`
36. `discussoes/2026-03-25_1653_APLICACAO_MV_S_015.md`
37. `sinteses/HIPOTESES_INICIAIS.md`
38. `discussoes/2026-03-25_1654_FASE_0_INVENTARIO_SUPERFICIES_CONSTRUCAO.md`
39. `discussoes/2026-03-25_1655_APLICACAO_SUPERFICIES_CONSTRUCAO_ENTRADA.md`
40. `discussoes/2026-03-25_1656_FASE_2_E_3_NAVEGACAO_INTERNA_CONSTRUCAO.md`
41. `discussoes/2026-03-25_1657_FASE_4_MICROCOPY_ACAO_PRINCIPAL_CONSTRUCAO.md`
42. `discussoes/2026-03-25_1658_CONSOLIDACAO_FRENTE_CONSTRUCAO_SEMENTES.md`

Nota:

- o arquivo `rodadas/ROUND_01_DISCUSSAO_INICIAL.md` foi mantido apenas como apontador de compatibilidade por causa de ruido de nome em Windows/OneDrive
- a fonte canonica da rodada 01 e `rodadas/ROUND_01_DISCUSSAO_INICIAL.md`

## Regra desta fase

Se a conversa comecar a parecer uma plataforma paralela, esta pasta esta errando o alvo.
