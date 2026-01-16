# WORKFLOW: Prototipação HTML → Gutenberg

**Data:** 16/01/2026 12:37
**Lição Piloto:** MV-S-001 (A Trindade na Palma)

---

## 📋 Lógica do Workflow

```
┌───────────────────────────────────────────────────────────────────┐
│                                                                   │
│   1. PROTOTIPAÇÃO                                                 │
│   ───────────────                                                 │
│   Editar diretamente: site/sementes/MV-S-001_*.html              │
│   - Ajustar layout, CSS, componentes                              │
│   - Ver resultado no browser em tempo real                        │
│   - Iterar até ficar impecável                                    │
│                                                                   │
│                         ▼                                         │
│                                                                   │
│   2. APROVAÇÃO                                                    │
│   ───────────                                                     │
│   Maestro valida visualmente                                      │
│   - "Está perfeito, pode transferir"                              │
│                                                                   │
│                         ▼                                         │
│                                                                   │
│   3. TRANSFERÊNCIA                                                │
│   ──────────────                                                  │
│   Migrar mudanças para templates Jinja2:                          │
│   - site/sementes/templates/base.j2                               │
│   - site/sementes/templates/licao.j2                              │
│   - site/sementes/templates/macros.j2                             │
│   - site/sementes/style.css                                       │
│                                                                   │
│                         ▼                                         │
│                                                                   │
│   4. REBUILD                                                      │
│   ─────────                                                       │
│   python build/forge.py --fase sementes                           │
│   - Regenera TODAS as lições com novo template                    │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

---

## 📁 Arquivos Envolvidos

| Fase | Arquivo | Tipo |
|:---|:---|:---|
| Prototipação | `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html` | HTML direto |
| Transferência | `site/sementes/templates/base.j2` | Template Jinja2 |
| Transferência | `site/sementes/templates/licao.j2` | Template Jinja2 |
| Transferência | `site/sementes/templates/macros.j2` | Componentes |
| Transferência | `site/sementes/style.css` | Estilos |

---

## ⚠️ IMPORTANTE

> **NÃO execute o build enquanto estiver prototipando!**
> 
> O build SOBRESCREVE os HTMLs. Se você editou o HTML diretamente e rodar o build, suas mudanças serão perdidas.
> 
> **Fluxo seguro:**
> 1. Editar HTML
> 2. Aprovar visual
> 3. Transferir para templates
> 4. SÓ ENTÃO rodar build

---

## 📝 Checklist de Prototipação

### MV-S-001 — A Trindade na Palma

- [ ] Ajustes de layout
- [ ] Ajustes de CSS
- [ ] Ajustes de componentes
- [ ] Aprovado pelo Maestro
- [ ] Transferido para templates
- [ ] Build executado

---

## 🏛️ DELIBERAÇÃO: REFINAMENTO VISUAL MV-S-001

> **Data:** 16/01/2026 12:48
> **Modo:** REUNIAO (orchestrator.yaml)
> **Pauta:** Analisar 16 pontos de feedback do Maestro

### Participantes

| Expert | Conselho | Foco |
|:---|:---|:---|
| Charlotte Mason | Pedagogia | Experiência da criança/família |
| Design | Design | Visual e estética |
| Beatrix Potter | Narrativa | Ilustrações e cards |
| Clean Code | Engenharia | Estrutura HTML |

---

## 📋 ANÁLISE DOS 16 PONTOS

### PONTO 1: Meta Tag Superior

**Atual:**
```
MV-S-001 • 15-20 min • 1
```

**Feedback do Maestro:**
> "Tirar MV-S-001, colocar Lição 01 e nome em português. 15-20 min dá muita opção, colocar tempo máximo 20 minutos."

**Proposta Design:**
```
Lição 01 • A Trindade na Palma • ⏱️ 20 min
```

**Deliberação:**
- ✅ Charlotte Mason: "Lição 01 é mais humano que código técnico."
- ✅ Design: "Emoji de relógio dá toque visual agradável."
- ✅ Clean Code: "Simples e limpo."

**DECISÃO:** Aprovar proposta. Mudar no HTML linha 81.

---

### PONTO 2: Dica do Coração

**Atual:** Box amarelo com instrução para o Portador.

**Feedback do Maestro:**
> "Está 90% bonito, mas poderia deixar melhor o formato."

**Proposta Design:**
- Reduzir padding de 1.25rem para 1rem
- Usar fonte ligeiramente menor (0.95rem)
- Manter a cor amarela (indica atenção gentil)

**Deliberação:**
- ✅ Charlotte Mason: "A Dica do Coração é para acalmar o Portador. Não deve ser gritante."
- ✅ Design: "Reduzir ligeiramente o tamanho mantém elegância."

**DECISÃO:** Ajuste fino de padding e font-size.

---

### PONTO 3: Materiais Necessários - Estrela

**Atual:**
```html
<li>3 sementes ou feijões (3) ⭐</li>
<li>Card Celeste (1) ⭐</li>
```

**Feedback do Maestro:**
> "Tem uma ESTRELA depois dos materiais, não entendi, não precisa disso."

**Análise:**
A estrela (⭐) indica materiais "essenciais" vs opcionais. Mas confunde mais do que ajuda.

**Proposta Design:**
Remover todas as estrelas. Se for essencial, não lista como opcional.

**DECISÃO:** Remover ⭐ de todos os itens de materiais.

---

### PONTO 4: Protocolo de Impecabilidade - Parágrafos

**Atual:**
```
NÃO EXPLIQUE os números. MOSTRE-OS.<br>
Coloque 1 semente na mão. Diga "Um". Espere.<br>
Método mão-na-mão — faça JUNTO, não PARA.<br>
```

**Feedback do Maestro:**
> "Está com parágrafo, deveria ser tudo fluido ou em tópicos."

**Proposta Design:**
Transformar em lista de tópicos para melhor leitura:

```html
<ul>
  <li>NÃO EXPLIQUE os números — MOSTRE-OS</li>
  <li>Coloque 1 semente na mão. Diga "Um". Espere.</li>
  <li>Método mão-na-mão: faça JUNTO, não PARA</li>
</ul>
```

**Deliberação:**
- ✅ Charlotte Mason: "Tópicos são mais fáceis de seguir durante a lição."
- ✅ Clean Code: "Lista ordenada melhora legibilidade."

**DECISÃO:** Converter para lista `<ul>` ou `<ol>`.

---

### PONTO 5: Nota de Graça - Linha Única

**Atual:**
```
Se contar errado, sorria. A semente já foi plantada. O Rei não tem pressa.
```

**Feedback do Maestro:**
> "Deixe tudo em uma linha só, sem parágrafo."

**Análise:**
Já está em uma linha. Verificar se há `<br>` desnecessário.

**DECISÃO:** Verificar e remover `<br>` se existir.

---

### PONTO 6: Avatar do PORTADOR

**Atual:**
```html
<img src="../assets/cards/guardioes/melquior-leao.png" class="script-avatar" alt="PORTADOR">
```

**Feedback do Maestro:**
> "Está aparecendo o LEÃO Melquior, mas o Portador da Tocha são os PAIS, não é o Melquior."

**Análise Crítica:**
Este é um BUG conceitual grave. O Portador (pai/mãe) não deve ter avatar de guardião.

**Proposta Design:**
Opções:
1. Criar ícone genérico de "família" ou "mãos"
2. Usar silhueta neutra
3. Não usar avatar para Portador

**Deliberação:**
- ⚠️ Charlotte Mason: "O Portador é o pai/mãe. Melquior é um Guardião. NUNCA misturar."
- ⚠️ Beatrix Potter: "Posso criar um ícone de 'mãos segurando' ou 'coração'."
- ✅ Design: "Proposta: usar 🙌 ou 🤲 como ícone, não imagem."

**DECISÃO:** Remover avatar PNG e usar emoji 🤲 ou criar ícone SVG simples.

**⚠️ AÇÃO FUTURA:** Este erro está no TEMPLATE. Corrigir em `licao.j2` também.

---

### PONTO 7: Card Visualizar

**Feedback do Maestro:**
> "Visualizar o card ficou muito legal."

**DECISÃO:** Manter como está. ✅

---

### PONTO 8: Local - Visualizar Card

**Atual:**
```html
📍 Local: Clareira Perguntas
```

**Feedback do Maestro:**
> "Faça aparecer o VISUALIZAR e o card dele, igual do guardião."

**Proposta Design:**
Criar componente visual para locais com mini-ilustração:

```html
<div class="local-card">
  <div class="local-header">📍 Local: Clareira das Perguntas</div>
  <div class="local-visual">
    <p style="font-size:0.9rem; color:#9CA3AF;">Visualizar</p>
    <img src="../assets/locais/clareira-perguntas.png" 
         style="width:120px; border-radius:12px; ..." />
  </div>
</div>
```

**Deliberação:**
- ✅ Beatrix Potter: "Posso criar ilustrações para cada local do Reino."
- ✅ Design: "Consistência visual é boa. Locais merecem cards também."

**DECISÃO:** Criar componente visual para locais.

**⚠️ AÇÃO FUTURA:** Precisamos de assets para locais (`LORE/locais.yaml`).

---

### PONTO 9: Guardião Falando

**Feedback do Maestro:**
> "Quando o Bernardo fala e tem ele do lado ficou ÓTIMO também."

**DECISÃO:** Manter como está. ✅

---

### PONTO 10: Mãozinha de Instrução

**Feedback do Maestro:**
> "Gostei da mãozinha do lado quando o pai tem que fazer algo, ficou bom."

**DECISÃO:** Manter como está. ✅

---

### PONTO 11: Norte Absoluto (80%)

**Atual:**
```
🧭 Norte Absoluto (80%): A maior parte da lição acontece aqui. Manipulação é onde a mágica vive.
```

**Feedback do Maestro:**
> "Essa parte acho que teremos que mudar no arquivo FONTE YAML para arrumar, está meio fora do contexto."

**Análise:**
Este é um comentário INTERNO para o Portador, não para a criança. Mas está perdido no meio do conteúdo.

**Proposta:**
1. Mover para seção "Para Portador" no início
2. Ou remover completamente (já está implícito)

**Deliberação:**
- ✅ Charlotte Mason: "O Portador já sabe que 80% é concreto. Não precisa repetir."
- ✅ Design: "Remove poluição visual."

**DECISÃO:** Remover do HTML. Avaliar se deve estar no YAML fonte.

**⚠️ AÇÃO FUTURA:** Revisar estrutura do YAML fonte.

---

### PONTO 12: Narramos Juntos

**Feedback do Maestro:**
> "Perfeito."

**DECISÃO:** Manter como está. ✅

---

### PONTO 13: Fio de Ouro

**Atual:**
```
🧵 Fio de Ouro: Bernardo está empilhando pedras. Quantas cabem em cada fileira? Vamos descobrir juntos.
```

**Feedback do Maestro:**
> "Não precisa disso pois já tem o LINKAGE, acho que precisaremos arrumar na fonte também."

**Análise:**
O "Fio de Ouro" é a conexão narrativa (próxima lição). O "Linkage" é a seção formal de navegação. São redundantes.

**Proposta:**
Remover "Fio de Ouro" do fechamento, já que "Conexão da Jornada" cobre isso.

**DECISÃO:** Remover do HTML.

**⚠️ AÇÃO FUTURA:** Remover do YAML ou unificar com Linkage.

---

### PONTO 14: PORTADOR Avatar (novamente)

**Feedback do Maestro:**
> "PORTADOR novamente está com o leão do lado."

**Análise:**
Mesmo problema do Ponto 6. Todas as ocorrências de PORTADOR com avatar de Melquior devem ser corrigidas.

**DECISÃO:** Aplicar correção do Ponto 6 em TODAS as ocorrências.

---

### PONTO 15: Conexão da Jornada - Títulos

**Atual:**
```
⬅️ Do que viemos: ...
➡️ Para onde vamos: ...
```

**Feedback do Maestro:**
> "Gostei da conexão, só não sei se 'Do que viemos' é bom. 'Para onde vamos' já gostei."

**Proposta Design:**
Alternativas para "Do que viemos":
1. "⬅️ Lição Anterior"
2. "⬅️ De onde viemos"
3. "⬅️ Última Aventura"

**Deliberação:**
- ✅ Charlotte Mason: "'Última Aventura' é mais narrativo e encantador."
- ✅ Design: "Consistência: 'Última Aventura' / 'Próxima Aventura'"

**DECISÃO:** 
- `⬅️ Última Aventura` (em vez de "Do que viemos")
- `➡️ Próxima Aventura` (em vez de "Para onde vamos")

---

### PONTO 16: Para a Família

**Feedback do Maestro (múltiplos sub-pontos):**

**16.1 - Identificar autor de cada fala:**
> "Cada tópico precisa vir explicando de quem é, do CM, do CPA, do Bruner."

**16.2 - Número do Princípio CM:**
> "Está aparecendo o NÚMERO da TIP, não precisa."

Atual: `Princípio CM #10`
Proposta: `Princípio Charlotte Mason`

**16.3 - Texto em inglês:**
> "Ter tradução depois da citação em inglês."

Atual:
```
"Ideas conveyed through living books and firsthand experiences."
```

Proposta:
```
"Ideas conveyed through living books and firsthand experiences."
(Ideias transmitidas através de livros vivos e experiências diretas.)
```

**16.4 - Cores por autor:**
> "Cada FALA ter uma cor também? Pense sobre isso."

**Proposta Design:**

| Autor | Cor de Fundo | Borda Esquerda |
|:---|:---|:---|
| Charlotte Mason | `#EDE9FE` (roxo claro) | `#8B5CF6` (roxo) |
| Jerome Bruner (CPA) | `#DBEAFE` (azul claro) | `#3B82F6` (azul) |
| Singapore Math | `#FEF3C7` (amarelo claro) | `#F59E0B` (amarelo) |

**Deliberação:**
- ✅ Charlotte Mason: "Identificar a fonte dá credibilidade."
- ✅ Design: "Cores por autor é elegante e funcional."
- ✅ Clean Code: "Criar classes CSS: `.cm-quote`, `.bruner-quote`, `.singapore-quote`"

**DECISÃO:** Implementar identificação de autor + cores + tradução.

---

## 📊 RESUMO DAS DECISÕES

| # | Ponto | Decisão | Onde Mudar |
|:---|:---|:---|:---|
| 1 | Meta tag | Lição 01 • Nome • 20 min | HTML |
| 2 | Dica do Coração | Ajuste fino padding/font | HTML |
| 3 | Estrela materiais | Remover ⭐ | HTML |
| 4 | Protocolo | Converter para lista | HTML |
| 5 | Nota de Graça | Verificar <br> | HTML |
| 6 | Avatar Portador | Usar emoji 🤲 | HTML + Template |
| 7 | Card Visualizar | ✅ Manter | - |
| 8 | Local card | Criar componente visual | HTML + Assets |
| 9 | Guardião falando | ✅ Manter | - |
| 10 | Mãozinha instrução | ✅ Manter | - |
| 11 | Norte Absoluto | Remover | HTML + YAML |
| 12 | Narramos Juntos | ✅ Manter | - |
| 13 | Fio de Ouro | Remover | HTML + YAML |
| 14 | Portador (2x) | Aplicar correção #6 | HTML |
| 15 | Títulos linkage | Última/Próxima Aventura | HTML |
| 16 | Para Família | Autor + cor + tradução | HTML |

---

## ✅ RESPOSTAS DO MAESTRO (16/01/2026 13:20)

### Pergunta 1: Avatar do Portador

**Resposta:** Usar TOCHA 🔥 (Portador da Tocha)

> "Pode ser uma TOCHA por ser o Portador da Tocha, pois iremos fazer um MANUAL para os pais explicando tudo isso."

**DECISÃO FINAL:** Substituir PNG do Melquior por emoji 🔥 ou ícone de tocha.

---

### Pergunta 2: Assets de Locais

**Resposta:** JÁ TEMOS! 18 ilustrações em `site/assets/cards/locais/`

**Assets disponíveis:**
- `local-clareira-perguntas.png` ✅
- `local-caverna-recomeco.png` ✅
- `local-oficina-bernardo.png` ✅
- `local-jardim-central.png` ✅
- `local-ninho-mirante.png` ✅
- `local-observatorio-iris.png` ✅
- `local-torre-relojoeiro.png` ✅
- `local-vila-oficios.png` ✅
- ... e mais 10 locais

> "Quando não tiver, fazer referência de um local e a Beatrix criar uma descrição para usarmos IA para criar."

**DECISÃO FINAL:** Usar assets existentes. Beatrix gera prompt para locais novos.

**⚠️ AÇÃO FUTURA:** Adicionar ao template de Sementes componente de visualização de local.

---

### Pergunta 3: Norte Absoluto e Fio de Ouro

**Resposta do Maestro:**
- **Norte Absoluto:** NÃO REMOVER, mas MELHORAR no template
  - Não usar a palavra "mágico" (requer deliberação)
  - Reposicionar ou reformular
- **Fio de Ouro:** REMOVER SIM (já tem LINKAGE abaixo que ficou "muuito bom")

**DECISÃO FINAL:**
- Norte Absoluto: MELHORAR texto e posição (não remover)
- Fio de Ouro: REMOVER completamente

---

### Pergunta 4: Cores por Autor

**Resposta:** "Acho que sim, vamos fazer e ver."

**DECISÃO FINAL:** APROVADO ✅

| Autor | Cor de Fundo | Borda |
|:---|:---|:---|
| Charlotte Mason | `#EDE9FE` | `#8B5CF6` (roxo) |
| Jerome Bruner | `#DBEAFE` | `#3B82F6` (azul) |
| Singapore Math | `#FEF3C7` | `#F59E0B` (amarelo) |

---

### Pergunta 5: Títulos de Navegação

**Resposta:** "Legal acho que sim"

**Deliberação adicional - Alternativas:**

| Opção | Anterior | Próxima |
|:---|:---|:---|
| A | ⬅️ Última Aventura | ➡️ Próxima Aventura |
| B | ⬅️ Caminho Percorrido | ➡️ Próximo Passo |
| C | ⬅️ O Que Já Vivemos | ➡️ O Que Vem a Seguir |

**DECISÃO FINAL:** Opção A aprovada (Última/Próxima Aventura)

---

## 🔥 DELIBERAÇÃO: NORTE ABSOLUTO

> **Pauta:** A palavra "mágica" deve ser usada?

**Atual:**
```
🧭 Norte Absoluto (80%): A maior parte da lição acontece aqui. Manipulação é onde a mágica vive.
```

**Problema levantado pelo Maestro:**
> "Não usamos a palavra mágico, pense sobre isso"

**Deliberação:**

#### Charlotte Mason
> "A educação não é mágica — é trabalho paciente e alegre. 'Mágica' sugere truques, atalhos. Sugiro: 'Manipulação é onde o aprendizado VIVE' ou 'é onde o REAL acontece'."

#### Tolkien (Narrativa)
> "Mágica no sentido de Faërie é aceitável — é maravilhamento, não ilusionismo. Mas se o contexto é educacional, concordo com Charlotte."

#### Design
> "Visualmente, a frase fica mais forte sem 'mágica': 'Manipulação é onde a compreensão nasce.'"

**Propostas de texto alternativo:**

| # | Proposta |
|:---|:---|
| 1 | "Manipulação é onde o aprendizado VIVE" |
| 2 | "80% da lição é TOCAR e FAZER" |
| 3 | "Aqui mora o REAL — toque, conte, sinta" |
| 4 | "A compreensão nasce nas mãos" |

**DECISÃO PRELIMINAR:** Usar proposta #4: "A compreensão nasce nas mãos"

**⚠️ NOTA:** Esta mudança afeta o TEMPLATE, não só o HTML.

---

## 📋 PLANO DE IMPLEMENTAÇÃO FINAL

### Alterações no HTML (MV-S-001)

| # | Linha | O que mudar | Código |
|:---|:---|:---|:---|
| 1 | 81 | Meta tag | `Lição 01 • A Trindade na Palma • ⏱️ 20 min` |
| 2 | 104-112 | Dica do Coração | Reduzir padding para 1rem |
| 3 | 121-127 | Materiais | Remover ⭐ de todos |
| 4 | 136 | Protocolo | Converter para `<ul>` |
| 5 | 137 | Nota de Graça | Verificar `<br>` |
| 6 | 176, 489 | Avatar Portador | 🔥 em vez de PNG |
| 7 | 215 | Local | Adicionar card visual |
| 8 | 401 | Norte Absoluto | "A compreensão nasce nas mãos" |
| 9 | 485 | Fio de Ouro | REMOVER bloco completo |
| 10 | 518-521 | Linkage títulos | Última/Próxima Aventura |
| 11 | 546-550 | CM Quote | Tirar #10, adicionar tradução |

### Alterações no CSS

```css
/* NOVAS CLASSES - Para a Família */
.cm-quote {
    background: #EDE9FE;
    border-left: 4px solid #8B5CF6;
    padding: 1rem;
    border-radius: 0 8px 8px 0;
    margin: 1rem 0;
}
.bruner-quote {
    background: #DBEAFE;
    border-left: 4px solid #3B82F6;
}
.singapore-quote {
    background: #FEF3C7;
    border-left: 4px solid #F59E0B;
}

/* PORTADOR - Tocha */
.portador-icon {
    font-size: 2rem;
    margin-right: 0.5rem;
}
```

### Alterações Futuras (Template Jinja2)

| Arquivo | Mudança |
|:---|:---|
| `licao.j2` | Avatar Portador: PNG → 🔥 |
| `licao.j2` | Adicionar componente de local |
| `licao.j2` | Remover Fio de Ouro |
| `licao.j2` | Reformular Norte Absoluto |
| `licao.j2` | Cores por autor em "Para Família" |
| `macros.j2` | Criar macro `local_card()` |
| `style.css` | Adicionar classes de cores |

### Alterações Futuras (YAML Fonte)

| Arquivo | Mudança |
|:---|:---|
| `_TEMPLATE_V6.yaml` | Remover `fio_de_ouro` do fechamento |
| `_TEMPLATE_V6.yaml` | Reformular `norte_absoluto` |
| Lições | Atualizar `norte_absoluto` texto |

---

## ⏱️ ORDEM DE EXECUÇÃO

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   FASE 1: PROTOTIPAÇÃO (AGORA)                                              │
│   ─────────────────────────────                                             │
│   1. Editar MV-S-001 HTML diretamente                                       │
│   2. Aplicar todas as 11 mudanças                                           │
│   3. Adicionar CSS inline para testar                                       │
│   4. Maestro validar visual no browser                                      │
│                                                                             │
│                         ▼                                                   │
│                                                                             │
│   FASE 2: TRANSFERÊNCIA (APÓS APROVAÇÃO)                                    │
│   ───────────────────────────────────────                                   │
│   1. Migrar mudanças para templates Jinja2                                  │
│   2. Atualizar style.css com novas classes                                  │
│   3. Atualizar _TEMPLATE_V6.yaml se necessário                              │
│                                                                             │
│                         ▼                                                   │
│                                                                             │
│   FASE 3: REBUILD E VALIDAÇÃO                                               │
│   ─────────────────────────────                                             │
│   1. python build/forge.py --fase sementes                                  │
│   2. Verificar TODAS as lições                                              │
│   3. Commit final                                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ❓ PERGUNTAS FINAIS ANTES DE IMPLEMENTAR

1. **Norte Absoluto:** Aprova o texto "A compreensão nasce nas mãos"? Ou prefere outra proposta?

2. **Ordem de implementação:** Posso começar a editar o HTML agora?

---

**Documento atualizado: 16/01/2026 13:20**
**Status: AGUARDANDO APROVAÇÃO FINAL**
