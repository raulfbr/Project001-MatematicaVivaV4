# TASK ROBUSTA - AUDITORIA SISTEMICA DE REENTRADA E COERENCIA DOCUMENTAL
Data: 2026-03-17
Status: feito
Escopo: garantir retomada correta do projeto e coerencia entre contexto vivo, quadro vivo, protocolo e trilha publicada

---

## 1) Objetivo
Esta task existe para fechar um risco sistemico da fase:

1. a proxima sessao podia recomecar pelo arquivo errado;
2. handoffs historicos ainda podiam competir com `README.md`, `AI_CONTEXT.md` e `005_STATUS_REVISAO_SEMENTES.md`;
3. parte da documentacao interna ainda soava mais ensaistica do que operacional.

Meta:
1. consolidar uma ordem unica de reentrada;
2. alinhar os docs vivos com o corte publicado em `MV-S-015`;
3. garantir que o sistema comece a proxima secao ja entendendo macro, contexto vivo e protocolo correto;
4. reforcar que escrita interna funcional deve ser pratica, curta e acionavel.

---

## 2) Escopo auditado
Arquivos auditados nesta rodada:

1. `README.md`
2. `AI_CONTEXT.md`
3. `Revisao/README.md`
4. `Revisao/000_COMECAR_AQUI.md`
5. `Revisao/001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/000_INDEX_SISTEMA_REVISAO.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/010_TEMPLATE_SESSAO_DIARIA_REVISAO.md`
10. `Revisao/00_SISTEMA_REVISAO_CANONICO/015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md`
11. `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
12. `site/index.html`
13. `site/templates/index.j2`
14. `site/sementes/MV-S-015_A_ESCADA_DE_LUZ.html`
15. `site/sementes/MV-S-016_O_BANDO_QUE_CRESCE.html`
16. `site/sementes/MV-S-017_O_HORIZONTE_ALÉM.html`
17. `site/sementes/MV-S-025_A_COMITIVA_DO_DEZ.html`

---

## 3) Findings principais

### 3.1 Risco de reentrada errada
Problema:
1. a ordem de retomada nao estava identica entre `README`, `AI_CONTEXT`, `000_INDEX` e `023`;
2. em alguns pontos, `001_CONTEXTO...` e `015_ESTADO_REAL...` ainda apareciam cedo demais.

Impacto:
1. uma nova sessao podia gastar energia em material historico antes de abrir o quadro vivo;
2. a IA podia herdar contexto parcial ou antigo antes de chegar ao protocolo correto.

### 3.2 Drift entre contexto vivo e protocolo
Problema:
1. `023` ainda carregava ordem antiga de leitura;
2. `000_INDEX` nao se incluia claramente como parte da trilha de reentrada;
3. `010_TEMPLATE` ainda nao obrigava consulta explicita de `README`, `AI_CONTEXT`, `000_COMECAR_AQUI` e `000_INDEX`.

Impacto:
1. a governanca dizia uma coisa e a ativacao pratica ainda podia fazer outra;
2. a criacao/revisao futura podia nascer sem contexto suficiente.

### 3.3 Escrita interna pouco pratica em zonas funcionais
Problema:
1. parte da documentacao ainda usava formulacao mais ampla do que o necessario em arquivos operacionais;
2. isso reduz velocidade de leitura e aumenta risco de releitura.

Impacto:
1. pior onboarding de sessao;
2. menor capacidade de usar o sistema como checklist real.

---

## 4) Decisoes canonicas fechadas

### 4.1 Ordem canonica de reentrada
Para retomar o projeto com seguranca:

1. `README.md`
2. `AI_CONTEXT.md`
3. `Revisao/README.md`
4. `Revisao/000_COMECAR_AQUI.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/000_INDEX_SISTEMA_REVISAO.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`

Uso complementar:
1. `001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md` = apoio historico;
2. `015_ESTADO_REAL...` = apoio historico;
3. `010_LENTE_ENCANTAMENTO...` = abrir quando houver criacao, reescrita profunda, imagem dominante fraca ou traducao mental da mae.

### 4.2 Regra de escrita interna
Para docs funcionais do sistema:

1. orientar antes de ornamentar;
2. usar listas acionaveis;
3. nomear proximo passo seguro;
4. evitar poesia em zonas de operacao;
5. deixar o tom literario para narrativa da licao, nao para checklist interno.

---

## 5) Correcoes aplicadas
1. `README.md`: reforcada a ordem pratica de retomada logo na abertura.
2. `AI_CONTEXT.md`: data atualizada e mantida a funcao de contexto vivo.
3. `Revisao/001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md`: rebaixado explicitamente para apoio historico e redirecionado para `000_COMECAR_AQUI`, `000_INDEX` e `005`.
4. `000_INDEX_SISTEMA_REVISAO.md`: corrigida a lista de ponto de entrada para incluir o proprio index e registrada esta task `049`.
5. `023_GUIA_CENTRAL...`: corrigida a ordem oficial de leitura para refletir o fluxo vivo atual.
6. `010_TEMPLATE_SESSAO_DIARIA_REVISAO.md`: ativacao agora exige marcar consulta de `README`, `AI_CONTEXT`, `Revisao/README`, `000_COMECAR_AQUI` e `000_INDEX`.
7. `015_ESTADO_REAL...`: texto interno ajustado para leitura mais pratica e aderente ao novo apontamento documental.
8. `005_STATUS_REVISAO_SEMENTES.md`: registrada esta auditoria como ativo concluido da fase.

---

## 6) Confirmacoes do site e da trilha publicada
Confirmado nesta rodada:

1. `site/index.html` nao deve expor `MV-S-016+` em cards;
2. `site/templates/index.j2` limita os cards publicados ate `MV-S-015`;
3. `MV-S-015` continua como ultimo passo da trilha ativa;
4. `MV-S-016` funciona como pagina de continuidade em construcao;
5. `MV-S-017+` permanecem fora da trilha publicada e redirecionam para `MV-S-016` ou home.

---

## 7) Definition of Done desta task
Esta task so fecha se:

1. `README`, `AI_CONTEXT`, `000_INDEX`, `005` e `023` apontarem para a mesma ordem de retomada;
2. `001_CONTEXTO...` e `015_ESTADO_REAL...` estiverem claramente marcados como apoio historico;
3. o template diario obrigar consulta do contexto vivo antes do patch;
4. a trilha publicada continuar coerente com `MV-S-015` como ultimo ponto publico;
5. os docs internos funcionais soarem praticos o bastante para uso real de sessao.

---

## 8) Proximo passo seguro
1. ao iniciar a proxima secao, abrir `README.md` e `AI_CONTEXT.md` antes de qualquer licao;
2. usar `005_STATUS_REVISAO_SEMENTES.md` para decidir o alvo real da rodada;
3. ativar a sessao por `023`;
4. revisar ou criar a licao alvo ja sob o protocolo endurecido com passada premium antecipada, radiacao local e passada premium final.
