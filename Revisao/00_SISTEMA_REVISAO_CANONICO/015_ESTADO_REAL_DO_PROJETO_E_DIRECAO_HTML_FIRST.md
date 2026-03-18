# ESTADO REAL DO PROJETO E DIRECAO DA REVISAO HTML-FIRST
Data: 2026-03-17
Escopo: projeto inteiro, com foco na fase ativa
Status: canonico para orientacao e retomada

---

## 1) Objetivo deste documento
1. registrar onde o projeto esta de verdade;
2. separar trilha ativa de trilha experimental;
3. reduzir drift entre documentacao, codigo e operacao;
4. servir como ancora rapida para entender o projeto antes de revisar HTML.

---

## 2) Sintese executiva
1. `Matematica Viva` e, antes de tudo, um sistema editorial, pedagogico e narrativo para familias.
2. O software existe para servir o conteudo, a experiencia da familia e a governanca da revisao.
3. Hoje, a experiencia final real vive principalmente em `site/sementes/*.html`, nao no piloto Next.
4. A trilha `apps/web` e importante, mas ainda e piloto tecnico contrato-first, nao a frente operacional principal da revisao premium.
5. A trilha publicada do site foi conscientemente cortada em `MV-S-015`; `MV-S-016` virou pagina de continuidade em construcao e `MV-S-017+` aguardam reconstrucao antes de voltar ao publicado.

Frase-sintese:
1. o coracao do projeto esta em `LORE` + `curriculo` + `site/sementes` + `Revisao`; o `apps/web` ainda esta provando infraestrutura.

---

## 3) Arquitetura real em camadas

### 3.1 Canon e identidade da obra
Fonte principal:
1. `LORE/north_star.yaml`
2. `LORE/guardioes.yaml`
3. `LORE/padroes_narrativos.yaml`
4. arquivos SSOT adjacentes de locais, climas e evolucao

Papel:
1. definir identidade;
2. fixar tom;
3. fixar guardioes;
4. governar progressao K-12;
5. impedir que a licao invente canon local.

### 3.2 Materia-prima curricular
Fonte principal:
1. `curriculo/01_SEMENTESV6/*.yaml`
2. `curriculo/_SISTEMA/`

Papel:
1. guardar o conteudo-base das licoes;
2. manter estrutura curricular;
3. sustentar navegacao, linkage e progressao de conceitos.

### 3.3 Experiencia final publicada hoje
Fonte principal:
1. `site/sementes/*.html`
2. `site/sementes/templates/`
3. `site/sementes/style.css`
4. `site/index.html` e demais paginas do `site/`

Papel:
1. entregar a experiencia que a familia realmente ve;
2. concentrar o trabalho premium de narrativa, clareza e leitura;
3. materializar o produto atual em uso.

### 3.4 Governanca da revisao
Fonte principal:
1. `Revisao/`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/`
3. `Revisao/01_REFERENCIAS_DE_APOIO/`

Papel:
1. transformar criterio em processo;
2. garantir que a revisao do HTML aconteca com contrato, rubrica e North Star;
3. impedir retrabalho circular e drift de qualidade.

### 3.5 Trilha tecnica futura e experimental
Fonte principal:
1. `apps/web/`
2. `content/lessons/`
3. `dist/`

Papel:
1. provar modelo contrato-first;
2. validar variantes, artefatos e relatorios;
3. preparar uma possivel migracao futura de pipeline.

Regra:
1. importante para a estrategia tecnica;
2. nao e, hoje, a fonte primaria da experiencia HTML revisada.

---

## 4) Fatos verificados nesta rodada

### 4.1 Documentacao e operacao ainda exigem disciplina de leitura
1. o repositorio continua guardando duas trilhas reais: a operacional `HTML-first` e a tecnica futura em `apps/web`;
2. a documentacao viva agora aponta de forma mais clara para `README.md` -> `AI_CONTEXT.md` -> `Revisao/README.md` -> `000_COMECAR_AQUI` -> `000_INDEX` -> `005`;
3. `001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md` e `015_ESTADO_REAL...` seguem uteis, mas como apoio historico e nao como SSOT.

Conclusao operacional:
1. a trilha ativa da sessao continua sendo a do HTML final;
2. contexto vivo e quadro vivo precisam ser lidos antes de qualquer retomada ou patch.

### 4.2 Pipeline Python/Jinja continua sendo o fluxo mais proximo da operacao atual
Verificado:
1. `python build/forge.py --fase sementes --dry-run` quebra em Windows CP1252 por emoji no logger.
2. com `PYTHONIOENCODING=utf-8`, o dry-run passou.
3. o dry-run validou 26 licoes e ignorou `_TEMPLATE_V6.yaml`.

Conclusao:
1. o bloqueio principal atual do Forge em Windows nao foi YAML quebrado, e sim encoding de terminal.

### 4.3 O HTML publicado das licoes iniciais esta protegido de overwrite automatico
Verificado em `build/fases/sementes.py`:
1. o driver calcula navegacao normalmente;
2. depois aplica filtro manual que pula render de `MV-S-000` ate `MV-S-025`.

Conclusao:
1. as licoes iniciais em `site/sementes/*.html` nao devem ser tratadas como output puro e facilmente regeneravel;
2. elas estao, na pratica, em regime de preservacao manual;
3. isso reforca que a revisao precisa olhar o HTML real como artefato principal.

### 4.4 Existe bug latente no driver de Sementes
Verificado:
1. `self.logger.warning(...)` aparece na validacao;
2. esse atributo nao existe nesse driver.

Conclusao:
1. o caminho feliz atual nao bate nesse ponto;
2. mas o bug continua la e pode explodir quando houver caso invalido.

### 4.5 O piloto Next esta tecnicamente verde, mas ainda e piloto de infraestrutura
Verificado:
1. `npm run validate:contract` passou;
2. `npm run validate:lessons:preview` passou;
3. `npm run build:artifacts` gerou artefatos para 3 licoes;
4. `npm run qa:reports` gerou `quality_report.json` com media 95 e zero bloqueios.

Tambem verificado:
1. o loader do piloto conhece apenas `MV-S-000`, `MV-S-001` e `MV-S-022`;
2. o renderer atual ainda mostra blocos em formato cru, proximo de dump de contrato.

Conclusao:
1. o piloto Next hoje prova contrato, variantes, navegacao e relatorios;
2. ele ainda nao prova experiencia premium final para familia.

### 4.6 Existe bloqueio de path para build Next no ambiente atual
Verificado:
1. `apps/web/scripts/build-web.ts` bloqueia `next build` se o path absoluto contiver `!`.

Conclusao:
1. neste workspace, o build full web continua sensivel ao path atual;
2. isso e detalhe tecnico real e nao deve ser esquecido em futuras sessoes.

### 4.7 O repositorio ja explorou orquestracao multi-agente
Verificado:
1. `bmad/orchestrator.yaml` define `super_agent`, `REVISAO`, `DELIBERACAO_AUTONOMA` e comando `/revisar-licao-auto`.
2. essa trilha existe como repertorio tecnico e historico dentro do repositorio.

Conclusao:
1. o projeto nao esta "atrasado" nesse tema; ele ja experimentou essa direcao;
2. o gargalo atual nao e falta de harness;
3. tentar subir multi-agent pesado agora tenderia a ser overengineering para a fase ativa.

### 4.8 O diferencial de curto prazo esta em `TASTE` editorial + feedback real
Verificado:
1. `MV-S-001` recebeu um recorte dirigido forte depois de caca explicita a `metaforas soltas`, mas ainda nao fechou leitura topica completa;
2. os proximos ganhos mais valiosos estao em unidade de imagem, leveza do Portador, tom vivo e realidade de uso;
3. ha valor claro em tratar feedback real de familias como calibracao de produto, sem entregar o volante ao feedback bruto.

Conclusao:
1. `TASTE` e hoje um fator de produto, nao ornamento;
2. feedback real de familias deve entrar como dado qualificado para calibrar a experiencia;
3. se o ciclo consolidar feedback de `4 familias`, isso tende a tornar o produto mais estruturado e mais real;
4. se algum apoio automatizado for usado, ele deve vir em forma de papeis e lentes leves, nao de orquestracao pesada.

### 4.9 A trilha publicada foi conscientemente reduzida para proteger o premium
Verificado:
1. o dashboard publico foi cortado em `MV-S-015`;
2. `MV-S-016` foi convertido em pagina de continuidade em construcao;
3. `MV-S-017+` sairam da trilha publicada enquanto o protocolo de criacao e revisao e endurecido.

Conclusao:
1. o projeto nao esta tentando manter publicado algo que ainda nao passou pelo padrao premium atual;
2. reconstruir melhor antes de republicar vale mais do que manter volume publicado com drift de qualidade;
3. a trilha publicada agora precisa ser tratada como contrato vivo, nao como espelho automatico do acervo historico.

---

## 5) Leitura correta do momento do projeto
1. o repositorio nao esta sem direcao;
2. ele esta em coexistencia controlada de duas frentes:
   a. frente de produto real em HTML estatico;
   b. frente de infraestrutura futura em Next/TypeScript.

Decisao operacional correta para agora:
1. fortalecer `Revisao/`;
2. usar `Revisao/` para auditar e padronizar o HTML real;
3. elevar `TASTE` a criterio operacional explicito;
4. usar feedback real de familias como calibracao qualificada;
5. manter a trilha publicada conscientemente limitada a `MV-S-015` enquanto `MV-S-016+` sao reconstruidas;
6. somente depois entrar em nova escala de licoes futuras;
7. deixar a trilha Next como apoio tecnico e referencia de contrato, nao como condutora da fase atual.

---

## 6) O que isso implica para a pasta `Revisao`
1. `Revisao` precisa governar o HTML real, nao uma interface futura hipotetica.
2. Todo documento da pasta deve assumir `site/sementes/*.html` como artefato sob auditoria.
3. Quando houver conflito entre:
   a. README raiz;
   b. docs legados;
   c. piloto Next;
   d. fluxo HTML-first;
   vence a frente ativa declarada para a fase.
4. O North Star precisa funcionar como gate real, nao como decoracao conceitual.
5. Descobertas de drift documental precisam ser registradas, nao apenas percebidas.

---

## 7) Regras praticas para as proximas sessoes
1. abrir primeiro este documento;
2. depois abrir `Revisao/README.md`;
3. depois abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/000_INDEX_SISTEMA_REVISAO.md`;
4. depois abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`;
5. so entao decidir a menor proxima acao segura.

Antes de editar qualquer licao:
1. confirmar se o artefato-alvo e o HTML final ou o YAML base;
2. confirmar o que esta sob preservacao manual;
3. confirmar se a licao esta na trilha publicada ou em reconstrucao;
4. confirmar as transversais que governam a secao;
5. confirmar que o sistema de revisao esta suficiente para sustentar a decisao.

Ao usar o Forge no Windows:
1. lembrar de `PYTHONIOENCODING=utf-8`.

Ao usar `apps/web`:
1. lembrar que o lote atual e de 3 licoes;
2. lembrar que a UI ainda nao e a experiencia premium final;
3. lembrar que `next build` fica bloqueado no path atual com `!`.

---

## 8) Estado de decisao neste momento
Fatos de decisao:
1. a frente ativa e a revisao HTML-first;
2. a pasta `Revisao` foi reorganizada e esta virando a governanca central da fase;
3. o protocolo central agora esta consolidado em `023` e auditado em `028`;
4. `Manual do Portador`, `MV-S-001` e `MV-S-002` ja passaram por rodada profunda e estao prontos para validacao humana;
5. `MV-S-003` e `MV-S-004` ja receberam rodadas profundas com feedback real forte;
6. a trilha publicada foi conscientemente reduzida a `MV-S-015`;
7. o proximo foco correto e fechar `MV-S-005` ate `MV-S-010` e so depois decidir a volta de `MV-S-016+`.

---

## 9) Definition of Ready para sair de sistema e entrar em licoes
1. este documento estiver integrado na navegacao principal da pasta;
2. `000_COMECAR_AQUI`, `README`, `000_INDEX` e `005_STATUS` apontarem para a mesma leitura do estado atual;
3. topicos e transversais estiverem legiveis sem drift de naming;
4. o piloto `001-003` tiver criterio claro de entrada;
5. qualquer IA nova conseguir responder em ate 2 minutos:
   a. onde estamos;
   b. qual trilha esta ativa;
   c. qual e o proximo passo seguro.

---

## 10) Veredito
1. o projeto esta tecnicamente bifurcado, mas operacionalmente inteligivel;
2. o HTML final continua sendo o centro da fase atual;
3. `Revisao` precisa ser tratada como sistema de governanca, nao apenas pasta de apoio;
4. o diferencial de curto prazo esta em `TASTE` editorial e realidade de uso familiar;
5. a trilha publicada atual vai somente ate `MV-S-015` por decisao de qualidade, nao por acaso;
6. a decisao correta agora e fechar `Revisao` com rigor antes de republicar `MV-S-016+`.

Frase final:
1. primeiro protocolo forte, depois feedback real incorporado, depois validacao humana, depois escala com seguranca.
