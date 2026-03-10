# 012 - NAVEGACAO INFERIOR

## Missao do topico
1. encerrar a pagina com navegacao segura, previsivel e coerente com o topo.

## Posicao no fluxo
1. ultimo bloco tecnico da licao;
2. vem depois da Formacao do Portador;
3. fecha a pagina sem disputar protagonismo com a narrativa.

## Transversais para consultar
1. `012_TRANSVERSAIS/002_REGRAS_DE_HTML_E_ANTI_PATTERNS.md`

## Contrato tecnico
1. usar `.lesson-nav` com botoes `prev` e `next`.
2. cada botao deve ter `nav-label` e `nav-title`.
3. footer simples deve existir ao final da pagina.
4. os arquivos e titulos precisam coincidir com o Header Superior e com `Conexao da Jornada`.
5. esta camada deve permanecer silenciosa: resolver navegacao sem reabrir a licao.

## Contrato visual
1. fechamento limpo, sem ruido e sem competir com a secao anterior.
2. os botoes devem ser legiveis e seguros no celular.

## Contrato pedagogico
1. protege continuidade do ciclo.
2. reduz friccao para familias que avancam licao por licao.
3. fecha o percurso com seguranca, sem roubar energia da secao anterior.

## Taste editorial
1. a navegacao inferior deve parecer quieta e confiavel;
2. ela nao disputa protagonismo com a formacao nem com o fechamento narrativo;
3. se chamar mais atencao que a ultima secao da licao, ha ruido desnecessario.

## Anti-patterns
1. links errados.
2. titulo trocado.
3. ausencia de footer.
4. navegacao inferior descoordenada do topo.
5. navegacao mais chamativa que o fechamento narrativo ou formativo anterior.

## PASS estrutural
1. anterior e proxima estao corretas.
2. labels e titulos estao coerentes.
3. footer simples fecha a pagina.

## BLOCK estrutural
1. qualquer divergencia de link ou titulo.
2. ausencia de um dos botoes obrigatorios.
3. incompatibilidade com Header Superior.

## Ambiguidades resolvidas
1. a navegacao inferior nao substitui `Conexao da Jornada`; ela e camada tecnica final.
2. o footer pode ser simples, mas nao deve desaparecer nas licoes padrao.
3. `simples` aqui significa confiavel e quieto, nao descuidado.

## Checklist de revisao
1. `prev` e `next` existem, com links e titulos corretos?
2. a navegacao inferior bate com Header Superior e `Conexao da Jornada`?
3. `nav-label`, `nav-title` e footer simples existem?
4. o bloco parece quieto e confiavel, sem competir com a secao anterior?
5. a camada tecnica final fecha a pagina sem tentar substituir a conexao narrativa?

## Prompt operacional para IA
`Revise a Navegacao Inferior validando lesson-nav, prev/next, labels, titulos e footer; trate qualquer divergencia com o Header Superior ou com Conexao da Jornada como bloqueio estrutural, e preserve esta camada como fechamento tecnico quieto e confiavel.`
