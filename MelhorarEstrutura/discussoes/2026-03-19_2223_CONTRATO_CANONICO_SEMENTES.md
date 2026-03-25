# DISCUSSAO - CONTRATO CANONICO DE SEMENTES

Data: 2026-03-19
Hora: 22:23
Tema: definir a lista canonica de blocos, sua ordem e sua funcao em `Sementes`
Status: recomendacao provisoria

## Leitura em 30 segundos

Decisao provisoria deste arquivo:

- os `12 topicos` continuam sendo a grade canonica de `Sementes`
- a ordem oficial foi mantida
- o contrato pode ser lido em camadas sem perder a sequencia

Papel deste arquivo hoje:

- estabilizar naming
- estabilizar ordem
- preparar a base para `review packs`

Se voce estiver lendo em sequencia, o proximo arquivo mais importante e:

- `discussoes/2026-03-19_2225_ANATOMIA_DO_REVIEW_PACK_POR_BLOCO.md`

## 1) Pergunta central

Qual deve ser o contrato canonico de `Sementes` para que:

- a equipe pare de oscilar entre nomes concorrentes
- a revisao continue topico a topico sem perder o fio
- o produto preserve a ordem viva da licao
- a futura geracao de `review packs` tenha base estavel

## 2) Fontes de evidencia

- `E1`: `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml`
- `E2`: `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/000_README.md`
- `E3`: `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/001_BASE_E_HERO.md`
- `E4`: `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/002_HEADER_SUPERIOR.md`
- `E5`: `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/006_O_CONCRETO.md`
- `E6`: `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/011_FORMACAO_DO_PORTADOR.md`
- `E7`: `rodadas/ROUND_02_BLOCO_MINIMO.md`
- `E8`: `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`
- `E9`: `site/sementes/MV-S-004_A_ORDEM_DO_DIA.html`
- `E10`: `site/sementes/MV-S-006_O_DESENHO_DO_REI.html`
- `E11`: `site/sementes/MV-S-008_O_PAR_PERFEITO.html`
- `E12`: `logs/2026.03.13/2026-03-13_REVISAO_L004_TOPICO_A_TOPICO.md`

## 3) Fatos observados

### 3.1 A revisao premium ja tem uma ordem oficial

`E2` fixa claramente a ordem oficial dos `12 topicos`:

1. `001_BASE_E_HERO`
2. `002_HEADER_SUPERIOR`
3. `003_PREPARACAO_DO_PORTADOR`
4. `004_RITUAL_DE_ENTRADA`
5. `005_A_JORNADA`
6. `006_O_CONCRETO`
7. `007_NARRAMOS_JUNTOS`
8. `008_RITUAL_DE_FECHAMENTO`
9. `009_CONEXAO_DA_JORNADA`
10. `010_SEMENTES_PARA_O_DIA`
11. `011_FORMACAO_DO_PORTADOR`
12. `012_NAVEGACAO_INFERIOR`

Leitura:

o sistema canonico de revisao ja opera com um contrato de fato. O problema hoje nao e ausencia de estrutura. O problema e que esse contrato ainda nao esta traduzido de forma simples para a camada de decisao estrutural.

### 3.2 O template V6.5 confirma parte do contrato, mas nao tudo

`E1` confirma chaves como:

- `para_portador`
- `ritual_abertura`
- `jornada`
- `narracao`
- `ritual_fechamento`
- `sementes_do_dia`
- `para_familia`
- `diario_portador`
- `auditoria_qa`

E tambem registra uma `ordem_preferida_blocos` visivel:

- `Ritual de Entrada`
- `A Jornada`
- `O Concreto`
- `Narramos Juntos`
- `Ritual de Fechamento`
- `Sementes para o Dia`
- `Formacao do Portador`

Leitura:

o template confirma o miolo, mas nao nomeia de forma tao explicita a moldura de publish nem resolve sozinho as fronteiras entre:

- `para_portador` e `Preparacao do Portador`
- `para_familia` e `Formacao do Portador`
- `linkage` e `Conexao da Jornada`

### 3.3 O HTML publicado repete um padrao muito estavel

`E8`, `E9`, `E10` e `E11` repetem, com alta consistencia:

- Preparacao do Portador
- Ritual de Entrada
- A Jornada
- O Concreto
- Narramos Juntos
- Ritual de Fechamento
- Conexao da Jornada
- Sementes para o Dia
- Formacao do Portador

Leitura:

isso mostra que esses blocos nao sao enfeites do template. Eles ja sao a experiencia real publicada.

### 3.4 Alguns topicos sao claramente de moldura, nao de miolo pedagogico

`E3` e `E4` deixam claro:

- `Base e Hero` abre a pagina e protege identidade, integridade e orientacao
- `Header Superior` orienta navegacao e continuidade

`E12` reforca essa leitura ao tratar `001`, `002` e `012` como topicos auditaveis, mas nao como o coracao pedagogico da licao.

### 3.5 `O Concreto` tem estabilidade semantica forte

`E5` e decisivo aqui:

- o nome correto da secao e `O Concreto`
- ele e o centro pedagogico da licao em `Sementes`
- ele vem depois da Jornada e antes de Narramos Juntos

Leitura:

isso pesa contra alternativas vagas como `momento de conexao`, porque elas apagam a funcao especifica desta secao.

### 3.6 `Formacao do Portador` tambem tem funcao propria e ordem canonica interna

`E6` mostra que:

- `Formacao do Portador` nao e apendice
- ela fecha a camada formativa antes da navegacao inferior
- ela tem ordem canonica interna estavel

Leitura:

isso confirma que `Formacao do Portador` deve continuar no contrato principal da licao publicada, mesmo que sua fonte upstream hoje ainda passe por `para_familia` e camadas associadas.

### 3.7 A rodada anterior ja separou shell, core e blocos reais de revisao

`E7` concluiu provisoriamente que:

- `jornada` e `concreto` ficam inteiros
- `Conexao da Jornada`, `Sementes para o Dia` e `Formacao do Portador` sao blocos reais
- `hero`, header e navegacao devem ser tratados como camada de shell/publish

Leitura:

esta discussao nao comeca do zero. Ela precisa agora congelar melhor essa separacao.

## 4) Tensoes reais

### Tensao 1 - O contrato de `Sementes` deve copiar os 12 topicos ou reduzir para o miolo?

- a favor de copiar os 12 topicos: conversa diretamente com a revisao premium existente
- a favor de reduzir para o miolo: parece mais simples para pensamento estrutural

Leitura:

copiar os 12 topicos ajuda a auditoria, mas pode confundir o que e `moldura` com o que e `coracao pedagogico`.

### Tensao 2 - `O Concreto` deve mudar de nome para algo mais amplo?

- a favor de mudar: alguns nomes alternativos soam mais fluidos no discurso
- contra mudar: `E5` torna `O Concreto` semanticamente preciso e pedagogicamente central

Leitura:

renomear `O Concreto` agora enfraqueceria um eixo que ja esta muito bem consolidado.

### Tensao 3 - `Conexao da Jornada`, `Sementes para o Dia` e `Formacao do Portador` sao centrais ou perifericos?

- a favor de periferizar: parecem camadas de apoio
- contra periferizar: HTML, logs e revisao premium os tratam como blocos reais e recorrentes

Leitura:

eles nao sao o centro da experiencia concreta da crianca, mas sao centrais para continuidade, pertencimento e formacao do Portador.

### Tensao 4 - `auditoria_qa`, `diario_portador`, `linkage` e metadados entram no mesmo contrato?

- a favor: tambem sao parte da licao em fonte
- contra: nao aparecem como experiencia publicada da familia

Leitura:

esses itens precisam existir, mas como camada de governanca e suporte, nao no mesmo plano dos blocos publicados.

## 5) Hipoteses consideradas

### Hipotese A - Contrato canonico igual aos 12 topicos, em lista plana

Vantagem:

- adere perfeitamente ao sistema de revisao atual

Risco:

- mistura publish shell com core pedagogico e governanca

### Hipotese B - Contrato canonico so com o miolo pedagogico

Vantagem:

- deixa a estrutura mais limpa

Risco:

- perde aderencia ao sistema de revisao premium e deixa navegação/shell sem lugar claro

### Hipotese C - Contrato canonico em 3 camadas

Camadas:

- `shell/publish`
- `core pedagogico`
- `governanca e suporte`

Vantagem:

- preserva aderencia aos 12 topicos
- esclarece o papel de cada bloco
- prepara melhor os futuros `review packs`

Risco:

- exige disciplina de nomenclatura para nao virar taxonomia demais

## 6) Leitura consolidada

A melhor leitura neste momento e:

o contrato canonico de `Sementes` nao deve abolir os `12 topicos`, porque eles ja governam a revisao real.

Mas ele tambem nao deve fingir que os 12 topicos sao todos do mesmo tipo.

Portanto, o contrato mais fiel hoje parece ser:

- manter os `12 topicos` como grade de revisao e publish
- organizar esses topicos em tres camadas distintas
- nomear explicitamente os artefatos invisiveis de governanca fora dessa grade publicada

## 7) Recomendacao provisoria

### 7.1 Grade canonica de revisao e publish para `Sementes`

| ordem | id canonico | camada | label principal | papel |
| --- | --- | --- | --- | --- |
| 001 | `base_hero` | shell | Base e Hero | abrir a pagina com integridade, identidade e promessa |
| 002 | `header_superior` | shell | Header Superior | orientar sequencia e navegacao |
| 003 | `preparacao_portador` | core | Preparacao do Portador | preparar o adulto para conduzir |
| 004 | `ritual_entrada` | core | Ritual de Entrada | abrir percepcao e atmosfera |
| 005 | `jornada` | core | A Jornada | revelar a verdade matematica narrativamente |
| 006 | `concreto` | core | O Concreto | encarnar a verdade nas maos e no corpo |
| 007 | `narramos_juntos` | core | Narramos Juntos | consolidar o vivido com respostas da crianca |
| 008 | `ritual_fechamento` | core | Ritual de Fechamento | devolver paz e fechar a travessia |
| 009 | `conexao_jornada` | core | Conexao da Jornada | ligar a experiencia ao proximo passo |
| 010 | `sementes_do_dia` | core | Sementes para o Dia | deixar um fruto leve e praticavel fora da pagina |
| 011 | `formacao_portador` | core | Formacao do Portador | formar, aliviar e dar criterio ao adulto |
| 012 | `navegacao_inferior` | shell | Navegacao Inferior | encerrar a pagina com continuidade tecnica |

### 7.2 Camada de governanca e suporte

Esta camada nao entra como topico publicado, mas precisa ser modelada no contrato:

- `metadados`
- `navegacao`
- `linkage`
- `diario_portador`
- `auditoria_qa`

Leitura:

esta camada alimenta continuidade, build, QA e revisao interna, mas nao deve concorrer com os blocos publicados na mente de quem revisa a licao como experiencia.

### 7.3 Mapeamento provisório entre fonte atual e contrato canonico

| fonte atual | contrato canonico sugerido | observacao |
| --- | --- | --- |
| `para_portador` | `preparacao_portador` | mapeamento forte |
| `ritual_abertura` | `ritual_entrada` | alias claro a consolidar |
| `jornada.narrativa_principal` | `jornada` | permanece como arco inteiro |
| `jornada.concreto` | `concreto` | hoje ainda nasce dentro de `jornada` na fonte |
| `narracao` | `narramos_juntos` | alias claro a consolidar |
| `ritual_fechamento` | `ritual_fechamento` | mapeamento forte |
| `sementes_do_dia` | `sementes_do_dia` | bloco ja nomeado no template atual |
| `para_familia` | `formacao_portador` | precisa mapeamento refinado, nao e sinonimo perfeito |
| `linkage` | `conexao_jornada` | ajuda na continuidade, mas nao cobre sozinho o bloco visivel |
| `auditoria_qa` | `auditoria_qa` | camada de governanca, nao publish |

## 8) Pontos de decisao desta discussao

Fatos:

- `E2` ja fixa oficialmente os 12 topicos da revisao
- `E1` fixa boa parte das chaves da fonte atual
- `E8-E11` confirmam repeticao forte da ordem publicada
- `E5` fixa `O Concreto` como nome correto e centro pedagogico
- `E6` fixa `Formacao do Portador` como bloco com peso proprio

Inferencia:

o contrato canonico mais seguro hoje e um contrato em tres camadas:

- shell/publish
- core pedagogico
- governanca e suporte

Decisoes provisórias:

- manter os `12 topicos` como grade oficial de revisao de `Sementes`
- tratar `001`, `002` e `012` como shell
- tratar `003` a `011` como core pedagogico publicado
- tratar `metadados`, `navegacao`, `linkage`, `diario_portador` e `auditoria_qa` como governanca e suporte
- consolidar `O Concreto` como nome canonico, sem substitui-lo por rótulos mais vagos

## 9) Riscos

- chamar tudo de `bloco` sem dizer a camada pode recriar ambiguidade
- consolidar cedo demais aliases ruins pode cristalizar drift de nomenclatura
- empurrar `Formacao do Portador` para fora do contrato principal enfraqueceria o `North Star`
- manter `concreto` escondido apenas dentro de `jornada` na fonte futura pode atrapalhar a geracao de `review packs`

## 10) Proximo tema sugerido

Tema:

`ANATOMIA_DO_REVIEW_PACK_POR_BLOCO`

Pergunta:

agora que a grade canonica de `Sementes` esta mais clara, qual e o menor `review pack` que cada um desses blocos precisa ter para podermos revisar com profundidade sem reabrir a licao inteira?
