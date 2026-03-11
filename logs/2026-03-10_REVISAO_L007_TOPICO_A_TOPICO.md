# REVISAO L007 TOPICO A TOPICO
Data: 2026-03-10
Licao: `MV-S-007_A_COROA_DA_SEMANA.html`
Metodo: `023` + `003` + `004` + `011_TOPICOS/001-012` + pacote transversal minimo `002/003/005/006/008`
Escopo congelado: revisar apenas `L007`, usando `L006` e `L008` como fronteiras curriculares; sem commit; sem push

---

## 1) Cerne macro da licao
1. `TGTB ref`: `000-L7 - Numbers 6 to 7 / Numeros 6 e 7`.
2. `Tema principal / ideia viva`: `A Coroa da Semana` - sete cores no arco-iris encontradas nas trilhas da Vastidao.
3. `Guardiao`: `Celeste`.
4. `Lugar`: a licao atual aponta para a `Clareira das Perguntas`; isso precisa ser validado no patch para que o Ritual revele local sem antecipar funcao indevida.
5. `Conceito vivo`: perceber `6` e `7` como quantidades que ultrapassam a mao completa e aparecem em imagens vivas do mundo.
6. `Papel no curriculo mestre`: abrir a passagem de `1-5` para `6-7`, mantendo o espirito de descoberta concreta e nao apenas ampliando contagem mecanica.
7. `Imagem dominante`: `coroa / arco-iris / semana / trilha da Vastidao`.
8. `Promessa da licao`: a crianca toca e reconhece `6` e `7` por meio de contagem concreta, imagem viva e ritmo reconhecivel do mundo.
9. `Fruto do dia`: a crianca conta ate `6` e `7` com sentido real e reconhece que essas quantidades ultrapassam a mao completa.
10. `Risco de descaracterizacao`: a licao virar apenas `contagem ampliada` ou `treino escolar de 6 e 7`, perdendo a `coroa da semana` como imagem dominante.
11. `Risco de fronteira`: `Jornada -> O Concreto` pode colapsar no mesmo gesto de contar objetos; `Conexao -> Sementes/Formacao` pode seguir legado e misturar funcoes.
12. `Risco familia real`: excesso de texto legado e estrutura quebrada aumentam carga cognitiva do Portador.
13. `Hospitalidade multi-crianca`: um irmao menor pode ajudar a reunir ou entregar objetos, sem trocar a descoberta principal do herdeiro.

---

## 2) Diagnostico inicial
### Estado encontrado
1. arquivo ainda em template legado, com forte mistura de markup antigo e inline styles;
2. mojibake visivel em titulo, meta tag, hero, icones e labels;
3. labels legadas presentes: `[Foco:]`, `Ritual de Abertura`, `Atividade Concreta`, `Para a Familia`;
4. `Conexao da Jornada` ainda usa `div onclick`;
5. `Sementes para o Dia` ausente;
6. `Formacao do Portador` ausente como secao canonica; no lugar ha bloco legado `Para a Familia`;
7. reveal do Ritual esta quebrado: o Ritual mostra a guardia e nao um reveal canonico do local;
8. `A Jornada` e `O Concreto` correm risco de repetir o mesmo gesto central de contagem.

### Findings iniciais por severidade
#### Criticos
1. encoding degradado em varias camadas da pagina;
2. `004_RITUAL_DE_ENTRADA` reprovado por naming legado e reveal quebrado;
3. `010_SEMENTES_PARA_O_DIA` ausente;
4. `011_FORMACAO_DO_PORTADOR` ausente como secao canonica;
5. `009_CONEXAO_DA_JORNADA` com CTA semantico quebrado via `div onclick`.

#### Altos
1. `003_PREPARACAO_DO_PORTADOR` ainda nao carrega a preparacao canonica atual;
2. `005_A_JORNADA` ainda opera em modelo legado e repete cartao/local de forma pouco premium;
3. `006_O_CONCRETO` segue como `Atividade Concreta` e corre risco de repetir a Jornada;
4. `007_NARRAMOS_JUNTOS` ainda esta mais perto de formulario simples do que de reconto premium.

#### Medios
1. hero e header superior existem, mas ainda nao respiram no padrao canonico novo;
2. navegacao inferior parece funcional, mas esta visualmente e semanticamente presa ao legado.

---

## 3) Matriz inicial `001-012`
1. `001_BASE_E_HERO` -> `BLOCK`
Motivo: hero existe, mas ha mojibake, home icon quebrado e acabamento legado.
2. `002_HEADER_SUPERIOR` -> `GAP`
Motivo: links existem, mas o topo ainda usa estrutura inline legado e selo central nao esta no contrato atual.
3. `003_PREPARACAO_DO_PORTADOR` -> `BLOCK`
Motivo: ainda usa `[Foco:]`, nao traz preparacao canonica atual nem fio da jornada no padrao novo.
4. `004_RITUAL_DE_ENTRADA` -> `BLOCK`
Motivo: secao ainda nomeada `Ritual de Abertura`; reveal de local e guardiao esta colapsado.
5. `005_A_JORNADA` -> `BLOCK`
Motivo: cenas legadas, repeticao de estrutura, guardia ja antecipada e gesto matematico pouco diferenciado.
6. `006_O_CONCRETO` -> `BLOCK`
Motivo: secao ainda nomeada `Atividade Concreta`; precisa objetivo, atividade principal, variacoes leves, fruto e ponte para narracao.
7. `007_NARRAMOS_JUNTOS` -> `GAP`
Motivo: secao existe, mas ainda opera em modelo antigo e ainda nao recolhe a experiencia com profundidade premium.
8. `008_RITUAL_DE_FECHAMENTO` -> `GAP`
Motivo: secao existe, mas o fechamento ainda e simples demais e presa ao legado.
9. `009_CONEXAO_DA_JORNADA` -> `BLOCK`
Motivo: bloco ainda usa copy e CTA legados; falta link semantico e fechamento canonico da trilha.
10. `010_SEMENTES_PARA_O_DIA` -> `BLOCK`
Motivo: ausente.
11. `011_FORMACAO_DO_PORTADOR` -> `BLOCK`
Motivo: substituida por `Para a Familia`.
12. `012_NAVEGACAO_INFERIOR` -> `GAP`
Motivo: navegacao existe, mas segue visual e texto legados e precisa checagem fina apos patch.

---

## 4) Fronteiras criticas iniciais
1. `003 -> 004` -> `BLOCK`
Preparacao ainda nao orienta no padrao novo; Ritual entra por contrato antigo.
2. `004 -> 005` -> `BLOCK`
Ritual ja antecipa demais Celeste; reveal do local e guardia nao estao limpos.
3. `005 -> 006` -> `BLOCK`
Licao corre risco de fazer contagem em dobro sem mudar o gesto central.
4. `006 -> 007` -> `GAP`
Existe transicao, mas ela ainda nao recolhe bem o gesto concreto.
5. `008 -> 009` -> `GAP`
Ha sequencia formal, mas o fecho ainda despeja no bloco legado de conexao.
6. `009 -> 010` -> `BLOCK`
`Sementes para o Dia` ausente.
7. `010 -> 011` -> `BLOCK`
`Formacao do Portador` nao existe como secao canonica.
8. `011 -> 012` -> `BLOCK`
Nao ha como validar essa fronteira sem restaurar `011`.

---

## 5) Hipoteses de trabalho
1. a licao vai exigir migracao ampla para o contrato canonico atual;
2. mesmo assim, o patch precisa nascer do cerne proprio da `L007`, e nao de copia rasa de `L006`;
3. o maior risco editorial e reduzir a licao a `6 e 7` sem honrar `coroa`, `arco-iris` e `semana`;
4. o maior risco pedagogico e deixar `Jornada` e `O Concreto` fazendo a mesma contagem;
5. a melhor ancora estrutural atual e a organizacao canonica vista em `L006`, mas com imagem dominante propria de `Celeste`.

---

## 6) Riscos residuais antecipados
1. `L008` ainda esta em contrato legado; portanto a fronteira `007 -> 008` precisa ser honesta sem depender de pagina seguinte ja corrigida.
2. o arquivo atual esta tecnicamente parseavel, mas editorialmente longe do premium.
3. se o patch nao proteger a imagem dominante, a licao pode sair mais limpa e menos verdadeira.

---

## 7) Revisao executada `001-012`
### `001_BASE_E_HERO` -> `PASS`
#### Confirmado
1. hero refeito no contrato atual, com `title`, `meta`, home button, guardia correta e copy centrada em `coroa / semana / arco-iris`;
2. encoding restaurado nas camadas principais da abertura;
3. a frase de hero protege a ideia de que `6` e `7` aparecem depois da mao inteira, sem colapsar a licao em treino de contagem.
#### Tensionado
1. o maior risco aqui era deixar a abertura bonita, mas generica; isso foi bloqueado mantendo Celeste e a imagem da coroa no centro.
#### Alterado
1. cabecalho inteiro reescrito em HTML canonico, com imagem da `celeste-raposa` e copy nova.

### `002_HEADER_SUPERIOR` -> `PASS`
#### Confirmado
1. navegacao superior agora referencia `L006` e `L008` com links semanticos;
2. selo central `Sementes` ficou coerente com o padrao recente;
3. a fronteira curricular ficou explicita sem roubar o centro da pagina.
#### Tensionado
1. a copia do topo precisava preparar o leitor sem antecipar o tema de `L008` em excesso.
#### Alterado
1. header legado foi substituido por `lesson-header-nav` no contrato atual.

### `003_PREPARACAO_DO_PORTADOR` -> `PASS`
#### Confirmado
1. `Foco da licao`, `Fio da Jornada`, materiais, plano B, fruto, segredo do maravilhamento e estrategia agora aparecem em forma canonica;
2. a preparacao ancora `L006 -> L007 -> L008` com coerencia curricular;
3. a opcao multi-crianca entrou como inclusao lateral, nao como troca do gesto central.
#### Tensionado
1. houve cuidado para nao reduzir `6` e `7` a "decore mais dois numerais";
2. o `Plano B` precisou preservar a experiencia da passagem sem alongar demais o dia da familia.
#### Alterado
1. bloco legado com `[Foco:]` foi removido;
2. preparacao foi reescrita em chave premium, html-first.

### `004_RITUAL_DE_ENTRADA` -> `PASS`
#### Confirmado
1. naming ajustado para `Ritual de Entrada`;
2. o Ritual agora revela o lugar (`Clareira das Perguntas`) e prepara a aparicao da coroa sem antecipar a guardia no lugar errado;
3. o tom do Portador ficou de convite e maravilhamento, sem burocracia.
#### Tensionado
1. o principal cuidado foi nao colapsar `lugar` e `guardia` no mesmo reveal, erro presente no legado.
#### Alterado
1. card local restaurado;
2. script do Portador refeito para a entrada canonica.

### `005_A_JORNADA` -> `PASS`
#### Confirmado
1. a Jornada ficou em tres movimentos claros: `trilha continua`, `sexto brilho`, `coroa do sete`;
2. Celeste aparece como guardia propria desta licao, com fala coerente com vastidao, trilha e beleza;
3. a imagem dominante da semana e do arco-iris entra no momento certo, como reconhecimento vivo do `7`.
#### Tensionado
1. o maior risco era repetir no concreto o mesmo gesto da Jornada;
2. por isso, a Jornada ficou como revelacao e reconhecimento, nao como atividade principal longa.
#### Alterado
1. cenas legadas foram substituidas por tres cenas novas com progressao matematica e narrativa.

### `006_O_CONCRETO` -> `PASS`
#### Confirmado
1. naming ajustado para `O Concreto`;
2. objetivo, ligacao com a Jornada, atividade principal, duas variacoes, falas de sustentacao, adaptacao, sinal de fruto e ponte para narracao estao presentes;
3. a atividade central ficou distinta da Jornada: a crianca se torna autora de duas coroas reais, uma de `6` e outra de `7`.
#### Tensionado
1. foi preciso impedir que a licao virasse "contar duas vezes a mesma coisa";
2. tambem foi preciso manter o `5` como base visivel, sem deixar a base engolir a novidade do `6` e do `7`.
#### Alterado
1. secao `Atividade Concreta` foi substituida pelo contrato atual;
2. a ponte para `Narramos Juntos` foi criada de forma explicita.

### `007_NARRAMOS_JUNTOS` -> `PASS`
#### Confirmado
1. `Narramos Juntos` agora abre escuta real, com postura do Portador, disparador da guardia, perguntas de reconto, perguntas do coracao e formas legitimas de narracao;
2. a narracao recolhe exatamente a passagem central da licao: onde a mao terminou e onde a coroa continuou;
3. gesto, apontar, remontagem e fala curta foram tratados como formas dignas.
#### Tensionado
1. o risco maior era transformar o bloco em mini-questionario escolar;
2. isso foi contido com perguntas abertas e foco no reconto da experiencia, nao na resposta certa.
#### Alterado
1. secao antiga foi substituida por narracao premium alinhada a Charlotte Mason.

### `008_RITUAL_DE_FECHAMENTO` -> `PASS`
#### Confirmado
1. Celeste se despede fechando a experiencia do `6` e do `7` com paz;
2. o Portador conduz retorno suave e domestico real;
3. o teaser da proxima licao nao invadiu o fechamento.
#### Tensionado
1. o cuidado aqui foi nao empurrar a pagina para `L008` antes da hora.
#### Alterado
1. fechamento legado simples foi reescrito com guardia + Portador, no padrao atual.

### `009_CONEXAO_DA_JORNADA` -> `PASS`
#### Confirmado
1. `Conexao da Jornada` ficou sem `div onclick` e com link semantico;
2. a memoria viva resume bem a licao sem duplicar o fechamento;
3. a ponte para `L008` apresenta `par` e `repouso` sem roubar o tema da proxima pagina.
#### Tensionado
1. a fronteira `007 -> 008` precisava ser honesta, mas leve, porque `L008` ainda esta em contrato legado.
#### Alterado
1. CTA legado foi substituido por card-link canonico para `MV-S-008_O_PAR_PERFEITO.html`.

### `010_SEMENTES_PARA_O_DIA` -> `PASS`
#### Confirmado
1. secao foi restaurada no lugar canonico, antes da Formacao;
2. ancora `Escolha 1 ou 2 movimentos` presente;
3. os cinco movimentos foram entregues: `Exploracao`, `Dramatizacao`, `Criacao`, `Narracao`, `Reflexao`;
4. a opcionalidade ficou explicita e leve.
#### Tensionado
1. foi preciso impedir que `Sementes` virasse repeticao pesada do concreto;
2. tambem foi preciso deixar a imagem da coroa viva sem transformar a semana em tarefa.
#### Alterado
1. bloco inexistente no legado foi criado do zero em chave canonica.

### `011_FORMACAO_DO_PORTADOR` -> `PASS`
#### Confirmado
1. `Formacao do Portador` voltou como secao propria, separada de `Sementes para o Dia`;
2. a estrategia do mestre foi nomeada em coerencia com o cerne da licao: `Passar da Mao sem Perder a Coroa`;
3. estao presentes `Por que isso importa`, `O que o Portador aprende hoje`, `CPA`, `Charlotte Mason`, `TGTB`, `Curriculo em espiral`, `Nota de Graca` e `As Sementes Continuam`.
#### Tensionado
1. o maior risco era virar texto adulto generico sobre contagem;
2. isso foi evitado ancorando toda a formacao na passagem do `5` para `6` e `7`.
#### Alterado
1. `Para a Familia` foi removido e substituido por formacao canonica integral.

### `012_NAVEGACAO_INFERIOR` -> `PASS`
#### Confirmado
1. navegacao inferior aponta corretamente para `L006` e `L008`;
2. labels de anterior/proxima estao no contrato recente;
3. a pagina fecha limpa, sem vazamento de blocos legados.
#### Tensionado
1. nenhuma tensao forte apos o patch principal; a checagem final foi mais tecnica do que editorial.
#### Alterado
1. a navegacao final foi preservada no novo esqueleto canonico.

---

## 8) Fronteiras criticas finais
1. `003 -> 004` -> `PASS`
Preparacao agora desemboca naturalmente num Ritual que revela lugar e prepara expectativa.
2. `004 -> 005` -> `PASS`
o Ritual prepara a clareira; a Jornada revela Celeste sem atropelo.
3. `005 -> 006` -> `PASS`
a Jornada mostra e interpreta; `O Concreto` entrega autoria manual distinta.
4. `006 -> 007` -> `PASS`
a ponte para narracao recolhe as duas coroas e abre o reconto do gesto central.
5. `008 -> 009` -> `PASS`
o fechamento pousa; a Conexao recorda e aponta adiante sem quebrar a paz.
6. `009 -> 010` -> `PASS`
Conexao termina no gancho; `Sementes` assume continuidades leves e opcionais.
7. `010 -> 011` -> `PASS`
`Sementes` continua a vida da casa; `Formacao` sobe para a leitura pedagogica do adulto.
8. `011 -> 012` -> `PASS`
o adulto recebe leitura final e a pagina fecha com navegacao limpa.

---

## 9) Matriz final `001-012`
1. `001_BASE_E_HERO` -> `PASS`
2. `002_HEADER_SUPERIOR` -> `PASS`
3. `003_PREPARACAO_DO_PORTADOR` -> `PASS`
4. `004_RITUAL_DE_ENTRADA` -> `PASS`
5. `005_A_JORNADA` -> `PASS`
6. `006_O_CONCRETO` -> `PASS`
7. `007_NARRAMOS_JUNTOS` -> `PASS`
8. `008_RITUAL_DE_FECHAMENTO` -> `PASS`
9. `009_CONEXAO_DA_JORNADA` -> `PASS`
10. `010_SEMENTES_PARA_O_DIA` -> `PASS`
11. `011_FORMACAO_DO_PORTADOR` -> `PASS`
12. `012_NAVEGACAO_INFERIOR` -> `PASS`

---

## 10) Sanity checks finais
1. busca por residuos legados nao encontrou `\[Foco:\]`, `Ritual de Abertura`, `Atividade Concreta`, `Para a Familia` nem `div onclick`;
2. busca por sinais comuns de mojibake nao retornou match na pagina final;
3. parser HTML simples retornou `OK`;
4. assets locais usados na pagina foram verificados e existem:
   - `../assets/sementes/guardioes/celeste-raposa.png`
   - `../assets/cards/guardioes/celeste-raposa.png`
   - `../assets/cards/locais/local-clareira-perguntas.png`
5. links locais para `L006` e `L008` estao presentes e apontam para arquivos existentes.

---

## 11) Veredito honesto
### O que ficou impecavel
1. a pagina saiu do legado e entrou no contrato canonico atual de ponta a ponta;
2. a ideia viva de `A Coroa da Semana` foi preservada: `6` e `7` aparecem como passagem alem da mao, ligados a semana, arco-iris e trilha da Vastidao;
3. `Jornada`, `O Concreto`, `Narramos Juntos`, `Conexao`, `Sementes` e `Formacao` agora tem funcoes distintas e legiveis;
4. a pagina ficou semanticamente mais limpa, com CTA semantico e sem residuos centrais do template antigo.

### O que ainda ficou em risco
1. `L008` ainda esta em contrato legado; portanto a experiencia de continuidade entre paginas ainda depende de futura revisao da proxima licao;
2. nao houve validacao visual em navegador nesta passada; a aprovacao aqui e estrutural, semantica e editorial no HTML.

### Decisao
1. `L007` passou na revisao topico a topico por IA.
2. estado final: pronta para futura validacao humana, sem necessidade de nova passada de patch antes disso, salvo se a validacao visual encontrar ajuste de layout.

---

## 12) Reauditoria do estado final
### Diagnostico inicial desta reabertura
1. a `L007` foi reaberta no estado final atual, nao no estado legado original;
2. nao apareceu `BLOCK` novo em nenhum dos `12` topicos;
3. a pagina segue no contrato canonico atual e esta coerente com o cerne curricular de `A Coroa da Semana`.

### Tema principal reconfirmado
1. `TGTB ref`: `000-L7 - Numbers 6 to 7 / Numeros 6 e 7`;
2. guardia: `Celeste`;
3. ideia viva: `A Coroa da Semana`, em que `6` e `7` surgem como passagem alem da mao, ligados a semana e ao arco-iris;
4. risco de descaracterizacao monitorado: a licao cair para treino generico de contagem.

### Matriz de reauditoria `001-012`
1. `001_BASE_E_HERO` -> `PASS`
hero segue ancorado em `Celeste`, `coroa`, `semana` e `arco-iris`, sem achatamento escolar.
2. `002_HEADER_SUPERIOR` -> `PASS`
navegacao superior segue limpa, com fronteiras honestas para `L006` e `L008`.
3. `003_PREPARACAO_DO_PORTADOR` -> `PASS`
preparacao continua completa, respiravel e alinhada ao fio da jornada.
4. `004_RITUAL_DE_ENTRADA` -> `PASS`
ritual preserva revelacao de lugar e entrada da guardia sem invadir a Jornada.
5. `005_A_JORNADA` -> `PASS`
as tres cenas seguem distintas e fieis ao cerne do `6` e `7` como coroacao da semana.
6. `006_O_CONCRETO` -> `PASS`
o bloco continua claramente separado da Jornada e encarna o gesto central da licao.
7. `007_NARRAMOS_JUNTOS` -> `PASS`
narracao permanece em chave de escuta, sem clima de prova.
8. `008_RITUAL_DE_FECHAMENTO` -> `PASS`
fechamento segue sereno e nao foi contaminado pelo teaser da proxima pagina.
9. `009_CONEXAO_DA_JORNADA` -> `PASS`
conexao continua sem `div onclick`, com link semantico e teaser controlado.
10. `010_SEMENTES_PARA_O_DIA` -> `PASS`
bloco canonicamente posicionado e sem fusao indevida com `Formacao do Portador`.
11. `011_FORMACAO_DO_PORTADOR` -> `PASS`
formacao segue integral, com `TGTB` explicitado em `000-L7`.
12. `012_NAVEGACAO_INFERIOR` -> `PASS`
fechamento da pagina permanece limpo e consistente com o topo.

### Confirmado nesta reauditoria
1. nao ha residuos legados como `Ritual de Abertura`, `Atividade Concreta`, `Para a Familia` ou `div onclick`;
2. nao houve match para sinais comuns de mojibake;
3. parser HTML simples retornou `OK`;
4. links para `MV-S-006_O_DESENHO_DO_REI.html` e `MV-S-008_O_PAR_PERFEITO.html` seguem corretos;
5. nao foi necessario patch adicional no HTML nesta reabertura.

### O que ficou tensionado
1. a continuidade externa ainda depende de `L008`, que permanece em contrato legado;
2. esta reauditoria foi estrutural, semantica e editorial no HTML; nao houve validacao visual em navegador.

### Decisao desta reabertura
1. a `L007` continua aprovada na revisao topico a topico por IA;
2. nesta passada nao houve alteracao do HTML, apenas consolidacao honesta do estado final no log.
