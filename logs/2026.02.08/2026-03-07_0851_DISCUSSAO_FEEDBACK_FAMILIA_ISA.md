# DISCUSSÃO: Feedback Real — Família Isa (3 filhos: José, Daniel, João)
Data: 2026-03-07 | 08h51
Tema: Primeiras impressões das Lições 000 e 001 por família pioneira ativa

---

## 0) Missão desta discussão

Este documento existe para:
1. registrar fielmente o feedback recebido;
2. analisar cada ponto com critério e voz dos experts;
3. decidir o que incorporar, o que não incorporar e por quê;
4. não confundir satisfazer feedback com melhorar o produto.

Regra de ouro: o feedback é dados valiosos, não ordens de mudança.

---

## 1) Contexto da família

- Mãe: Isa
- Filhos: José (mais novo, muito envolvido), Daniel e João (mais velhos, mais críticos)
- Perfil materno: parece um híbrido de `Débora (A Iniciante)` + `Júlia (A Relacional)` — aplicou com boa-vontade mas ficou com dúvidas sobre se fez certo, e se preocupou com o vínculo entre os filhos e o material.
- Material usado: L000 (03/03/2026) e L001 (05/03/2026)

---

## 2) Feedback bruto organizado por tema

### 2.1 Reação das crianças — L000
- José (menor): olhinhos brilhavam, queria segurar os personagens, entrou no clima.
- Daniel: envolvido, fazia perguntas, queria adivinhar o que aconteceria.
- João: medio indiferente, mas disse que gostou.

### 2.2 Reação das crianças — L001
- José: empolgado, falava baixinho, queria guardar segredo, tinha cuidado com as sementes.
- Daniel e João: acharam a história muito rápida e simples. Não entenderam quais eram as promessas do Rei.

### 2.3 Feedback da mãe — L000
1. Gostou do ambiente informal e lúdico.
2. Difícil aplicar olhando no celular — preferiria impresso ou em livro.
3. O momento de introdução de novos personagens poderia ser mais indicado.
4. Sugestão de ordem: falar o texto primeiro, depois mostrar a figura (não o contrário).
5. Havia repetição de palavras desnecessária (ver foto do texto).
6. Não gostou da frase de efeito de Bernardo (ver screenshot) — sugeriu: "Conte comigo, vamos tentar mais uma vez!"

### 2.4 Feedback da mãe — L001
1. Ficou com dúvida se aplicou corretamente.
2. Não entendeu quais eram as "três promessas do Rei" no enredo.
3. Sentiu falta de desenvolvimento da história.
4. Precisou de mais instruções para aplicar com múltiplas crianças (todas queriam segurar as sementes; as contagens ficaram fragmentadas porque as sementes não estavam juntas).

---

## 3) Análise por tema

---

### TEMA A: "Difícil aplicar olhando no celular. Preferiria impresso ou livro."

**Classificação:** Feedback de canal e formato, não de conteúdo.

**Análise:**
Este é um ponto de UX real, mas precisamos distinguir o que é pedido do que está sendo sentido. O que Isa realmente está sentindo é: **"não consigo conduzir e ler ao mesmo tempo com naturalidade."** Isso é diferente de precisar de um livro físico.

**Voz dos experts:**

> **Charlotte Mason (CM):** "A Mãe precisa de leveza. VR-007 — Exige preparo excessivo = VETO. Se a aplicação exige que a mãe reparta atenção entre tela e criança de forma que gere friccão, o produto falhá no teste Abra e Faça."

> **Priscila (A Prática, Tribunal Café Manhã):** "Funciona agora? Então uso. Se precisa de impressão ou adaptação manual, vou esquecer de preparar e não usar."

> **Débora (A Iniciante):** "Preciso de mão segurando. Se olho pro celular e perco o fio, fico insegura."

**Diagnóstico:**
O problema não é celular vs. impresso. O problema é que o Portador ainda não internalizou o fluxo — a L000 e a L001 são as primeiras lições dela. A dificuldade vai diminuir com repetição. MAS: isso é um sinal de que a estrutura da página precisa ajudar mais o olhar a encontrar rapidamente o que fazer. Blocos muito próximos, instruções e falas sem diferenciação visual suficiente tornam o escaneamento difícil.

**Decisão:**
- ❌ Não redesenhar para livro/impresso agora — não é o produto.
- ✅ Verificar se a diferenciação visual entre "instrução do Portador" e "fala para a criança" está clara o suficiente no CSS e na hierarquia horizontal.
- ✅ Adicionar, no topo da Preparação, uma nota curta de como usar: "Você pode ler a preparação antes e depois abrir na Jornada."
- ✅ Registrar como dado para o produto futuro: a versão física pode ser um add-on premium.

---

### TEMA B: "O momento de introdução dos personagens pode ser melhor indicado."

**Classificação:** Feedback de UX do Portador + protocolo de reveal.

**Análise:**
Isa descreve a seguinte confusão: entendeu que devia mostrar o card ANTES de falar o texto, mas achou que seria mais natural falar o texto ANTES e mostrar a figura. Ela está certa — e isso é exatamente o que o nosso protocolo de reveal já define (TX04/004_GUARDIOES_CARDS_E_REVEAL). O problema foi que a instrução não ficou clara o bastante na página.

**Voz dos experts:**

> **CS Lewis:** "A surpresa é parte da alma da história. Se a figura aparece antes da expectativa estar instalada, o guardião vira personagem de papelaria, não presença viva."

> **JRR Tolkien:** "A consistência interna do mundo depende de que cada elemento apareça no momento correto de acordo com a lei interna da narrativa. Mostrar o guardião antes de A Jornada é revelar o final do primeiro ato."

> **Débora (A Iniciante):** "Preciso que a instrução me diga: 'Fale o texto. Depois mostre.' Com clareza. Não devo adivinhar."

**Diagnóstico:**
A instrução de como usar o card provavelmente não está explícita o suficiente no `instruction-box` do Ritual ou da Jornada. O Portador fez o que achou mais intuitivo (mostrar figura) em vez de seguir o protocolo ideal.

**Decisão:**
- ✅ Verificar em L000 e L001 se o instruction-box antes do reveal do guardião diz explicitamente a ordem: "Fale o texto primeiro. Depois, mostre o card."
- ✅ Adicionar um micro-cue visual antes do card: ex. um badge ou instrução curta tipo "[Fale antes de mostrar]".
- ❌ Não mudar a ordem real do reveal — a intuição da Isa é boa, mas nossa ordem já é a correta.

---

### TEMA C: Repetição de palavras e frase de Bernardo ("Mais uma vez. Comigo.")

**Classificação:** Feedback editorial direto sobre dois problemas distintos.

**Análise parte 1 — Repetição de palavras:**
O screenshot mostra o trecho da L000. A repetição é um problema real de edição — faz o texto soar menos premium. Esse é um finding de revisão editorial standard.

**Análise parte 2 — Frase de Bernardo:**
A frase atual: *"Quando você errar, Bernardo vai dizer: 'Mais uma vez. Comigo.'"*
Sugestão da Isa: *"Conte comigo, vamos tentar mais uma vez!"*

Esta é uma decisão editorial importante que precisa de deliberação.

**Voz dos experts:**

> **CS Lewis:** "A frase-assinatura de um personagem deve soar como esse personagem, não como bordão infantil genérico. 'Mais uma vez. Comigo.' tem economia e peso — é firme sem ser duro. A versão sugerida soa mais casual e perde o tom Bernardo. Criança como pessoa merece a firmeza nobre, não o diminutivo do entusiasmo."

> **Charlotte Mason:** "Hábito de atenção depende de tom claro. Bernardo é persistência — 'Mais uma vez. Comigo.' é ritmo de marcha, de fôlego retomado. É pedagogicamente mais honesto que 'vamos tentar'."

> **Júlia (A Relacional):** "Entendo a Isa. 'Mais uma vez. Comigo.' pode soar seco para algumas mães. Mas depende de como o Portador lê. Se a instrução de tom for clara — 'com calor, não com cobrança' — a frase original funciona."

> **Débora (A Iniciante):** "A frase da Isa soa mais gentil ao primeiro contato. Mas é menos memorável. E a identidade do Bernardo precisa ser reconhecível entre lições."

**Diagnóstico:**
A frase-assinatura de Bernardo é parte da identidade tribal e não deve ser alterada. O que precisa melhorar é a **instrução de tom** antes da fala — garantir que o Portador saiba que deve dizer com calor genuíno, não com cobrança.

**Decisão:**
- ❌ Não alterar "Mais uma vez. Comigo." — é frase-assinatura e tem identidade.
- ✅ Verificar se o `script-tone` antes da frase de Bernardo instrui o Portador com clareza: ex. "[Com calor, não cobrança. Como quem levanta a mão de um amigo]."
- ✅ Corrigir as repetições de palavras identificadas na captura de tela (tarefa editorial para a sessão de revisão da L000).

---

### TEMA D: "Não entendeu quais eram as três promessas do Rei."

**Classificação:** Feedback narrativo crítico — afeta tanto a mãe quanto as crianças maiores.

**Análise:**
Este é o ponto de maior peso desta discussão. Tanto a Isa (mãe) quanto Daniel e João (crianças maiores) não entenderam o que são "as promessas do Rei." A metáfora "sementes de carvalho como promessas do Rei" parece não ter raízes suficientes dentro da própria licão.

**Voz dos experts:**

> **JRR Tolkien:** "O objeto mágico precisa de lei interna. Por que são 'promessas do Rei'? O que o Rei prometeu? A criança percebe a ausência de fundamento. Não é preciso explicar tudo — mas a metáfora precisa ter peso dentro da história, não ser apenas frase decorativa."

> **CS Lewis:** "Supposal não é alegoria. 'Três promessas do Rei' é uma alegoria sem ancoragem — vira frase bonita solta, não imagem pregnante. Para funcionar como supposal, a criança deveria poder intuir: 'Ah, o Rei plantou algo que vai crescer.' A Jornada precisa fazer esse solo."

> **Charlotte Mason:** "Ideia Viva versus fato seco. 'Promessa do Rei' vira fato seco se o Rei não foi apresentado de forma que torne a promessa sentível. A L000 apresentou o Reino. A L001 usa a metáfora. Mas a ponte pode ainda estar fraca."

> **Renata (A Experiente):** "Se a mãe não entendeu, as crianças maiores vão questionar. Crianças pequenas como José entram no clima sem precisar entender — isso é normal e bom. Mas se o Portador não sabe o que está conduzindo, ele perde confiança."

**Diagnóstico crítico:**
A frase "sementes como promessas do Rei" é usada na L001 como imagem central (hero-quote e fala de Celeste). Mas a L000 não plantou o contexto de que o Rei faz promessas — o Portal apresentou o Reino e os guardiões, mas não estabeleceu a narrativa de que o Rei planta coisas que crescem.

Há dois problemas:
1. **Para crianças maiores (Daniel e João, ~8-12 anos):** o enredo de 1-2-3 sementes na palma foi percebido como simples demais. Isso é natural — é uma lição para 4-6 anos. A questão é: a família toda está aplicando juntos?
2. **Para a mãe:** a falta de entendimento do metáfora "promessa" é um gap real que pode ser resolvido com uma linha na Preparação explicando o que é esse motivo narrativo.

**Decisão:**
- ✅ Verificar se a Preparação do Portador explica, em linguagem simples, o que são "promessas do Rei" no contexto narrativo de Matemática Viva.
- ✅ Adicionar ao `Fio da Jornada` da L001 uma linha que ancore a metáfora: ex. "No Reino Contado, Celeste entende que cada semente guarda em si uma forma de crescimento que o Rei já plantou — elas são pequenas, mas não estão vazias."
- ✅ Considerar nota breve na Preparação sobre aplicação com crianças de idades mistas — isso afeta mais de uma família.
- ❌ Não mudar a frase-assinatura "três pequenas promessas do Rei" — é bela e funcionou bem para José. O problema não é a frase, é a ausência de ancoragem antes dela.

---

### TEMA E: "Mais instruções para aplicar com mais de uma criança."

**Classificação:** Pedido operacional legítimo — gap de UX para famílias com múltiplos filhos.

**Análise:**
Este é um dos pontos mais acionáveis e mais importantes do feedback. Temos famílias com 3-4 filhos. A lição foi desenhada com gestos que pressupõem uma criança de cada vez (sementes na palma, cada uma por vez). Com 3 filhos, o caos é real.

**Voz dos experts:**

> **Renata (A Experiente):** "Logística caótica com 4 idades é minha vida. Se a lição não tem uma variante para múltiplas crianças, eu improviso — e o improviso pode quebrar a experiência ou me estressar."

> **Charlotte Mason (VR-006 / Princípio Bernardo):** "Caminhos diferentes chegam ao mesmo destino. A licação pode ter uma nota de adaptação para múltiplas crianças sem precisar ser reescrita — basta que a variação seja digna e clara."

> **Priscila (A Prática):** "Me diz o que fazer com 3 filhos. Não me deixa descobrir na hora."

**Diagnóstico:**
O ciclo Sementes foi desenhado para crianças 4-6 anos, mas famílias têm filhos de idades mistas. A lição não precisa ser reescrita — mas a `Estratégia do Mestre` ou a seção de materiais pode incluir uma nota específica: **"Se houver mais de uma criança: dê uma semente para cada um. A contagem acontece coordenada entre as palmas, não em uma palma só."**

**Decisão:**
- ✅ Adicionar à Preparação do Portador (ou ao materials-box) da L001 uma nota de adaptação para famílias com múltiplos filhos aplicando juntos.
- ✅ Incluir variante específica: "cada criança recebe uma semente para segurar durante a Jornada; as contagens acontecem em voz alta juntos."
- ✅ Considerar se essa nota vale como item de retrofit para L002 e L003 também.
- ❌ Não redesenhar a lição para o cenário multi-criança como padrão — o design de 1 palma é correto para a idade-alvo.

---

## 4) Quadro de decisões consolidado

| # | Ponto do Feedback | Decisão | Ação |
|---|---|---|---|
| A | Difícil no celular | Não mudar formato; melhorar escaneabilidade | Revisar hierarquia visual Portador vs. fala |
| B | Ordem do reveal de personagens | Não mudar ordem; tornar instrução explícita | Micro-cue antes do card: "Fale antes de mostrar" |
| C | Repetição de palavras | Corrigir | Revisão editorial L000 |
| C | Frase de Bernardo | Não alterar | Melhorar script-tone antes da fala |
| D | "Promessas do Rei" sem ancoragem | Ancorar na Preparação | Linha no Fio da Jornada L001 |
| E | Múltiplas crianças | Adicionar nota de adaptação | Materials-box ou Estratégia do Mestre L001 |

---

## 5) O que NÃO fazer (e por quê)

1. **Não adicionar mais texto explicativo sobre o enredo.** O risco é que a L001 se torne mais pesada para o Portador. A solução é ancoragem cirúrgica, não expansão narrativa.
2. **Não mudar a frase-assinatura de Bernardo.** Identidade tribal. A Isa representa uma perspectiva; Lewis e CM representam o contrato da obra.
3. **Não redesenhar para livro físico.** É um produto digital. A dificuldade no celular vai diminuir com a familiarização. Se vier impressão no futuro, é add-on.
4. **Não tratar Daniel e João como target principal da L001.** São crianças mais velhas, e é natural que a L001 (Sementes, 4-6 anos) seja simples para eles. Isso não é defeito — é escopo.

---

## 6) Próximos passos de ação

Prioridade máxima (sessão atual):
1. Adicionar nota de adaptação multi-criança na L001 (materials-box ou Preparação).
2. Adicionar linha de ancoragem para "promessas do Rei" no Fio da Jornada da L001.
3. Melhorar `script-tone` da fala de Bernardo em L000 para deixar a instrução de calor mais explícita.

Prioridade alta (próxima sessão):
4. Revisar L000 para corrigir as repetições de palavras identificadas na captura da Isa.
5. Adicionar micro-cue de reveal em L000 e L001: "Fale antes de mostrar o card."
6. Avaliar se a hierarquia visual da página (Portador vs. fala narrativa) está clara no CSS.

Prioridade média (antes de L004+):
7. Criar uma nota geral na Preparação de lições Sementes para famílias com múltiplos filhos.
8. Registrar o perfil da Isa como "família de idades mistas" nos dados de produto.

---

## 7) Frase-síntese desta discussão

O feedback da Isa é ouro: é real, específico e vem de boa-fé.
Mas a obra não serve a uma família — serve a todas as famílias.
Cada ajuste precisa passar pelo Tribunal Café Manhã completo antes de entrar no produto.
O que Isa pediu e faz sentido, incorporamos.
O que Isa pediu e trai o North Star, agradecemos e explicamos.
