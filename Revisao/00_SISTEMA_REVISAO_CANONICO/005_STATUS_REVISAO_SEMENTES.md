# STATUS DA REVISAO SEMENTES
Data base: 2026-03-06
Status geral: base canonica criada; pronto para precheck aprofundado

---

## 1) Objetivo deste quadro
Este arquivo e o quadro de bordo da revisao.

Serve para:
1. mostrar em que fase o sistema documental esta;
2. mostrar quais licoes podem entrar em revisao;
3. impedir perda de contexto entre sessoes.

---

## 2) Fase atual
Fase ativa:
1. sistema canonico de revisao HTML-first estruturado

Antes de escalar revisao de licoes:
1. validar no piloto `001-003`;
2. validar o gate North Star no piloto;
3. entrar em cadencia `2/dia`.

---

## 3) Status dos ativos centrais

| Ativo | Status | Observacao |
|---|---|---|
| `001_TASK_ROBUSTA_SISTEMA_REVISAO_HTML_FIRST.md` | Feito | Task canonica criada |
| `002_ESQUELETO_GERAL_LICAO_SEMENTES.md` | Feito | Estrutura geral definida |
| `003_PROTOCOLO_REVISAO_POR_LICAO.md` | Feito | Fluxo operacional definido |
| `004_RUBRICA_PREMIUM_REVISAO.md` | Feito | Rubrica objetiva criada |
| `008_NORTH_STAR_OPERACIONAL.md` | Feito | North Star virou regra operacional |
| `007_TASK_ROBUSTA_PILOTO_001_003.md` | Feito | Execucao futura do piloto estruturada |
| `008_TEMPLATE_RELATORIO_PILOTO_001_003.md` | Feito | Template de auditoria do piloto criado |
| `009_TASK_ROBUSTA_CADENCIA_2_LICOES_DIA.md` | Feito | Cadencia operacional detalhada |
| `010_TEMPLATE_SESSAO_DIARIA_REVISAO.md` | Feito | Template de handoff e sessao diaria criado |
| `015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md` | Feito | Estado real do projeto e frente ativa consolidados |
| Pasta `topicos/` | Feito | 12 guias criados |
| Pasta `transversais/` | Feito | 8 regras transversais criadas |
| Piloto `001-003` com novo sistema | Pendente | Base documental pronta; falta execucao nas licoes |

---

## 3.1 Fatos operacionais confirmados agora
1. a frente ativa continua sendo a revisao `HTML-first`;
2. `apps/web` segue como piloto tecnico contrato-first, ainda com lote de 3 licoes;
3. o Forge de Sementes validou 26 licoes em dry-run quando executado com `PYTHONIOENCODING=utf-8`;
4. o bloqueio observado no Forge do Windows foi encoding de terminal, nao YAML invalido;
5. `build/fases/sementes.py` ainda protege `MV-S-000` ate `MV-S-025` de overwrite automatico;
6. existe bug latente em `self.logger.warning` no driver de Sementes;
7. o piloto Next passou em validacao de contrato, licoes, artefatos e QA, mas ainda nao representa a UX premium final da familia.

---

## 4) Ordem de execucao aprovada
1. Validar no piloto `001-003`
2. Validar gate North Star no piloto
3. Entrar em cadencia `2/dia`

---

## 5) Backlog imediato
Prioridade maxima:
1. manter `Revisao/` impecavel e coerente com `015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md`
2. executar precheck do sistema do piloto
3. executar diagnostico puro de `MV-S-001`
4. executar diagnostico puro de `MV-S-002`
5. executar diagnostico puro de `MV-S-003`
6. registrar PASS/BLOCK North Star em cada uma

Prioridade alta:
1. registrar findings de cobertura dos topicos
2. ajustar qualquer ambiguidade encontrada no piloto
3. decidir se o sistema esta pronto para patches
4. preparar lote `004-006`
5. confirmar regra de ativacao da cadencia `2/dia`

Prioridade media:
1. refinar os prompts operacionais dos topicos
2. harmonizar legados remanescentes de nomenclatura
3. avaliar se `Sementes para o Dia` precisa de nota de transicao para o acervo

---

## 6) Piloto planejado
Licoes do piloto:
1. `MV-S-001`
2. `MV-S-002`
3. `MV-S-003`

Objetivos do piloto:
1. testar cobertura real do sistema;
2. validar se os guias por topico bastam;
3. medir se a revisao fica mais rapida e mais consistente;
4. confirmar que o sistema suporta a cadencia `2/dia`;
5. confirmar fidelidade pratica ao North Star.

---

## 7) Regra de uso deste quadro
Ao final de cada sessao:
1. atualizar o que foi criado;
2. marcar bloqueios;
3. registrar o proximo passo menor e mais seguro.
