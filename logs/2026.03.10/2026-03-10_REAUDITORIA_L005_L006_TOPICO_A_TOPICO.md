# REAUDITORIA L005-L006 TOPICO A TOPICO
Data: 2026-03-10
Escopo: `MV-S-005_O_ESCONDERIJO_DA_GLÓRIA.html` e `MV-S-006_O_DESENHO_DO_REI.html`
Metodo: `023` + `003` + `011_TOPICOS/001-012` + pacote transversal minimo + conselho `experts`

---

## 1) Diagnostico inicial
Estado encontrado antes do patch:
1. `L005` e `L006` estavam em colagem hibrida entre contrato antigo e naming novo.
2. Havia markup legado, estrutura inconsistente e fechamento quebrado da cauda da pagina.
3. `Sementes para o Dia` e `Formacao do Portador` estavam mutiladas.
4. A relacao `Jornada -> O Concreto` ainda estava fraca e proxima de repeticao.

Decisao da sessao:
1. reescrever as duas licoes por inteiro no contrato canonico atual;
2. preservar apenas o cerne vivo de cada licao;
3. fechar `T01-T12` de cada arquivo na mesma passada.

---

## 2) Cerne macro
### L005
1. Promessa da licao: perceber onde um pequeno tesouro descansa em relacao a outra coisa.
2. Guardiao: `Celeste`.
3. Lugar: `Clareira das Perguntas`.
4. Conceito vivo: posicoes espaciais iniciais `em cima`, `embaixo`, `atras`, `na frente`.
5. Imagem dominante: tesouro escondido e lugar de repouso.
6. Fruto do dia: a crianca mostra ou nomeia ao menos um lugar com sentido real.

### L006
1. Promessa da licao: perceber que os numerais de `1-5` possuem forma propria e caminho reconhecivel.
2. Guardiao: `Iris`.
3. Lugar: `Ninho Mirante`.
4. Conceito vivo: forma dos numerais antes da escrita formal.
5. Imagem dominante: galeria de numeros e caminho percorrido pelo dedo.
6. Fruto do dia: a crianca reconhece ou percorre com o dedo ao menos um numeral com sentido.

---

## 3) Matriz topica final
### L005
1. `001_BASE_E_HERO` -> PASS
2. `002_HEADER_SUPERIOR` -> PASS
3. `003_PREPARACAO_DO_PORTADOR` -> PASS
4. `004_RITUAL_DE_ENTRADA` -> PASS
5. `005_A_JORNADA` -> PASS
6. `006_O_CONCRETO` -> PASS
7. `007_NARRAMOS_JUNTOS` -> PASS
8. `008_RITUAL_DE_FECHAMENTO` -> PASS
9. `009_CONEXAO_DA_JORNADA` -> PASS
10. `010_SEMENTES_PARA_O_DIA` -> PASS
11. `011_FORMACAO_DO_PORTADOR` -> PASS
12. `012_NAVEGACAO_INFERIOR` -> PASS

### L006
1. `001_BASE_E_HERO` -> PASS
2. `002_HEADER_SUPERIOR` -> PASS
3. `003_PREPARACAO_DO_PORTADOR` -> PASS
4. `004_RITUAL_DE_ENTRADA` -> PASS
5. `005_A_JORNADA` -> PASS
6. `006_O_CONCRETO` -> PASS
7. `007_NARRAMOS_JUNTOS` -> PASS
8. `008_RITUAL_DE_FECHAMENTO` -> PASS
9. `009_CONEXAO_DA_JORNADA` -> PASS
10. `010_SEMENTES_PARA_O_DIA` -> PASS
11. `011_FORMACAO_DO_PORTADOR` -> PASS
12. `012_NAVEGACAO_INFERIOR` -> PASS

---

## 4) Fronteiras criticas
### L005
1. `003 -> 004` -> PASS: preparacao orienta sem gastar o portal.
2. `004 -> 005` -> PASS: ritual revela local; Celeste entra formalmente na Jornada.
3. `005 -> 006` -> PASS: Jornada prepara a busca; O Concreto muda para autoria dos lugares.
4. `006 -> 007` -> PASS: o ultimo lugar escolhido abre o reconto.
5. `008 -> 009` -> PASS
6. `009 -> 010` -> PASS
7. `010 -> 011` -> PASS
8. `011 -> 012` -> PASS

### L006
1. `003 -> 004` -> PASS
2. `004 -> 005` -> PASS: local neutralizado para nao carregar o nome da guardia.
3. `005 -> 006` -> PASS: Jornada contempla e introduz; O Concreto vira percurso tatil e corporal.
4. `006 -> 007` -> PASS
5. `008 -> 009` -> PASS
6. `009 -> 010` -> PASS
7. `010 -> 011` -> PASS
8. `011 -> 012` -> PASS

---

## 5) Conselho experts
### Charlotte Mason
1. PASS: licoes curtas, dignidade preservada, narracao presente e concreto dominante.

### Jerome Bruner
1. PASS: `Jornada` e `O Concreto` deixaram de repetir o mesmo gesto central.
2. PASS: concreto veio antes de qualquer formalizacao abstrata.

### Susan Macaulay
1. PASS: materiais simples, aplicacao domestica realista, linguagem usavel em casa.

### Mae Ansiosa
1. PASS: fruto do dia ficou mais claro e menos culpabilizante.

### Mae Veterana
1. PASS: promessas mais honestas, sem performance impossivel no primeiro mes.

### Beatrix Potter + Design
1. PASS: estrutura voltou ao padrao premium, com respiro e atmosfera coerente.

### Engenharia
1. PASS: sem `div onclick`, sem labels legados e sem markup claramente inferior ao contrato novo.

---

## 6) Sanity check
Checagens executadas:
1. busca por anti-patterns legados principais -> limpa em `L005-L006`;
2. parser HTML simples -> `OK` nas duas paginas;
3. checagem de referencias adjacentes -> `OK`;
4. checagem de `Sementes para o Dia` com `5 movimentos` -> `OK`.

---

## 7) Veredito
1. `L005` -> alinhada ao protocolo atual e pronta para reauditoria visual futura.
2. `L006` -> alinhada ao protocolo atual e pronta para reauditoria visual futura.

As duas licoes sairam do estado quebrado e hoje so ficam com risco residual de:
1. validacao visual em navegador ainda nao executada nesta sessao;
2. continuidade externa com `L007`, que ainda permanece em contrato legado.
