# TASK ROBUSTA - CADENCIA DE 2 LICOES POR DIA
Data: 2026-03-06
Escopo: operacao da revisao HTML-first apos validacao do piloto
Restricao: nao editar licoes nesta task
Status: estruturacao operacional

---

## 0) Decisao desta task
1. A meta `2 licoes por dia` nao sera tratada como desejo abstrato; vira protocolo operacional.
2. Antes de entrar em cadencia, a equipe precisa de:
   - criterio de entrada;
   - distribuicao de trabalho por sessao;
   - formato de handoff;
   - criterio de bloqueio;
   - criterio de encerramento diario.
3. Esta task existe para impedir que a velocidade destrua o padrao premium.

---

## 1) Problema que esta task resolve
Hoje o sistema documental ja existe, mas ainda faltava estruturar:
1. como abrir uma sessao de revisao;
2. quantas licoes podem entrar no mesmo dia com seguranca;
3. como lidar com bloqueios sem perder contexto;
4. como registrar o estado do lote ao fim da sessao;
5. como manter qualidade constante mesmo quando o volume aumentar.

Sem isso, o risco e:
1. revisar demais e revisar mal;
2. abrir licoes demais ao mesmo tempo;
3. fechar dia sem diagnostico claro;
4. acumular remendos em vez de progresso.

---

## 2) Objetivo
Definir o sistema de execucao diaria da revisao premium.

Resultado esperado:
1. uma sessao futura consegue sair do zero ao fechamento sem improviso;
2. a meta `2/dia` fica condicionada a gates claros;
3. a revisao vira operacao repetivel e auditavel.

---

## 3) Fontes obrigatorias
1. `Revisao/RadmeRevisao.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/007_TASK_ROBUSTA_PILOTO_001_003.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/008_TEMPLATE_RELATORIO_PILOTO_001_003.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`

---

## 4) Regra de ativacao da cadencia
A cadencia `2 licoes por dia` so pode ser ativada quando:
1. o piloto `001-003` estiver concluido;
2. o sistema estiver com cobertura suficiente;
3. nao houver ambiguidade estrutural grande nos topicos;
4. o gate North Star tiver se mostrado claro e utilizavel;
5. houver confianca real de que o metodo nao exige reinterpretacao a cada licao.

Se qualquer item falhar:
1. a cadencia fica em `1 licao por dia` ou `diagnostico puro`.

---

## 5) Modelo de sessao diaria
Cada dia de revisao deve ser dividido em 5 blocos.

### Bloco 1 - Preparacao
1. abrir `005_STATUS_REVISAO_SEMENTES.md`
2. definir as 2 licoes do dia
3. abrir atual, anterior e proxima de cada uma
4. abrir topicos e transversais mais provaveis

Saida:
1. escopo do dia congelado

### Bloco 2 - Diagnostico
1. revisar licao A
2. revisar licao B
3. levantar findings sem editar

Saida:
1. findings completos das duas licoes

### Bloco 3 - Patch
1. aplicar correcoes estruturais primeiro
2. aplicar narrativas depois
3. aplicar pedagogia e acabamento por ultimo

Saida:
1. patches minimamente arriscados e verificaveis

### Bloco 4 - Validacao
1. rodar gates por licao
2. verificar navegacao
3. verificar North Star
4. rodar sanity check de encoding

Saida:
1. PASS/BLOCK por licao

### Bloco 5 - Handoff
1. atualizar status
2. registrar risco residual
3. definir proximo passo minimo

Saida:
1. sessao encerrada sem perda de contexto

---

## 6) Regra de congelamento de escopo diario
Uma vez definidas as 2 licoes do dia:
1. nao abrir terceira licao para editar;
2. so consultar licao adjacente como contexto;
3. nao puxar backlog paralelo;
4. nao misturar com YAML, Next ou refactor amplo.

Objetivo:
1. proteger foco e qualidade.

---

## 7) Criterio de composicao do par diario
A dupla de licoes do dia deve seguir ordem logica.

Preferencia:
1. licoes consecutivas
2. licoes do mesmo microbloco curricular
3. licoes com guardioes ou problemas parecidos

Evitar:
1. misturar duas licoes muito pesadas no mesmo dia;
2. misturar uma licao em bloqueio severo com outra muito aberta;
3. abrir lote distante sem fechar o anterior.

---

## 8) Limite de WIP
WIP maximo:
1. `2 licoes em revisao ativa`

Pode consultar:
1. a anterior
2. a proxima
3. documentos centrais

Nao pode:
1. deixar 3 ou 4 licoes parcialmente mexidas ao mesmo tempo.

---

## 9) Criterio de BLOCK diario
O dia deve ser interrompido ou reduzido quando:
1. uma licao revelar falha sistemica dos topicos;
2. o gate North Star estiver vago demais para decidir;
3. houver risco de encoding ou regressao estrutural;
4. a primeira licao consumir o tempo mental previsto inteiro;
5. surgir contradicao forte entre documentos canônicos.

Acao correta:
1. congelar a segunda licao;
2. registrar bloqueio;
3. ajustar o sistema antes de continuar.

---

## 10) Criterio de fechamento do dia
Um dia so e considerado bem fechado quando:
1. as duas licoes foram diagnosticadas e validadas;
2. ou uma foi concluida e a outra foi conscientemente adiada;
3. o quadro de status foi atualizado;
4. existe log claro de risco residual;
5. o proximo passo do dia seguinte esta definido.

---

## 11) Formato de handoff por sessao
Ao final da sessao, registrar:

```md
## Sessao [data]
- Licoes alvo:
- Status final de cada uma:
- Gates:
- Riscos residuais:
- Bloqueios do sistema:
- Proximo par sugerido:
```

---

## 12) Definicao de produtividade saudavel
Produtividade correta nao e:
1. numero bruto de arquivos alterados;
2. velocidade aparente;
3. quantidade de texto reescrito.

Produtividade correta e:
1. licao fechada com PASS real;
2. menos ambiguidades no sistema;
3. mais previsibilidade para a proxima sessao.

---

## 13) Gatilhos para voltar da cadencia 2/dia para 1/dia
Se ocorrer qualquer um:
1. dois dias seguidos com bloqueio sistêmico;
2. aumento de regressao estrutural;
3. excesso de reabertura de licoes;
4. queda de nitidez no gate North Star;
5. cansaco operacional visivel nos logs.

Entao:
1. reduzir para `1/dia`;
2. reparar o sistema;
3. so depois retomar `2/dia`.

---

## 14) Entregaveis desta task
1. protocolo diario de cadencia
2. criterio de entrada na cadencia
3. criterio de bloqueio
4. criterio de handoff
5. criterio de retorno para `1/dia`

---

## 15) Definition of Done
Esta task fecha quando:
1. a equipe consegue abrir uma sessao futura sem improviso;
2. o `005_STATUS_REVISAO_SEMENTES.md` consegue usar esta cadencia;
3. a meta `2/dia` deixa de ser aspiracional e vira processo.

---

## 16) Proximo passo recomendado
1. criar um template de sessao diaria;
2. integrar esta task ao quadro de status;
3. so depois usar isso em execucao real.
