# 📋 Tópicos de Lição — Checklist de Revisão

> **Fonte:** L000 (O Portal do Reino) — Padrão Ouro  
> **Última Atualização:** 05/02/2026  
> **Referência:** `Revisao/01_REFERENCIAS_DE_APOIO/padrao_visual_sementes.md`

Este documento define **TODAS** as seções e elementos obrigatórios de uma lição Sementes, na ordem exata de aparição.

> [!IMPORTANT]
> **Prioridade de Norma (SSOT):** em caso de conflito entre este arquivo e `Revisao/01_REFERENCIAS_DE_APOIO/padrao_visual_sementes.md`, prevalece `padrao_visual_sementes.md` (seção **18**: Estrutura Narrativa & Ordem + Contrato de Tópicos/Subtópicos).
>
> **Nota de compatibilidade:** alguns exemplos deste documento estão em formato legado; use-os como referência histórica, não como regra final.

---

## 🔍 Checklist Rápido (Copie para cada lição)

```markdown
## Revisão L[XXX] — [Título]

### Estrutura Base
- [ ] Contrato canônico T0-T9 completo (ver `padrao_visual_sementes.md` seção 18.1)
- [ ] `<head>`: title, style.css, Google Fonts, Phosphor CDN, favicon
- [ ] `<body class="clima-X">`: clima-0 (L000) ou clima-1 (L001+)
- [ ] Home Button: `ph-house duotone-forest`
- [ ] Header Nav: `ph-plant duotone-forest` + "Sementes"
- [ ] Hero: meta-tag, title, quote, guardian image

### Preparação do Portador
- [ ] Scene Header: `ph-clipboard-text duotone-terra`
- [ ] Dica do Coração: `ph-lightbulb duotone-gold`
- [ ] Materials Box: essencial + opcional
- [ ] "Seu filho vai descobrir": `ph-sparkle duotone-magic`
- [ ] "Segredo do Maravilhamento": `ph-sparkle duotone-magic`
- [ ] "Nota de Graça": `ph-heart duotone-heart`

### Ritual de Entrada
- [ ] Scene Header: `ph-film-strip duotone-magic`
- [ ] Instruction Box: `ph-lamp duotone-gold`
- [ ] Portador Block ÚNICO (Voz Única)
- [ ] Acting Cues em `[ ]` estilo dourado itálico
- [ ] Card do Local com label "Mostrar Card"

### A Jornada
- [ ] H2: `ph-map-trifold duotone-gold`
- [ ] Scene Headers com ícones temáticos
- [ ] Card Container com `rotate-left hover-float`
- [ ] Instruction Box: `ph-hand-pointing duotone-neutral`
- [ ] Script Block com Tom: `(Tom: [Adj] — descrição)`
- [ ] Guardião: Card UMA VEZ por lição

### O Concreto / Momento de Conexão
- [ ] H2/Scene: `ph-wall duotone-terra` ou `ph-cube`
- [ ] Tom sugestivo (não imperativo)
- [ ] Objetivo claro + Sugestões

### Narramos Juntos
- [ ] Scene Header: `ph-chat-circle-dots duotone-terra`
- [ ] Instruction Box: `ph-ear duotone-neutral`
- [ ] Perguntas do Coração (lista)

### Ritual de Fechamento
- [ ] Scene Header: `ph-flag duotone-forest`
- [ ] Fala final do Guardião
- [ ] Portador Block de Fechamento

### Conexão da Jornada
- [ ] Scene Header: `ph-link duotone-indigo`
- [ ] Link clicável para próxima lição
- [ ] Teaser com `ph-arrow-right duotone-gold`

### Sementes para o Dia
- [ ] Scene Header: `ph-plant duotone-forest`
- [ ] Box verde (#F0FDF4)
- [ ] 5 atividades com ícones corretos
- [ ] Frase de fechamento itálica

### Formação do Portador
- [ ] Scene Header: `ph-graduation-cap duotone-terra`
- [ ] "Por que importa": `.cm-box` + `ph-books`
- [ ] "Método CPA": `.bruner-box` + `ph-brain`
- [ ] "Charlotte Mason": `.cm-box` + `ph-feather`
- [ ] "Conexão TGTB": `.tgtb-box` + `ph-link`
- [ ] "Currículo Espiral": `.bruner-box` + `ph-spiral`
- [ ] "Reflexão Espiritual": `.espiritual-box` + `ph-sparkle`
- [ ] "Nota de Graça": `.graca-box` + `ph-heart`
- [ ] "Sementes Continuam": `.sementes-box` + `ph-plant`
- [ ] ❌ Proibido: `<br>` após `<strong>` (usar `<p>`)

### Navigation Footer
- [ ] `.lesson-nav` com botões prev/next
- [ ] Footer com "Matemática Viva"
```

---

## 🏗️ 1. Estrutura HTML Base

### 1.1 `<head>` — Metadados
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Nome da Lição] | Matemática Viva</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700&family=Lora:ital,wght@0,400;0,600;1,400&family=Gloria+Hallelujah&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="icon" href="../favicon.ico" type="image/x-icon">
</head>
```

### 1.2 `<body>` — Classe de Clima
```html
<body class="clima-0">  <!-- L000: Portal -->
<body class="clima-1">  <!-- L001+: Padrão -->
```

### 1.3 Home Button (Fixo)
```html
<a href="../index.html" class="home-btn" title="Voltar ao Dashboard">
    <i class="ph-duotone ph-house duotone-forest"></i>
</a>
```

### 1.4 Lesson Container + Header Navigation
```html
<div class="lesson-container">
    <div class="lesson-header-nav">
        <div style="width: 33%;">
            <a href="MV-S-000_O_PORTAL_DO_REINO.html" class="nav-mini-link">
                <span>←</span> <span>O Portal do Reino</span>
            </a>
        </div>

        <div style="width: 33%; text-align: center;">
            <i class="ph-duotone ph-plant duotone-forest" style="font-size: 1.5rem;"></i>
            <span style="font-family: var(--font-heading); font-weight: 700; color: var(--primary); font-size: 0.9rem; margin-left: 0.5rem;">Sementes</span>
        </div>

        <div style="width: 33%; text-align: right;">
            <a href="MV-S-002_AS_PEDRAS_DA_FORTALEZA.html" class="nav-mini-link" style="justify-content: flex-end;">
                <span>As Pedras da Fortaleza</span> <span>→</span>
            </a>
        </div>
    </div>
```

### 1.5 Hero Section
```html
<header class="lesson-hero">
    <div class="lesson-meta-tag">
        Lição XXX • Título • <i class="ph-duotone ph-timer duotone-carmim"></i> 15-20 min
    </div>
    <h1 class="hero-title">Título da Lição</h1>
    <p class="hero-quote">"Frase de impacto entre aspas"</p>
    <img src="../assets/sementes/guardioes/[nome].png" 
         onError="this.src='../assets/sementes/guardioes/placeholder.png'" 
         alt="[nome]" class="hero-guardian">
</header>
```

### 1.6 Lesson Nav Grid (Opcional)
```html
<nav class="lesson-nav-grid" aria-label="Navegação da Lição">
    <div class="nav-col prev">
        <a href="[anterior].html">← Anterior</a>
    </div>
    <div class="nav-col logo">
        <img src="../assets/icon-sementes.png" alt="Sementes" class="nav-logo-img">
    </div>
    <div class="nav-col next">
        <a href="[proxima].html">[Título] →</a>
    </div>
</nav>
```

---

## 📦 2. Preparação do Portador

### Scene Header
```html
<div class="scene-header">
    <i class="ph-duotone ph-clipboard-text duotone-terra" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Preparação do Portador
</div>
```

### 2.1 Dica do Coração
```html
<div class="instruction-box">
    <i class="ph-duotone ph-lightbulb duotone-gold" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    <div>
        <strong>Dica do Coração:</strong> [Texto explicativo...]
        <br><br>
        O ritual começa quando vocês decidem que começa. <strong>Você é a voz de [Guardião].</strong>
    </div>
</div>
```

### 2.2 Materials Box
```html
<aside class="materials-box" aria-label="Lista de Materiais">
    <p><strong><i class="ph-duotone ph-target duotone-terra"></i> Essencial:</strong></p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>

    <p style="margin-top:1rem;"><strong><i class="ph-duotone ph-package duotone-gold"></i> Se tiver:</strong></p>
    <ul style="color:#6B7280;">
        <li>Item opcional</li>
    </ul>
</aside>
```

### 2.3 Seu filho vai descobrir
```html
<p><strong><i class="ph-duotone ph-sparkle duotone-magic"></i> Seu filho vai descobrir:</strong> 
    [Descrição do que a criança vai aprender/vivenciar]
</p>
```

### 2.4 Segredo do Maravilhamento
```html
<p><strong><i class="ph-duotone ph-sparkle duotone-magic"></i> Segredo do Maravilhamento:</strong>
    Não precisa explicar nada. Apenas <strong>viva a narrativa</strong>. 
    Se a criança perguntar, sorria e diga: "Você vai descobrir...". 
    O <strong>maravilhamento</strong> é mais importante que a compreensão — por enquanto.
</p>
```

### 2.5 Nota de Graça
```html
<p><strong><i class="ph-duotone ph-heart duotone-heart"></i> Nota de Graça:</strong> 
    Se a criança não "entrar" na história hoje, <strong>tudo bem</strong>. 
    A semente foi plantada. Amanhã ela pode brotar.
</p>
```

---

## 🎬 3. Ritual de Entrada

### Scene Header
```html
<div class="scene-header">
    <i class="ph-duotone ph-film-strip duotone-magic" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Ritual de Entrada
</div>
```

### 3.1 Instruction Box (Preparação)
```html
<div class="instruction-box">
    <i class="ph-duotone ph-lamp duotone-gold" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    <div>
        <strong>Preparação:</strong>
        <ul style="margin: 0.5rem 0 0 0; padding-left: 1.2rem; font-size: 0.95rem;">
            <li>Tenha a <strong>Luz Amarela</strong> à mão.</li>
            <li>Sentem-se confortavelmente.</li>
            <li>Ao acender a luz, leia as falas abaixo.</li>
        </ul>
    </div>
</div>
```

### 3.2 Portador Block (MONOBLOCO — Lei da Voz Única)
```html
<div class="script-persona-block portador-block">
    <div class="script-avatar-icon">
        <i class="ph-duotone ph-fire duotone-carmim"></i>
    </div>
    <div class="script-content">
        <div class="script-header">
            <span class="script-name">Portador da Tocha</span>
        </div>
        <div class="script-text">
            <p>"Luz de fora acalma.</p>
            <p>Sol de dentro acende.</p>
            <p>Respirem... Estamos no Reino."</p>

            <!-- Acting Cue Interno -->
            <p style="color: var(--accent-gold); font-style: italic; margin-top: 1rem;">
                [Feche os olhos. Respire fundo...]
            </p>

            <p>"Quando você abrir os olhos, estaremos em um lugar muito especial..."</p>

            <!-- VISUAL REVEAL -->
            <div class="card-container" style="margin: 1.5rem 0;">
                <p class="local-label">Mostrar Card</p>
                <img src="../assets/cards/locais/[local].png" 
                     style="width: 100%; max-width: 400px; border-radius: 12px; 
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 4px solid #FFF;" 
                     alt="[Nome do Local]">
                <p style="margin-top: 0.5rem; font-weight: 700; font-size: 1.1rem; 
                          color: var(--primary); text-align: center;">
                    ✨ [Nome do Local] ✨
                </p>
            </div>

            <!-- IMMERSION -->
            <p>"[Descrição sensorial do ambiente...]"</p>
        </div>
    </div>
</div>
```

---

## 🗺️ 4. A Jornada

### H2 Header
```html
<h2><i class="ph-duotone ph-map-trifold duotone-gold" style="margin-right:0.5rem;"></i> A Jornada</h2>
```

### 4.1 Scene Card (por cena)
```html
<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-[icone] duotone-[cor]" style="font-size:1.5rem; margin-right:0.5rem;"></i>
        [Título da Cena]
    </div>

    <!-- Card Container -->
    <div class="card-container">
        <p class="local-label">Mostrar Card</p>
        <img src="../assets/cards/guardioes/[guardiao].png" 
             class="card-visual-asset rotate-left hover-float"
             onError="this.src='../assets/cards/guardioes/placeholder.png'" 
             alt="[Descrição]">
    </div>

    <!-- Instruction Box -->
    <div class="instruction-box">
        <i class="ph-duotone ph-hand-pointing duotone-neutral rotate-90" 
           style="font-size:1.5rem; margin-right:0.5rem;"></i>
        <div>[Instrução de ação para o pai]</div>
    </div>

    <!-- Script Block -->
    <div class="script-persona-block">
        <img src="../assets/cards/guardioes/[guardiao].png" class="script-avatar" alt="[nome]">
        <div class="script-content">
            <div class="script-header">
                <span class="script-name">[Nome]</span>
                <span style="font-style: normal;">
                    <i class="ph-duotone ph-[icone-tom] duotone-[cor]"></i>
                </span>
                (Tom: [Adjetivo] — [Descrição de como atuar])
            </div>
            <div class="script-text">
                <p>"[Diálogo...]"</p>
                <p>[Acting cue inline]</p>
            </div>
        </div>
    </div>
</div>
```

### 4.2 Tabela de Tons por Personagem

| Personagem | Tom | Descrição | Ícone |
|------------|-----|-----------|-------|
| **Melquior** | Acolhedor | Sorriso na voz, braços abertos | `ph-smiley duotone-gold` |
| | Nobre | Postura ereta, voz profunda mas gentil | `ph-shield-check duotone-forest` |
| | Reverente | Voz calma, ritmo lento, como oração | `ph-hands-praying duotone-terra` |
| | Esperançoso | Olhar nos olhos, transmitir confiança | `ph-sun duotone-gold` |
| **Noé** | Respeitoso | Admiração, levemente sussurrado | `ph-hands-praying duotone-terra` |
| | Sábio | Pausado, contemplativo | `ph-eye duotone-terra` |
| **Celeste** | Animado | Entusiasmo, brilho nos olhos | `ph-confetti duotone-gold` |
| | Curioso | Farejando mistérios | `ph-magnifying-glass duotone-indigo` |
| **Bernardo** | Firme | Voz segura, grave, com peso | `ph-shield-check duotone-forest` |
| | Encorajador | "Mais uma vez. Comigo." | `ph-heart duotone-heart` |
| **Íris** | Delicado | Suave, leve, como asa de borboleta | `ph-butterfly duotone-forest` |
| | Maravilhado | Descobrindo beleza | `ph-sparkle duotone-magic` |
| **Portador** | (ritual) | Voz do Narrador | `ph-fire duotone-carmim` |

---

## 🧱 5. O Concreto / Momento de Conexão

### H2 + Scene Header
```html
<h2><i class="ph-duotone ph-wall duotone-terra" style="margin-right:0.5rem;"></i> O Concreto</h2>

<div class="scene-header">
    <i class="ph-duotone ph-wall duotone-terra" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Atividade Concreta
</div>
```

### 5.1 Instruction Box
```html
<div class="instruction-box">
    <i class="ph-duotone ph-heart duotone-heart" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    <div>
        <p style="margin-bottom: 0.75rem; color: #374151;">
            <strong>Objetivo:</strong> [Descrição do objetivo]
        </p>

        <p style="margin-bottom: 0.5rem;"><strong>Sugestões:</strong></p>
        <ul style="padding-left: 1.2rem; line-height: 1.8; margin-bottom: 0.75rem;">
            <li><strong>Se tiver [X]:</strong> [Sugestão]</li>
            <li><strong>Se não tiver:</strong> [Alternativa]</li>
        </ul>

        <p style="font-size: 0.9rem; color: #6B7280; font-style: italic;">
            Quando estiverem prontos, sigam para <strong>Narramos Juntos</strong>.
        </p>
    </div>
</div>
```

---

## 💬 6. Narramos Juntos

### Scene Header
```html
<div class="scene-header">
    <i class="ph-duotone ph-chat-circle-dots duotone-terra" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Narramos Juntos
</div>
```

### 6.1 Instruction Box
```html
<div class="instruction-box">
    <i class="ph-duotone ph-ear duotone-neutral" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    <div>
        Não force perguntas hoje.<br>
        Se a criança quiser falar, ouça.<br>
        Se preferir silêncio, respeite. O coração guardou.
    </div>
</div>
```

### 6.2 Script Block + Perguntas
```html
<div class="script-persona-block">
    <img src="../assets/cards/guardioes/[guardiao].png" class="script-avatar" alt="[nome]">
    <div class="script-content">
        <div class="script-header">
            <span class="script-name">[Nome]</span>
        </div>
        <div class="script-text">
            "[Pergunta de reflexão]"
        </div>
    </div>
</div>

<p><strong>Perguntas do Coração:</strong></p>
<ul style="margin-left:1.5rem; margin-top:0.5rem;">
    <li>Pergunta 1?</li>
    <li>Pergunta 2?</li>
    <li>Pergunta 3?</li>
    <li>Pergunta 4?</li>
</ul>
```

---

## 🏁 7. Ritual de Fechamento

### Scene Header
```html
<div class="scene-header">
    <i class="ph-duotone ph-flag duotone-forest" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Ritual de Fechamento
</div>
```

### 7.1 Fala do Guardião + Portador
```html
<!-- Guardião -->
<div class="script-persona-block">
    <img src="../assets/cards/guardioes/[guardiao].png" class="script-avatar" alt="[nome]">
    <div class="script-content">
        <div class="script-header">
            <span class="script-name">[Nome]</span>
            <span style="font-style: normal;"><i class="ph-duotone ph-sun duotone-gold"></i></span>
            (Tom: Esperançoso)
        </div>
        <div class="script-text">
            "[Despedida do Guardião...]"
        </div>
    </div>
</div>

<!-- Portador -->
<div class="script-persona-block portador-block">
    <div class="script-avatar-icon">
        <i class="ph-duotone ph-fire duotone-carmim"></i>
    </div>
    <div class="script-content">
        <div class="script-header">
            <span class="script-name">Portador da Tocha</span>
        </div>
        <div class="script-text">
            "A Luz se apaga, mas o brilho fica no coração."<br>
            "O Reino descansa. Até amanhã, Herdeiro."
        </div>
    </div>
</div>
```

---

## 🔗 8. Conexão da Jornada

### Scene Header
```html
<div class="scene-header">
    <i class="ph-duotone ph-link duotone-indigo" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Conexão da Jornada
</div>
```

### 8.1 Link Clicável
```html
<div onclick="window.location.href='[proxima].html'" style="cursor: pointer;">
    <p><strong><i class="ph-duotone ph-arrow-right duotone-gold"></i> Próxima Aventura:</strong> 
       [Teaser da próxima lição]
    </p>
    <div style="margin-top:0.5rem; text-align:right;">
        <span style="font-size:0.85rem; color:#4B5563; background:#F3F4F6; 
                     padding:0.25rem 0.75rem; border-radius:1rem;">
            Ir para [Título] →
        </span>
    </div>
</div>
```

---

## 🌱 9. Sementes para o Dia

### Scene Header
```html
<div class="scene-header">
    <i class="ph-duotone ph-plant duotone-forest" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Sementes para o Dia
</div>
```

### 9.1 Box Verde
```html
<div class="instruction-box" style="background-color: #F0FDF4; border-left-color: #166534;">
    <div>
        <p style="margin-top: 0.5rem; font-size: 0.95rem; color: #374151;">
            Ao longo do dia, a criança pode continuar vivendo no Reino.
            Estas atividades são <strong>opcionais</strong> — a lição já está completa.
        </p>

        <ul style="margin-top: 0.75rem; padding-left: 1.2rem; line-height: 1.8;">
            <li><strong><i class="ph-duotone ph-magnifying-glass duotone-forest"></i> [Exploração]:</strong> [Descrição]</li>
            <li><strong><i class="ph-duotone ph-mask-happy duotone-indigo"></i> [Dramatização]:</strong> [Descrição]</li>
            <li><strong><i class="ph-duotone ph-pencil-simple duotone-terra"></i> [Criação]:</strong> [Descrição]</li>
            <li><strong><i class="ph-duotone ph-chat-circle duotone-carmim"></i> [Narração]:</strong> [Descrição]</li>
            <li><strong><i class="ph-duotone ph-moon-stars duotone-sky"></i> [Reflexão Noturna]:</strong> [Descrição]</li>
        </ul>

        <p style="font-size: 0.85rem; color: #6B7280; margin-top: 0.75rem; font-style: italic;">
            "O Reino não acaba quando a lição termina. Ele vive no coração do Herdeiro."
            — Matemática Viva
        </p>
    </div>
</div>
```

### 9.2 Tabela de Ícones por Atividade

| # | Tipo | Ícone | Cor |
|---|------|-------|-----|
| 1 | Exploração | `ph-magnifying-glass` | forest |
| 2 | Dramatização | `ph-mask-happy` | indigo |
| 3 | Criação | `ph-pencil-simple` | terra |
| 4 | Narração | `ph-chat-circle` | carmim |
| 5 | Reflexão | `ph-moon-stars` | sky |

---

## 🎓 10. Formação do Portador

### Scene Header
```html
<div class="scene-header">
    <i class="ph-duotone ph-graduation-cap duotone-terra" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Formação do Portador
</div>
```

### 10.1 Por que isso importa
```html
<div class="cm-box">
    <strong><i class="ph-duotone ph-books duotone-forest"></i> Por que isso importa:</strong>

    <p style="margin-top: 0.75rem;">[Contexto pedagógico...]</p>
    <p style="margin-top: 0.5rem;">[Explicação...]</p>
    
    <ul style="margin: 0.5rem 0 0 1.5rem; line-height: 1.6;">
        <li><strong>[Item]</strong>: [Descrição]</li>
    </ul>
</div>
```

### 10.2 Método CPA (Bruner)
```html
<div class="bruner-box">
    <strong><i class="ph-duotone ph-brain duotone-terra"></i> Método CPA (Jerome Bruner):</strong>
    
    <ul style="margin:0.5rem 0 0 1.5rem;">
        <li><strong>Concreto:</strong> [Descrição]</li>
        <li><strong>Pictórico:</strong> [Descrição]</li>
        <li><strong>Abstrato:</strong> [Descrição]</li>
    </ul>

    <span style="color:#6B7280; font-size:0.9rem;">
        No Ciclo Sementes, quase tudo é <strong>concreto</strong>.
    </span>
</div>
```

### 10.3 Charlotte Mason
```html
<div class="cm-box">
    <strong><i class="ph-duotone ph-feather duotone-forest"></i> Princípio Charlotte Mason:</strong>

    <p style="margin-top: 0.5rem; font-style: italic; color: #4B5563;">
        "[Citação original em inglês]"
    </p>

    <p style="margin-top: 0.25rem; font-weight: 600; color: #5B21B6; font-size: 0.95rem;">
        "[Tradução em português]"
    </p>

    <p style="margin-top: 0.5rem; color: #6B7280;">
        [Explicação e aplicação...]
    </p>
</div>
```

### 10.4 Conexão TGTB
```html
<div class="tgtb-box">
    <strong><i class="ph-duotone ph-link duotone-indigo"></i> Conexão TGTB:</strong>

    <p style="margin-top: 0.5rem; color: #92400E;">
        [Referência ao currículo TGTB...]
    </p>
</div>
```

### 10.5 Currículo Espiral
```html
<div class="bruner-box">
    <strong><i class="ph-duotone ph-spiral duotone-forest"></i> Currículo em Espiral (Bruner):</strong>

    <ul style="margin: 0.5rem 0 0 1.5rem; line-height: 1.6;">
        <li><strong>Agora:</strong> [O que fazemos nesta lição]</li>
        <li><strong>Depois:</strong> [Como revisitaremos no futuro]</li>
    </ul>

    <p style="margin-top: 0.5rem; color: #6B7280; font-size: 0.9rem;">
        [Observação...]
    </p>
</div>
```

### 10.6 Reflexão Espiritual
```html
<div class="espiritual-box">
    <strong><i class="ph-duotone ph-sparkle duotone-gold"></i> Reflexão Espiritual:</strong>

    <p style="margin-top: 0.5rem; color: #166534; font-style: italic;">
        "[Versículo ou frase inspiradora]"
    </p>

    <p style="margin-top: 0.5rem; color: #166534;">
        [Reflexão teológica...]
    </p>
</div>
```

### 10.7 Nota de Graça
```html
<div class="graca-box">
    <strong><i class="ph-duotone ph-heart duotone-heart"></i> Nota de Graça:</strong>

    <p style="margin-top: 0.5rem;">
        [Encorajamento para os pais...]
    </p>
</div>
```

### 10.8 Sementes Continuam
```html
<div class="sementes-box">
    <strong><i class="ph-duotone ph-plant duotone-forest"></i> As Sementes Continuam:</strong>

    <p style="margin-top: 0.5rem;">
        [Explicação sobre as atividades opcionais...]
    </p>

    <p style="margin-top: 0.75rem;"><strong>Por que isso funciona?</strong></p>
    <ul style="margin: 0.5rem 0 0 1.5rem; line-height: 1.6;">
        <li><strong>Reforço Natural:</strong> [Descrição]</li>
        <li><strong>Desejo Próprio:</strong> [Descrição]</li>
        <li><strong>Conexão Familiar:</strong> [Descrição]</li>
        <li><strong>Restauração do Pai:</strong> [Descrição]</li>
    </ul>

    <p style="margin-top: 0.75rem; font-size: 0.9rem; color: #6B7280; font-style: italic;">
        "O medo acaba em você. O encantamento começa neles."<br>
        "A cada lição, o filho aprende e o pai é restaurado." — Matemática Viva
    </p>
</div>
```

---

## 🧭 11. Navigation Footer

```html
<nav class="lesson-nav">
    <a href="[anterior].html" class="nav-btn prev">
        <span class="nav-label">← Anterior</span>
        <span class="nav-title">[Título Anterior]</span>
    </a>

    <a href="[proxima].html" class="nav-btn next">
        <span class="nav-label">Próxima →</span>
        <span class="nav-title">[Título Próxima]</span>
    </a>
</nav>

<footer style="text-align: center; margin-top: 4rem; color: #A8A29E; font-size: 0.8rem;">
    Matemática Viva • Forjado com Estilo e Propósito
</footer>
```

---

## ✅ Regras Globais de Conformidade

| Regra | Verificação | Seção Padrão |
|-------|-------------|--------------|
| Emojis estruturais | ❌ Zero (usar Phosphor) | §7 |
| Labels de card | "Mostrar Card" (não "Visualizar") | §11.1 |
| Capitalização | Guardiões sempre capitalizados | §10.2 |
| Tom | Sem "Shhh...", sem imperativo | §10.4, §19.2 |
| Cards | Guardião aparece UMA VEZ | §6 |
| Portador Block | `ph-fire duotone-carmim` + `.script-avatar-icon` | §1 |
| Boxes | Sem `<br>`, usar `<p>` com margins | §20.1 |
| North Star | ❌ Nunca usar (usar "Matemática Viva") | §21.2 |
| Acting Cues | Em `[ ]` com estilo dourado itálico | §5 |
| Voz Única | Portador não sai de cena no Ritual | §4 |
| Separação Ritual/Jornada | Guardião após "A Jornada" | §4.1 |

---

## 🎨 Paleta de Cores Litúrgicas

| Nome | Classe | Hex | Uso Principal |
|------|--------|-----|---------------|
| Carmim | `duotone-carmim` | #960018 | Portador, Paixão |
| Gold | `duotone-gold` | #F59E0B | Melquior, Luz, Glória |
| Forest | `duotone-forest` | #166534 | Sementes, Natureza, Vida |
| Terra | `duotone-terra` | #92400E | Noé, Bastidores, Base |
| Sky | `duotone-sky` | #0284C7 | Bruner, Reflexão |
| Indigo | `duotone-indigo` | #4F46E5 | Celeste, Magia |
| Magic | `duotone-magic` | (variável) | Maravilhamento |
| Heart | `duotone-heart` | (variável) | Graça, Amor |
| Neutral | `duotone-neutral` | (variável) | Instruções gerais |

---

## 🤖 Protocolo IA — Sanity Check

### Arquivos de Referência (Ordem)
1. 📜 `Revisao/01_REFERENCIAS_DE_APOIO/padrao_visual_sementes.md` — Regras
2. 💎 `site/sementes/lab_icones.html` — Assets & Ícones
3. 🧱 `site/sementes/style.css` — CSS

### Antes de dizer "Terminei"
1. **Ícones:** `ph-graduation-cap` em Formação? Sementes Box único?
2. **CPA:** Conteúdo abstrato em Sementes? → **VETO**
3. **Tom:** "Faça isso" ou "Convide a criança..."?
4. **Boxes:** Limpas, sem `<br>` após `<strong>`, parágrafos elegantes?

> **Lembrete:** "Você não está editando HTML. Você está construindo a catedral onde memórias entre pai e filho serão forjadas."

---

> **Uso:** Este checklist deve ser usado para revisar TODAS as lições do ciclo Sementes antes de publicação.
