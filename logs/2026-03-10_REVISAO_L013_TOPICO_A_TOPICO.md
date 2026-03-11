# REVISÃO L013 — TOPICO A TOPICO
Data: 2026-03-10
Skill: `revisao-sementes-topico-a-topico`

## MV-S-013 - O Rio que se Une

### Findings do Diagnóstico Inicial
- Critico: lição inteira em formato legado (não migrada para contrato canônico 031)
- Alto: tópico T010 `Sementes para o Dia` completamente ausente; `div onclick` para navegação (l.607); CSS inline duplicando `style.css` (l.12-73); nomes legados (`Ritual de Abertura`, `Atividade Concreta`, `Para a Família`); emojis em vez de Phosphor Icons; `Pictórico: Vetado` (anti-projeto); Melquior em minúsculas (l.301)
- Medio: Sem Fio da Jornada, Descoberta da Criança, Sinal de Fruto, Segredo do Maravilhamento, Estratégia do Mestre, Sussurro do Portal, variações, ponte para Narramos, adaptação casa viva, postura de escuta; `[Foco: ...]` com colchetes template (l.133); `Reflexão Espiritual` fora do contrato; nav legada com `img` central
- Baixo: `favicon.ico` referenciado; card local sem formato canônico

### Cerne Macro
- TGTB ref: `000-L13 - Plus and Equals Signs / Sinais de Mais e Igual`
- Promessa: a criança descobre que `+` significa "juntar" e `=` significa "virar" através de dois rios de pedras que se encontram
- Guardião e Lugar: Melquior (leão) no Jardim Central
- Imagem Dominante: dois riachos de pedras que se unem / confluência / força da união
- Conceito Vivo: `+` como juntar e `=` como resultado — símbolos como histórias, não como abstração
- Fruto do Dia: a criança junta dois grupos, conta o total e reconhece que `+` e `=` contam essa história

### Resíduos Legados (20+ encontrados)
1. `Ritual de Abertura` em vez de `Ritual de Entrada` (l.198)
2. `Atividade Concreta` em vez de `O Concreto` (l.433)
3. `Para a Família` em vez de `Formação do Portador` (l.631)
4. `div onclick` para navegação (l.607)
5. Emojis inline (🏡, 🗺️, 🧱, 🗣️, 🏁, 🔗, 👨‍👩‍👧‍👦, 💡, 📋, etc.) em vez de Phosphor Icons
6. CSS inline crítico duplicando `style.css` (l.12-73)
7. `[Foco: ...]` com colchetes de template (l.133)
8. Sem `<nav>` semântico superior com Phosphor
9. Sem `Sementes para o Dia` — tópico T010 ausente
10. `Conexão da Jornada` com `⬅️ Última Aventura` / `➡️ Próxima Aventura`
11. Sem `section` tags canônicos (`journey-section`, `concrete-section`, etc.)
12. Sem `prep-bridge-box` (Fio da Jornada)
13. Sem `Segredo do Maravilhamento`
14. Sem `Estratégia do Mestre` na Preparação
15. Sem `Descoberta da Criança`
16. Sem `Sinal de Fruto de Hoje`
17. Sem `Sussurro do Portal`
18. Sem `acting-cue` / pausa
19. Guardião `melquior` em minúsculas (l.301)
20. Sem `footer` padronizado (usa footer custom inline, l.733)
21. Card do local com formato legado (l.271-275)

### Matriz Tópica (PASS/GAP/BLOCK)
- 001 Base e Hero: GAP — Hero quote presente mas sem HTML entities. Sem Phosphor icons. Meta-tag com emojis. Alt text genérico (`melquior`).
- 002 Header Superior: BLOCK — `div` não-semântica, `img` para ícone central, estilos inline rígidos. Sem `<nav>` com Phosphor.
- 003 Preparacao do Portador: BLOCK — Foco com colchetes template. Sem Fio da Jornada. Sem Descoberta da Criança. Sem Sinal de Fruto. Sem Segredo do Maravilhamento. Sem Estratégia do Mestre. Materiais mínimos sem substituições caseiras. Sem Plano B. Graça presente mas minimalista.
- 004 Ritual de Entrada: BLOCK — `Ritual de Abertura`. Sem card canônico do local. Sem Sussurro do Portal. Sensory box com estilo inline. `Transição` em vez de tom canônico do Portador.
- 005 A Jornada: GAP — Três cenas presentes (Dois Rios, A União, O Resultado). Melquior com falas coerentes. Mas: sem `journey-section`, gesto do Portador simplificado, nome em minúsculas, card local em formato legado.
- 006 O Concreto: GAP — Passo a passo com 4 passos. `Atividade Concreta`. Sem ligação explícita com Jornada. Sem variação. Sem adaptação casa viva. Sem ponte para Narramos.
- 007 Narramos Juntos: GAP — Perguntas presentes. Mas: sem postura de escuta do Portador, sem formas legítimas expandidas, sem adaptação digna. Instrução pede guardar pedras antes de narrar.
- 008 Ritual de Fechamento: GAP — Melquior e Portador presentes. Tom minimalista, sem acting-cue, sem devolução da casa.
- 009 Conexao da Jornada: BLOCK — Formato legado com `div onclick`. Sem memória viva. Sem teaser narrativo real. `⬅️/➡️ Última/Próxima Aventura`.
- 010 Sementes para o Dia: BLOCK — AUSENTE. Tópico completamente inexistente.
- 011 Formacao do Portador: BLOCK — `Para a Família`. `Pictórico: Vetado`. Sem `O que o Portador aprende`. Sem Espiral expandida. Sem Estratégia do Mestre. `Reflexão Espiritual` fora do contrato canônico.
- 012 Navegacao Inferior: GAP — Links corretos mas emojis (←/→), `lesson-nav` em vez de `lesson-footer-nav`.

### Fronteiras Críticas Inspecionadas
- 003 -> 004: GAP — Preparação com colchetes não desemboca de forma canônica no Ritual legado.
- 004 -> 005: GAP — Ritual revela lugar sem Sussurro; Jornada revela Melquior sem card canônico.
- 005 -> 006: GAP — Sem ligação explícita Jornada → Concreto.
- 006 -> 007: GAP — Falta ponte explícita para narração.
- 008 -> 009: GAP — Fechamento minimalista antes de Conexão legada.
- 009 -> 010: BLOCK — Sementes ausente.
- 010 -> 011: BLOCK — Não aplicável (Sementes ausente).
- 011 -> 012: GAP — Formação legada seguida de navegação legada.

### Pareceres e Conselhos dos Experts
- **Charlotte Mason:** BLOCK. Criança recebe instruções diretas com `<br>` sem mediação narrativa na Preparação. `Pictórico: Vetado` contradiz o espírito do projeto.
- **Jerome Bruner:** GAP. CPA presente mas `Pictórico: Vetado` — projeto adia, nunca veta. Abstrato (símbolos + e =) aparece quase em paralelo ao concreto, sem camada pictórica intermediária.
- **Susan Macaulay:** GAP. Legível mas com emojis sem classes semânticas, `<br>` excessivos e colchetes template. Mãe precisa de reler.
- **Mãe Ansiosa:** GAP. Graça presente (`O Rei sorriu ao ver você chegar`) mas sem proteção contra ansiedade de "não entender símbolos novos".
- **Mãe Veterana:** GAP. Plano B ausente. Sem adaptação para dia curto. Sem substituições caseiras expandidas.
- **Beatrix Potter:** GAP. Imagem dos rios existe no Hero mas se dilui em tom instrucional durante o Concreto.
- **Engenharia:** BLOCK. CSS inline duplicado. `div onclick`. Emojis vs Phosphor. Encoding misto (UTF-8 direto). Sem `<section>` canônicos.
- **Design:** BLOCK. Layout antigo. Sem hierarquia visual canônica. Cards sem classes corretas.

### Patch e Adequações Realizadas
- Estruturais: nenhum patch possível — requer reescrita completa
- Narrativas: nenhum patch possível — requer reescrita completa
- Pedagógicas: nenhum patch possível — requer reescrita completa
- Lapidação / Taste: nenhum patch possível — requer migração ao contrato canônico

### Tabela de Validação de Fechamento
- Cobertura topica: BLOCK (T010 ausente)
- Fronteiras topicas: GAP
- North Star: BLOCK
- Estrutura: BLOCK
- Narrativa: GAP
- Pedagogia: GAP
- Navegacao: BLOCK
- Tecnica: BLOCK
- Taste editorial: GAP
- Leveza da Mãe: Parcial — sem Fio, sem Fruto, sem Plano B. Símbols novos (+ e =) podem gerar ansiedade.
- Status Geral: BLOCK — REESCRITA NECESSÁRIA

### Risco residual e Proximo passo
- A lição inteira precisa ser migrada para o contrato canônico usando L009 ou L010 como modelo estrutural.
- O que é aproveitável na reescrita: as 3 cenas da Jornada (Dois Rios, A União, O Resultado) com Melquior, o conceito vivo (+ como juntar, = como resultado) e o passo a passo do Concreto.
- Após reescrita, submeter a nova revisão tópico a tópico.
