# EXECUCAO - TEXT WRAP DE ICONES EM INSTRUCTION BOXES - L003
Data: 2026-03-12
Status: implementado de forma incremental
Escopo: introduzir o modificador opt-in `instruction-box--wrap` no design system e aplica-lo nas caixas densas da `L003`

---

## 1) Decisao arquitetural
1. manter `.instruction-box` legado em `display: flex`;
2. criar `.instruction-box--wrap` como modificador opt-in;
3. aplicar o wrap apenas nas caixas longas ou com listas;
4. preservar caixas curtas no layout antigo para evitar regressao visual desnecessaria.

---

## 2) O que entrou no CSS global
Arquivo: `site/sementes/style.css`

1. `.instruction-box--wrap { display: block; overflow: hidden; }`
2. `float: left` no primeiro icone da caixa;
3. blindagem com `!important` para `font-size` e margens do icone;
4. tratamento de `ol` e `ul` com `list-style-position: inside`;
5. reset de padding em `li` para proteger o mobile.

---

## 3) Caixas da L003 que receberam o modificador
Arquivo: `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html`

1. `prep-heart-box`
2. `ritual-whisper-box`
3. todas as `journey-instruction-box`
4. objetivo de `O Concreto`
5. atividade principal de `O Concreto`
6. variacoes de `O Concreto`
7. `bridge-highlight-box`
8. postura de escuta em `Narramos Juntos`
9. perguntas de reconto em `Narramos Juntos`
10. `Conexao da Jornada`
11. `formation-intro-box`

---

## 4) Caixas preservadas em flex
1. `ritual-bastidores-box`
2. `Como conduzir agora`
3. `daily-seeds-box`

Motivo:
1. sao blocos curtos ou com outra estrutura interna;
2. nao precisavam do wrap para ganhar legibilidade;
3. isso reduz risco de alterar intencoes visuais compactas.

---

## 5) Limpeza de inline styles
1. removidos os `style="font-size:1.5rem; margin-right:0.5rem;"` apenas dos icones das caixas migradas;
2. caixas nao migradas permanecem intactas.

---

## 6) Sanity checks
1. componente base legado preservado;
2. listas dentro de caixas com wrap agora passam pelo guardrail do modificador;
3. o modificador nao foi aplicado a caixas sem icone estrutural de abertura.

---

## 7) Proximo passo recomendado
1. validacao visual no navegador, com foco mobile;
2. se a leitura ficar claramente melhor, repetir o padrao em `L001` e `L002` apenas onde houver densidade parecida.
