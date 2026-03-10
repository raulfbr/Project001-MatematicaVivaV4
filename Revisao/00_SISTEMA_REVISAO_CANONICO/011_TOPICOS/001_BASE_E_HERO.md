# 001 - BASE E HERO

## Missao do topico
1. garantir integridade tecnica da pagina e abrir a licao com identidade premium reconhecivel e acolhedora.

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
1. o documento deve abrir com `<!DOCTYPE html>` e usar `<html lang="pt-BR">`.
2. `<head>` deve conter `meta charset`, `viewport`, `title`, `style.css`, Google Fonts, Phosphor CDN e favicon.
3. `<body>` deve usar classe de clima compativel com licao padrao (`clima-1` para `MV-S-001+`).
4. `home-btn` deve existir com `ph-house duotone-forest`.
5. `lesson-container` deve envolver a pagina antes das secoes da licao.
6. o Hero deve conter `lesson-meta-tag`, `hero-title`, `hero-quote` e asset principal coerente.
7. o asset principal deve ajudar o adulto a identificar rapidamente quem ou o que ocupa o centro simbolico da licao.
8. imagem principal deve ter `alt` util e fallback previsivel quando aplicavel.
9. o Hero nao substitui o Header Superior; ambos precisam coexistir.

## Contrato visual e de assets
1. o meta-tag deve orientar rapidamente: numero da licao, titulo sintese e duracao, sem obrigar leitura demorada.
2. o asset principal deve parecer parte da obra, nao capa generica.
3. a paleta e os icones devem seguir a liturgia visual do ciclo Sementes.

## Contrato narrativo e pedagogico
1. o Hero deve preparar o adulto para a atmosfera da licao sem antecipar a secao narrativa.
2. a frase de impacto deve prometer maravilhamento, nao marketing vazio.
3. o adulto precisa entender o foco da licao em poucos segundos.
4. o Hero deve situar sem intimidar: a familia precisa sentir convite, nao pressao de performance.

## Anti-patterns
1. omitir dependencias do `<head>`.
2. usar imagem desconectada do guardiao, local ou proposta da licao.
3. hero com titulo frio, burocratico ou intercambiavel.
4. misturar navegacao superior dentro do Hero.
5. hero bonito, mas vago demais para orientar o adulto.

## PASS estrutural
1. pagina carrega com fontes, icones e CSS previstos.
2. `home-btn`, `lesson-container` e Hero estao presentes.
3. Hero possui meta, titulo, frase e imagem coerentes.
4. o adulto entende rapidamente onde entrou e qual e o clima da licao.

## BLOCK estrutural
1. falta algum elemento base do documento.
2. Hero sem identidade suficiente para orientar a licao.
3. asset principal quebrado, ausente ou evidentemente desalinhado.
4. abertura gera confusao ou parece capa generica reaproveitada.

## Ambiguidades resolvidas
1. Base do Documento e Hero compartilham o mesmo topico por serem camada de abertura, mas o Header Superior continua sendo topico proprio.
2. `MV-S-000` pode divergir em clima e composicao, mas `MV-S-001+` segue este contrato.

## Checklist de revisao
1. `doctype`, `html lang`, `head`, `body`, `home-btn` e `lesson-container` existem e estao corretos?
2. o Hero tem `lesson-meta-tag`, `hero-title`, `hero-quote` e asset principal coerente?
3. o asset principal tem `alt` util e fallback quando necessario?
4. a frase do Hero orienta a familia em segundos sem soar marketing vazio?
5. o Hero abre a licao com identidade propria sem competir com o Header Superior?

## Prompt operacional para IA
`Revise Base e Hero validando doctype, html lang, head, body, home-btn, lesson-container e Hero completo; bloqueie qualquer quebra de integridade, identidade ou abertura generica.`
