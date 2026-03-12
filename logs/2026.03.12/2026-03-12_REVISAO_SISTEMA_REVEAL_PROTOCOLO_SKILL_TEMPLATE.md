## Revisao de Sistema - Reveal, Protocolo, Skill e Template
Data: 2026-03-12
Escopo: reconciliar a regra viva de reveal com o canônico, a skill, o template gerador e as referências de apoio

### Findings
- Alto: o canônico principal ja tinha sido corrigido, mas o template gerador ainda emitia `Visualizar` e `Mostrar Card`, o que mantinha risco real de regressao em futuros renders.
- Alto: as referências de apoio ainda ensinavam a regra anterior, o que poderia contaminar revisões futuras mesmo sem mexer no canônico principal.
- Medio: a skill de revisão ainda não chamava explicitamente a atenção para a clareza operacional do reveal no momento em que a mãe precisa agir.
- Medio: o protocolo geral de revisão ainda não nomeava claramente a pergunta `a mãe sabe quando mostrar o card?`.

### Decisoes aplicadas
- Canonizar o label visível preferencial dos cards de reveal como `Mostre este card a crianca.`.
- Manter a distinção entre `local` e `guardiao` pela arquitetura da seção, e não pelo texto do label.
- Ensinar a mesma regra em quatro camadas:
  - canônico principal
  - template gerador
  - referências de apoio
  - skill + protocolo de revisão

### Arquivos ajustados
- `site/sementes/templates/macros.j2`
- `site/sementes/templates/licao.j2`
- `Revisao/01_REFERENCIAS_DE_APOIO/topicos_licao_revisao.md`
- `Revisao/01_REFERENCIAS_DE_APOIO/padrao_visual_sementes.md`
- `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
- `Revisao/00_SISTEMA_REVISAO_CANONICO/010_TEMPLATE_SESSAO_DIARIA_REVISAO.md`
- `C:/Users/Raul/.codex/skills/revisao-sementes-topico-a-topico/SKILL.md`

### Verificacao
- Varredura sem resquicios da regra antiga nos arquivos vivos de governança, template e skill.
- `licao.j2` e `macros.j2` recompilados com Jinja sem erro de sintaxe.

### Risco residual
- Ainda existem licoes HTML antigas fora do recorte revisado de hoje com labels antigos de reveal.
- Isso nao quebra o sistema daqui para frente, porque:
  - o canônico principal agora ensina certo;
  - a skill agora revisa certo;
  - o template agora gera certo.
- Mas essas licoes antigas ainda precisam ser tocadas quando entrarem em revisão.

### Proximo passo sugerido
- Não abrir rodada separada só para trocar labels em todas as lições antigas.
- Corrigir isso naturalmente, lição por lição, quando cada HTML entrar no protocolo de revisão.
