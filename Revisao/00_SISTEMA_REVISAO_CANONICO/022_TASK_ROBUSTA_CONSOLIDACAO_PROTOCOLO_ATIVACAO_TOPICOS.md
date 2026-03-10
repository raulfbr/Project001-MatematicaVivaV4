# 022 - TASK ROBUSTA DE CONSOLIDACAO DO PROTOCOLO DE ATIVACAO POR TOPICOS
Data: 2026-03-10
Status: concluida
Escopo: endurecer o sistema canonico para que toda revisao de licao seja ativada por topicos, ponto a ponto, com gates premium estaveis

---

## 1) Missao
Esta task existe para consolidar o protocolo premium de revisao por topicos.

Objetivo:
1. impedir ativacao frouxa do sistema;
2. fechar drift entre protocolo, rubrica, topicos e template;
3. tornar obrigatoria a matriz `001-012`;
4. institucionalizar auditoria de fronteiras entre secoes adjacentes;
5. deixar o sistema mais seguro para produzir licoes impecaveis, alinhadas e premium.

---

## 2) Diagnostico desta passada
Antes desta consolidacao, o sistema ja estava forte, mas ainda tinha brechas operacionais:
1. `003_PROTOCOLO_REVISAO_POR_LICAO.md` ainda permitia leitura por `topicos relevantes`, o que enfraquecia a passada `001-012`;
2. a rubrica ainda podia ser usada por impressao geral, sem matriz topica completa;
3. o template diario nao obrigava cobertura topica nem auditoria de fronteiras;
4. `011_TOPICOS/000_README.md` ainda nao explicitava o modo de ativacao do protocolo;
5. `012_TRANSVERSAIS/000_README.md` ainda nao explicitava o pacote minimo transversal;
6. os topicos `001`, `002`, `003`, `008`, `009` e `012` ainda nao tinham `Checklist de revisao`;
7. o sistema ainda nao tratava de forma suficientemente explicita a auditoria das fronteiras criticas:
   a. `004 -> 005`;
   b. `005 -> 006`;
   c. `006 -> 007`;
   d. `008 -> 009`;
   e. `009 -> 010`;
   f. `010 -> 011`.

---

## 3) Decisao canonica desta task
A partir desta consolidacao:
1. toda revisao de licao padrao abre os 12 topicos oficiais;
2. toda revisao registra `PASS / GAP / BLOCK` por topico;
3. toda revisao audita fronteiras criticas entre secoes adjacentes;
4. a rubrica so pode ser aplicada depois da matriz topica;
5. `TASTE` continua gate editorial transversal;
6. `North Star` continua gate espiritual final;
7. `topicos relevantes` passa a valer apenas para transversais adicionais, nao para os 12 topicos.

---

## 4) Arquivos sob intervencao
1. `000_INDEX_SISTEMA_REVISAO.md`
2. `003_PROTOCOLO_REVISAO_POR_LICAO.md`
3. `004_RUBRICA_PREMIUM_REVISAO.md`
4. `010_TEMPLATE_SESSAO_DIARIA_REVISAO.md`
5. `011_TOPICOS/000_README.md`
6. `012_TRANSVERSAIS/000_README.md`
7. `011_TOPICOS/001_BASE_E_HERO.md`
8. `011_TOPICOS/002_HEADER_SUPERIOR.md`
9. `011_TOPICOS/003_PREPARACAO_DO_PORTADOR.md`
10. `011_TOPICOS/008_RITUAL_DE_FECHAMENTO.md`
11. `011_TOPICOS/009_CONEXAO_DA_JORNADA.md`
12. `011_TOPICOS/012_NAVEGACAO_INFERIOR.md`

---

## 5) Patches executados

### 5.1 Index
1. adicionada rota rapida de `como ativar agora o protocolo de revisao por topicos`;
2. adicionada esta task `022` como documento de consolidacao;
3. reforcada a leitura operacional de ativacao por topicos.

### 5.2 Protocolo por licao
1. protocolo reescrito para exigir ativacao formal;
2. leitura dos 12 topicos virou obrigatoria;
3. criada a matriz topica `PASS / GAP / BLOCK`;
4. criada auditoria obrigatoria de fronteiras criticas;
5. adicionada reauditoria depois do patch;
6. gates finais agora incluem:
   a. `Cobertura topica`;
   b. `Fronteiras topicas`;
   c. `North Star`;
   d. `Taste editorial`;
7. `Definition of Ready` e `Definition of Done` foram endurecidas.

### 5.3 Rubrica premium
1. adicionadas pre-condicoes antes da pontuacao;
2. a rubrica agora depende de matriz topica e fronteiras;
3. `Cobertura topica` e `Fronteiras topicas` viraram gates formais;
4. `PASS PREMIUM` agora exige esses gates em `PASS`.

### 5.4 Template diario
1. o template agora abre com ativacao explicita do protocolo;
2. passou a carregar matriz topica `001-012` para `Licao A` e `Licao B`;
3. passou a carregar bloco proprio para fronteiras criticas;
4. os gates finais ficaram alinhados ao protocolo novo.

### 5.5 README dos topicos
1. o modo de ativacao por topicos foi explicitado;
2. o README agora exige matriz completa e auditoria de fronteiras;
3. o documento passou a citar `Checklist de revisao` como parte do contrato de cada topico.

### 5.6 README das transversais
1. o pacote minimo transversal foi explicitado;
2. `006_ENCODING_E_SANITY_CHECK.md` foi reforcado como obrigatorio apos patch;
3. `008_NORTH_STAR_OPERACIONAL.md` foi reforcado como gate desde o diagnostico, nao apenas no fim.

### 5.7 Topicos sem checklist
Foram completados os checklists faltantes em:
1. `001_BASE_E_HERO.md`
2. `002_HEADER_SUPERIOR.md`
3. `003_PREPARACAO_DO_PORTADOR.md`
4. `008_RITUAL_DE_FECHAMENTO.md`
5. `009_CONEXAO_DA_JORNADA.md`
6. `012_NAVEGACAO_INFERIOR.md`

---

## 6) O que muda na pratica
Quando o protocolo for acionado, o revisor agora deve:
1. abrir `003`, `004`, `011_TOPICOS/000_README`, `012_TRANSVERSAIS/000_README`;
2. abrir os 12 topicos `001-012`;
3. abrir o pacote minimo transversal `002`, `003`, `005`, `006`, `008`;
4. abrir a licao atual, a anterior e a seguinte;
5. preencher a matriz topica;
6. auditar as fronteiras criticas;
7. so depois patchar o HTML;
8. reauditar topicos tocados e vizinhos;
9. fechar os gates finais.

---

## 7) Definition of Done desta consolidacao
Esta task so passa se:
1. o protocolo deixar de depender de leitura por impressao geral;
2. a matriz topica `001-012` virar parte obrigatoria do fluxo;
3. a auditoria de fronteiras ficar canonizada;
4. a rubrica bloquear fechamento sem cobertura topica;
5. o template diario carregar o fluxo novo;
6. os topicos ativos nao tiverem mais lacunas de checklist.

Resultado:
1. esta consolidacao passa.

---

## 8) Riscos residuais
1. o sistema agora esta mais forte documentalmente, mas ainda depende de disciplina real na execucao;
2. a prova final do protocolo continua sendo aplicacao repetida em licoes reais;
3. se uma nova licao revelar ambiguidade recorrente entre topicos adjacentes, o sistema deve ser reaberto antes de a licao virar baseline.

---

## 9) Veredito
O protocolo de ativacao por topicos ficou consideravelmente mais robusto, mais premium e mais dificil de usar de forma frouxa.

Estado atual:
1. melhor para revisao dirigida;
2. melhor para padronizacao;
3. melhor para detectar drift;
4. melhor para sustentar `TASTE` sem perder rigor;
5. melhor para fazer revisao `ponto a ponto` de verdade.
