# Topicos da Revisao

Esta pasta contem um arquivo por secao da licao canonica.

Este diretorio define o contrato canonico-alvo da revisao premium.
Ele nao prova, por si so, que o HTML legado ja cumpra tudo.

Use a pasta assim:
1. leia `003_PROTOCOLO_REVISAO_POR_LICAO.md` e `004_RUBRICA_PREMIUM_REVISAO.md`;
2. leia os topicos `001-012` na ordem oficial, sem pular os "obvios";
3. confira o HTML real da licao;
4. registre `PASS`, `GAP` ou `BLOCK` por topico;
5. audite as fronteiras criticas entre topicos adjacentes;
6. trate divergencia entre topico e HTML como finding de revisao;
7. so patchar HTML depois de a matriz topica inteira estar preenchida.

Cada arquivo deve cobrir:
1. contrato tecnico;
2. contrato narrativo;
3. contrato pedagogico;
4. anti-patterns;
5. PASS estrutural;
6. BLOCK estrutural;
7. ambiguidades resolvidas;
8. checklist de revisao;
9. prompt operacional para IA.

## Modo de ativacao do protocolo por topicos
1. abrir os 12 topicos oficiais;
2. preencher a matriz `001-012` com `PASS / GAP / BLOCK`;
3. conferir, no minimo, estas fronteiras:
   a. `003 -> 004`;
   b. `004 -> 005`;
   c. `005 -> 006`;
   d. `006 -> 007`;
   e. `008 -> 009`;
   f. `009 -> 010`;
   g. `010 -> 011`;
   h. `011 -> 012`;
4. consultar o pacote minimo transversal: `002`, `003`, `005`, `006`, `008`;
5. reauditar os topicos tocados e seus vizinhos imediatos depois do patch;
6. so chamar uma licao de alinhada quando os 12 topicos e as fronteiras criticas tiverem passado.

Ordem oficial:
1. `001_BASE_E_HERO.md`
2. `002_HEADER_SUPERIOR.md`
3. `003_PREPARACAO_DO_PORTADOR.md`
4. `004_RITUAL_DE_ENTRADA.md`
5. `005_A_JORNADA.md`
6. `006_O_CONCRETO.md`
7. `007_NARRAMOS_JUNTOS.md`
8. `008_RITUAL_DE_FECHAMENTO.md`
9. `009_CONEXAO_DA_JORNADA.md`
10. `010_SEMENTES_PARA_O_DIA.md`
11. `011_FORMACAO_DO_PORTADOR.md`
12. `012_NAVEGACAO_INFERIOR.md`

Auditoria inicial ja registrada:
1. `013_AUDITORIA_LICOES_001_003.md`
2. `014_DELIBERACAO_MODELO_001_003.md`

Observacao:
1. o naming oficial da pasta agora segue `001..012`;
2. referencias antigas `00..09` devem ser tratadas como legado e ajustadas quando encontradas em tasks e templates;
3. as licoes `001-003` ainda misturam contrato premium e estruturas legadas; consulte a auditoria antes de assumir que todo topico ja esta refletido no HTML.
4. quando houver duvida de arquitetura entre secoes adjacentes, consulte a deliberacao `014` antes de editar HTML familiar.
5. na subfase atual, a passada mais critica com foco em `TASTE` comeca em `006` e segue ate `012`;
6. `MV-S-001` ainda nao deve ser lida como baseline total enquanto essa passada nao estiver consolidada.
7. o protocolo premium agora exige matriz topica completa; `topicos relevantes` so vale para transversais, nao para os 12 topicos da licao.
