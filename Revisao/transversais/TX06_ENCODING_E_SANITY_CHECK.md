# TX06 - ENCODING E SANITY CHECK

## Quando consultar
1. toda vez que editar HTML, MD ou YAML ligado a licoes.

## Regra canonica
1. salvar sempre em UTF-8;
2. nao converter encoding no meio da sessao;
3. tratar qualquer sinal de corrupcao como bloqueio de fechamento.

## Sanity check
```powershell
rg -n "Ã|Â|â|\b\w+\?\w+\b" site/sementes/MV-S-00[0-3]*.html
```

## PASS
1. texto limpo;
2. acentos inteiros;
3. nada de ruido visual.

## FAIL
1. `CoraÃ§ao`, `narracÃ£o`, `vocÃª`;
2. palavras quebradas por `?`;
3. qualquer suspeita de encoding salvo errado.

## Impacto no premium
1. encoding quebrado derruba credibilidade imediata.

