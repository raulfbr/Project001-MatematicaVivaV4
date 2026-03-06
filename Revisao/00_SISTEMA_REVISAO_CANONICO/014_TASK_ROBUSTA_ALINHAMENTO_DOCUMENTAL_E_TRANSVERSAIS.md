# TASK ROBUSTA - ALINHAMENTO DOCUMENTAL E ENDURECIMENTO DAS TRANSVERSAIS
Data: 2026-03-06
Escopo: sistema canonico de revisao, sem editar licoes HTML
Prioridade: alta
Status: executada nesta sessao

---

## 1) Missao desta task
1. eliminar drift entre os topicos canonicos reais e os documentos operacionais que vao governar o piloto;
2. endurecer as transversais mais fracas para que os topicos novos tenham sustentacao suficiente;
3. preparar o sistema para validacao humana antes de qualquer dry-run do piloto `001-003`.

---

## 2) Problema que esta task resolve
Antes desta rodada, havia dois tipos de incoerencia:

1. drift de naming:
   a. os arquivos reais em `011_TOPICOS/` estavam em `001..012`;
   b. tasks, templates e readmes ainda falavam em `00..09` em varios pontos.
2. drift de contrato:
   a. os topicos novos passaram a usar `PASS estrutural`, `BLOCK estrutural` e `ambiguidades resolvidas`;
   b. parte da documentacao adjacente ainda descrevia a pasta como se ela tivesse apenas checklist simples.

Consequencia:
1. risco alto de a proxima sessao abrir documentos certos, mas aplicar nomes errados;
2. risco de o piloto nascer com planilhas/templates desalinhados do sistema real;
3. risco de os topicos ficarem mais fortes que as transversais que deveriam sustentá-los.

---

## 3) Escopo executado

### 3.1 Alinhamento documental
Arquivos ajustados:
1. `011_TOPICOS/000_README.md`
2. `001_TASK_ROBUSTA_SISTEMA_REVISAO_HTML_FIRST.md`
3. `007_TASK_ROBUSTA_PILOTO_001_003.md`
4. `008_TEMPLATE_RELATORIO_PILOTO_001_003.md`

Correcoes feitas:
1. naming dos topicos alinhado para `001_BASE_E_HERO` ate `012_NAVEGACAO_INFERIOR`;
2. contrato da pasta atualizado para refletir:
   a. `PASS estrutural`;
   b. `BLOCK estrutural`;
   c. `ambiguidades resolvidas`;
   d. prompts operacionais;
3. task do sistema atualizada para parar de referenciar nomes legados inexistentes;
4. task e template do piloto atualizados para medir cobertura usando o naming real.

### 3.2 Endurecimento de transversais prioritarias
Arquivos alvo:
1. `012_TRANSVERSAIS/001_ICONES_CORES_E_ASSETS.md`
2. `012_TRANSVERSAIS/003_TOM_NARRATIVO_E_DIRECAO_DO_PORTADOR.md`

Objetivo:
1. sair do nivel de resumo curto;
2. aproximar o valor dessas transversais do papel real que elas exercem nos topicos.

---

## 4) Criterio de saida desta task
Esta task so e considerada bem sucedida se:
1. nao houver mais conflito operacional entre naming dos topicos e templates do piloto;
2. a pasta `011_TOPICOS/` puder ser lida sem contradicao interna;
3. as transversais reforcadas passarem a responder melhor:
   a. que regra vale;
   b. o que aprova;
   c. o que reprova;
   d. onde o legado ainda exige cuidado.

---

## 5) Nao-escopo mantido
1. nenhuma licao HTML foi editada;
2. nenhum piloto foi executado;
3. nenhuma revisao qualitativa completa pelas 7 lentes foi iniciada ainda.

---

## 6) Proximo gate
1. validar humanamente esta rodada;
2. se aprovada, escolher entre:
   a. aprofundar mais transversais restantes;
   b. ou iniciar dry-run documental do piloto `001-003`.
