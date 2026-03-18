# GUIA CENTRAL - ATIVACAO DA REVISAO TOPICO A TOPICO
Data: 2026-03-17
Status: canonico
Escopo: fonte central unica para ativar a revisao premium de licoes `Sementes`

---

## 1) Missao deste guia
Este arquivo existe para ser a fonte central unica da ativacao do protocolo.

Ele deve permitir que uma IA ou um humano:
1. saiba o que abrir e em que ordem;
2. pense primeiro no macro da licao antes de mexer nos blocos;
3. projete o cerne da ideia da licao sobre os 12 topicos oficiais;
4. revise ponto a ponto sem pular secoes nem confundir fronteiras;
5. entregue uma licao pronta para validacao humana final da Familia Rodrigues.

---

## 2) Regra de autoridade e anti-duplicacao
Este guia e a fonte unica para:
1. ordem oficial de ativacao;
2. leitura minima antes do primeiro patch;
3. construcao do cerne macro da licao;
4. algoritmo de revisao ponta a ponta;
5. definicao do pacote minimo de leitura para a IA entrar numa licao sem intuicao frouxa.

Cada arquivo satelite deve servir a uma funcao especifica:
1. `023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`: ativacao, ordem de leitura, cerne macro, algoritmo.
2. `003_PROTOCOLO_REVISAO_POR_LICAO.md`: execucao da revisao, patch, reauditoria, gates e formato de log.
3. `004_RUBRICA_PREMIUM_REVISAO.md`: pontuacao, thresholds e veredito.
4. `005_STATUS_REVISAO_SEMENTES.md`: fase atual, backlog e proximo passo seguro.
5. `010_TEMPLATE_SESSAO_DIARIA_REVISAO.md`: template preenchivel da sessao.
6. `011_TOPICOS/`: contrato de cada topico.
7. `012_TRANSVERSAIS/`: regras que atravessam varios topicos.
8. tasks `016+`: memoria de aplicacao e historico, nao fonte procedural primaria.

Regra:
1. se o passo a passo de ativacao mudar, mudar primeiro este `023`;
2. os demais arquivos devem apontar para este guia em vez de repetir a mesma lista;
3. evitar criar task nova para reescrever regras que ja moram aqui.

---

## 3) Base de discernimento desta fase
Este guia foi estabilizado em coerencia com:
1. `Charlotte Mason`: dignidade da crianca, licao curta, narracao, coisas antes de sinais;
2. `Jerome Bruner`: concreto dominante, descoberta guiada, curriculo em espiral;
3. `Susan Macaulay`: funcao real em casa com bebe no colo e feijao no fogo;
4. `Mae Ansiosa`: reduzir medo, clarificar fruto e evitar comparacao toxica;
5. `Mae Veterana` e `UX Familias`: leveza, honestidade e viabilidade multi-crianca.

Consequencia pratica:
1. a revisao nao fecha em teoria bonita;
2. a revisao precisa produzir uma licao usavel, viva, concreta e premium.
3. quando houver feedback real de mae, ele entra como calibragem qualificada do uso real e do `TASTE`.

---

## 4) Ordem oficial de leitura antes de revisar uma licao
Abrir sempre nesta ordem:
1. `README.md`
2. `AI_CONTEXT.md`
3. `Revisao/README.md`
4. `Revisao/000_COMECAR_AQUI.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/000_INDEX_SISTEMA_REVISAO.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
10. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
11. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/000_README.md`
12. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/001_BASE_E_HERO.md` ate `012_NAVEGACAO_INFERIOR.md`, na ordem oficial
13. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/000_README.md`
14. pacote minimo transversal: `002`, `003`, `005`, `006`, `008`, `009`
15. quando houver criacao de licao, reescrita profunda, imagem dominante nebulosa ou duvida sobre ancora concreta do conceito, abrir tambem `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md`
16. licao atual
17. licao anterior
18. licao seguinte
19. task especifica da licao, se existir
20. caso e sintese de `Revisao/FEEDBACK_MAES_REAIS/`, se houver feedback real relevante
21. `Revisao/00_SISTEMA_REVISAO_CANONICO/010_TEMPLATE_SESSAO_DIARIA_REVISAO.md`

Regra:
1. transversais adicionais entram por necessidade;
2. `010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md` e a transversal indicada quando a dificuldade principal for encarnar melhor o conceito sem perder rigor;
3. os 12 topicos sempre entram;
4. nenhuma licao deve ser auditada isoladamente do seu antes e depois;
5. `001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md` e `015_ESTADO_REAL...` ficam como apoio historico e entram so quando ajudarem a explicar uma tensao antiga.

---

## 5) Congelamento de escopo da sessao
Antes de editar:
1. nomear quais licoes entram na sessao;
2. nomear o que esta fora de escopo;
3. registrar se a sessao mexe no sistema, na licao ou nos dois;
4. registrar se a validacao humana da Familia Rodrigues ja ocorreu ou ainda esta pendente.

Regra:
1. sem escopo congelado, a revisao vira deriva;
2. mexer em sistema e licao na mesma sessao e permitido, desde que o fluxo continue macro -> topicos -> auditoria.

---

## 6) Cerne macro da licao
Antes de olhar topico por topico, preencher o cerne macro da licao.

Registrar no minimo:
1. `Promessa da licao`: o que a crianca vai tocar ou perceber hoje.
2. `Guardiao`: quem conduz a experiencia.
3. `Lugar`: qual local o Ritual revela.
4. `Conceito vivo`: qual verdade matematica concreta esta encarnada.
5. `Papel no curriculo mestre`: por que este passo existe agora em `TGTB`.
6. `Imagem dominante`: qual imagem precisa atravessar a pagina sem ser trocada por sinonimos frouxos.
7. `Fruto do dia`: o que conta como sucesso real hoje.
8. `Risco de fronteira`: onde a licao pode confundir topicos adjacentes.
9. `Risco familia real`: onde uma casa cansada, com mais de uma crianca, pode travar.
10. `Hospitalidade multi-crianca`: como um irmao menor pode entrar sem dissolver o foco do herdeiro de `5-6 anos`.
11. `Ancora concreta`: onde o conceito pousa melhor na criacao, na casa, no corpo, no ritmo, no caminho ou em objetos cotidianos.
12. `Frase de boca do Portador`: a formulacao que realmente cabe na voz do adulto em casa.
13. `Pergunta respondivel principal`: a pergunta mais viva que a crianca consegue responder sem traducao adulta.
14. `Microfriccoes previsiveis`: ambiguidades, nomes frouxos, comandos escondidos ou trocas de concreto que podem gerar atrito fino depois.

Regra:
1. nao patchar HTML antes de esse cerne estar claro;
2. se a imagem dominante ou o fruto do dia estiverem nebulosos, diagnosticar antes de editar;
3. se a ancora concreta tambem estiver nebulosa, abrir `010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md` antes de patchar;
4. a frase de boca, a pergunta respondivel principal e as microfriccoes previsiveis devem ser travadas antes do primeiro patch forte;
5. a matriz `001-012` deve ser lida a partir deste cerne, nao contra ele.

---

## 7) Projecao macro sobre os 12 topicos
Depois de formar o cerne, pensar a licao inteira antes de alterar qualquer bloco.

Perguntas obrigatorias:
1. como a promessa da licao aparece em `001-012` sem fragmentar a pagina?
2. qual topico carrega o peso principal da descoberta hoje?
3. qual topico corre risco de roubar a funcao do outro?
4. a progressao `Ritual -> Jornada -> O Concreto -> Narramos -> Fechamento -> Conexao -> Sementes -> Formacao` respira?
5. o adulto termina a pagina mais leve, mais seguro e mais capaz?

Regra:
1. primeiro enxergar o arco inteiro;
2. so depois entrar na auditoria ponto a ponto.

---

## 8) Algoritmo oficial da revisao
Executar nesta ordem:
1. ativar a leitura minima oficial;
2. congelar o escopo da sessao;
3. preencher o cerne macro da licao;
4. rodar a passada premium antecipada ainda no plano da licao;
5. preencher a matriz `001-012` com `PASS / GAP / BLOCK`;
6. auditar as fronteiras criticas;
7. classificar findings por severidade;
8. patchar primeiro estrutura e fronteiras;
9. patchar depois narrativa e pedagogia;
10. irradiar os ajustes para ecos proximos da licao inteira;
11. rodar a passada premium final de microdetalhes;
12. reauditar os topicos tocados e seus vizinhos imediatos;
13. fechar a rubrica;
14. registrar veredito honesto;
15. entregar a licao para validacao humana final da Familia Rodrigues.

Fronteiras criticas obrigatorias:
1. `003 -> 004`
2. `004 -> 005`
3. `005 -> 006`
4. `006 -> 007`
5. `008 -> 009`
6. `009 -> 010`
7. `010 -> 011`
8. `011 -> 012`

---

## 9) Regra operacional por camada
### Macro
1. proteger promessa, imagem dominante, fruto e papel curricular.

### Topicos
1. auditar todos os 12;
2. nao pular topico "obvio".

### Fronteiras
1. impedir que secoes vizinhas facam quase o mesmo trabalho.

### Patch
1. estrutura antes de prosa;
2. pedagogia antes de perfume;
3. pergunta respondivel antes de pergunta bonita;
4. um concreto por vez;
5. comando visivel no ponto certo;
6. `Taste` so fecha depois de funcao, clareza, respiracao e radiacao local.

### Reauditoria
1. topico tocado;
2. vizinho anterior;
3. vizinho seguinte;
4. gate de encoding, se houver HTML.

---

## 10) Saidas obrigatorias da sessao
Ao final de uma revisao robusta, deve existir:
1. registro da sessao no `010_TEMPLATE_SESSAO_DIARIA_REVISAO.md` ou documento equivalente;
2. licao patchada;
3. matriz `001-012` fechada;
4. veredito da rubrica;
5. registro de risco residual;
6. indicacao clara se a Familia Rodrigues ainda precisa validar.

Regra:
1. `aprovado por IA` nao substitui validacao humana final;
2. o melhor fechamento de uma IA e `alinhada ao protocolo e pronta para validacao humana`.

---

## 11) Definition of Ready de uma licao para entrar em revisao
1. arquivo correto identificado;
2. licao anterior e proxima abertas;
3. guia central `023` consultado;
4. cerne macro preenchido;
5. frase de boca, pergunta respondivel principal e microfriccoes previsiveis registradas;
6. topicos `001-012` abertos;
7. pacote minimo transversal aberto;
8. escopo congelado.

## 12) Definition of Done de uma licao revisada
1. matriz `001-012` completa;
2. fronteiras criticas auditadas;
3. `BLOCK` duro inexistente;
4. passada premium antecipada concluida;
5. radiacao local concluida;
6. passada premium final de microdetalhes concluida;
7. rubrica fechada com veredito honesto;
8. HTML relido apos patch;
9. risco residual nomeado;
10. pronta para validacao humana da Familia Rodrigues.

---

## 13) Regra de manutencao do sistema
1. se uma regra procedural aparecer repetida em varios arquivos, ela deve morar aqui;
2. se um arquivo satelite estiver explicando de novo a ativacao completa, simplificar e apontar para `023`;
3. contratos de topico ficam nos topicos;
4. regras transversais ficam nos transversais;
5. tarefas historicas documentam aplicacoes, nao governanca.
