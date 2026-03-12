# Conversa Guiada — Entendimento do Projeto, Revisão TASTE e Comparação com PRD-LOVABLE
Data: 2026-03-08
Escopo: entendimento real do projeto + estado da revisao + MV-S-002 + comparacao com `logs/2026-03-08-PRD-LOVABLE`
Origem desta conversa:
1. leitura do `README.md` da raiz;
2. leitura do sistema canonico em `Revisao/`;
3. leitura de `logs/2026-03-07-09h46-revisao002.md`;
4. leitura da `MV-S-002` real em `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`;
5. leitura do canon em `LORE/`;
6. leitura de `logs/2026-03-08-PRD-LOVABLE`.

---

## Raul
Quero entender o projeto de verdade. O que ele e hoje?

## Codex
Hoje, `Matematica Viva` nao e principalmente um app.

Hoje ele e, antes de tudo, uma obra editorial, pedagogica e narrativa para familias.
O software existe para servir essa obra.

Na pratica, o coracao atual do projeto esta em quatro camadas:
1. `LORE/` = canon narrativo, tom, guardioes, North Star, Rei e Reino.
2. `curriculo/` = materia-prima curricular e mapa mestre das licoes.
3. `site/sementes/*.html` = experiencia real que a familia le e usa.
4. `Revisao/` = sistema de governanca que esta fechando o padrao premium dessa experiencia.

Em resumo:
1. o produto que vale hoje esta no HTML real;
2. o resto do repositorio serve para sustentar, revisar ou preparar a evolucao disso.

---

## Raul
Entao o projeto nao e o `apps/web`?

## Codex
Nao como frente principal desta fase.

O proprio documento canonico `015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md` fixa isso:
1. a frente ativa e `HTML-first`;
2. `apps/web` e piloto tecnico contrato-first;
3. ele prova infraestrutura, nao a experiencia premium final da familia.

Traduzindo:
1. `apps/web` importa;
2. mas ele ainda nao dita a sessao;
3. quem dita a sessao agora e o HTML revisado em `site/sementes`.

---

## Raul
Entao qual e a diferenca entre o projeto real e o `PRD-LOVABLE`?

## Codex
O `PRD-LOVABLE` e util como fotografia de uma ambicao anterior de produto.
Mas ele nao descreve com precisao a governanca ativa de hoje.

As diferencas mais importantes sao estas:

1. Centro do produto
- `PRD-LOVABLE`: o centro parece ser um produto React/Vite/Tailwind com licoes jogaveis.
- Projeto real hoje: o centro operacional e o HTML revisado, com `Revisao/` governando a qualidade.

2. Stack principal
- `PRD-LOVABLE`: React 18 + TypeScript + Vite + Tailwind + Framer Motion + Shadcn.
- Projeto real hoje: coexistencia de frentes.
  - frente ativa: HTML estatico em `site/sementes`;
  - frente tecnica paralela: `apps/web` em Next/TypeScript, ainda piloto.

3. Estado das licoes
- `PRD-LOVABLE`: fala em 6 licoes jogaveis `000-005`.
- Projeto real hoje: o acervo HTML vai alem disso, mas as licoes iniciais `000-025` estao em preservacao manual e as `001-003` seguem em calibracao premium.

4. Estrutura da licao
- `PRD-LOVABLE`: liturgia de 8 fases, incluindo `O Caos` e `Momento de Conexao`.
- Projeto real hoje: o contrato canonico da licao tem 13 blocos, com `O Concreto`, `Narramos Juntos`, `Conexao da Jornada`, `Sementes para o Dia` e `Formacao do Portador` como estrutura oficial da fase.

5. Papel da revisao
- `PRD-LOVABLE`: fala mais como PRD de produto.
- Projeto real hoje: a pasta `Revisao/` virou sistema de governanca editorial e pedagogica.

6. Gargalo principal
- `PRD-LOVABLE`: o gargalo parece plataforma e completude de produto.
- Projeto real hoje: o gargalo e `TASTE`.
  - unidade de imagem;
  - leveza para o Portador;
  - fim de metaforas soltas;
  - realidade de uso familiar;
  - texto que soe vivo e recognoscivel como `Matematica Viva`.

7. Exemplo concreto da divergencia
- `PRD-LOVABLE`: a `MV-S-002` e quase uma licao de ten frame com 10 objetos.
- Projeto real hoje: a `MV-S-002` revisada trabalha 5 pedras em fileira para tornar quantidade visivel pela ordem.

Conclusao curta:
o `PRD-LOVABLE` mostra uma fase importante da visao de produto.
Mas o SSOT de hoje nao esta nele.
O SSOT de hoje esta distribuido entre `Revisao/`, `LORE/`, `curriculo/` e o HTML real.

---

## Raul
E qual e a alma do projeto, se eu tiver que explicar para alguem em poucas linhas?

## Codex
Eu explicaria assim:

`Matematica Viva` e um curriculo narrativo para familias em que a matematica aparece como algo vivo, concreto e belo.
O pai ou a mae nao entrega uma aula fria; conduz uma pequena jornada domestica.
A crianca nao recebe conteudo para repetir; ela ouve, toca, conta e reencontra.
O objetivo nao e apenas ensinar conta.
E formar cultura de lar, memoria afetiva e sentido matematico ao mesmo tempo.

---

## Raul
E onde entra o tal `TASTE`? Porque ele virou tao central?

## Codex
Porque a estrutura ja esta suficientemente madura para mostrar outro tipo de problema.

Hoje o sistema ja sabe detectar:
1. secao faltando;
2. nome de bloco errado;
3. link quebrado;
4. guardiao aparecendo cedo;
5. atividade concreta fraca.

So que isso nao basta para fazer a licao soar premium.

`TASTE` e o que decide entre:
1. um texto correto;
2. e um texto inevitavel, leve, vivo e recognoscivel como `Matematica Viva`.

Na pratica, `TASTE` aparece quando:
1. a imagem dominante da licao se mantem inteira;
2. a voz do guardiao nao vira caricatura;
3. a mae consegue ler e conduzir ao mesmo tempo;
4. a secao nao parece bloco tecnico colado;
5. a familia sente calor, nao sobrecarga.

---

## Raul
Me explica a `MV-S-002` como se eu fosse aprender com ela o metodo.

## Codex
A `MV-S-002` ensina uma verdade simples e profunda:

`quantidade fica mais visivel quando encontra ordem`

Mas o jeito de ensinar isso importa mais do que a frase.

O arco da licao e:
1. ontem, a contagem coube na palma com Celeste;
2. hoje, Bernardo pega essa mesma quantidade e a coloca em fileira;
3. a crianca percebe que ordem nao e bronca nem controle;
4. ordem e uma forma de o olho descansar e ver melhor;
5. amanha, essa ordem vai poder ganhar moldura e forma com Iris.

O aprendizado metodologico mais forte da `L002` e este:
1. `A Jornada` dramatiza por que a ordem ajuda a ver;
2. `O Concreto` da a crianca uma autoria manual nova;
3. `Narramos Juntos` recolhe o que ela viveu, sem interrogatorio;
4. `Formacao do Portador` explica por que isso funciona sem virar aula universitaria.

Se uma dessas quatro partes colapsa na outra, a licao fica correta por fora e fraca por dentro.

---

## Raul
E onde a `MV-S-002` estava fraca? E onde ela esta melhor agora?

## Codex
O log de `2026-03-07-09h46` mostrava varios problemas estruturais e editoriais.
Boa parte deles ja foi corrigida antes desta conversa.

O que ja melhorou de forma objetiva:
1. `Atividade Concreta` virou `O Concreto`;
2. entrou objetivo, ligacao com a Jornada, adaptacao, sinal de fruto e ponte para `Narramos Juntos`;
3. saiu o `div onclick` e entrou link semantico na `Conexao da Jornada`;
4. entrou `Estrategia do Mestre` na abertura da `Formacao do Portador`;
5. o tom de Bernardo ficou mais firme e manso;
6. a licao ficou mais aplicavel para mais de uma crianca;
7. o retorno ao cotidiano no fechamento ficou mais claro;
8. a `L002` agora conversa melhor com `L001` e prepara `L003` com mais elegancia.

O que eu refinei nesta passada:
1. deixei o hero menos explicativo e mais vivo;
2. troquei a pergunta de entrada da Jornada para um convite mais natural;
3. alinhei `Narramos Juntos` ao icone canonico de escuta/conversa;
4. deixei a `Formacao do Portador` explicitar `Conexao TGTB`;
5. alinhei pequenos detalhes de acessibilidade e consistencia.

O que ainda nao chamaria de veredito final:
1. a `L002` ja se aproxima de `PASS ESTRUTURAL`;
2. mas o `PASS PREMIUM` ainda pede releitura do todo com calma, incluindo confronto com uso humano real.

---

## Raul
O feedback real de familia muda o projeto?

## Codex
Sim, mas nao governa sozinho.

O principio que o sistema fixou esta certo:
`feedback real e dado valioso, nao ordem de mudanca`

No caso da Familia Isa, o feedback ensinou coisas muito concretas:
1. escaneabilidade no celular importa de verdade;
2. a mae precisa de mais paz para conduzir;
3. familias com mais de uma crianca precisam de adaptacoes leves;
4. certas imagens narrativas lindas no papel precisam de ancora melhor para o adulto;
5. a frase-assinatura de Bernardo nao devia ser trocada, mas o tom precisava ser melhor guiado.

Isso afeta `TASTE` porque ajuda a separar:
1. o que a IA acha bonito;
2. do que a familia realmente consegue usar sem perder o fio.

---

## Raul
Se eu quiser explicar o momento do projeto para mim mesmo sem me confundir, como eu digo?

## Codex
Voce pode dizer assim:

`Estamos fechando o sistema de revisao premium do HTML real.`

Mais detalhado:
1. o projeto tem uma frente tecnica futura;
2. mas a frente ativa hoje e editorial e HTML-first;
3. a `MV-S-001` ensinou muito, mas ainda nao e baseline total;
4. a tarefa da fase e fechar a camada de topicos e transversais com foco em `TASTE`;
5. a `MV-S-002` entrou como licao-laboratorio para mostrar o que o sistema ainda nao enxerga sozinho;
6. o ganho de curto prazo nao esta em novo harness nem em mais pipeline;
7. esta em fazer a licao soar mais una, mais leve, mais real e mais `Matematica Viva`.

---

## Raul
Entao o que voce conclui, em uma frase?

## Codex
O projeto real hoje e menos um app em busca de features e mais uma obra viva em fase de fechamento editorial, onde `Revisao/` governa o HTML real e `TASTE` virou o principal diferencial de produto.

---

## Proximo passo seguro
1. reler a `MV-S-002` inteira como experiencia unica com `T00-T13`;
2. decidir se ela ja sobe para `PASS ESTRUTURAL` ou se ainda fica `EM REFINAMENTO`;
3. devolver para `L001` e para o sistema qualquer aprendizado de `TASTE` que tenha aparecido mais nitido aqui;
4. so depois abrir o mesmo criterio para `L003` ou lote `001-003`.
