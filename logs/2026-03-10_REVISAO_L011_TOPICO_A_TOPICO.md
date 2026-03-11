# REVISÃO L011 — TOPICO A TOPICO
Data: 2026-03-10
Skill: `revisao-sementes-topico-a-topico`

## MV-S-011 - A Plenitude das Mãos

### Findings do Diagnóstico Inicial
- Critico: lição inteira em formato legado (não migrada para contrato canônico 031)
- Alto: tópico T010 `Sementes para o Dia` completamente ausente; `div onclick` para navegação; CSS inline duplicando `style.css`; nomes legados (`Ritual de Abertura`, `Atividade Concreta`, `Para a Família`); emojis em vez de Phosphor Icons; `Pictórico: Vetado` (anti-projeto)
- Medio: Sem Fio da Jornada, Descoberta da Criança, Sinal de Fruto, Segredo do Maravilhamento, Estratégia do Mestre expandida, Sussurro do Portal, card do local, variações, ponte, adaptação, postura de escuta; Celeste em minúsculas; encoding misto
- Baixo: `favicon.ico` referenciado; `Reflexão Espiritual` fora do contrato canônico

### Cerne Macro
- TGTB ref: `000-L11 - Numbers 10 to 11 / Números 10 e 11`
- Promessa: a criança descobre que duas mãos completas fazem `10` e que `11` é "um a mais"
- Guardião e Lugar: Celeste (raposa) na Clareira das Perguntas
- Imagem Dominante: duas mãos abertas / dez dedos / um a mais / céu
- Conceito Vivo: `10` como plenitude das mãos; `11` como surpresa após a completude
- Fruto do Dia: a criança conta 10 com as mãos e percebe que 11 vai além

### Resíduos Legados (21 encontrados)
1. `Ritual de Abertura` em vez de `Ritual de Entrada` (l.193)
2. `Atividade Concreta` em vez de `O Concreto` (l.431)
3. `Para a Família` em vez de `Formação do Portador` (l.628)
4. `div onclick` para navegação (l.604)
5. Emojis inline em vez de Phosphor Icons
6. CSS inline crítico duplicando `style.css` (l.12-73)
7. `[Foco: ...]` com colchetes de template (l.133)
8. Sem `<nav>` semântico superior com Phosphor
9. Sem `Sementes para o Dia`
10. `Conexão da Jornada` com `⬅️/➡️ Última/Próxima Aventura`
11. Sem `scene-card` canônico com classes `section`
12. Sem `prep-bridge-box` (Fio da Jornada)
13. Sem `Segredo do Maravilhamento`
14. Sem `Estratégia do Mestre` na Preparação
15. Sem `Descoberta da Criança`
16. Sem `Sinal de Fruto de Hoje`
17. Sem `Sussurro do Portal`
18. Sem card do local revelado
19. Sem `acting-cue` / pausa
20. Guardião `celeste` em minúsculas (l.297)
21. Sem `footer` padronizado

### Matriz Tópica (PASS/GAP/BLOCK)
- 001 Base e Hero: GAP — Hero quote presente mas sem HTML entities. Sem Phosphor icons. Meta-tag com emojis.
- 002 Header Superior: BLOCK — `<nav>` não-semântica, `img` para ícone central, estilos inline.
- 003 Preparacao do Portador: BLOCK — Foco com colchetes template. Sem Fio, Descoberta, Fruto, Maravilhamento, Estratégia expandida. Graça minimalista.
- 004 Ritual de Entrada: BLOCK — `Ritual de Abertura`. Sem card do local. Sem Sussurro do Portal. Sensory box inline.
- 005 A Jornada: GAP — Três cenas presentes e Celeste coerente. Mas sem `journey-scene` classes, gesto simplificado, nome em minúsculas.
- 006 O Concreto: GAP — Passo a passo presente. `Atividade Concreta`. Sem ligação Jornada, variação, adaptação, ponte.
- 007 Narramos Juntos: GAP — Perguntas de coração presentes. Sem postura de escuta, formas legítimas expandidas, adaptação digna.
- 008 Ritual de Fechamento: GAP — Celeste e Portador presentes. Tom minimalista, sem acting-cue.
- 009 Conexao da Jornada: BLOCK — Formato legado com `div onclick`. Sem memória viva. Sem teaser narrativo real.
- 010 Sementes para o Dia: BLOCK — AUSENTE. Tópico completamente inexistente.
- 011 Formacao do Portador: BLOCK — `Para a Família`. `Pictórico: Vetado`. Sem `O que o Portador aprende`. Sem Espiral expandida. `Reflexão Espiritual` fora do contrato.
- 012 Navegacao Inferior: GAP — Links corretos mas emojis em vez de Phosphor e `lesson-nav` em vez de `lesson-footer-nav`.

### Fronteiras Críticas Inspecionadas
- 003 -> 004: GAP — Preparação não desemboca de forma canônica no Ritual (nomes legados).
- 004 -> 005: GAP — Ritual revela lugar sem Sussurro; Jornada revela Celeste sem card.
- 005 -> 006: GAP — Sem ligação explícita Jornada → Concreto.
- 006 -> 007: GAP — Falta ponte explícita.
- 008 -> 009: GAP — Fechamento minimalista antes de Conexão legada.
- 009 -> 010: BLOCK — Sementes ausente.
- 010 -> 011: BLOCK — Não aplicável (Sementes ausente).
- 011 -> 012: GAP — Formação legada seguida de navegação legada.

### Pareceres e Conselhos dos Experts
- **Charlotte Mason:** BLOCK. Criança recebe instruções diretas sem mediação de narração viva na Preparação. `Pictórico: Vetado` contradiz o espírito do projeto.
- **Jerome Bruner:** GAP. CPA presente mas `Pictórico: Vetado`. O projeto adia, nunca veta. Abstrato cedo demais (símbolos 10, 11).
- **Susan Macaulay:** GAP. Legível mas com colchetes template, emojis sem classes semânticas, `<br>` excessivos.
- **Mãe Ansiosa:** GAP. Graça genérica. `chegamos ao DEZ!` pode pressionar.
- **Mãe Veterana:** GAP. Plano B ausente. Sem adaptação para dia curto. Sem substituições caseiras.
- **Beatrix Potter:** GAP. Imagem dominante nasce no Hero mas se dilui em tom instrucional.
- **Engenharia:** BLOCK. CSS inline duplicado. `div onclick`. Emojis vs Phosphor. Encoding misto. Sem `<section>` canônicos.
- **Design:** BLOCK. Layout antigo. Sem hierarquia visual canônica. Breakpoints fixos em inline CSS.

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
- Leveza da Mãe: Parcial — sem Fio, sem Fruto, sem Plano B. `chegamos ao DEZ!` pode gerar ansiedade de marco.
- Status Geral: BLOCK — REESCRITA NECESSÁRIA

### Risco residual e Proximo passo
- A lição inteira precisa ser migrada para o contrato canônico usando L009 ou L010 como modelo.
- O que é aproveitável na reescrita: as 3 cenas da Jornada (Duas Mãos, Número Perfeito, Um a Mais), o conceito vivo (10 como plenitude) e o passo a passo do Concreto.
- Após reescrita, submeter a nova revisão tópico a tópico.
