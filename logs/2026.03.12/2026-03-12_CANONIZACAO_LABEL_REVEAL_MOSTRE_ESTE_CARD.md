## Canonizacao - Label de Reveal `Mostre este card a crianca`
Data: 2026-03-12
Motivo: incorporar feedback de mae real e alinhar o HTML familiar a instrucoes mais claras para o Portador

### Decisao
- Nos cards de reveal visiveis para a familia, o label preferencial passa a ser `Mostre este card a crianca.`.
- A distincao entre `local` e `guardiao` continua sendo governada pela arquitetura da secao:
  - `Ritual de Entrada` revela o local
  - `A Jornada` revela o guardiao
- Quando o timing do gesto pedir mais apoio, a mesma instrucao pode ser repetida no `instruction-box`.

### Contradicao resolvida
- O canônico anterior ainda preferia labels como `Lugar revelado`, `Guardiao revelado` e `Guardia revelada`.
- A pratica viva ja havia avancado em `MV-S-003`, onde o feedback de mae real validou melhor a instrucao explicita.
- A partir desta rodada, a regra viva sobe para o canônico.

### Arquivos ajustados
- `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/001_ICONES_CORES_E_ASSETS.md`
- `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/004_GUARDIOES_CARDS_E_REVEAL.md`
- `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/004_RITUAL_DE_ENTRADA.md`
- `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/005_A_JORNADA.md`
- `site/sementes/MV-S-000_O_PORTAL_DO_REINO.html`
- `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html`

### Verificacao
- `L000` e `L001` ficaram sem resquicio dos labels antigos nos cards tocados.
- Checagem visual rapida em mobile: o label novo coube bem e permaneceu legivel.

### Impacto
- Menos traducao mental para a mae.
- Reveal mais acionavel no momento exato.
- Maior coerencia entre `L003` e as licoes revisadas.
