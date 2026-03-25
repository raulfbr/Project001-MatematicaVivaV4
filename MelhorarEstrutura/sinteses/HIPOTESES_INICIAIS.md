# Hipoteses Iniciais

## Hipotese 1 - Melhorar so o processo em cima do HTML/YAML atual

Vantagem:

- menor mudanca estrutural imediata

Risco:

- a unidade de revisao continua grande demais

## Hipotese 2 - Adotar contrato por blocos menores que a licao inteira

Vantagem:

- reduz contexto por revisao
- conversa com o piloto `apps/web`
- nao exige backend novo

Risco:

- precisa de fronteiras bem escolhidas para nao fragmentar demais

## Hipotese 3 - Migrar rapido demais para uma arquitetura nova completa

Vantagem:

- promete resolver tudo de uma vez

Risco:

- overengineering
- cria segunda plataforma antes de validar a unidade revisavel

## Recomendacao preliminar

A melhor aposta inicial e a Hipotese 2:

Discutir contrato por blocos menores que a licao inteira, mantendo Vercel-first e reconhecendo que, no curto prazo, o HTML ainda e a superficie operacional real de revisao.

## O que ainda nao esta decidido

- se o formato final sera YAML unico, JSON ou multi-arquivo
- se `jornada` continua como bloco unico ou se quebra em cenas
- quais blocos devem ser obrigatorios em toda licao
- em que momento o HTML final entra como gate visual

## Riscos de continuar revisando direto em HTML

- alto custo de releitura
- maior chance de perder contexto no meio da revisao
- retrabalho entre estrutura, narrativa e visual
- baixa escalabilidade para o restante de Sementes

## Proxima conversa sugerida

Tema:

Definir qual e a menor unidade de bloco que continua pedagogicamente inteligivel e operacionalmente revisavel.

Nota:

Essa conversa ja foi iniciada em `rodadas/ROUND_02_BLOCO_MINIMO.md`.

Leitura atualizada:

A `ROUND 02` apontou provisoriamente para macro-blocos pedagogicos, mantendo `jornada` e `concreto` inteiros como unidade principal de revisao.

Perguntas sugeridas:

- `jornada` fica inteira ou vira cenas?
- `concreto` deve ser um bloco unico ou separar atividade de instrucoes?
- quais blocos sao obrigatorios em toda licao?
- que evidencias minimas precisam existir antes de abrir o HTML final?
