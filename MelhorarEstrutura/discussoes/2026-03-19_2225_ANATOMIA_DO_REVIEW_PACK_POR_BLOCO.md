# DISCUSSAO - ANATOMIA DO REVIEW PACK POR BLOCO

Data: 2026-03-19
Hora: 22:25
Tema: definir o menor artefato de revisao por bloco que entrega contexto suficiente sem reabrir a licao inteira
Status: recomendacao provisoria

## Leitura em 30 segundos

Decisao provisoria deste arquivo:

- a menor unidade confiavel de revisao nao e a licao inteira
- tambem nao e um trecho cru sem contexto
- o melhor candidato ate aqui e um `review pack` por bloco com fronteiras e zona de decisao

Papel deste arquivo hoje:

- transformar a ideia de modularidade em um artefato concreto de revisao
- reduzir custo de contexto sem perder funcao do bloco

Se voce estiver lendo em sequencia, o proximo arquivo mais importante e:

- `discussoes/2026-03-19_2228_FLUXO_EDITORIAL_SEMENTES.md`

## 1) Pergunta central

Agora que a grade canonica de `Sementes` esta mais clara, qual e o menor `review pack` que cada bloco precisa ter para que:

- a IA revise com profundidade
- o humano acompanhe sem releitura da licao inteira
- o `North Star` continue pesando
- as fronteiras entre blocos nao se percam
- o HTML deixe de ser a unica superficie de pensamento

## 2) Fontes de evidencia

- `E1`: `discussoes/2026-03-19_2223_CONTRATO_CANONICO_SEMENTES.md`
- `E2`: `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/003_PREPARACAO_DO_PORTADOR.md`
- `E3`: `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/005_A_JORNADA.md`
- `E4`: `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/007_NARRAMOS_JUNTOS.md`
- `E5`: `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/009_CONEXAO_DA_JORNADA.md`
- `E6`: `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/010_SEMENTES_PARA_O_DIA.md`
- `E7`: `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`
- `E8`: `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/009_TASTE_EDITORIAL_E_AUTORIA_HUMANA.md`
- `E9`: `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md`
- `E10`: `logs/2026.03.13/2026-03-13_REVISAO_L004_TOPICO_A_TOPICO.md`
- `E11`: `logs/2026.03.10/2026-03-10_REVISAO_L006_TOPICO_A_TOPICO.md`

## 3) Fatos observados

### 3.1 Cada bloco ja tem contrato proprio

`E2`, `E3`, `E4`, `E5` e `E6` mostram que a revisao canonica nao olha apenas para um titulo de secao.

Cada topico ja carrega:

- missao
- posicao no fluxo
- contrato tecnico
- contrato pedagogico
- contrato narrativo
- anti-patterns
- checklist
- prompt operacional

Leitura:

um `review pack` bom nao pode ser apenas "copie o bloco e revise". Ele precisa carregar a funcao do bloco.

### 3.2 Os problemas reais aparecem tambem nas fronteiras

`E10` e `E11` mostram que a revisao real nao se limita ao bloco isolado. Ela audita muito:

- o proprio bloco
- a fronteira com o bloco anterior
- a fronteira com o bloco seguinte

Exemplos:

- `005 -> 006`
- `006 -> 007`
- `010 -> 011`

Leitura:

um `review pack` sem contexto de fronteira seria pequeno demais para ser confiavel.

### 3.3 Nem todos os blocos precisam da mesma densidade de contexto

`E1` definiu tres camadas:

- shell
- core pedagogico
- governanca e suporte

Leitura:

`Base e Hero` nao precisa do mesmo tipo de pack que `A Jornada`.
`Conexao da Jornada` nao precisa da mesma profundidade de cenas que `O Concreto`.

### 3.4 `North Star`, `TASTE` e `TX10` pesam de modos diferentes conforme o bloco

`E7`, `E8` e `E9` mostram que:

- `North Star` pesa em todos os blocos
- `TASTE` pesa mais em frases, tom, costura e respiracao
- `TX10` pesa mais quando ha ancora concreta, revelacao, gesto e forma de nomear

Leitura:

um `review pack` bom precisa carregar transversais aplicaveis, nao despejar todas sempre com o mesmo peso.

### 3.5 O custo de contexto atual vem da mistura de quatro coisas

O HTML inteiro obriga revisar junto:

- texto do bloco
- funcao do bloco
- relacao com vizinhos
- markup final publicado

Leitura:

o `review pack` ideal deve separar melhor essas quatro camadas.

## 4) Tensoes reais

### Tensao 1 - pack unico para todos os blocos ou packs por familia de bloco?

- a favor de um unico modelo: mais simples de manter
- contra: perde especificidade e vira checklist genérico

### Tensao 2 - incluir o texto completo da licao ou so o bloco alvo?

- a favor de incluir tudo: nenhum contexto se perde
- contra: volta o problema original de token e releitura

### Tensao 3 - pack de diagnostico ou pack com espaco para patch?

- a favor de diagnostico puro: evita pular cedo para reescrita
- contra: obriga outro artefato para a decisao e quebra o fluxo

### Tensao 4 - pack humano ou pack IA?

- a favor de pack humano: legibilidade e aprendizado
- a favor de pack IA: campos mais objetivos e comparaveis

Leitura:

o melhor caminho parece ser um artefato hibrido:

- legivel para humano
- estruturado o bastante para IA
- pequeno no corpo principal
- com espaco final para decisao e patch

## 5) Hipoteses consideradas

### Hipotese A - pack ultraleve

Conteudo:

- bloco alvo
- texto do bloco
- duas perguntas

Vantagem:

- muito barato em contexto

Risco:

- perde funcao, fronteira e criterio

### Hipotese B - pack completo demais

Conteudo:

- licao inteira
- todos os blocos
- todos os contratos
- todos os logs

Vantagem:

- zero perda de contexto

Risco:

- reproduz o problema atual em outro formato

### Hipotese C - pack em camadas

Conteudo:

- cabecalho minimo comum
- contexto de fronteira
- funcao do bloco
- texto atual do bloco
- perguntas cirurgicas
- zona de decisao

Vantagem:

- mantem contexto suficiente sem reabrir a licao inteira

Risco:

- exige desenho melhor dos campos obrigatorios

## 6) Leitura consolidada

A melhor aposta agora e a `Hipotese C`.

O `review pack` precisa ser:

- menor que a licao inteira
- maior que um bloco cru solto
- sensivel a fronteiras
- sensivel ao tipo de bloco
- orientado por funcao, nao so por texto

Portanto, o desenho mais promissor e:

`pack em 3 camadas`

1. `cabecalho comum`
2. `corpo especifico do bloco`
3. `zona de decisao`

## 7) Recomendacao provisoria

### 7.1 Estrutura minima obrigatoria de todo review pack

Todo `review pack` de bloco deve ter:

1. `identificacao`
2. `contexto minimo`
3. `funcao do bloco`
4. `texto atual do bloco`
5. `fronteiras`
6. `perguntas de revisao`
7. `zona de decisao`

### 7.2 Cabecalho comum do pack

Campos obrigatorios:

- `licao_id`
- `titulo`
- `bloco_id`
- `bloco_label`
- `camada`
- `guardiao_lider`
- `conceito_vivo`
- `imagem_dominante`
- `fruto_do_dia`
- `licao_anterior`
- `licao_proxima`

Leitura:

isso da o minimo de identidade e espiral sem exigir a licao toda.

### 7.3 Contexto minimo comum

Todo pack deve trazer:

- `resumo_da_licao_em_3_linhas`
- `papel_deste_bloco_na_licao`
- `o_que_veio_antes`
- `o_que_precisa_ficar_pronto_para_o_bloco_seguinte`

Regra:

nao copiar blocos vizinhos inteiros.
Trazer apenas um resumo funcional da fronteira.

### 7.4 Bloco de fronteira obrigatorio

Todo pack deve ter uma secao chamada `fronteiras_criticas` com:

- `fronteira_anterior`
- `fronteira_posterior`
- `risco_de_repeticao`
- `risco_de_quebra_de_fio`

Exemplo:

- `005 -> 006`: a Jornada nao pode esgotar o gesto principal
- `006 -> 007`: Narramos precisa recolher o vivido sem virar prova
- `010 -> 011`: o prolongamento domestico nao pode competir com a formacao do adulto

Leitura:

essa secao nasce diretamente de `E10` e `E11`.

### 7.5 Transversais aplicaveis

Todo pack deve declarar explicitamente:

- `North Star`: sempre obrigatorio
- `TASTE`: opcional forte
- `TX10`: obrigatorio ou opcional forte conforme o bloco

Modelo:

| bloco | North Star | Taste | TX10 |
| --- | --- | --- | --- |
| `preparacao_portador` | obrigatorio | opcional forte | opcional forte |
| `ritual_entrada` | obrigatorio | opcional forte | obrigatorio |
| `jornada` | obrigatorio | opcional forte | obrigatorio |
| `concreto` | obrigatorio | opcional forte | obrigatorio |
| `narramos_juntos` | obrigatorio | opcional forte | opcional forte |
| `ritual_fechamento` | obrigatorio | opcional forte | opcional forte |
| `conexao_jornada` | obrigatorio | opcional forte | leve |
| `sementes_do_dia` | obrigatorio | opcional forte | opcional forte |
| `formacao_portador` | obrigatorio | opcional forte | leve |
| `shell` | obrigatorio | leve | leve |

### 7.6 Corpo especifico por familia de bloco

#### Familia A - shell

Blocos:

- `base_hero`
- `header_superior`
- `navegacao_inferior`

Campos extras:

- `integridade_tecnica`
- `coerencia_visual`
- `coerencia_de_navegacao`
- `promessa_de_abertura_ou_fecho`

#### Familia B - blocos de preparacao e sustentacao do adulto

Blocos:

- `preparacao_portador`
- `formacao_portador`

Campos extras:

- `o_que_o_portador_precisa_entender`
- `o_que_o_portador_precisa_fazer`
- `pontos_de_traducao_mental`
- `sinais_de_culpa_ou_peso`
- `frases_que_nao_cabem_em_voz_alta`

#### Familia C - blocos narrativo-centrais

Blocos:

- `ritual_entrada`
- `jornada`
- `ritual_fechamento`

Campos extras:

- `imagem_dominante_em_acao`
- `gesto_central`
- `voz_do_guardiao`
- `o_que_nao_deve_ser_gasto_cedo_demais`
- `ponte_para_o_proximo_bloco`

#### Familia D - blocos de experiencia e consolidacao

Blocos:

- `concreto`
- `narramos_juntos`

Campos extras:

- `acao_principal`
- `diferenca_em_relacao_ao_bloco_anterior`
- `sinal_de_fruto`
- `formas_de_resposta_legitimas`
- `risco_de_repeticao_ou_escolarizacao`

#### Familia E - blocos de continuidade

Blocos:

- `conexao_jornada`
- `sementes_do_dia`

Campos extras:

- `fruto_que_precisa_pousar`
- `continuidade_sem_peso`
- `teaser_ou_prolongamento`
- `risco_de_CTA_ou_tarefa_disfarcada`

### 7.7 Texto atual do bloco

O pack deve conter o `texto atual do bloco` em forma limpa, mas com estas regras:

- levar apenas o bloco alvo
- remover ruido de layout que nao ajuda na decisao
- preservar headings e subtopicos internos
- manter nomes das classes ou markup apenas quando forem relevantes para o contrato tecnico

Leitura:

o objetivo e revisar a funcao e a escrita, nao reler o HTML bruto inteiro.

### 7.8 Zona de perguntas cirurgicas

Todo pack deve terminar com perguntas obrigatorias:

1. este bloco cumpre sua funcao?
2. este bloco ajuda ou aumenta traducao mental?
3. este bloco preserva a imagem dominante?
4. este bloco prepara bem o seguinte?
5. este bloco repete indevidamente o anterior?

E uma pergunta especifica da familia do bloco.

Exemplos:

- `jornada`: o guardiao revela ou so explica?
- `concreto`: a atividade principal e realmente nova em relacao a Jornada?
- `narramos_juntos`: a secao convida narracao ou puxa prova?
- `sementes_do_dia`: o tom continua opcional de verdade?
- `formacao_portador`: o adulto termina mais leve ou mais pressionado?

### 7.9 Zona de decisao

Todo pack deve fechar com:

- `o_que_esta_forte`
- `friccoes_reais`
- `tipo_de_problema`
- `patch_sugerido`
- `riscos_residuais`
- `impacto_na_fronteira_anterior`
- `impacto_na_fronteira_posterior`

Campo `tipo_de_problema` deve usar vocabulario restrito:

- `tom`
- `funcao`
- `clareza`
- `gesto`
- `ordem`
- `fronteira`
- `naming`
- `tecnico`

Leitura:

isso ajuda a IA e o humano a falarem a mesma lingua diagnostica.

## 8) Template minimo recomendado

```text
# REVIEW PACK - [bloco_label]

## Identificacao
- licao_id:
- titulo:
- bloco_id:
- camada:
- guardiao_lider:

## Contexto minimo
- conceito_vivo:
- imagem_dominante:
- fruto_do_dia:
- resumo_da_licao_em_3_linhas:
- licao_anterior:
- licao_proxima:

## Funcao do bloco
- papel_deste_bloco:
- o_que_veio_antes:
- o_que_precisa_ficar_pronto_para_o_bloco_seguinte:
- transversais_aplicaveis:

## Fronteiras criticas
- fronteira_anterior:
- fronteira_posterior:
- risco_de_repeticao:
- risco_de_quebra_de_fio:

## Corpo do bloco
- subtopicos_esperados:
- texto_atual_do_bloco:

## Perguntas de revisao
1.
2.
3.
4.
5.

## Decisao
- o_que_esta_forte:
- friccoes_reais:
- tipo_de_problema:
- patch_sugerido:
- riscos_residuais:
```

## 9) Recomendacao provisoria final desta discussao

O menor `review pack` inteligente para `Sementes` nao deve ser:

- nem um bloco cru
- nem uma licao inteira recortada

Ele deve ser:

- `um pacote por bloco`
- com `cabecalho comum`
- `fronteiras explicitas`
- `funcao do bloco`
- `texto limpo do bloco`
- `perguntas cirurgicas`
- `zona de decisao`

Isso parece o melhor ponto de equilibrio entre:

- custo de contexto
- seguranca editorial
- fidelidade ao `North Star`
- capacidade real de revisao por IA e por humano

## 10) Riscos

- querer deixar o pack bonito demais e ele crescer alem do necessario
- incluir texto demais dos vizinhos e reintroduzir a licao inteira por outro nome
- esquecer a fronteira e transformar o pack em bloco solto
- esquecer o `North Star` e transformar o pack em checklist estrutural seco
- usar o pack para substituir o juizo humano de `TASTE`

## 11) Proximo tema sugerido

Tema:

`FLUXO_EDITORIAL_SEMENTES`

Pergunta:

agora que temos contrato canonico e anatomia do `review pack`, em que ordem o time deve passar por fonte, pack, HTML e validacao final para reduzir retrabalho sem burocratizar a revisao?
