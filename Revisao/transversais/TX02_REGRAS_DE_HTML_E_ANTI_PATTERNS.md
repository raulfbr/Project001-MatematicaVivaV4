# TX02 - REGRAS DE HTML E ANTI-PATTERNS

## Quando consultar
1. sempre que houver ajuste de markup, boxes, wrappers ou navegacao.

## Regra canonica
1. preservar estrutura limpa e previsivel;
2. preferir blocos semanticamente claros;
3. nao usar HTML improvisado para resolver escrita ruim;
4. nao espalhar ajustes de layout em markup desnecessario.

## Anti-patterns proibidos
1. fragmentar o Portador em varios blocos sem necessidade;
2. usar `<br>` para montar boxes pedagogicas;
3. misturar voz tecnica e voz narrativa no mesmo bloco sem distincao;
4. quebrar ordem das secoes;
5. duplicar scripts ou assets;
6. remover wrappers essenciais de boxes ou cards.

## PASS
1. markup legivel;
2. blocos coerentes;
3. estrutura facil de auditar.

## FAIL
1. remendo rapido que piora consistencia;
2. HTML que so "parece funcionar";
3. variacao estrutural sem justificativa.

## Impacto no premium
1. HTML limpo reduz drift e facilita revisao diaria.

