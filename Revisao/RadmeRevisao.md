# README REVISAO - Fase de Revisão Premium

Este arquivo é o ponto de entrada da fase de revisão.

## Ordem de Leitura (obrigatória)
1. `README.md` (visão geral e contexto do projeto).
2. `Revisao/RadmeRevisao.md` (este arquivo).
3. `Revisao/padrao_visual_sementes.md` (fonte principal de padrão).
4. `Revisao/topicos_licao_revisao.md` (checklist operacional por lição).
5. `Revisao/framework_estrategia_mestria.md` (estratégia narrativa/pedagógica premium).

## SSOT da Revisão
1. `padrao_visual_sementes.md` = contrato visual/estrutural canônico.
2. `topicos_licao_revisao.md` = checklist de execução da auditoria.
3. `framework_estrategia_mestria.md` = profundidade narrativa e intenção pedagógica.

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
1. L001-L003 revisadas com foco estrutural e narrativo.
2. Fluxo geral de revisão organizado nesta pasta.
3. Próximo ciclo será orientado por esqueleto base único.

## Próxima Sessão (anotado)
Vamos executar a estratégia que você definiu:

1. Criar um `ESQUELETO_GERAL` canônico de lição.
2. Para cada tópico do esqueleto, criar um arquivo próprio em `Revisao/`.
3. Em cada arquivo de tópico, separar:
- contrato técnico HTML/CSS;
- contrato de escrita narrativa/pedagógica;
- critérios de qualidade (PASS/FAIL).
4. Ligar tudo no esqueleto central para revisão progressiva ponto a ponto.

Arquivo de apoio já criado para amanhã:
`Revisao/ESQUELETO_GERAL_PLANO_PROXIMA_SESSAO.md`

## Arquivos Históricos
Conteúdos antigos/contextuais estão em:
`logs/Outros/Revisao_Legado/`
