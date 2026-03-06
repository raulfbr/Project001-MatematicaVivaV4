# 001 - BASE E HERO

## Missao do topico
1. garantir integridade tecnica da pagina e abrir a licao com identidade premium reconhecivel.

## Posicao no fluxo
1. camada base do documento, antes da experiencia pedagogica;
2. sustenta Hero e Header Superior;
3. se falhar, a licao inteira entra em risco tecnico e visual.

## Transversais para consultar
1. `012_TRANSVERSAIS/001_ICONES_CORES_E_ASSETS.md`
2. `012_TRANSVERSAIS/002_REGRAS_DE_HTML_E_ANTI_PATTERNS.md`
3. `012_TRANSVERSAIS/006_ENCODING_E_SANITY_CHECK.md`
4. `012_TRANSVERSAIS/008_NORTH_STAR_OPERACIONAL.md`

## Contrato tecnico
1. `<head>` deve conter `meta charset`, `viewport`, `title`, `style.css`, Google Fonts, Phosphor CDN e favicon.
2. `<body>` deve usar classe de clima compativel com licao padrao (`clima-1` para `MV-S-001+`).
3. `home-btn` deve existir com `ph-house duotone-forest`.
4. `lesson-container` deve envolver a pagina antes das secoes da licao.
5. o Hero deve conter `lesson-meta-tag`, `hero-title`, `hero-quote` e asset principal coerente.
6. imagem principal deve ter `alt` util e fallback previsivel quando aplicavel.
7. o Hero nao substitui o Header Superior; ambos precisam coexistir.

## Contrato visual e de assets
1. o meta-tag deve orientar rapidamente: numero da licao, titulo sintese e duracao.
2. o asset principal deve parecer parte da obra, nao capa generica.
3. a paleta e os icones devem seguir a liturgia visual do ciclo Sementes.

## Contrato narrativo e pedagogico
1. o Hero deve preparar o adulto para a atmosfera da licao sem antecipar a secao narrativa.
2. a frase de impacto deve prometer maravilhamento, nao marketing vazio.
3. o adulto precisa entender o foco da licao em poucos segundos.

## Anti-patterns
1. omitir dependencias do `<head>`.
2. usar imagem desconectada do guardiao, local ou proposta da licao.
3. hero com titulo frio, burocratico ou intercambiavel.
4. misturar navegacao superior dentro do Hero.

## PASS estrutural
1. pagina carrega com fontes, icones e CSS previstos.
2. `home-btn`, `lesson-container` e Hero estao presentes.
3. Hero possui meta, titulo, frase e imagem coerentes.

## BLOCK estrutural
1. falta algum elemento base do documento.
2. Hero sem identidade suficiente para orientar a licao.
3. asset principal quebrado, ausente ou evidentemente desalinhado.

## Ambiguidades resolvidas
1. Base do Documento e Hero compartilham o mesmo topico por serem camada de abertura, mas o Header Superior continua sendo topico proprio.
2. `MV-S-000` pode divergir em clima e composicao, mas `MV-S-001+` segue este contrato.

## Prompt operacional para IA
`Revise Base e Hero validando head, body, home-btn, lesson-container e Hero completo; bloqueie qualquer quebra de integridade, identidade ou asset principal.`
