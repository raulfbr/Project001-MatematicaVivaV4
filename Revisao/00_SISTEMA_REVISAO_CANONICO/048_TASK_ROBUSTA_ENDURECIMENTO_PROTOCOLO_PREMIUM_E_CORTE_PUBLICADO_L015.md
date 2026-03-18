# TASK ROBUSTA - ENDURECIMENTO DO PROTOCOLO PREMIUM E CORTE PUBLICADO EM L015
Data: 2026-03-17
Status: concluida
Escopo: governanca do sistema, trilha publicada do site e protocolo de criacao/revisao

---

## 1) Objetivo
Esta task existe para registrar uma decisao de produto e sistema tomada na fase HTML-first:

1. a trilha publicada de `Sementes` passa a ir apenas ate `MV-S-015`;
2. `MV-S-016` vira pagina de continuidade em construcao;
3. `MV-S-017+` saem da trilha publicada ate reconstrucao;
4. criacao e revisao passam a exigir passada premium antecipada, radiacao local e passada premium final de microdetalhes.

---

## 2) Motivo da decisao
Leitura consolidada:

1. o lote `MV-S-003` e `MV-S-004` mostrou que ganhos decisivos de qualidade vieram de microdetalhes de uso real, nao apenas de correcoes macro;
2. feedback de maes reais revelou que pergunta bonita, nome frouxo e comando escondido ainda passavam cedo demais no sistema;
3. manter `MV-S-016+` publicadas enquanto o protocolo ainda estava aprendendo isso aumentaria retrabalho e risco de drift;
4. por isso, ficou melhor cortar o publicado antes, endurecer o sistema e so depois reconstruir a trilha longa.

---

## 3) Decisoes executadas

### 3.1 Site publicado
1. `site/index.html` e `site/templates/index.j2` passaram a expor somente `MV-S-000` ate `MV-S-015`;
2. `MV-S-015_A_ESCADA_DE_LUZ.html` agora aponta para `Licao 016 em construcao`;
3. `MV-S-016_O_BANDO_QUE_CRESCE.html` foi convertida em pagina de continuidade em construcao, com retorno para `MV-S-015` e para a home;
4. `MV-S-017+` foram retiradas da trilha publicada e neutralizadas no acervo publicado enquanto aguardam reconstrucao.

### 3.2 Docs vivos
1. `005_STATUS_REVISAO_SEMENTES.md` passou a declarar a trilha publicada ate `MV-S-015`;
2. `015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md` passou a registrar o corte publicado como decisao operacional de qualidade;
3. `023`, `003`, `004`, `002` e `010_TEMPLATE` foram endurecidos para suportar premium desde o primeiro ciclo de criacao/revisao.

---

## 4) Mudanca canonica de processo

### 4.1 Novo contrato minimo
Toda licao, em criacao ou revisao, passa a exigir:

1. `frase de boca do Portador`;
2. `pergunta respondivel principal`;
3. `microfriccoes previsiveis`;
4. `passada premium antecipada`;
5. `radiacao local`;
6. `passada premium final de microdetalhes`.

### 4.2 Heuristicas explicitadas
1. pergunta respondivel antes de pergunta bonita;
2. um concreto por vez;
3. comando visivel no ponto certo;
4. nomeacao consistente de numeros, pecas, lugares, gestos e objetos;
5. sem falsa simetria entre concretos visualmente diferentes;
6. formulacao que cabe na boca da mae real.

---

## 5) Arquivos diretamente afetados
1. `site/index.html`
2. `site/templates/index.j2`
3. `site/sementes/MV-S-015_A_ESCADA_DE_LUZ.html`
4. `site/sementes/MV-S-016_O_BANDO_QUE_CRESCE.html`
5. `site/sementes/MV-S-017_*` ate `MV-S-025_*`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
10. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
11. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
12. `Revisao/00_SISTEMA_REVISAO_CANONICO/010_TEMPLATE_SESSAO_DIARIA_REVISAO.md`

---

## 6) Definition of Done desta task
Esta task so conta como concluida quando:

1. o dashboard publicado mostrar so ate `MV-S-015`;
2. `MV-S-016` funcionar como pagina de construcao com saida segura;
3. os docs vivos registrarem a trilha publicada atual;
4. criacao e revisao estiverem cobertas pela nova camada premium obrigatoria;
5. o sistema deixar claro que `MV-S-016+` so volta ao publicado apos reconstrucao sob o novo contrato.
