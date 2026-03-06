# 002 - HEADER SUPERIOR

## Missao do topico
1. dar norte imediato de navegacao e situar a familia dentro da jornada Sementes.

## Posicao no fluxo
1. aparece no topo da experiencia, logo apos a abertura da pagina;
2. precede a leitura do corpo da licao;
3. conversa com a Navegacao Inferior, mas nao a substitui.

## Transversais para consultar
1. `012_TRANSVERSAIS/001_ICONES_CORES_E_ASSETS.md`
2. `012_TRANSVERSAIS/002_REGRAS_DE_HTML_E_ANTI_PATTERNS.md`

## Contrato tecnico
1. usar `lesson-header-nav` como wrapper canonico.
2. estrutura em 3 zonas fixas:
   a. esquerda = licao anterior;
   b. centro = `ph-plant duotone-forest` + label `Sementes`;
   c. direita = proxima licao.
3. links laterais devem usar `nav-mini-link`.
4. links precisam apontar para arquivos adjacentes reais do ciclo.
5. em `MV-S-001+` e proibido usar "Voltar" generico como substituto do header canonico.

## Contrato visual
1. o bloco central deve parecer eixo de estabilidade, nao enfeite lateral.
2. a simetria basica do topo deve ser preservada.
3. o header nao pode competir com o Hero em peso visual.

## Contrato narrativo e pedagogico
1. orienta sem quebrar o clima da licao.
2. reforca que existe sequencia, progresso e continuidade curricular.

## Anti-patterns
1. link anterior ou proximo trocado.
2. centro sem selo `Sementes`.
3. topologia assimetrica que dificulta leitura no celular.
4. uso de rotulo generico sem nome da licao adjacente.

## PASS estrutural
1. anterior, centro e proxima existem.
2. nomes e arquivos das licoes adjacentes estao corretos.
3. header superior e navegacao inferior contam a mesma sequencia.

## BLOCK estrutural
1. qualquer link errado ou ausente.
2. ausencia do selo `Sementes` no centro.
3. header reduzido a um simples "Voltar".

## Ambiguidades resolvidas
1. a excecao do Portal vale para `MV-S-000`; para `MV-S-001+` o contrato e fixo.
2. o header superior e obrigatorio mesmo quando o footer ja existe.

## Prompt operacional para IA
`Revise o Header Superior conferindo estrutura em 3 zonas, selo Sementes central e links adjacentes corretos; trate qualquer erro de navegacao como bloqueio.`
