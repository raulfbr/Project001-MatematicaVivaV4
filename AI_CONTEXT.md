# AI CONTEXT - Matemática Viva

Data de atualização: 2026-03-17
Status: arquivo vivo de retomada macro + estado atual

## Missão deste arquivo

Este arquivo existe para que qualquer pessoa ou IA retome o projeto sem ambiguidade.

Ele responde:

1. o que o projeto é de verdade;
2. qual trilha está ativa agora;
3. onde estamos pontualmente;
4. o que já foi decidido;
5. o que não fazer agora;
6. quais arquivos governam cada tipo de decisão;
7. qual é o próximo passo seguro.

Regra:

1. este arquivo é a fonte principal de contexto vivo;
2. `README.md` continua sendo a porta de entrada geral;
3. `Revisao/` continua sendo a fonte operacional da execução;
4. este arquivo não substitui o protocolo, mas orienta a leitura correta dele.

## Síntese do projeto

Matemática Viva é um sistema editorial, pedagógico e narrativo para famílias.

O software existe para servir:

1. o cânone da obra;
2. o currículo;
3. a experiência real da família;
4. a governança da revisão;
5. a evolução futura da infraestrutura.

O centro da obra não é a tecnologia em si.
O centro é a família vivendo uma matemática concreta, narrativa, digna e memorável.

## Ultima rodada fechada

1. a rodada mais recente fechou principalmente a base tecnica e documental do projeto;
2. a home e a trilha publicada foram padronizadas para nomes ASCII, para evitar URLs instaveis e links quebrados por acento;
3. isso nao significa que a camada editorial fina esteja encerrada;
4. a proxima melhora importante deve voltar a textos, tom, fluidez e TASTE, usando os feedbacks da Marina como insumo central;
5. a leitura desta fase nao deve confundir estabilizacao tecnica com fechamento editorial total.

## Fontes de verdade do projeto

### 1. Espírito, identidade e critérios de fidelidade

Arquivos:

1. `LORE/north_star.yaml`
2. `LORE/guardioes.yaml`
3. `LORE/padroes_narrativos.yaml`

Leitura correta:

1. `LORE/north_star.yaml` é o North Star da obra.
2. Ele responde quem somos, para quem existimos, qual tom usamos e quais princípios não são negociáveis.
3. Ele evita que o projeto fique tecnicamente arrumado e editorialmente falso.

### 2. Tradução operacional do North Star

Arquivo:

1. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`

Leitura correta:

1. este arquivo pega o espírito do `LORE/north_star.yaml` e o transforma em critério aplicável de revisão;
2. ele responde se uma lição consola o adulto, encanta a criança, honra a dignidade e sustenta a identidade da obra;
3. ele é o gate final entre "ficou correto" e "ficou fiel".

Conclusão:

1. o `North Star` ajuda muito;
2. o `North Star Operacional` ajuda a aplicar esse norte em decisões reais de revisão;
3. juntos, eles precisam aparecer na leitura de retomada, porque sem eles uma IA pode seguir o protocolo e ainda errar o espírito.

### 3. Currículo

Arquivos:

1. `curriculo/01_SEMENTESV6/`
2. `curriculo/_SISTEMA/`

Função:

1. guardar a matéria-prima curricular;
2. sustentar progressão e linkage;
3. impedir improviso curricular fora de lugar.

### 4. Produto publicado

Arquivos:

1. `site/manual-portador.html`
2. `site/sementes/*.html`
3. `site/sementes/style.css`

Função:

1. materializar a experiência real que a família vê;
2. concentrar narrativa, usabilidade e clareza final.

### 5. Governança da revisão

Arquivos:

1. `Revisao/README.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`

Função:

1. transformar critério em processo;
2. auditar as lições reais;
3. impedir drift procedural;
4. sustentar revisão `HTML-first`.

### 5.1 O que torna uma lição realmente premium

Arquivos:

1. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/009_TASTE_EDITORIAL_E_AUTORIA_HUMANA.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`

Leitura correta:

1. `premium` nao significa apenas licao bonita ou bem diagramada;
2. `premium` significa licao que passou em estrutura, narrativa, pedagogia, UX do Portador e North Star;
3. a rubrica oficial exige nota alta nesses eixos e `Taste editorial` aprovado;
4. `TASTE` e a lente que separa licao correta de licao verdadeiramente recognoscivel como Matematica Viva;
5. sem `TASTE`, a obra pode ficar funcional e ainda assim soar generica ou exigir traducao mental da mae;
6. sem `North Star`, a obra pode ficar correta na forma e falsa no espirito.

### 5.2 O que `TASTE` significa no sistema

Leitura correta:

1. `TASTE` nao e enfeite e nao e perfumaria textual;
2. ele e discernimento editorial encarnado;
3. ele entra quando duas versoes sao tecnicamente validas e precisamos escolher a que melhor:
   a. ajuda a mae;
   b. honra a crianca;
   c. preserva o Reino;
   d. respira bem em voz alta;
   e. soa como Matematica Viva;
4. feedback real de mae entra aqui como calibragem muito poderosa, porque revela releitura, traducao mental, improviso e friccao real;
5. `TASTE` e parte do premium, nao uma camada opcional fora dele.

### 5.3 Onde mora a inteligencia dos `experts`

Arquivos:

1. `bmad/experts/pedagogia/charlotte_mason.yaml`
2. `bmad/experts/matematica/jerome_bruner.yaml`
3. `bmad/experts/pedagogia/susan_macaulay.yaml`
4. `bmad/experts/narrativa/beatrix_potter.yaml`
5. `bmad/experts/ux_familias/maes_personas.yaml`
6. `bmad/experts/externos/mae_ansiosa.yaml`
7. `bmad/experts/externos/mae_veterana.yaml`
8. `bmad/experts/engenharia/engenharia.yaml`
9. `bmad/experts/design/design.yaml`

Leitura correta:

1. os `experts` nao sao enfeite de brainstorming;
2. eles funcionam como lentes de julgamento, veto, tensao e refinamento;
3. ajudam a revisar pedagogia, narrativa, tom, viabilidade domestica, UX, design e engenharia;
4. o eixo mais sensivel para o produto hoje e `ux_familias` + `maes personas`, porque o produto precisa caber na vida real da mae.

### 5.4 Feedback real de maes como ativo estrategico

Arquivos:

1. `Revisao/FEEDBACK_MAES_REAIS/000_README.md`
2. `Revisao/FEEDBACK_MAES_REAIS/INDEX_PROMOCAO_CANONICA.md`
3. `Revisao/FEEDBACK_MAES_REAIS/002_LISTA_VIVA_CANDIDATOS_NORTH_STAR.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/033_PLANO_SISTEMA_FEEDBACK_MAES_REAIS_E_CANONIZACAO_NORTH_STAR.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/034_TASK_ROBUSTA_IMPLANTACAO_SISTEMA_FEEDBACK_MAES_REAIS.md`

Leitura correta:

1. feedback real de maes e um dos ativos mais poderosos do projeto;
2. ele nao existe apenas para corrigir licao pontual;
3. ele existe para ensinar o sistema a criar licoes mais reais para maes reais;
4. a trilha oficial ja foi desenhada para isso com a formula:
   `feedback bruto -> leitura critica -> sintese -> canonizacao seletiva`
5. a decisao correta do sistema foi nao jogar feedback bruto direto no `North Star`;
6. primeiro ele vira caso, depois sintese, depois candidato a regra, e so entao pode subir para transversal ou `North Star`.

### 6. Trilha técnica paralela

Arquivos:

1. `apps/web/`
2. `content/lessons/`
3. `dist/`

Leitura correta:

1. esta trilha é relevante;
2. ela não é, por padrão, a frente ativa principal da fase de revisão premium;
3. serve como laboratório de infraestrutura e pipeline futura.

## Onde estamos agora

Leitura mais segura do estado atual:

1. a frente ativa continua sendo a revisao `HTML-first`;
2. a experiencia final real vive principalmente em `site/sementes/*.html`;
3. a trilha publicada do site agora vai ate `MV-S-015`;
4. `MV-S-016` funciona como pagina de continuidade em construcao;
5. `MV-S-017+` sairam da trilha publicada e aguardam reconstrucao;
6. o protocolo de revisao esta consolidado em `023`, com execucao em `003`, veredito em `004`, quadro operacional em `005` e registro de sessao em `010_TEMPLATE`;
7. `MV-S-003` e `MV-S-004` estao fechadas para a rodada atual, salvo novo feedback relevante;
8. o proximo foco seguro do lote e revisar `MV-S-005` ate `MV-S-010` sob o protocolo endurecido;
9. existe trilha tecnica paralela em `apps/web`, mas ela nao governa a sessao atual por padrao.

## O que o projeto ja sabe sobre maes reais

Leitura correta:

1. feedback real de maes e ativo de produto, nao anexo;
2. ele serve para corrigir licao local e tambem para ensinar o sistema;
3. o melhor uso do feedback nao e obediencia cega, e sim calibragem editorial e operacional;
4. quando houver caso semelhante, consultar `Revisao/FEEDBACK_MAES_REAIS/` antes de patchar;
5. quando houver evidencia forte, a formulacao final deve reduzir releitura, improviso e traducao adulta.

## Tensao documental que precisa ser lida corretamente

1. `README.md` pode preservar snapshots historicos no final;
2. `001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md` e `015_ESTADO_REAL...` continuam uteis, mas nao sao SSOT do momento;
3. a leitura viva atual e: `README.md` -> `AI_CONTEXT.md` -> `Revisao/README.md` -> `000_COMECAR_AQUI` -> `000_INDEX` -> `005` -> `023` -> `003` -> `004`.

## Proximo passo seguro

Em termos de governanca:

1. usar este `AI_CONTEXT.md` como ponto central de retomada macro;
2. usar `README.md` como portal estavel;
3. usar `Revisao/README.md` e `000_COMECAR_AQUI` como entrada operacional curta;
4. usar `005_STATUS_REVISAO_SEMENTES.md` como quadro vivo do lote;
5. evitar criar novo handoff quando uma atualizacao em `AI_CONTEXT.md` resolver.

Em termos de fase de revisao:

1. seguir `029` e `030` para o lote `MV-S-003` ate `MV-S-010`;
2. tratar `MV-S-003` e `MV-S-004` como referencias fechadas da rodada atual;
3. aplicar o protocolo endurecido em `MV-S-005` ate `MV-S-010`;
4. executar sempre via `023 -> 003 -> 004`, com apoio de `011_TOPICOS/` e `012_TRANSVERSAIS/`;
5. consultar `008_NORTH_STAR_OPERACIONAL.md` antes de considerar uma licao pronta;
6. consultar `009_TASTE_EDITORIAL_E_AUTORIA_HUMANA.md` em desempate fino;
7. consultar `010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md` quando houver criacao, reescrita profunda, imagem dominante nebulosa, ancora concreta fraca ou traducao mental da mae;
8. nao reabrir `MV-S-016+` para publicacao antes da reconstrucao sob o novo contrato premium.

## Experimento ativo - MelhorarEstrutura

Existe agora um experimento ativo em `MelhorarEstrutura/`.

Leitura correta:

1. este experimento nao substitui a frente operacional principal;
2. ele existe para testar se uma abordagem guiada por experts, tasks robustas e discussoes com evidencia melhora a qualidade da decisao estrutural;
3. o foco imediato do experimento e `Sementes`;
4. a verdade operacional continua sendo: hoje a revisao real ainda acontece no HTML;
5. portanto, `MelhorarEstrutura` e um laboratorio de convergencia, nao ainda a nova arquitetura oficial do projeto.

Estado atual do experimento:

1. experts locais em `BMAD YAML` foram criados;
2. tasks robustas de exploracao, aplicacao e convergencia foram escritas;
3. rodadas e discussoes com evidencia real do repo ja foram abertas;
4. as tres discussoes mais recentes fecharam leituras provisiorias sobre:
   a. contrato canonico de `Sementes`;
   b. anatomia do `review pack` por bloco;
   c. fluxo editorial recomendado para esta fase;
5. a formula provisoria mais forte ate aqui e:
   `macro -> contrato -> review pack -> patch HTML localizado -> costura HTML -> rubrica -> validacao humana`;
6. isto ainda e teste;
7. a proxima retomada segura do experimento deve partir de `MelhorarEstrutura/ENTENDA_MELHORAR_ESTRUTURA.md`;
8. o proximo tema sugerido para continuar a trilha e `PRODUTO_PUBLICADO_E_SUPERFICIES`.

## Ordem de leitura para retomar o projeto

### Se a meta e entender o projeto no macro
1. `README.md`
2. `AI_CONTEXT.md`
3. `LORE/north_star.yaml`

### Se a meta e retomar a fase ativa
1. `README.md`
2. `AI_CONTEXT.md`
3. `Revisao/README.md`
4. `Revisao/000_COMECAR_AQUI.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/000_INDEX_SISTEMA_REVISAO.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
10. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`
11. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md`, quando necessario
12. licao alvo + anterior + seguinte
13. caso relevante em `Revisao/FEEDBACK_MAES_REAIS/`, se houver

## Regra de manutencao

1. se mudar a visao geral do projeto, atualizar `README.md`;
2. se mudar o estado real da fase, atualizar `AI_CONTEXT.md`;
3. se mudar o andamento do lote, atualizar `005_STATUS_REVISAO_SEMENTES.md`;
4. se mudar o metodo, atualizar `023`, `003`, `004`, `002` ou `010_TEMPLATE`;
5. se um arquivo historico voltar a competir com o contexto vivo, corrigir o apontador no mesmo dia.
