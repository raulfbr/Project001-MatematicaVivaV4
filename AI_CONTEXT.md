# AI CONTEXT - Matemática Viva

Data de atualização: 2026-03-16
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

1. a frente ativa continua sendo a revisão `HTML-first`;
2. a experiência final real ainda vive principalmente em `site/sementes/*.html`;
3. o protocolo de revisão está consolidado em `023`, com execução em `003`, veredito em `004` e quadro operacional em `005`;
4. o `Manual do Portador`, `MV-S-001` e `MV-S-002` já passaram por rodada profunda e auditoria por IA;
5. o lote `MV-S-004` ate `MV-S-015` tambem ja passou por reauditoria profunda por IA nesta frente, com logs e governanca atualizados;
6. `005_STATUS_REVISAO_SEMENTES.md` continua sendo o quadro operacional base, mas a leitura correta do momento precisa incluir este fechamento de `2026-03-16`;
7. existe trilha técnica paralela em `apps/web`, mas ela não governa a sessão atual por padrão.

## Fechamento da sessao de hoje - 2026-03-16

1. a sessao de hoje fechou o lote `L004-L015` no nivel de reauditoria por IA;
2. as licoes publicadas desse lote ficaram limpas de residuos estruturais mais recorrentes da fase;
3. os logs do dia foram alinhados ao que realmente foi feito;
4. a governanca tambem foi ajustada para deixar claro que:
   a. `AI_CONTEXT.md` + `005_STATUS_REVISAO_SEMENTES.md` sao a leitura viva atual;
   b. `015_ESTADO_REAL...` e apoio historico, nao SSOT da fase.
5. foi criada uma task de fechamento do lote:
   `Revisao/00_SISTEMA_REVISAO_CANONICO/046_TASK_ROBUSTA_FECHAMENTO_PREMIUM_LOTE_L008_L015_E_GOVERNANCA.md`.
6. o proximo gate principal nao e novo patch automatico, e sim:
   a. validacao humana real com familias;
   b. eventual sincronizacao curricular dos YAMLs;
   c. manutencao disciplinada da governanca viva.
7. em reauditorias profundas desta fase, o arquivo `010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md` passa a ser a lente principal sempre que houver friccao de ancora concreta, imagem dominante, encarnacao do conceito ou pressao indevida sobre a mae.

## O que o projeto ja sabe sobre maes reais

Leitura correta:

1. o projeto ja reconhece explicitamente que o produto e para maes reais em contexto real;
2. a pasta `Revisao/FEEDBACK_MAES_REAIS/` existe justamente para impedir que esse ouro se perca;
3. o sistema ja diferencia critica local, sintese transversal e canonizacao;
4. o feedback da mae deve registrar nao so o que falhou, mas tambem o que ela validou;
5. o melhor uso desse feedback nao e obediencia cega, e sim aprendizado editorial e operacional.

Pergunta de controle:

1. estamos ouvindo a mae real como evidencia qualificada ou apenas reagindo ao ultimo comentario?

## Tensão documental que precisa ser lida corretamente

Hoje há um ponto de atenção importante:

1. `README.md` antigo, `015_ESTADO_REAL...` e `001_CONTEXTO...` preservavam um momento em que o próximo passo seguro ainda era validar humano antes de abrir `MV-S-003`;
2. o quadro mais recente em `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md` já registra avanço do lote `MV-S-003` até `MV-S-010`;
3. portanto, não basta abrir um documento isolado e assumir que ele resume tudo.

Regra de leitura:

1. `README.md` = macro;
2. `AI_CONTEXT.md` = interpretação correta do momento;
3. `005_STATUS_REVISAO_SEMENTES.md` = estado operacional mais atual da fase;
4. `023/003/004` = método canônico de execução.

## Decisões já tomadas

1. a pasta `Revisao/` é a governança viva da fase ativa;
2. a revisão atual deve ser lida como `HTML-first`;
3. o HTML real publicado é artefato principal de revisão, não mero output descartável;
4. `TASTE` editorial é diferencial de produto, não enfeite;
5. feedback real de famílias entra como calibragem qualificada, não como volante automático;
6. orquestração multiagente pesada não é o gargalo principal agora;
7. o North Star precisa governar a leitura do projeto, não ficar como documento decorativo;
8. o repositório precisa de uma retomada mais confiável, centralizada e menos contraditória.
9. feedback real de maes deve ser tratado como ativo de produto e de sistema, nao como anexo secundario.
10. `TASTE`, `premium`, `experts` e `feedback real` fazem parte do nucleo de qualidade desta fase.

## O que não fazer agora

1. não tratar `apps/web` como centro da fase por default;
2. não usar apenas tasks históricas como onboarding;
3. não tomar um único handoff antigo como verdade final do estado atual;
4. não confundir protocolo bonito com fidelidade real ao espírito da obra;
5. não abrir novas camadas documentais para cada sessão sem necessidade clara.
6. nao revisar licoes ignorando o que a trilha `FEEDBACK_MAES_REAIS/` ja ensinou.
7. nao confundir gosto pessoal isolado com evidência recorrente de mae real.

## Próximo passo seguro

Em termos de governança de documentação:

1. usar este `AI_CONTEXT.md` como ponto central de retomada;
2. usar `README.md` como portal estável;
3. deixar `Revisao/` com papel cada vez mais operacional e menos de onboarding geral;
4. reduzir duplicação futura, atualizando contexto vivo aqui em vez de criar handoffs paralelos.

Em termos de fase de revisão:

1. consultar `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`;
2. seguir a task ativa do lote vigente, lendo esse quadro junto do fechamento desta sessao;
3. executar sempre via `023 -> 003 -> 004`, com apoio de `011_TOPICOS/` e `012_TRANSVERSAIS/`;
4. usar `008_NORTH_STAR_OPERACIONAL.md` como gate real antes de considerar uma lição pronta.
5. quando houver caso relevante de mae real, consultar tambem `Revisao/FEEDBACK_MAES_REAIS/` antes de patchar.
6. quando houver desempate fino ou fechamento premium, consultar tambem `009_TASTE_EDITORIAL_E_AUTORIA_HUMANA.md`.
7. quando a reauditoria profunda envolver ancora concreta, imagem dominante, encarnacao do conceito ou friccao de usabilidade da mae real, consultar explicitamente `010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md`.

## Ordem de leitura para retomar o projeto

### Se a meta é entender o projeto no macro

1. `README.md`
2. `AI_CONTEXT.md`
3. `LORE/north_star.yaml`

### Se a meta é retomar a fase ativa

1. `README.md`
2. `AI_CONTEXT.md`
3. `Revisao/README.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md`, quando a reauditoria for profunda ou a mae real ainda exigir traducao mental
9. lição alvo + lição anterior + lição seguinte
10. caso relevante em `Revisao/FEEDBACK_MAES_REAIS/`, se houver friccao semelhante
11. `009_TASTE_EDITORIAL_E_AUTORIA_HUMANA.md`, quando o fechamento premium exigir desempate fino

### Se a dúvida é "onde mora cada tipo de verdade?"

1. identidade: `LORE/`
2. currículo: `curriculo/`
3. produto real: `site/`
4. execução da revisão: `Revisao/`
5. contexto vivo: `AI_CONTEXT.md`

## Regra de manutenção

1. se mudar a visão geral do projeto, atualizar `README.md`;
2. se mudar o estado real da fase, atualizar `AI_CONTEXT.md`;
3. se mudar o andamento do lote de revisão, atualizar `005_STATUS_REVISAO_SEMENTES.md`;
4. se mudar o método, atualizar `023`, `003`, `004` ou documentos canônicos correlatos;
5. evitar criar novo arquivo de handoff se uma atualização em `AI_CONTEXT.md` resolver.
