# 013 - AUDITORIA LICOES 001-003

## Escopo
1. arquivos lidos:
   a. `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html`
   b. `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`
   c. `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html`
2. objetivo:
   a. verificar se os 12 topicos do contrato canonico aparecem de forma rapida e reconhecivel;
   b. apontar onde o topico esta correto, mas ainda nao foi plenamente refletido no HTML;
   c. separar gap de licao versus gap de contrato.

## Achados principais
1. `002_HEADER_SUPERIOR.md` foi recalibrado com base em `L003`, e as licoes `001-003` agora compartilham a topologia canonica de 3 zonas no topo.
2. `004_RITUAL_DE_ENTRADA.md` foi recalibrado e agora tem reflexo mais fiel nas licoes `001-003`: bastidor curto, monobloco do Portador, reveal do local e limiar vivo.
3. `005_A_JORNADA.md` foi recalibrado como coracao narrativo e agora se reflete melhor nas licoes `001-003`, com reveal formal, progressao de cenas, voz propria dos guardioes e ponte mais clara para o concreto.
4. `006_O_CONCRETO.md` esta direcionalmente correto, mas hoje cobre uma realidade mista: `001` usa `O Concreto`, enquanto `002` e `003` ainda usam `O Concreto`.
5. `011_FORMACAO_DO_PORTADOR.md` descreve bem o alvo premium, mas as licoes `002` e `003` ainda nao entregam a abertura canonica com `Estrategia do Mestre` dentro da propria secao.
6. `003_PREPARACAO_DO_PORTADOR.md` foi recalibrado, e as licoes `001-003` agora compartilham uma preparacao mais estavel, com `Fio da Jornada` e `Estrategia do Mestre` no proprio topo da experiencia do Portador.

## Topico por topico
### 001 - Base e Hero
1. `001`: presente e claro.
2. `002`: presente e claro.
3. `003`: presente e claro.
4. leitura rapida: o topico esta correto e e entendido em segundos nas tres licoes.
5. observacao: `003` duplica o script do Phosphor no `<head>`, o que e ruido tecnico, nao quebra estrutural.

### 002 - Header Superior
1. `001`: PASS. tem 3 zonas, selo `Sementes` e adjacencias corretas.
2. `002`: PASS. agora tem 3 zonas, selo `Sementes` e adjacencias corretas.
3. `003`: PASS. e a referencia visual adotada para este topico.
4. leitura rapida: o topico e facil de entender nas tres licoes.
5. faltando: nada relevante neste recorte.

### 003 - Preparacao do Portador
1. `001`: PASS forte. a secao ja abre com foco, fio da jornada, dica, materiais, descoberta, segredo, estrategia e graca.
2. `002`: PASS forte. a preparacao agora conversa melhor com `001` e antecipa `003`.
3. `003`: PASS forte. a licao aprofunda o mesmo padrao e mantem a camada estrategica ligada ao tema da mesa.
4. leitura rapida: o topico esta claro e padronizado nas tres licoes.
5. faltando: nada estrutural neste recorte; o trabalho principal agora migra para os topicos seguintes.

### 004 - Ritual de Entrada
1. `001`: PASS forte. bastidor, monobloco do Portador, local revelado e fecho de misterio estao em ordem.
2. `002`: PASS forte. mesma estrutura, com melhor coerencia visual e narrativa.
3. `003`: PASS forte. o ritual agora revela apenas o `Ninho Mirante` e preserva o guardiao para a Jornada.
4. leitura rapida: o topico esta claro, padronizado e facil de reconhecer nas tres licoes.
5. faltando: nada bloqueante neste recorte.

### 005 - A Jornada
1. `001`: PASS forte. Celeste conduz uma progressao clara de `1 -> 2 -> 3`, com maravilhamento, contagem encarnada e ponte elegante para `002`.
2. `002`: PASS forte. Bernardo agora dramatiza bem a passagem de tesouros espalhados para fileira legivel, sem perder o tema da fortaleza.
3. `003`: PASS forte. `Iris` reaparece no lugar certo, a trilha `4 -> 5` esta mais inteligivel e a fala ja prepara naturalmente `004`.
4. leitura rapida: o topico esta forte, reconhecivel e mais premium nas tres licoes.
5. faltando: nada bloqueante neste recorte; os proximos ganhos serao por refinamento de outras secoes.

### 006 - O Concreto
1. `001`: PASS parcial. usa nome canonico e o nucleo concreto esta forte.
2. `002`: PARCIAL. usa alias legado `O Concreto`.
3. `003`: PARCIAL. usa alias legado `O Concreto`.
4. leitura rapida: a funcao do topico e entendida nas tres licoes, mas o naming ainda nao esta estabilizado.
5. faltando:
   a. `001` e `002` nao explicitam tao bem `objetivo + fallback/adaptacao + ponte para Narramos Juntos`;
   b. `002` e `003` ainda nao migraram o nome da secao.

### 007 - Narramos Juntos
1. `001`: PASS. instruction box de escuta, disparador vivo e perguntas abertas.
2. `002`: PASS. segue quase o mesmo padrao de `001`.
3. `003`: PARCIAL. a secao existe, mas a instruction box esta mais fraca e duas perguntas ja embutem a resposta.
4. leitura rapida: o topico e facilmente localizavel nas tres licoes.
5. faltando em `003`: reforcar escuta e abrir mais o reconto da crianca.

### 008 - Ritual de Fechamento
1. `001`: PASS com ressalva. ha despedida do guardiao e fechamento do Portador.
2. `002`: PASS com ressalva. mesma estrutura.
3. `003`: PASS. fechamento limpo e suave.
4. leitura rapida: o topico esta claro nas tres licoes.
5. observacao: `001` e `002` ja insinuam fortemente a proxima licao aqui; o contrato novo prefere deixar o teaser principal para `Conexao da Jornada`.

### 009 - Conexao da Jornada
1. `001`: PASS parcial. proxima licao correta.
2. `002`: PASS parcial. proxima licao correta.
3. `003`: PASS parcial. proxima licao correta.
4. leitura rapida: o topico existe e funciona nas tres licoes.
5. faltando nas tres:
   a. o CTA principal esta em `div onclick`, nao em link semantico;
   b. a secao esta clicavel, mas nao plenamente auditavel do ponto de vista HTML.

### 010 - Sementes para o Dia
1. `001`: PARCIAL. tem os 5 movimentos, mas a opcionalidade nao esta explicita e falta frase final de fechamento da secao.
2. `002`: PARCIAL. mesma situacao de `001`.
3. `003`: PASS. opcionalidade explicita, 5 movimentos distintos e frase final.
4. leitura rapida: o topico e facil de entender nas tres licoes.
5. faltando em `001-002`: explicitar que a licao ja esta completa sem as extensoes.

### 011 - Formacao do Portador
1. `001`: PASS forte. abre com `Estrategia do Mestre` e organiza bem as boxes formativas.
2. `002`: PARCIAL. a secao e robusta, mas nao abre com `Estrategia do Mestre` e usa bastante `<br>` para sustentar layout.
3. `003`: PARCIAL. a secao e inteligivel, mas nao abre com `Estrategia do Mestre`; o bloco aparece antes, em `Preparacao do Portador`.
4. leitura rapida: o topico e compreensivel nas tres licoes, mas a aderencia ao contrato premium ainda e irregular.
5. faltando:
   a. `002` e `003` precisam abrir a propria secao com `Estrategia do Mestre`;
   b. `001` e `002` nao trazem `Sementes Continuam` dentro da secao formativa; em `003` ele aparece dentro da Formacao.

### 012 - Navegacao Inferior
1. `001`: PASS. anterior e proxima corretas.
2. `002`: PASS. cadeia correta.
3. `003`: PASS. cadeia correta.
4. leitura rapida: topico simples, claro e estavel nas tres licoes.
5. faltando: nada relevante no recorte `001-003`.

## Leitura rapida por licao
1. `001` e a mais alinhada ao contrato dos topicos. Ela ja parece uma boa referencia base.
2. `002` esta mais coesa depois do alinhamento do header superior, da Preparacao do Portador e da Jornada; o principal drift remanescente esta na abertura de Formacao do Portador.
3. `003` deixou de ser a mais critica no eixo Ritual/Jornada; ela ainda pede refinamentos futuros, mas o bloco central da narrativa agora esta no trilho certo.

## Conclusao operacional
1. `000_README.md` esta correto como indice e ordem de revisao.
2. o problema principal nao esta no indice; esta na distancia entre contrato premium e HTML legado das licoes.
3. melhor ordem de detalhamento agora:
   a. `011_FORMACAO_DO_PORTADOR`
   b. `006_MOMENTO_DE_CONEXAO`
   c. `009_CONEXAO_DA_JORNADA`
   d. `007_NARRAMOS_JUNTOS`
   e. `010_SEMENTES_PARA_O_DIA`
