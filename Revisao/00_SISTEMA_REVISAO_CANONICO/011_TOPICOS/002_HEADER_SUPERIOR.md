# 002 - HEADER SUPERIOR

## Missao do topico
1. dar norte imediato de navegacao e situar a familia dentro da jornada Sementes sem quebrar o clima da licao.

## Posicao no fluxo
1. aparece no topo da experiencia, logo apos a abertura da pagina;
2. precede a leitura do corpo da licao;
3. conversa com a Navegacao Inferior, mas nao a substitui.

## Transversais para consultar
1. `012_TRANSVERSAIS/001_ICONES_CORES_E_ASSETS.md`
2. `012_TRANSVERSAIS/002_REGRAS_DE_HTML_E_ANTI_PATTERNS.md`

## Contrato tecnico
1. usar `lesson-header-nav` como wrapper canonico.
2. a referencia visual deste topico e o padrao visto em `MV-S-003`.
3. o elemento pode ser `nav` ou `div`, desde que preserve a mesma topologia e leitura.
4. estrutura em 3 zonas fixas:
   a. esquerda = licao anterior;
   b. centro = `ph-plant duotone-forest` + label `Sementes`;
   c. direita = proxima licao.
5. links laterais devem usar `nav-mini-link`.
6. as zonas laterais devem expor o nome da licao adjacente; `Anterior` e `Proxima` sozinhos nao bastam.
7. a zona central deve permanecer visualmente centrada mesmo quando os lados tiverem textos de tamanhos diferentes.
8. o link da direita deve permanecer alinhado a direita.
9. links precisam apontar para arquivos adjacentes reais do ciclo e bater com a Navegacao Inferior.
10. em `MV-S-001+` e proibido usar `Voltar` generico como substituto do header canonico.

## Contrato visual
1. a leitura esquerda -> centro -> direita deve ser entendida num unico olhar.
2. o bloco central deve parecer eixo de estabilidade, nao enfeite lateral.
3. a simetria basica do topo deve ser preservada mesmo em telas menores.
4. o header nao pode competir com o Hero em peso visual.

## Contrato narrativo e pedagogico
1. orienta sem arrancar a familia da atmosfera da licao.
2. reforca que existe sequencia, progresso e continuidade curricular.
3. o adulto deve perceber rapidamente onde esta e para onde a jornada segue.

## Anti-patterns
1. link anterior ou proximo trocado.
2. centro sem selo `Sementes`.
3. topologia assimetrica que dificulta leitura no celular.
4. uso de rotulo generico sem nome da licao adjacente.
5. transformar o topo em simples botao de retorno.

## PASS estrutural
1. anterior, centro e proxima existem.
2. nomes e arquivos das licoes adjacentes estao corretos.
3. centro permanece estavel e reconhecivel.
4. header superior e navegacao inferior contam a mesma sequencia.

## BLOCK estrutural
1. qualquer link errado ou ausente.
2. ausencia do selo `Sementes` no centro.
3. header reduzido a um simples `Voltar`.
4. direita sem a proxima licao visivel.

## Ambiguidades resolvidas
1. `MV-S-003` e a referencia visual deste topico.
2. a excecao do Portal vale para `MV-S-000`; para `MV-S-001+` o contrato e fixo.
3. o header superior e obrigatorio mesmo quando o footer ja existe.
4. a tag HTML pode variar, mas a topologia de 3 zonas nao.

## Prompt operacional para IA
`Revise o Header Superior tomando MV-S-003 como referencia visual: exija 3 zonas, selo Sementes central, licao anterior a esquerda e proxima licao a direita; trate genericidade ou erro de navegacao como bloqueio.`
