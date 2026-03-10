# CONTEXTO DETALHADO - PROXIMA SESSAO DE REVISAO

## Objetivo deste arquivo
Este arquivo existe para que a proxima sessao retome o trabalho sem ambiguidade.

Ele responde:
1. onde estamos agora;
2. o que ja foi decidido;
3. o que ainda nao vamos fazer;
4. o que precisa ser lido primeiro;
5. qual e a primeira acao correta da proxima sessao.

## Onde estamos agora
1. a frente ativa continua sendo a revisao `HTML-first`;
2. o protocolo central de revisao agora esta consolidado em `023` e auditado em `028`;
3. `Manual do Portador`, `MV-S-001` e `MV-S-002` ja passaram por rodada profunda, auditoria por IA e publicacao;
4. `MV-S-001` e `MV-S-002` nao devem ser lidas isoladamente como baseline total; o baseline operacional mora no sistema central + nas auditorias `025` e `028` + nas duas licoes em conjunto;
5. `MV-S-003` continua fora do lote ate a validacao humana da Familia Rodrigues confirmar o metodo em uso real;
6. o nome fisico `00_SISTEMA_REVISAO_CANONICO` foi mantido por estabilidade, mas agora ele ja funciona como governanca viva da fase;
7. a proxima sessao ja nao comeca do zero: ela comeca com validacao humana do manual e das licoes `001-002`.

## O que ja foi decidido
1. nao entrar agora em Next, refactor amplo de app ou expansao de pipeline;
2. manter o foco na trilha `HTML-first`;
3. tratar `TASTE` como diferencial operacional real desta fase;
4. usar feedback real de familias como dado qualificado de produto, nao como ordem de mudanca;
5. nao subir agora uma camada nova de multi-agent pesado; se houver apoio extra, ele deve vir em papeis ou lentes leves;
6. nao usar `MV-S-001` isoladamente como baseline total; usar o sistema central e as auditorias finais como referencia principal;
7. manter `MV-S-001` e `MV-S-002` como par auditado para validacao humana;
8. usar validacao humana de familias pioneiras, incluindo a Familia Rodrigues, como calibracao real do produto.

## O que ainda nao vamos fazer
1. nao entrar ainda em cadencia `2/dia`;
2. nao escalar para `004+`;
3. nao tratar os HTML atuais alem de `001-002` como definitivos;
4. nao abrir `003` em lote antes de validar manual e `001-002` em familia real;
5. nao pular a ideia geral da licao antes da revisao por topicos;
6. nao confundir feedback de familia com veto automatico do produto;
7. nao investir agora em harness novo antes de elevar `TASTE` e realidade de uso.

## O que precisa ser lido no inicio da proxima sessao
1. `README.md` da raiz do projeto
2. `Revisao/000_COMECAR_AQUI.md`
3. `Revisao/README.md`
4. `Revisao/001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/000_INDEX_SISTEMA_REVISAO.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/025_AUDITORIA_FINAL_L001_L002_PROTOCOLO_CENTRAL.md`
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/028_AUDITORIA_FINAL_GERAL_PROTOCOLO_MANUAL_L001_L002.md`
10. `site/manual-portador.html`
11. `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html`
12. `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`

## Onde moram todas as diretrizes
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md` = contrato macro da licao.
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md` = processo de revisao.
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md` = criterio de PASS/BLOCK.
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/` = diretrizes por secao da licao.
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/` = diretrizes que atravessam varias secoes.
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md` = filtro final de fidelidade.
7. `Revisao/01_REFERENCIAS_DE_APOIO/` = apoio forte, mas nao fonte primaria.

## Metodo da proxima sessao
Primeiro vamos validar manualmente o que a ultima passada realmente sustentou no manual e nas licoes `001-002`.

Ordem:
1. abrir `005_STATUS_REVISAO_SEMENTES.md` e confirmar o registro da passada mais recente;
2. abrir `028_AUDITORIA_FINAL_GERAL_PROTOCOLO_MANUAL_L001_L002.md`;
3. reler `site/manual-portador.html`, `MV-S-001` e `MV-S-002` como experiencia real de familia;
4. realizar revisao manual da Familia Rodrigues;
5. registrar o que a leitura humana confirmou, tensionou ou recusou;
6. so depois decidir se ainda falta nova passada editorial ou se o sistema pode liberar a entrada de `MV-S-003`;
7. devolver para o sistema o que a validacao humana revelar sobre `TASTE`, realidade de uso e clareza do metodo.

## Primeira acao concreta da proxima sessao
1. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`;
2. abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/028_AUDITORIA_FINAL_GERAL_PROTOCOLO_MANUAL_L001_L002.md`;
3. reler `site/manual-portador.html`, `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html` e `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`;
4. fazer a revisao manual da Familia Rodrigues;
5. registrar o que foi confirmado e o que ainda incomoda;
6. so depois entrar em patch, se necessario;
7. registrar o que precisa voltar para o sistema antes de liberar `MV-S-003`.

## Definicao de sucesso da proxima sessao
1. qualquer pessoa consegue reabrir a pasta e saber o que ler primeiro;
2. fica claro onde moram todas as diretrizes;
3. fica claro que o baseline operacional mora no sistema central e nas auditorias, nao numa licao isolada;
4. manual, `L001` e `L002` recebem selo humano ou findings concretos de uso;
5. a proxima decisao sobre `MV-S-003` nasce de validacao real, nao de memoria difusa;
6. o status da fase nao contradiz o estado real.

## Frase-sintese
Primeiro validamos em familia real o que o sistema consolidou.
Depois registramos o que essa validacao confirmar ou tensionar.
So depois decidimos a entrada da `MV-S-003`.

## Prompt pronto para retomar
Use este comando na proxima sessao:

`Leia README.md, Revisao/README.md, Revisao/000_COMECAR_AQUI.md, Revisao/001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md, Revisao/00_SISTEMA_REVISAO_CANONICO/000_INDEX_SISTEMA_REVISAO.md, Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md e Revisao/00_SISTEMA_REVISAO_CANONICO/018_TASK_ROBUSTA_REVISAO_DIRIGIDA_L002.md. Depois continue exatamente de onde paramos: revise 011_TOPICOS a partir de 006 e 012_TRANSVERSAIS com foco explicito em TASTE, retome a revisao dirigida da MV-S-002 usando logs/2026-03-07-09h46-revisao002.md, e registre o que precisar voltar para a L001 e para o sistema.`
