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
