# ROUND 00 - DIAGNOSTICO

Data: 2026-03-19
Fase: abertura
Status: consolidado

## 1) Pergunta da rodada

Qual e a dor estrutural real que esta tornando a revisao das licoes cada vez menos escalavel?

## 2) Evidencias usadas

- `E1`: `docs/MAPA_EXECUCAO_PROJETO.md` registra que a arquitetura atual em producao e `YAML -> Jinja -> HTML estatico -> Vercel`
- `E2`: `build/fases/sementes.py` confirma o trilho principal atual e ainda carrega filtro manual para nao sobrescrever `000-025`
- `E3`: `vercel.json` reescreve o deploy para `/site/*`
- `E4`: `apps/web/lib/content/loader.ts` mostra um piloto atomico ainda parcial, hoje limitado a `MV-S-000`, `MV-S-001` e `MV-S-022`
- `E5`: `apps/web/lib/contracts/lesson-structure.ts` ja nomeia blocos estruturais reutilizaveis

## 3) O que o repo mostra hoje

O projeto atual opera em duas frentes ao mesmo tempo:

- frente principal: `YAML -> Jinja -> HTML estatico -> Vercel` apoiada por `E1`, `E2` e `E3`
- frente piloto: `content/lessons + apps/web`, ainda parcial, apoiada por `E4` e `E5`

Leitura consolidada das evidencias:

- `E1` e `E2` mostram que o fluxo real ainda vive no gerador principal
- `E2` mostra que ha remendos operacionais locais, sinal de que a camada atual ja esta carregando muita responsabilidade
- `E4` e `E5` mostram que o repo ja ensaia uma estrutura por blocos menores

## 4) O gargalo real de revisao

A revisao hoje sofre porque o artefato final e grande demais para ser a principal unidade de pensamento.

Amostra observada:

- `MV-S-002` HTML: 615 linhas
- `MV-S-004` HTML: 618 linhas
- `MV-S-006` HTML: 644 linhas
- `MV-S-008` HTML: 662 linhas

Mesmo quando o YAML e menor, ele ainda representa uma licao inteira:

- `002_PEDRAS_FORTALEZA.yaml`: 270 linhas
- `004_A_ORDEM_DO_DIA.yaml`: 208 linhas
- `006_O_DESENHO_DO_REI.yaml`: 208 linhas
- `008_O_PAR_PERFEITO.yaml`: 257 linhas

Enquanto isso, o piloto atomico aponta outra direcao:

- `content/lessons/MV-S-001/sayings.pt-BR.json`: 28 linhas

Leitura central:

Nao falta apenas um gerador melhor. Falta uma unidade menor de revisao.

## 5) O que esta ficando inviavel

- reler HTML inteiro para ajustar poucas partes
- manter contexto da licao toda em toda revisao
- revisar varias licoes em lote sem exaustao
- garantir continuidade sem depender da memoria da sessao

Consequencia operacional:

A equipe fica oscilando entre dois extremos ruins:

- revisar tarde demais, no HTML final
- ou revisar cedo demais, mas ainda no nivel de uma licao inteira

Verdade operacional importante:

Hoje a revisao que realmente decide o texto publicado ainda esta acontecendo no HTML. Portanto, o HTML nao e apenas evidencia futura; ele e a superficie de trabalho atual.

## 6) Decisao provisoria

Fato observado:

- `E1`, `E2` e `E3` mostram que a base atual e estatica e compativel com Vercel
- `E4` e `E5` mostram um piloto que ja aponta para blocos menores

Inferencia:

A saida promissora nao parece ser voltar para banco ou runtime stateful.

A saida promissora parece ser:

- manter Vercel como base inicial
- separar melhor fonte de conteudo e artefato final
- discutir contrato por blocos menores que a licao inteira
- decidir conscientemente se o HTML continua como superficie principal no curto prazo ou se passa a virar evidencia mais adiante

## 7) Pergunta que abre a rodada seguinte

Qual e o menor recorte estrutural que reduz a dor agora sem criar um segundo sistema pesado demais?
