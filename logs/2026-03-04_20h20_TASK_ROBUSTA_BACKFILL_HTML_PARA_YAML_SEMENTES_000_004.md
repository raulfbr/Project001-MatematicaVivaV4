# TASK EXECUTIVA V3 - BACKFILL HTML -> YAML (SEMENTES 000-004)
Data: 2026-03-04 20:20 (America/Sao_Paulo)  
Revisao: 2026-03-04 (versao operacional detalhada)  
Escopo: `MV-S-000` a `MV-S-004`  
Missao: converter fielmente o conteudo final dos HTMLs para os YAMLs V6, removendo drift entre front e fonte estruturada, e tratar explicitamente o caso de template YAML desatualizado.

---

## 0) Decisao desta fase (obrigatoria)
1. Fonte de verdade temporaria: HTML (`site/sementes/MV-S-000..004_*.html`).
2. Acao desta fase: backfill HTML -> YAML em `curriculo/01_SEMENTESV6`.
3. Regra estrutural: preservar schema YAML existente em cada licao.
4. Regra editorial: preservar tom narrativo do HTML (Portador + Guardioes).
5. Proxima fase: com YAML sincronizado, voltar para fluxo YAML-first.
6. Excecao desta versao: se o `_TEMPLATE_V6.yaml` estiver defasado em relacao ao padrao real 000-004, atualizar template de forma controlada (sem quebrar retrocompatibilidade).

---

## 1) Escopo, nao-escopo e entregaveis
Escopo:
1. Sincronizar os pares HTML/YAML das licoes 000, 001, 002, 003 e 004.
2. Validar coerencia narrativa, matematica, curricular e tecnica por licao.
3. Registrar decisoes e riscos por licao.

Nao-escopo:
1. Nao criar licao nova.
2. Nao alterar licoes 005+.
3. Nao reescrever design do HTML.
4. Nao refatorar schema V6.

Entregaveis:
1. 5 YAMLs atualizados e validados.
2. Relatorio de execucao por licao (PASS/BLOCK por gate).
3. Registro de conflitos e decisoes.
4. Diagnostico de defasagem do template (`_TEMPLATE_V6.yaml`) com status: `SEM_DRIFT`, `DRIFT_LEVE`, `DRIFT_MODERADO` ou `DRIFT_ALTO`.
5. Se houver `DRIFT_MODERADO` ou `DRIFT_ALTO`: template atualizado (ou template candidato versionado) + notas de migracao.

---

## 2) Arquivos e referencias oficiais
Pares 1:1:
1. `site/sementes/MV-S-000_O_PORTAL_DO_REINO.html` -> `curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml`
2. `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html` -> `curriculo/01_SEMENTESV6/001_TRINDADE_PALMA.yaml`
3. `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html` -> `curriculo/01_SEMENTESV6/002_PEDRAS_FORTALEZA.yaml`
4. `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html` -> `curriculo/01_SEMENTESV6/003_ESTRELA_REINO.yaml`
5. `site/sementes/MV-S-004_A_ORDEM_DO_DIA.html` -> `curriculo/01_SEMENTESV6/004_A_ORDEM_DO_DIA.yaml`

Referencias de alinhamento:
1. `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md`
2. `logs/2026-03-04_19h56_Padronizar`
3. `bmad/orchestrator.yaml` (apenas como checklist de orquestracao/revisao, sem sobrepor fonte de verdade desta fase)
4. `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml` (template operacional atual)
5. `bmad/templates/00_K_sementes/licao-template.yaml` (template BMAD de referencia)

---

## 3) Pre-flight tecnico (obrigatorio antes de editar)
Executar e registrar resultado:

```powershell
$targets = @(
  @{id='MV-S-000'; html='site/sementes/MV-S-000_O_PORTAL_DO_REINO.html'; yaml='curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml'},
  @{id='MV-S-001'; html='site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html'; yaml='curriculo/01_SEMENTESV6/001_TRINDADE_PALMA.yaml'},
  @{id='MV-S-002'; html='site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html'; yaml='curriculo/01_SEMENTESV6/002_PEDRAS_FORTALEZA.yaml'},
  @{id='MV-S-003'; html='site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html'; yaml='curriculo/01_SEMENTESV6/003_ESTRELA_REINO.yaml'},
  @{id='MV-S-004'; html='site/sementes/MV-S-004_A_ORDEM_DO_DIA.html'; yaml='curriculo/01_SEMENTESV6/004_A_ORDEM_DO_DIA.yaml'}
)

$targets | ForEach-Object {
  "{0} | HTML:{1} | YAML:{2}" -f $_.id, (Test-Path $_.html), (Test-Path $_.yaml)
}
```

Backup antes da primeira alteracao:

```powershell
$stamp = Get-Date -Format "yyyy-MM-dd_HHmm"
$bk = "logs/backups/$stamp"
New-Item -ItemType Directory -Path $bk -Force | Out-Null
$targets | ForEach-Object { Copy-Item $_.yaml "$bk/$($_.id)_pre-backfill.yaml" -Force }
```

Bloqueio de execucao:
1. Se qualquer arquivo do par faltar: `BLOCK`.
2. Se backup falhar: `BLOCK`.

### 3.1) Diagnostico obrigatorio de defasagem do template
Objetivo:
1. Detectar se o template atual cobre o padrao real das licoes 000-004.
2. Classificar severidade de drift antes de editar template.

Comando sugerido (comparacao robusta de chaves de 1o nivel em `licao.*`, sem depender de parser YAML estrito):

```powershell
$tpl = 'curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml'
$lessons = @(
  'curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml',
  'curriculo/01_SEMENTESV6/001_TRINDADE_PALMA.yaml',
  'curriculo/01_SEMENTESV6/002_PEDRAS_FORTALEZA.yaml',
  'curriculo/01_SEMENTESV6/003_ESTRELA_REINO.yaml',
  'curriculo/01_SEMENTESV6/004_A_ORDEM_DO_DIA.yaml'
)

function Get-LicaoTopKeys($path){
  $lines = Get-Content -Path $path -Encoding UTF8
  $keys = New-Object System.Collections.Generic.HashSet[string]
  $inLicao = $false
  foreach($line in $lines){
    if($line -match '^licao:\s*$'){ $inLicao = $true; continue }
    if($inLicao){
      if($line -match '^[^\s]'){ break }
      if($line -match '^  ([a-zA-Z_][a-zA-Z0-9_]*):'){ [void]$keys.Add($matches[1]) }
    }
  }
  return $keys
}

$tplKeys = Get-LicaoTopKeys $tpl
$union = New-Object System.Collections.Generic.HashSet[string]
foreach($l in $lessons){
  $k = Get-LicaoTopKeys $l
  foreach($x in $k){ [void]$union.Add($x) }
}

$missing = @($union | Where-Object { -not $tplKeys.Contains($_) } | Sort-Object)
$extra   = @($tplKeys | Where-Object { -not $union.Contains($_) } | Sort-Object)

"MISSING_IN_TEMPLATE: $($missing -join ', ')"
"EXTRA_IN_TEMPLATE:   $($extra -join ', ')"
```

Classificacao de drift:
1. `SEM_DRIFT`: sem faltas relevantes.
2. `DRIFT_LEVE`: faltas pequenas (campos nao-criticos, sem impacto de render).
3. `DRIFT_MODERADO`: faltam blocos relevantes em pelo menos 1 secao pedagogica.
4. `DRIFT_ALTO`: template nao representa estrutura real (risco alto de regressao em geracao futura).

Regra de acao:
1. `SEM_DRIFT` ou `DRIFT_LEVE`: seguir backfill, sem mexer em template nesta fase.
2. `DRIFT_MODERADO`: atualizar `_TEMPLATE_V6.yaml` de forma retrocompativel.
3. `DRIFT_ALTO`: criar `curriculo/01_SEMENTESV6/_TEMPLATE_V6_4_CANONICO_000_004.yaml` e manter `_TEMPLATE_V6.yaml` congelado para nao quebrar pipelines legados.

---

## 4) Mapeamento canonico HTML -> YAML (versao aplicada ao schema real)
Regra: mapear para chaves ja existentes na licao. Se uma chave nao existir no YAML da licao, nao inventar schema; usar bloco equivalente existente e registrar decisao.

1. Hero e metadados:
- HTML: meta da licao, titulo, frase de destaque
- YAML alvo: `licao.metadados.*` + `para_portador.ideia_viva.frase`

2. Navegacao e ganchos:
- HTML: links anterior/proxima + frase de continuidade
- YAML alvo: `navegacao.*` + `linkage.*`

3. Preparacao do Portador:
- HTML: dicas, segredo pedagogico, materiais
- YAML alvo: `para_portador.*` + `para_portador.preparacao.materiais`

4. Ritual de abertura:
- HTML: ambiente, transicao, fala inicial
- YAML alvo: `ritual_abertura.*`

5. Jornada narrativa:
- HTML: cenas, falas de guardiao, instrucoes do portador
- YAML alvo: `jornada.narrativa_principal[]`

6. Momento concreto:
- HTML: atividade concreta/manipulativa
- YAML alvo: `jornada.concreto.*`

7. Narracao:
- HTML: perguntas do coracao + pergunta principal
- YAML alvo: `narracao.*`

8. Fechamento:
- HTML: fala final, fio de ouro, volta
- YAML alvo: `ritual_fechamento.*`

9. Formacao pedagógica:
- HTML: estrategia do mestre, CM/CPA, orientacoes familia
- YAML alvo: `para_familia.*`

10. Sementes para o dia:
- HTML: micro-praticas pos-licao
- YAML alvo preferencial: `sementes_do_dia.*` (se existir na licao).  
Se nao existir: manter no bloco equivalente ja existente e registrar no log.

Observacao importante:
1. `MV-S-000` e liturgica/narrativa; nao forcar matematica onde o HTML nao propoe.
2. Em `MV-S-003` ja ha variacao estrutural (`sementes_do_dia`); preservar.
3. Se bloco existir nas licoes e nao existir no template: marcar no diagnostico de drift.

---

## 5) Gates de qualidade (Definition of Done)
Cada licao so pode ser `APROVADA` se passar todos os gates:

1. Gate Narrativa:
- Guardiao lider correto.
- Local e clima coerentes do inicio ao fim.
- Fio de ouro conecta com proxima licao.

2. Gate Matematica:
- Objetivo da licao aparece em `licao.metadados.objetivo_pedagogico` ou equivalente.
- Atividade manipulativa esta clara em `jornada.concreto`.
- Passos sao executaveis por adulto em casa.

3. Gate Curricular (CM + Curriculo Mestre):
- Nao contradiz a progressao 000_K.
- Mantem principio "coisas antes de signos" no nivel Sementes.
- Nao acelera abstracao sem ponte concreta.

4. Gate Tecnico:
- YAML legivel, sem corromper acentos.
- Indentacao consistente.
- Sem campos criticos vazios apos sincronizacao.

5. Gate Template (global da fase):
- `_TEMPLATE_V6.yaml` avaliado contra 000-004.
- Se drift >= moderado: acao de template executada e registrada.
- Template final nao pode reduzir cobertura das secoes canonicas.

Status final por licao:
1. `APROVADA`: 4 gates PASS.
2. `BLOCK`: qualquer gate falhou.

Status global da fase:
1. `CONCLUIDA`: 5 licoes aprovadas + Gate Template PASS.
2. `PARCIAL`: licoes aprovadas, mas Gate Template pendente.

---

## 6) Protocolo operacional por licao (atomico)
Usar exatamente este fluxo em cada licao.

### Passo A - Diagnostico comparativo
1. Abrir HTML e YAML lado a lado.
2. Preencher matriz de 10 blocos: `OK`, `AJUSTAR`, `AUSENTE`.
3. Anotar divergencias criticas:
- narrativa (guardiao/local/tom),
- matematica (objetivo/pratica),
- navegacao (anterior/proxima).

Saida A:
1. Matriz de divergencia por bloco.
2. Lista curta de ajustes obrigatorios.

### Passo B - Extracao fiel do HTML
1. Capturar texto final de cada bloco (sem rascunhos paralelos).
2. Capturar ordem das cenas da jornada.
3. Capturar linguagem exata de instrucoes concretas.

Saida B:
1. Rascunho de transferencia por bloco.
2. Lista de frases-chave que nao podem ser perdidas.

### Passo C - Aplicacao no YAML (sem mudar schema)
1. Atualizar apenas campos equivalentes ja existentes.
2. Preservar ordem de blocos no YAML.
3. Atualizar listas (`materiais`, `instrucoes_portador`, `perguntas_coracao`, `sugestoes`).
4. Revisar navegacao e linkage apos ajustes de texto.

Regra de conflito estrutural:
1. Campo nao existe no YAML da licao: nao criar chave nova sem necessidade.
2. Usar bloco equivalente ja existente.
3. Registrar decisao no relatorio.

Saida C:
1. YAML sincronizado.
2. Lista de decisoes de mapeamento.

### Passo D - Validacao em 2 camadas
Camada 1 (conteudo):
1. Releitura completa da licao no YAML.
2. Confirmar continuidade narrativa com anterior/proxima.
3. Confirmar pratica concreta fiel ao HTML.

Camada 2 (tecnica):
1. Procurar tabs:
```powershell
rg -n "\t" curriculo/01_SEMENTESV6/00[0-4]_*.yaml
```
2. Verificar sinais de campos vazios apos ajuste:
```powershell
rg -n "titulo:\\s*$|frase:\\s*$|desc:\\s*$|script:\\s*$" curriculo/01_SEMENTESV6/00[0-4]_*.yaml
```
3. Validacao por parser (opcional, quando disponivel):
```powershell
@'
import pathlib, sys
try:
    import yaml
except Exception:
    print("WARN: PyYAML nao disponivel; manter validacao manual.")
    sys.exit(0)
files = [
    "curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml",
    "curriculo/01_SEMENTESV6/001_TRINDADE_PALMA.yaml",
    "curriculo/01_SEMENTESV6/002_PEDRAS_FORTALEZA.yaml",
    "curriculo/01_SEMENTESV6/003_ESTRELA_REINO.yaml",
    "curriculo/01_SEMENTESV6/004_A_ORDEM_DO_DIA.yaml",
]
for f in files:
    yaml.safe_load(pathlib.Path(f).read_text(encoding="utf-8"))
    print("OK:", f)
'@ | python -
```

Saida D:
1. PASS/BLOCK por gate.
2. Lista de correcoes tecnicas finais (se houver).

### Passo E - Registro e fechamento da licao
1. Registrar resumo do que mudou.
2. Registrar riscos residuais.
3. Registrar decisoes em ambiguidade.
4. Marcar status final da licao.

Saida E:
1. Linha-resumo padrao:
`L00X | Narrativa: PASS/BLOCK | Matematica: PASS/BLOCK | Curricular: PASS/BLOCK | Tecnica: PASS/BLOCK | Status: APROVADA/BLOCK`

### Passo F - Atualizacao de template (somente se drift >= moderado)
1. Consolidar uniao de blocos reais observados nas licoes 000-004.
2. Atualizar placeholders e exemplos do template para refletir o padrao real.
3. Garantir retrocompatibilidade:
- Nao remover blocos usados por licoes existentes.
- Nao renomear chaves sem alias ou nota de migracao.
4. Se risco alto de quebra:
- criar novo arquivo versionado (`_TEMPLATE_V6_4_CANONICO_000_004.yaml`);
- manter `_TEMPLATE_V6.yaml` intacto e apontar plano de migracao.

Saida F:
1. Status do template: `SEM_DRIFT | DRIFT_LEVE | DRIFT_MODERADO | DRIFT_ALTO`.
2. Arquivo final do template (atualizado ou versionado).
3. Nota de migracao (quando aplicavel).

---

## 7) Template obrigatorio de relatorio por licao
Copiar e preencher para cada licao:

```md
### L00X - [TITULO]
- Arquivos:
  - HTML: [...]
  - YAML: [...]
- Matriz 10 blocos:
  - Hero:
  - Navegacao:
  - Preparacao do Portador:
  - Ritual de Entrada:
  - Jornada:
  - Momento Concreto:
  - Narracao:
  - Ritual de Fechamento:
  - Formacao do Portador:
  - Sementes para o Dia:
- Principais alteracoes aplicadas:
  - [...]
- Decisoes de mapeamento (quando campo nao existia):
  - [...]
- Validacao por gate:
  - Narrativa: PASS/BLOCK
  - Matematica: PASS/BLOCK
  - Curricular: PASS/BLOCK
  - Tecnica: PASS/BLOCK
- Template drift observado:
  - SEM_DRIFT | DRIFT_LEVE | DRIFT_MODERADO | DRIFT_ALTO
- Risco residual:
  - [...]
- Status final:
  - APROVADA/BLOCK
```

---

## 8) Ordem de execucao recomendada
1. `MV-S-001` (base 1-3)
2. `MV-S-002` (organizacao/construcao)
3. `MV-S-003` (forma 4-5 + variacao estrutural)
4. `MV-S-004` (ordem/sequencia; atualmente mais propensa a drift)
5. `MV-S-000` (liturgica; fechar por ultimo para manter coerencia de tom global)

Racional:
1. Primeiro estabiliza progressao numerica.
2. Depois fecha continuidade narrativa e excecao liturgica.

---

## 9) Regras de decisao em conflito (obrigatorias)
1. HTML vs YAML: HTML vence nesta fase.
2. HTML vs Curriculo Mestre:
- se contradizer objetivo central da estacao: `BLOCK` e abrir decisao.
- se for variacao de redacao mantendo objetivo: manter HTML.
3. Dúvida de tom: manter fala do HTML.
4. Dúvida de schema: preservar estrutura YAML existente.
5. Dúvida nao resolvivel com evidencias locais: marcar `BLOCK` com pergunta objetiva.
6. Template vs licoes 000-004: nesta fase, licoes reais vencem para definir atualizacao do template.
7. Template novo vs template legado: preferir arquivo versionado quando houver risco de quebra.

---

## 10) Controle global de execucao (quadro de bordo)
Preencher ao final:

```md
| Licao | Narrativa | Matematica | Curricular | Tecnica | Status |
|------|-----------|------------|------------|---------|--------|
| 000  |           |            |            |         |        |
| 001  |           |            |            |         |        |
| 002  |           |            |            |         |        |
| 003  |           |            |            |         |        |
| 004  |           |            |            |         |        |
```

Definicao de conclusao da fase:
1. Todas as 5 licoes em `APROVADA`.
2. Sem `BLOCK` aberto.
3. Relatorio completo salvo em `logs`.
4. Gate Template em `PASS` (com ou sem versao nova).

---

## 11) Proxima fase (apos concluir esta)
1. Congelar YAML 000-004 como nova base confiavel.
2. Congelar template final da fase (`_TEMPLATE_V6.yaml` atualizado ou `_TEMPLATE_V6_4_CANONICO_000_004.yaml`).
3. Migrar para revisao YAML-first com gates permanentes (CM/CPA/Engenharia + Template Gate).
4. Avancar para 005+ sem reintroduzir drift HTML/YAML.

---

## 12) Nota de especialista (produto premium)
Esta fase nao e criativa, e estrutural: ela garante consistencia entre experiencia publicada (HTML) e fonte curricular (YAML). Sem essa sincronizacao, qualquer render futuro tende a regredir qualidade. Com ela, o projeto ganha previsibilidade editorial, integridade pedagogica e base solida para escala.
