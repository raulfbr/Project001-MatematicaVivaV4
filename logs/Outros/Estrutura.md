# ESTRUTURA CANÔNICA DE UMA LIÇÃO SEMENTES

> **Fonte:** Análise das Lições 000-004 do site/sementes
> **Data:** 2026-02-17
> **Objetivo:** Documentar o esqueleto perfeito para criar/auditar lições

---

## ESTRUTURA HTML COMPLETA

### 1. HEAD Section
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[TÍTULO] | Matemática Viva</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700&family=Lora:ital,wght@0,400;0,600;1,400&family=Gloria+Hallelujah&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="icon" href="../favicon.ico" type="image/x-icon">
</head>
```

**Elementos obrigatórios:**
- Charset UTF-8
- Viewport responsivo
- CSS isolado de Sementes (style.css)
- Google Fonts: Outfit, Lora, Gloria Hallelujah
- Phosphor Icons (duotone)
- Favicon

---

### 2. BODY E CLASSES DE CLIMA
```html
<body class="clima-0">  <!-- L000: clima-0 (especial) -->
<body class="clima-1">  <!-- L001+: clima-1 (padrão) -->
```

**Regra:** L000 usa `clima-0` (dourado especial), demais lições usam `clima-1`

---

### 3. HERO SECTION
```html
<header class="lesson-hero">
    <div class="lesson-meta-tag">Lição XXX • [TÍTULO] • ⏱️ 15-20 min</div>
    <h1 class="hero-title">[TÍTULO DA LIÇÃO]</h1>
    <p class="hero-quote">"[CITAÇÃO TEMÁTICA]"</p>
    <img src="../assets/sementes/guardioes/[GUARDIÃO].png" 
         onError="this.src='../assets/sementes/guardioes/placeholder.png'"
         alt="[NOME GUARDIÃO]" class="hero-guardian">
</header>
```

**Elementos:**
- **meta-tag**: Número da lição, título, tempo estimado
- **hero-title**: Título completo da lição
- **hero-quote**: Citação temática (frase do Guardião ou conceito)
- **hero-guardian**: Imagem do Guardião principal da lição

---

### 4. NAVEGAÇÃO ENTRE LIÇÕES
```html
<nav class="lesson-header-nav">
    <div style="width: 33%;">
        <a href="[LIÇÃO ANTERIOR].html" class="nav-mini-link">
            <span>←</span> <span>[Título Anterior]</span>
        </a>
    </div>
    <div style="width: 33%; text-align: center;">
        <i class="ph-duotone ph-plant duotone-forest"></i>
        <span>Sementes</span>
    </div>
    <div style="width: 33%; text-align: right;">
        <a href="[PRÓXIMA LIÇÃO].html" class="nav-mini-link">
            <span>[Título Próximo]</span> <span>→</span>
        </a>
    </div>
</nav>
```

**Regra:** Sempre link para anterior/próxima, exceto L000 (apenas próxima)

---

## SEÇÕES PRINCIPAIS (scene-card)

### 5. PREPARAÇÃO DO PORTADOR
```html
<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-clipboard-text duotone-terra"></i>
        Preparação do Portador
    </div>
    
    <!-- FOCO DA LIÇÃO -->
    <div style="text-align: center; color: #6B7280; font-style: italic;">
        [Foco: Números X a Y e Conceito]
    </div>
    
    <!-- DICA DO CORAÇÃO -->
    <div class="instruction-box">
        <i class="ph-duotone ph-lightbulb duotone-gold"></i>
        <div>
            <strong>Dica do Coração:</strong> [Mensagem de encorajamento para o pai]
        </div>
    </div>
    
    <!-- MATERIAIS -->
    <aside class="materials-box">
        <p><strong>🎯 Essencial:</strong></p>
        <ul>
            <li>[Item 1] (quantidade)</li>
            <li>[Item 2] (quantidade)</li>
        </ul>
        <p><strong>📦 Se tiver:</strong></p>
        <ul style="color:#6B7280;">
            <li>[Item opcional]</li>
        </ul>
    </aside>
    
    <!-- DESCORBERTAS -->
    <p><strong>🌟 Seu filho vai descobrir:</strong></p>
    <ul>
        <li>[Descoberta conceitual 1]</li>
        <li>[Descoberta conceitual 2]</li>
    </ul>
    
    <!-- SEGREDO DO MARAVILHAMENTO -->
    <p><strong>✨ Segredo do Maravilhamento:</strong>
        [Dica de como criar o momento "uau"]
    </p>
    
    <!-- PROTOCOLO DE IMPECABILIDADE -->
    <p><strong>🛡️ Protocolo de Impecabilidade:</strong>
        [Regra prática de execução]
    </p>
    
    <!-- NOTA DE GRAÇA -->
    <p><strong>🕊️ Nota de Graça:</strong>
        [Permissão para errar sem culpa]
    </p>
</div>
```

**Elementos obrigatórios:**
1. **Foco da Lição**: O que será ensinado (em itálico, centralizado)
2. **Dica do Coração**: Encorajamento para o pai
3. **Materiais**: Lista Essencial + Se tiver
4. **Descobertas**: O que a criança vai aprender
5. **Segredo do Maravilhamento**: Como criar encantamento
6. **Protocolo de Impecabilidade**: Regras de execução
7. **Nota de Graça**: Permissão para imperfeição

---

### 6. RITUAL DE ENTRADA
```html
<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-film-strip duotone-magic"></i>
        Ritual de Entrada
    </div>
    
    <!-- BASTIDORES -->
    <div class="instruction-box">
        <i class="ph-duotone ph-lamp duotone-gold"></i>
        <div>
            <strong>Bastidores:</strong> [Ambiente físico - tapete, luz, silêncio]
        </div>
    </div>
    
    <!-- MONOBLOCO DO PORTADOR -->
    <div class="script-persona-block portador-block">
        <div class="script-avatar-icon">
            <i class="ph-duotone ph-fire duotone-carmim"></i>
        </div>
        <div class="script-content">
            <div class="script-header">
                <span class="script-name">Portador da Tocha</span>
            </div>
            <div class="script-text">
                <p>"Viajante, feche os olhos. Respire fundo três vezes..."</p>
                <p>[Transição para o local do Reino]</p>
                <p class="acting-cue">[Pausa dramática. Descrição sensorial.]</p>
                <p>[Descrição do ambiente - cheiro, som, luz]</p>
                <p>"Pronto?"</p>
            </div>
        </div>
    </div>
    
    <!-- CARD DO LOCAL -->
    <div style="text-align:center; margin-top:2rem;">
        <p class="local-label">Mostrar Card</p>
        <img src="../assets/cards/locais/[LOCAL].png"
             class="card-visual-asset rotate-left hover-float"
             alt="[Nome do Local]">
    </div>
</div>
```

**Elementos:**
1. **Bastidores**: Preparação física do ambiente
2. **Portador da Tocha**: Monobloco com script de transição
3. **Card do Local**: Imagem do local onde a história acontece

**Padrão do Ritual:**
- Respiração (3 vezes)
- Transição ("não estaremos mais em casa")
- Descrição sensorial (cheiro, som, luz)
- Pergunta de engajamento ("Pronto?")

---

### 7. A JORNADA (Múltiplas Cenas)
```html
<h2><i class="ph-duotone ph-map-trifold duotone-gold"></i> A Jornada</h2>

<!-- CENA 1 -->
<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-[ÍCONE] duotone-[COR]"></i>
        [Título da Cena]
    </div>
    
    <!-- CARD DO GUARDIÃO -->
    <div style="text-align:center; margin-bottom:2rem;">
        <p class="local-label">Mostrar Card</p>
        <img src="../assets/cards/guardioes/[GUARDIÃO].png"
             class="card-visual-asset rotate-left hover-float"
             alt="Card [Guardião]">
    </div>
    
    <!-- INSTRUÇÃO -->
    <div class="instruction-box">
        <i class="ph-duotone ph-hand-pointing duotone-neutral"></i>
        <div>
            [Instrução para o pai - o que fazer/mostrar]
        </div>
    </div>
    
    <!-- DIÁLOGO DO GUARDIÃO -->
    <div class="script-persona-block">
        <img src="../assets/cards/guardioes/[GUARDIÃO].png" class="script-avatar" alt="[Guardião]">
        <div class="script-content">
            <div class="script-header">
                <span class="script-name">[Nome Guardião]</span>
                <span style="font-style: normal;"><i class="ph-duotone ph-[ÍCONE] duotone-[COR]"></i></span>
                (Tom: [DESCRIÇÃO DO TOM])
            </div>
            <div class="script-text">
                <p>"[Diálogo do Guardião]"</p>
                <p>[Acting Cue em colchetes]</p>
                <p>"[Mais diálogo]"</p>
            </div>
        </div>
    </div>
</div>

<!-- Repetir para cada cena da jornada -->
```

**Estrutura de cada Cena:**
1. **scene-header**: Título da cena com ícone temático
2. **Card do Guardião**: Com "Mostrar Card" e rotação
3. **instruction-box**: O que o pai deve fazer
4. **script-persona-block**: Diálogo do Guardião com tom e acting cues

**Padrão de Tom:**
```
(Tom: [ADJETIVO] — [DESCRIÇÃO FÍSICA])
```
Exemplos:
- `(Tom: Acolhedor — Sorriso na voz, braços abertos.)`
- `(Tom: Animado — Com entusiasmo, sorrindo, e brilho nos olhos!)`
- `(Tom: Firme — Voz segura, grave, com peso.)`
- `(Tom: Reverente — Voz calma, ritmo lento, como uma oração.)`

---

### 8. O CONCRETO
```html
<h2><i class="ph-duotone ph-wall duotone-terra"></i> O Concreto</h2>

<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-wall duotone-terra"></i>
        Atividade Concreta
    </div>
    
    <div class="instruction-box">
        <i class="ph-duotone ph-clipboard-text duotone-neutral"></i>
        <div>
            <strong>Passo a Passo:</strong>
            <ol>
                <li>
                    [Ação 1]
                    <br><em>Fala sugerida: "[FALA]"</em>
                </li>
                <li>
                    [Ação 2]
                    <br><em>Fala sugerida: "[FALA]"</em>
                </li>
                <li>
                    [Ação 3]
                    <br><em>Fala sugerida: "[FALA]"</em>
                </li>
            </ol>
        </div>
    </div>
</div>
```

**Elementos:**
- Título "Atividade Concreta"
- Passo a passo numerado
- Fala sugerida em itálico para cada passo

---

### 9. NARRAMOS JUNTOS
```html
<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-chat-circle-text duotone-indigo"></i>
        Narramos Juntos
    </div>
    
    <div class="instruction-box">
        <i class="ph-duotone ph-question duotone-indigo"></i>
        <div>
            <strong>Perguntas para a criança narrar:</strong>
            <ul>
                <li>"Me conta, quantos [OBJETOS] o [GUARDIÃO] tinha?"</li>
                <li>"O que aconteceu quando [EVENTO]?"</li>
                <li>"Qual número você mais gostou de descobrir hoje?"</li>
            </ul>
        </div>
    </div>
</div>
```

**Regra:** Perguntas abertas, sem "certo/errado". Foco em fazer a criança recontar.

---

### 10. RITUAL DE FECHAMENTO
```html
<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-sun-horizon duotone-gold"></i>
        Ritual de Fechamento
    </div>
    
    <!-- INSTRUÇÃO -->
    <div class="instruction-box">
        <i class="ph-duotone ph-hand-pointing duotone-neutral"></i>
        <div>
            [Instrução para encerramento - guardar materiais, apagar luz]
        </div>
    </div>
    
    <!-- DESPEDIDA DO GUARDIÃO -->
    <div class="script-persona-block">
        <img src="../assets/cards/guardioes/[GUARDIÃO].png" class="script-avatar" alt="[Guardião]">
        <div class="script-content">
            <div class="script-header">
                <span class="script-name">[Nome Guardião]</span>
            </div>
            <div class="script-text">
                <p>"[Frase de despedida]"</p>
                <p>"O Reino vive em você."</p>
            </div>
        </div>
    </div>
</div>
```

**Elementos:**
- Instrução de encerramento
- Despedida do Guardião
- Frase canônica: "O Reino vive em você."

---

### 11. FORMAÇÃO DO PORTADOR
```html
<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-graduation-cap duotone-forest"></i>
        Formação do Portador
    </div>
    
    <div class="instruction-box" style="background-color: #F0FDF4; border-left-color: #15803D;">
        <i class="ph-duotone ph-strategy duotone-forest"></i>
        <div>
            <strong>Estratégia do Mestre:</strong> [Título da estratégia]
            <p style="margin-top:0.5rem; color:#374151;">
                [Explicação pedagógica profunda]
            </p>
            <p style="margin-top:0.5rem; color:#374151;">
                <strong>Ação:</strong> [Como aplicar na prática]
            </p>
        </div>
    </div>
</div>
```

**Elementos:**
- Título "Formação do Portador"
- Estratégia do Mestre com explicação pedagógica
- Ação prática para o pai

---

## ÍCONES PHOSPHOR POR SEÇÃO

| Seção | Ícone | Cor Duotone |
|-------|-------|-------------|
| Preparação do Portador | `ph-clipboard-text` | `duotone-terra` |
| Ritual de Entrada | `ph-film-strip` | `duotone-magic` |
| A Jornada | `ph-map-trifold` | `duotone-gold` |
| O Concreto | `ph-wall` | `duotone-terra` |
| Narramos Juntos | `ph-chat-circle-text` | `duotone-indigo` |
| Ritual de Fechamento | `ph-sun-horizon` | `duotone-gold` |
| Formação do Portador | `ph-graduation-cap` | `duotone-forest` |

**Ícones de Guardião:**
- Melquior: `ph-crown` (gold)
- Noé: `ph-eyeglasses` (terra)
- Celeste: `ph-star-four` (magic)
- Bernardo: `ph-paw-print` (forest)
- Íris: `ph-bird` (magic)

---

## CHECKLIST DE VALIDAÇÃO

### Estrutural
- [ ] HEAD completo (charset, viewport, CSS, fonts, icons, favicon)
- [ ] BODY com classe de clima correta
- [ ] HERO Section (meta-tag, título, citação, guardião)
- [ ] Navegação entre lições
- [ ] Preparação do Portador (7 elementos)
- [ ] Ritual de Entrada (bastidores + monobloco + local)
- [ ] A Jornada (múltiplas cenas com cards)
- [ ] O Concreto (passo a passo)
- [ ] Narramos Juntos (perguntas abertas)
- [ ] Ritual de Fechamento
- [ ] Formação do Portador

### Narrativo
- [ ] Tom indicado em cada bloco de fala
- [ ] Acting Cues em colchetes
- [ ] Cards apresentados com "Mostrar Card"
- [ ] Instruction Box com orientações claras
- [ ] Frase canônica de encerramento

### Pedagógico
- [ ] Dica do Coração presente
- [ ] Materiais listados (Essencial + Se tiver)
- [ ] Segredo do Maravilhamento
- [ ] Protocolo de Impecabilidade
- [ ] Nota de Graça

---

## VARIAÇÕES POR TIPO DE LIÇÃO

### Lição de Introdução (L000)
- `clima-0` (dourado especial)
- Apresenta todos os 5 Guardiões
- Sem navegação anterior
- Mais longa (20-25 min)

### Lição Padrão (L001+)
- `clima-1` (padrão)
- 1 Guardião principal
- Navegação completa
- 15-20 min

### Lição de Celebração (L020, L025)
- Estrutura especial de revisão
- Múltiplos Guardiões
- Atividade de síntese

---

## PRÓXIMOS PASSOS

1. Usar este esqueleto para auditar lições existentes
2. Identificar lacunas em cada lição
3. Padronizar estrutura em todas as lições
4. Criar template HTML reutilizável
5. Documentar variações por tipo de lição
