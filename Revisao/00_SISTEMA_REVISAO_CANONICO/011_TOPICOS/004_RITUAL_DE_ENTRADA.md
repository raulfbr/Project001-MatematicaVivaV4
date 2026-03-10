# 004 - RITUAL DE ENTRADA

## Missao do topico
1. tirar a familia do ritmo comum e consagrar a mesa como portal;
2. fazer o Portador da Tocha entrar primeiro, para que a crianca possa entrar com seguranca;
3. revelar o lugar da licao sem gastar ainda o reveal do guardiao;
4. preparar expectativa, silencio, desejo e atencao antes da Jornada.

## Posicao no fluxo
1. vem imediatamente depois da `003_PREPARACAO_DO_PORTADOR.md`;
2. e o primeiro momento plenamente dramatizado da experiencia;
3. antecede obrigatoriamente `005_A_JORNADA.md`;
4. fecha o limiar entre casa comum e Reino vivo.

## Transversais para consultar
1. `012_TRANSVERSAIS/001_ICONES_CORES_E_ASSETS.md`
2. `012_TRANSVERSAIS/002_REGRAS_DE_HTML_E_ANTI_PATTERNS.md`
3. `012_TRANSVERSAIS/003_TOM_NARRATIVO_E_DIRECAO_DO_PORTADOR.md`
4. `012_TRANSVERSAIS/004_GUARDIOES_CARDS_E_REVEAL.md`

## Contrato tecnico
1. a secao deve abrir com `scene-card` + `scene-header` proprio do Ritual de Entrada.
2. a preparacao do ambiente deve vir em `instruction-box ritual-bastidores-box` ou classe equivalente da mesma familia visual.
3. o roteiro do Portador deve vir em um unico `script-persona-block portador-block ritual-portador-block`.
4. o nome do bloco permanece `Portador da Tocha`; o tom pode aparecer em `script-tone`.
5. acting cues ficam dentro de `script-text`, em `p.acting-cue`, nunca como caixa paralela.
6. o reveal do local deve usar `card-container ritual-local-card` com label canonico e card centralizado.
7. evitar `style=""` inline quando a classe do sistema ja resolve espacamento, cor, alinhamento ou hierarquia.
8. o HTML deve permanecer leve e escaneavel: bastidor, monobloco do Portador, card do local e fecho de passagem.

## Subtopicos canonicos
### 1. Preparacao do ambiente
1. diz ao adulto o que ajustar no ambiente antes da fala com a crianca.
2. deve ser curto, concreto e elegante: luz, objetos, ritmo, seguranca, disposicao da mesa.
3. quando houver material sensivel, a regra de seguranca entra aqui sem quebrar o tom.
4. o bastidor prepara o adulto; nao substitui o roteiro falado.
5. o label recomendado para a familia e `Preparacao`, seguindo a boa intuicao da licao `000`.
6. `Bastidores do Portador` pode sobreviver como nome interno de revisao, mas nao precisa aparecer como titulo visivel para a familia.

### 2. Monobloco do Portador
1. o Portador conduz toda a travessia em uma unica fala nobre, calma e respiravel.
2. a ordem interna ideal e:
   a. desacelerar o corpo;
   b. deslocar a imaginacao;
   c. adensar o ambiente com 1 a 3 sinais sensoriais;
   d. aproximar a familia do limiar.
3. a crianca deve sentir: `algo vivo vai comecar agora`.
4. o adulto deve sentir: `eu consigo sustentar essa entrada sem teatro artificial`.

### 3. Reveal do local
1. o Ritual revela o lugar da licao, nao o guardiao.
2. a label deve ser clara, bonita e consistente. padrao recomendado: `Lugar revelado`.
3. o card do local deve confirmar visualmente o destino da familia.
4. o texto do Portador e o card precisam apontar para o mesmo lugar.

### 4. Fecho de limiar
1. o ultimo paragrafo deve deixar a familia na beira da Jornada.
2. ele pode sugerir presenca, som, movimento ou misterio.
3. ele nao pode nomear, mostrar, descrever com precisao ou identificar o guardiao.
4. a secao deve terminar com impulso natural para a primeira cena seguinte.

## Contrato de reveal
1. Ritual revela o local.
2. Jornada revela guardiao, card do guardiao, nome, primeira fala e papel narrativo.
3. antes da Jornada, o texto pode no maximo insinuar presenca anonima ou movimento difuso.
4. antes da Jornada, e proibido antecipar:
   a. nome do guardiao;
   b. especie ou identidade precisa;
   c. card ou imagem do guardiao;
   d. fala propria do guardiao;
   e. qualquer formula que ja resolva o misterio.

## Contrato narrativo e empatico
1. o Portador fala como quem acolhe e guia, nao como narrador apressado nem como ator excessivo.
2. a linguagem deve ser simples, elevada e calorosa.
3. cada ritual precisa ajudar o adulto a desacelerar junto com a crianca.
4. a experiencia deve ser agradavel para a familia inteira: menos verborragia, mais atmosfera.
5. o Ritual nao explica matematica; ele abre o coracao, o foco e a imaginacao para a matematica que vira.

## O que precisa estar escrito
1. um convite claro para respirar, desacelerar ou cruzar o limiar.
2. 1 a 3 pistas sensoriais concretas do lugar: luz, cheiro, textura, vento, som, temperatura.
3. uma frase que situe o destino da familia no Reino.
4. um fecho que deixe a sensacao de `estamos chegando em algo importante`.
5. quando couber, uma ponte leve com a licao anterior ou com o gesto matematico que amadurece na proxima cena, sem transformar o Ritual em explicacao.

## Padrao de qualidade premium
1. o adulto entende a cena em segundos e consegue executa-la sem ansiedade.
2. a crianca sente mudanca real de clima, mesmo com poucos recursos.
3. o visual da secao e limpo, centralizado e cerimonial.
4. o texto parece oral, mas nao frouxo; poetico, mas nao nebuloso.
5. o guardiao continua desejado, ainda nao entregue.

## Anti-patterns
1. fragmentar o Portador em varios blocos pequenos sem necessidade.
2. usar `Mostrar Card` como label generica quando o local ja pode ser nomeado com beleza.
3. gastar o misterio cedo demais com card, nome ou imagem do guardiao.
4. encher o bastidor de instrucoes operacionais secas.
5. explicar o conceito matematico aqui como se fosse aula expositiva.
6. usar inline styles para resolver o que deveria virar padrao CSS.

## PASS estrutural
1. ha bastidor curto, monobloco do Portador, reveal do local e frase de limiar.
2. o local fica claro e bonito.
3. o guardiao segue oculto.
4. a Jornada recebe a familia com tensao viva, nao com energia gasta.

## BLOCK estrutural
1. o guardiao aparece antes da Jornada.
2. o Portador vira colagem de caixas desconectadas.
3. o local nao fica evidente ou nao conversa com o texto.
4. o ritual soa tecnico, frio ou apressado.

## Ambiguidades resolvidas
1. o Ritual pode insinuar que ha alguem ou algo por perto, desde que a identidade continue inteiramente aberta.
2. o Bastidor pode carregar regra de seguranca, mas a alma da secao continua no roteiro falado.
3. o card do local faz parte do Ritual; o card do guardiao pertence a Jornada.
4. para a familia, o nome preferencial do bloco curto e `Preparacao:`; isso soa mais claro, mais nobre e menos teatral que `Bastidores do Portador`.

## Checklist de revisao
1. o adulto consegue preparar o ambiente sem reler cinco vezes?
2. a fala do Portador cabe naturalmente na boca de um pai ou mae real?
3. o local foi revelado com clareza e unidade visual?
4. o guardiao continua protegido para a Jornada?
5. o fecho deixa vontade de seguir?

## Prompt operacional para IA
`Revise o Ritual de Entrada como portal cerimonial da licao: preserve uma Preparacao curta do ambiente, monobloco nobre do Portador, reveal exclusivo do local e um fecho de limiar vivo. Se o guardiao aparecer antes da Jornada, a secao reprova.`
