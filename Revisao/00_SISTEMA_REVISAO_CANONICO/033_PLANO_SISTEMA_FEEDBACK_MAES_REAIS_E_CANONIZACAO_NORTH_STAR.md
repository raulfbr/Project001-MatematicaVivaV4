# PLANO - SISTEMA DE FEEDBACK DE MAES REAIS E CANONIZACAO DO NORTH STAR
Data: 2026-03-12
Status: proposta de arquitetura e governanca
Escopo: organizar captura, leitura, sintese e promocao de feedback real de maes para o sistema de revisao

---

## 1) Decisao central
A melhor decisao e:
1. NAO colocar feedback bruto de maes diretamente dentro de `008_NORTH_STAR_OPERACIONAL.md`;
2. criar uma trilha propria para `feedback de maes reais`;
3. usar essa trilha como camada de evidencia;
4. promover para o `North Star` apenas o que se provar:
   a. transversal;
   b. estavel;
   c. coerente com a identidade de Matematica Viva;
   d. util para varias licoes, e nao apenas para um caso isolado.

Formula curta:
`feedback bruto -> leitura critica -> sintese transversal -> canonizacao seletiva`

---

## 2) Problema que este plano resolve
Hoje existe um risco real de cair em um de dois erros:

### Erro 1 - perder o ouro
1. feedback real de mae aparece em conversa ou log local;
2. ele ajuda uma licao;
3. depois se perde;
4. o sistema nao aprende.

### Erro 2 - canonizar cedo demais
1. um feedback isolado entra no `North Star`;
2. o arquivo fica inchado;
3. principios estaveis se misturam com detalhes taticos;
4. o sistema fica mais confuso, nao mais sabio.

Este plano existe para evitar os dois erros ao mesmo tempo.

---

## 3) Principio de arquitetura
O sistema deve ter 3 camadas.

### Camada A - Evidencia bruta
Onde guardamos o que a mae realmente disse.

Funcao:
1. preservar a voz real;
2. evitar reinterpretacao precoce;
3. manter historico.

### Camada B - Leitura e decisao
Onde analisamos o feedback e decidimos:
1. o que vale para a licao;
2. o que vale para o sistema;
3. o que foi aplicado;
4. o que ficou pendente;
5. o que NAO deve ser promovido.

### Camada C - Canonizacao
Onde sobe apenas o que virou regra duravel.

Funcao:
1. reforcar o `North Star`;
2. reforcar transversais operacionais;
3. evitar que o sistema reaprenda a mesma coisa toda semana.

---

## 4) Melhor estrutura proposta
### 4.1 Pasta nova
Criar:
`Revisao/FEEDBACK_MAES_REAIS/`

Motivo:
1. feedback de maes reais e uma classe propria de evidencia;
2. nao deve ficar espalhado apenas em pastas por data;
3. precisa ser facil de consultar depois.

### 4.2 Estrutura interna recomendada
```text
Revisao/FEEDBACK_MAES_REAIS/
  000_README.md
  001_TEMPLATE_CASO_FEEDBACK_MAE_REAL.md
  002_LISTA_VIVA_CANDIDATOS_NORTH_STAR.md
  CASOS/
    2026/
      2026-03-12_MARINA_MV-S-003.md
  SINTESIS/
    2026-03-XX_SINTESIS_PADROES_FEEDBACK_MAES_REAIS.md
  INDEX_PROMOCAO_CANONICA.md
```

Funcao da `002_LISTA_VIVA_CANDIDATOS_NORTH_STAR.md`:
1. concentrar frases e heuristicas fortes ainda nao canonizadas;
2. evitar que candidatos ao `008` fiquem espalhados em varios casos;
3. permitir confirmacao por recorrencia antes de subida canonica.

Decisao importante:
Nao recomendo criar uma pasta separada `BRUTO/` e outra `DISCUSSAO/` para cada caso neste primeiro momento.

Melhor:
1. um arquivo-dossie por caso;
2. dentro dele, manter:
   a. feedback bruto;
   b. leitura;
   c. decisao;
   d. o que foi aplicado;
   e. o que pode subir de nivel.

Razao:
1. reduz fragmentacao;
2. facilita consulta humana;
3. bate com o que voce pediu: "no final do arquivo, o que realmente fizemos e o que e importante".

---

## 5) Formato recomendado do arquivo de caso
Exemplo:
`Revisao/FEEDBACK_MAES_REAIS/CASOS/2026/2026-03-12_MARINA_MV-S-003.md`

Estrutura recomendada:

```md
# CASO - FEEDBACK MAE REAL
Data:
Mae:
Licao:
Origem:
Status do caso:
Status de promocao atual:

## 1) Feedback bruto
[copiar o texto da mae, sem reescrever]

## 2) Leitura editorial e pedagogica
- o que procede
- o que nao procede
- o que e local
- o que e transversal

## 3) Decisoes
- o que vamos mudar
- o que nao vamos mudar
- o que vamos preservar

## 4) O que foi aplicado
- patch local executado
- arquivo(s) tocado(s)
- data da execucao

## 5) O que este caso ensina ao sistema
- heuristicas novas
- anti-patterns identificados
- frases ou criterios candidatos a canonizacao

## 6) Status de promocao
- fica local
- entra em sintese transversal
- candidato a North Star
- candidato a nova transversal
```

Regra critica:
O bloco `Feedback bruto` deve ser tratado como quase imutavel.

Permitido:
1. corrigir metadados;
2. marcar origem;
3. limpar formacao grotesca de copia, se necessario.

Nao permitido:
1. reescrever o tom da mae;
2. suavizar artificialmente o que ela disse.

---

## 6) Camada de sintese
### Funcao da `SINTESIS/`
Transformar casos isolados em padroes.

Exemplo de saida:
1. `poesia no lugar errado`
2. `mae nao sabe se aquilo e para falar ou para fazer`
3. `perguntas demais ou sem hierarquia geram inseguranca`
4. `blocos de cor ajudam leitura real`
5. `quando comando fica abstrato, a mae perde paz`

### Regra
Nada sobe para o `North Star` sem antes aparecer na camada de sintese.

Motivo:
1. o `North Star` nao deve absorver ruido;
2. ele deve absorver sabedoria confirmada.

---

## 7) Melhor decisao para o `North Star`
### O que o `008_NORTH_STAR_OPERACIONAL.md` deve receber
Apenas principios de alto nivel que se mostraram duraveis.

Exemplos de bons candidatos:
1. `Se a mae precisa traduzir mentalmente o que dizer ou fazer, o bloco esta pesado demais.`
2. `Poesia atmosferica pode respirar; linguagem operacional deve ser clara.`
3. `Feedback real de maes deve entrar como dado qualificado, nao como ordem automatica.`
4. `Se a narrativa e a instrucao parecem linguagens concorrentes, a licao afasta do North Star.`
5. `A mae deve sair mais aliviada, nao mais insegura.`

### O que o `008` NAO deve receber
1. comentarios circunstanciais de uma licao so;
2. exemplos muito locais;
3. historico de conversa;
4. listas grandes de casos;
5. discussao editorial detalhada de uma unica mae.

---

## 8) Melhor decisao adicional: criar uma nova transversal
Eu recomendo criar depois:
`Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/009_EMPATIA_OPERACIONAL_E_TESTE_DA_MAE_REAL.md`

Funcao desse novo arquivo:
1. ser a ponte entre feedback real e sistema canonico;
2. carregar heuristicas mais operacionais do que o `008`;
3. preservar testes concretos de empatia sem poluir o `North Star`.

### Papel do `008`
Constituicao.

### Papel do futuro `009`
Jurisprudencia operacional.

Essa e a melhor separacao.

---

## 9) Regras de promocao canonica
### Nivel 1 - Local
Fica apenas no caso quando:
1. e especifico daquela licao;
2. nao reaparece em outros casos;
3. nao altera o sistema.

### Nivel 2 - Sintese transversal
Sobe para `SINTESIS/` quando:
1. o caso revela um padrao repetivel;
2. o aprendizado serve para mais de uma licao;
3. ainda nao esta maduro para virar `CANDIDATO A TRANSVERSAL`.

### Nivel 3 - Transversal operacional
Sobe para o futuro `009_EMPATIA_OPERACIONAL_E_TESTE_DA_MAE_REAL.md` quando:
1. o padrao ja se repetiu ou ficou muito claro;
2. ele gera heuristica de revisao acionavel;
3. ele melhora a pratica da IA e do humano.

### Nivel 4 - North Star
Sobe para o `008` apenas quando:
1. o padrao e claramente duravel;
2. ele toca identidade, tom ou criterio espiritual da obra;
3. ele vale como principio, nao so como tecnica;
4. se nao entrar, o sistema corre risco de voltar a ferir a mae real.

---

## 10) Teste de promocao para o `North Star`
Antes de subir qualquer coisa ao `008`, responder:

1. Isto vale para muitas licoes ou so para uma?
2. Isto e principio ou so boa tecnica?
3. Isto protege a mae de um erro recorrente do sistema?
4. Isto reforca a identidade de Matematica Viva?
5. Isto continuaria verdadeiro daqui a 6 meses?

Se a resposta for `nao` em 2 ou mais pontos:
1. nao sobe para o `008`;
2. fica na sintese ou na transversal operacional.

---

## 11) O que este sistema deve capturar melhor
Os feedbacks de maes reais devem nos ajudar a detectar:
1. onde a mae precisa traduzir;
2. onde a mae nao sabe se aquilo e fala, gesto ou instrucao;
3. onde as perguntas geram inseguranca;
4. onde a pagina esta bonita, mas pouco usavel;
5. onde a pagina esta clara, mas generica demais;
6. onde a atmosfera sustenta a licao;
7. onde o Reino realmente ajuda;
8. onde os blocos de cor aliviam a leitura;
9. onde a pedagogia esta certa, mas a experiencia esta errada;
10. onde a obra consola o adulto de verdade.

---

## 12) Melhor forma de usar a voz da mae sem distorcer o sistema
Regra de ouro:
Feedback real de mae nao e soberano sozinho, mas tambem nao e detalhe.

Leitura correta:
1. a mae mostra friccao real;
2. o sistema interpreta a friccao;
3. o patch resolve localmente;
4. a sintese decide se isso ensina algo ao sistema inteiro.

Assim:
1. nao viramos refens de feedback isolado;
2. nao ignoramos o dado mais precioso do projeto.

---

## 13) Fases recomendadas de execucao
### Fase 1 - Estrutura
1. criar `Revisao/FEEDBACK_MAES_REAIS/`;
2. criar `000_README.md`;
3. criar `001_TEMPLATE_CASO_FEEDBACK_MAE_REAL.md`;
4. criar `002_LISTA_VIVA_CANDIDATOS_NORTH_STAR.md`;
5. criar `INDEX_PROMOCAO_CANONICA.md`.

### Fase 2 - Caso piloto
1. migrar o caso `Marina x L003` para o novo formato;
2. tratar esse caso como piloto do sistema.

### Fase 3 - Sintese
1. abrir a primeira sintese transversal com os aprendizados de `L003`;
2. separar:
   a. local;
   b. transversal;
   c. candidato a sistema.

### Fase 4 - Ponte canonica
1. criar a nova transversal `009_EMPATIA_OPERACIONAL_E_TESTE_DA_MAE_REAL.md`;
2. subir para la os aprendizados operacionais confirmados.

### Fase 5 - North Star
1. revisar o `008`;
2. inserir so os principios realmente duraveis.

---

## 14) Melhor decisao sobre o que fazer AGORA
Se quisermos fazer da melhor forma, a ordem correta e:

1. aprovar esta arquitetura;
2. criar a pasta e os templates;
3. migrar o caso Marina/L003 como piloto;
4. so depois editar o `008`.

Motivo:
Editar o `North Star` antes de termos o sistema de evidencia organizado e pular etapa.

---

## 15) Recommendation final
Sim, faz MUITO sentido usar feedback real de maes para tornar o sistema mais empatico.

Mas a melhor forma de fazer isso e:
1. `feedback bruto` em trilha propria;
2. `leitura e decisao` em dossie de caso;
3. `padroes` em sintese transversal;
4. `principios duraveis` no `North Star`.

Formula final:
`a mae real nao entra no sistema como ruido; ela entra como evidencia`

Essa e a arquitetura mais criteriosa, mais segura e mais fiel ao que o projeto quer ser.
