# TASK ROBUSTA - REVISAO DO MANUAL DO PORTADOR E AUDITORIA FINAL
Data: 2026-03-10
Status: concluida por IA / validacao humana pendente
Escopo: revisar licoes `001` e `002`, revisar o `Manual do Portador` no novo contexto e fechar a rodada com auditoria e publicacao

---

## 1) Objetivo desta task
Entregar uma rodada final consistente em cinco frentes:
1. revisar o que foi feito no protocolo e nas licoes `001` e `002`;
2. repensar a abertura do `Manual do Portador` para reduzir friccao e levar a familia direto para a `Licao 000`;
3. atualizar o manual para refletir o metodo real de hoje, incluindo `mobile-first`, impressao opcional e anatomia real da licao;
4. revisar tudo outra vez para remover drift documental e textual;
5. commitar e publicar no GitHub para acionar o Vercel.

---

## 2) Perguntas norteadoras desta rodada
1. a familia consegue sair do manual e entrar na `Licao 000` em poucos minutos, sem ler o documento inteiro?
2. o manual explica o metodo real, ou ainda descreve uma versao antiga da licao?
3. `MV-S-001` e `MV-S-002` continuam alinhadas ao protocolo depois da ultima passada?
4. o sistema documental ficou sem contradicoes internas?
5. a publicacao vai levar apenas o que foi realmente validado nesta rodada?

---

## 3) Decisoes de arquitetura desta rodada
1. o protocolo de revisao continua centralizado em `023`.
2. a auditoria vigente de `L001` e `L002` continua em `025`.
3. para esta release, o artefato publicado do manual e `site/manual-portador.html`.
4. `curriculo/01_SEMENTESV6/_Manuais/MANUAL_PORTADOR_TOCHA.md` permanece como referencia historica de conteudo, mas nao sera tratado como artefato publicado nesta rodada para evitar duplicacao de manutencao sem pipeline.

---

## 4) Focos obrigatorios do Manual do Portador
1. a abertura precisa levar a familia para a `Licao 000` com paz e clareza;
2. o celular deve ser apresentado como caminho padrao de uso;
3. a impressao deve aparecer como opcionalidade real, com orientacao honesta sobre `2 colunas` versus `normal`;
4. a parte profunda do manual deve continuar existindo, mas sem bloquear a primeira experiencia;
5. a anatomia da licao precisa refletir o fluxo real atual, incluindo `O Concreto`, `Narramos Juntos`, `Sementes para o Dia` e `Formacao do Portador`;
6. o manual precisa ajudar o Portador a se acostumar com o metodo, nao apenas entendelo em tese.

---

## 5) Focos obrigatorios de auditoria
### `MV-S-001`
1. confirmar `PASS` de `006`, `007`, `010` e `011`;
2. revisar coerencia final de narrativa, iconografia e escaneabilidade.

### `MV-S-002`
1. confirmar `PASS` da fronteira `005 -> 006`;
2. revisar coerencia final de multi-crianca, preparacao e formacao do Portador.

### Sistema
1. remover contradicoes em `005_STATUS_REVISAO_SEMENTES.md`;
2. manter `023`, `003`, `004` e `010` coerentes com a fase atual.

---

## 6) Artefatos desta rodada
1. `026_TASK_ROBUSTA_REVISAO_MANUAL_PORTADOR_E_AUDITORIA_FINAL.md`
2. `027_DISCUSSAO_MUDANCA_E_MELHORIA_MANUAL_PORTADOR_L000_MOBILE.md`
3. `028_AUDITORIA_FINAL_GERAL_PROTOCOLO_MANUAL_L001_L002.md`
4. `site/manual-portador.html`
5. `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html`
6. `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`

---

## 7) Criterio de saida
1. manual com abertura mais leve, mais clara e mais alinhada ao uso real;
2. anatomia do metodo explicada sem descrever estruturas antigas;
3. `L001` e `L002` revalidadas;
4. status e auditorias sem contradicao interna;
5. commit detalhado e push concluido.
