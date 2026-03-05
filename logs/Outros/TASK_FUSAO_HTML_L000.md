# TASK: Fusão HTML da Lição 000 (O Portal do Reino)

> **Data:** 18/02/2026
> **Status:** PRONTO PARA EXECUÇÃO
> **Modo Alvo:** Code (geração de HTML)

---

## 1. OBJETIVO

Gerar um arquivo HTML completo e visualmente impecável da **Lição 000 - O Portal do Reino**, fundindo:
- **Narrativa rica** do YAML existente (`curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml`)
- **Estrutura QA** do YAML gerado (`logs/L000_PORTAL_REINO_GERADO.yaml`)
- **Estilo visual** do CSS (`curriculo/_SISTEMA/TEMPLATES/style.css`)
- **Padrões HTML** do guia visual (`Revisao/padrao_visual_sementes.md` e `Revisao/topicos_licao_revisao.md`)

---

## 2. FONTES SSOT

### 2.1 Conteúdo Narrativo (Primário)
| Arquivo | O que fornece |
|---------|---------------|
| `curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml` | Narrativa completa, diálogos de Melquior, apresentação dos 5 Guardiões, backstory do Reino, frases canônicas |
| `LORE/guardioes.yaml` | Dados visuais dos Guardiões (nomes, cores, emojis, frases) |
| `LORE/locais.yaml` | Descrição do Jardim Central (atmosfera sensorial) |
| `LORE/climas.yaml` | Clima "ensolarado" (descrição sensorial) |

### 2.2 Estrutura Visual (Primário)
| Arquivo | O que fornece |
|---------|---------------|
| `curriculo/_SISTEMA/TEMPLATES/style.css` | CSS completo com variáveis, componentes, animações |
| `Revisao/padrao_visual_sementes.md` | Padrão visual obrigatório (avatar, cards, acting cues) |
| `Revisao/topicos_licao_revisao.md` | Checklist de seções HTML, snippets de código |

### 2.3 Validação (Referência)
| Arquivo | O que fornece |
|---------|---------------|
| `logs/L000_PORTAL_REINO_GERADO.yaml` | Auditoria QA, evidências de validação |
| `LORE/north_star.yaml` | Princípios CM, estrutura de comunicação |
| `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md` | Objetivos pedagógicos |

---

## 3. ESPECIFICAÇÃO TÉCNICA

### 3.1 Estrutura HTML Obrigatória

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <!-- Metadados -->
    <!-- Google Fonts: Merriweather, Inter -->
    <!-- Phosphor Icons CDN -->
    <!-- Favicon -->
    <!-- style.css -->
</head>
<body class="clima-0">
    <!-- Home Button (fixo) -->
    <div class="lesson-container">
        <!-- Header Navigation -->
        <!-- Hero Section -->
        <!-- Preparação do Portador -->
        <!-- Ritual de Entrada -->
        <!-- A Jornada -->
        <!-- O Concreto -->
        <!-- Narramos Juntos -->
        <!-- Ritual de Fechamento -->
        <!-- Conexão da Jornada -->
        <!-- Sementes para o Dia -->
        <!-- Formação do Portador -->
        <!-- Navigation Footer -->
    </div>
    <!-- Footer -->
</body>
</html>
```

### 3.2 Classes CSS Principais (do style.css)

| Classe | Uso |
|--------|-----|
| `.hero` | Seção hero com fundo verde |
| `.lesson-content` | Container de conteúdo com sombra |
| `.scene-header` | Títulos de seção com ícone |
| `.instruction-box` | Caixas de instrução amarelas |
| `.script-persona-block` | Blocos de fala de personagem |
| `.portador-block` | Bloco do Portador da Tocha (carmim) |
| `.script-avatar` | Avatar do Guardião |
| `.script-avatar-icon` | Ícone do Portador (ph-fire) |
| `.card-container` | Container centralizado de cards |
| `.card-visual-asset` | Imagem de card com animação |
| `.guardian-card` | Card de Guardião |
| `.nav-btn` | Botões de navegação |
| `.btn-cta` | Botão CTA dourado |

### 3.3 Variáveis CSS (Premium Sementes)

```css
--color-gold: #C5A059;       /* Old Gold - Melquior, destaque */
--color-green: #2A3B33;      /* Deep Forest - Sementes, fundo */
--color-cream: #F9F7F1;      /* Paper Texture - fundo claro */
--color-accent: #BC5D41;     /* Clay Red - ênfase */
--font-heading: 'Merriweather', Georgia, serif;
--font-body: 'Inter', system-ui, sans-serif;
```

### 3.4 Ícones Phosphor (duotone)

| Contexto | Ícone | Classe |
|----------|-------|--------|
| Portador da Tocha | Fogo | `ph-fire duotone-carmim` |
| Sementes (ciclo) | Planta | `ph-plant duotone-forest` |
| Melquior | Sol/Escudo | `ph-sun duotone-gold` |
| Dica do Coração | Lâmpada | `ph-lightbulb duotone-gold` |
| Ritual | Filme | `ph-film-strip duotone-magic` |
| Jornada | Mapa | `ph-map-trifold duotone-gold` |
| Concreto | Parede/Cubo | `ph-wall duotone-terra` |
| Narração | Chat | `ph-chat-circle-dots duotone-terra` |
| Fechamento | Bandeira | `ph-flag duotone-forest` |
| Graça | Coração | `ph-heart duotone-heart` |

---

## 4. CONTEÚDO A SER FUNDIDO

### 4.1 Hero Section
```yaml
# Do YAML existente:
titulo: "O Portal do Reino"
meta: "Lição 000 · Introdução · 15-20 min"
frase_impacto: "Onde a matemática vira aventura, e cada número conta uma história."
guardiao: melquior
clima: ensolarado
```

### 4.2 Preparação do Portador
```yaml
# Do YAML existente:
dica_coracao: |
  Hoje não há matemática. Só maravilhamento.
  Seu único trabalho é criar o ambiente sagrado.
  Acenda a Luz Amarela (ou seu sinal escolhido), estenda o tapete.
  Melquior fará o resto.

filho_descobre: |
  Que existe um Reino especial chamado Reino Contado.
  Que cinco Guardiões vão caminhar com ele nesta jornada.
  Que ele é um Herdeiro -- alguém especial, esperado.

materiais:
  essencial:
    - Tapete ou cobertor (Tapete do Reino)
    - Luz Amarela (Gatilho de Foco e Imersão)
    - Cards dos 5 Guardiões
    - Cards dos 5 Locais
  opcional:
    - Música ambiente suave

nota_graca: |
  Se a criança não "entrar" na história hoje, tudo bem.
  A semente foi plantada. Amanhã ela pode brotar.
```

### 4.3 Ritual de Entrada (Voz Única)
```yaml
# Do YAML existente - MONOBLOCO do Portador:
ritual:
  fala_abertura: |
    "Luz de fora acalma."
    "Sol de dentro acende."
    "Respirem... Estamos no Reino."
  
  acting_cue: "[Feche os olhos. Respire fundo...]"
  
  transicao: |
    "Quando abrir os olhos, estaremos em um lugar muito especial...
    O Jardim Central do Reino Contado."
  
  card_local: jardim_central
  
  imersao_sensorial: |
    "O ar cheira a terra molhada e musgo fresco.
    O sol dourado aquece o rosto. Pássaros cantam ao longe.
    Em um banco de pedra antiga, sentado com as patas cruzadas,
    está um grande Leão de juba dourada. Ele sorri ao ver você chegar."
```

### 4.4 A Jornada - Apresentação dos Guardiões

#### Cena 1: O Encontro com Melquior
```yaml
# Do YAML existente:
melquior_acolhimento: |
  "Aproxime-se, pequeno Herdeiro.
  Sente-se aqui, no tapete de musgo, sob o brilho da Luz Amarela."

melquior_backstory: |
  "Antes de você nascer, o Grande Rei olhou para o mundo
  e viu que faltava algo muito importante.
  Ele disse com sua voz de trovão suave:
  'Criarei um Reino onde os números não sejam frios,
  onde contar seja uma aventura,
  e onde cada criança saiba que foi feita para descobrir.'
  E assim nasceu o Reino Contado.
  Esse jardim onde estamos? O Rei o plantou pensando em você.
  Cada árvore, cada flor, cada caminho...
  Tudo foi preparado para seus olhos, Herdeiro."

melquior_apresentacao: |
  "Eu sou Melquior, o Leão Dourado.
  Eu sabia que você viria.
  O Portal estava esperando por você.
  Minha juba brilha com a luz da sabedoria,
  e meu rugido... bem, meu rugido é gentil.
  Eu não assusto -- eu acolho.
  Venha. Deixe-me apresentar meus amigos."
```

#### Cena 2: Os Quatro Companheiros
```yaml
# Do YAML existente - apresentação por Melquior:

noe: |
  "Veja! Ali, no galho mais alto...
  Olhos grandes que veem o tempo passar devagar.
  É a Coruja Noé.
  Ele nos ensina a ouvir o silêncio e a esperar com paciência.
  [Aponte para cima]
  Consegue vê-lo? Seus olhos são como duas luas amarelas.
  Quando você precisar de calma, Noé estará lá."

celeste: |
  "Sente este vento rápido?
  Um vulto laranja que corre entre as árvores!
  Rápida como um pensamento.
  É a Raposa Celeste!
  Ela adora segredos e padrões.
  [Fareja o ar]
  Está sentindo? Cheira a aventura!
  Celeste é curiosa como você. Ela fareja mistérios!"

bernardo: |
  "Uma montanha de pelo quente e bondade.
  Ouça o passo firme na terra...
  Tum-tum-arrasta.
  É o Urso Bernardo!
  Ele é forte e gentil.
  Vê a pata manca dele? Bernardo se machucou salvando seus amigos.
  Mas isso nunca o parou.
  Quando você errar, Bernardo vai dizer: 'Mais uma vez. Comigo.'"

iris: |
  "E olhe bem de perto para aquela flor...
  Ela é pequena, mas vê coisas gigantes.
  Lá está Íris, a pequena Pardal!
  Ela vê o que ninguém mais vê:
  a beleza num grão de areia.
  [Aponte para baixo, para algo pequeno]
  Você consegue ver o brilho do colar dela?
  Íris tem olhos de artista. Ela encontra beleza em tudo."
```

#### Cena 3: O Convite Final
```yaml
# Do YAML existente:
convite_final: |
  "Noé, Celeste, Bernardo, Íris... e eu, Melquior.
  
  Todos nós estamos aqui para caminhar com você.
  Você é o Herdeiro -- alguém que o Rei esperava.
  
  Amanhã, Celeste vai nos levar à Clareira das Perguntas.
  Ela encontrou algo especial debaixo do carvalho mais velho...
  Três sementes. Três promessas.
  
  Mas isso é para amanhã.
  
  Hoje... bem-vindo ao Reino."

instrucao_portador: "Abrace a criança ou aperte sua mão. Este é o momento de selamento."
```

### 4.5 O Concreto (Vivência)
```yaml
# Do YAML existente:
desc: "Esta lição não tem atividade concreta matemática. O 'concreto' é a experiência sensorial."

instrucoes:
  - passo: 1
    acao: "Mantenham-se sentados no tapete por um momento em silêncio"
    fala: "Vamos guardar esse momento no coração?"
  - passo: 2
    acao: "Pergunte à criança qual guardião ela mais gostou"
    fala: "Qual deles você quer conhecer melhor?"

norte_absoluto: "O objetivo é SENTIR, não aprender. Se a criança estiver encantada, a lição foi perfeita."

adaptacao_bernardo: |
  Para crianças com dificuldade de atenção, mantenha a narrativa mais curta.
  Apresente apenas 2-3 guardiões hoje e os outros amanhã.
```

### 4.6 Narramos Juntos
```yaml
# Do YAML existente:
instrucao: |
  Não force perguntas hoje.
  Se a criança quiser falar, ouça.
  Se preferir silêncio, respeite. O coração guardou.

pergunta_principal: "O que você achou do Reino Contado?"

perguntas_coracao:
  - "Qual guardião você quer conhecer melhor?"
  - "Como é o jardim que você imaginou?"
  - "O que você acha que Celeste encontrou?"

nota_cm: |
  Esta é uma lição de ATMOSFERA (Charlotte Mason).
  Não avalie. Não corrija. Apenas esteja presente.
```

### 4.7 Ritual de Fechamento
```yaml
# Do YAML existente:
fala_melquior: |
  "Herdeiro... obrigado por ter vindo hoje.
  
  Amanhã Celeste estará esperando na Clareira.
  As três sementes do carvalho estão guardadas para você.
  
  Descanse bem. O Reino espera seu retorno."

fala_portador: |
  "A Luz se apaga, mas o brilho fica no coração.
  O Reino descansa. Até amanhã, Herdeiro."

fio_ouro: "Amanhã, Celeste nos mostrará as três sementes do carvalho mais velho."
```

### 4.8 Formação do Portador
```yaml
# Do YAML existente:
porque_importa: |
  Esta lição não contém matemática -- e isso é intencional.
  
  Charlotte Mason ensinava que a "atmosfera" é um terço da educação.
  Antes de ensinar QUALQUER coisa, precisamos criar um ambiente de
  maravilhamento, segurança e pertencimento.

metodo_cpa:
  concreto: "Experiência sensorial (luz, tapete, ambiente)"
  pictorico: "Não aplicável (lição litúrgica)"
  abstrato: "Não aplicável"

principio_cm:
  numero: 6
  citacao: "Education is an atmosphere, a discipline, a life."
  citacao_pt: "Educação é atmosfera, disciplina, vida."

espiral:
  conceito: "Atmosfera sagrada"
  volta_atual: "Sementes -- Primeiro contato com o Reino e os Guardiões"
  proxima_volta: "Raízes -- Revisitamos os Guardiões com novas responsabilidades"

reflexao_espiritual: |
  "Tudo o que vê aqui foi feito para seus olhos."
  
  Melquior lembra à criança que ela é esperada, desejada, preparada.
  Em um mundo que muitas vezes diz "você não é suficiente",
  o Reino Contado sussurra: "Você é o Herdeiro."
```

---

## 5. REGRAS DE IMPLEMENTAÇÃO

### 5.1 Regras Visuais (de `padrao_visual_sementes.md`)

1. **Voz Única do Portador**: UM único `.portador-block` no Ritual de Entrada
2. **Card do Guardião**: Aparece UMA ÚNICA VEZ por lição (no momento de introdução)
3. **Acting Cues**: Usar `[ ]` em estilo dourado/itálico dentro do bloco
4. **Capitalização**: Guardiões sempre com inicial maiúscula
5. **Centralização**: Cards centralizados com `.card-container`
6. **Sem Quote Clutter**: Aspas apenas em diálogos diretos

### 5.2 Regras de CSS

1. Usar variáveis CSS (não hardcode de cores)
2. Aplicar `duotone-*` para ícones Phosphor
3. Usar `rotate-left hover-float` para cards
4. Aplicar sombras e transições conforme style.css

### 5.3 Regras de Acessibilidade

1. `alt` text em todas as imagens
2. `aria-label` em elementos interativos
3. Contraste adequado (fundo verde texto branco)
4. Responsividade mobile

---

## 6. ESTRUTURA DE SEÇÕES HTML

### 6.1 Head
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>O Portal do Reino | Matemática Viva</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="icon" href="../favicon.ico" type="image/x-icon">
</head>
```

### 6.2 Body Class
```html
<body class="clima-0">  <!-- L000: Portal do Reino -->
```

### 6.3 Home Button
```html
<a href="../index.html" class="home-btn" title="Voltar ao Dashboard">
    <i class="ph-duotone ph-house duotone-forest"></i>
</a>
```

### 6.4 Header Navigation
```html
<div class="lesson-header-nav">
    <a href="../index.html" class="nav-back-link">
        <i class="ph-duotone ph-arrow-left"></i> Voltar
    </a>
    <div style="display: flex; align-items: center; gap: 0.5rem;">
        <i class="ph-duotone ph-plant duotone-forest" style="font-size: 1.5rem;"></i>
        <span style="font-family: var(--font-heading); font-weight: 700; color: var(--color-green); font-size: 0.9rem;">Sementes</span>
    </div>
</div>
```

### 6.5 Hero Section
```html
<header class="lesson-hero">
    <div class="lesson-meta-tag">
        Lição 000 · O Portal do Reino · <i class="ph-duotone ph-timer duotone-carmim"></i> 15-20 min
    </div>
    <h1 class="hero-title">O Portal do Reino</h1>
    <p class="hero-quote">"Onde a matemática vira aventura, e cada número conta uma história."</p>
    <img src="../assets/sementes/guardioes/melquior-leao.png" 
         onError="this.src='../assets/sementes/guardioes/placeholder.png'" 
         alt="Melquior, o Leão Dourado" class="hero-guardian">
</header>
```

### 6.6 Preparação do Portador
```html
<div class="scene-header">
    <i class="ph-duotone ph-clipboard-text duotone-terra" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Preparação do Portador
</div>

<!-- Dica do Coração -->
<div class="instruction-box">
    <i class="ph-duotone ph-lightbulb duotone-gold" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    <div>
        <strong>Dica do Coração:</strong> Hoje não há matemática. Só maravilhamento.
        Seu único trabalho é criar o ambiente sagrado.
        Acenda a Luz Amarela (ou seu sinal escolhido), estenda o tapete.
        <strong>Melquior fará o resto.</strong>
    </div>
</div>

<!-- Materiais -->
<aside class="materials-box">
    <p><strong><i class="ph-duotone ph-target duotone-terra"></i> Essencial:</strong></p>
    <ul>
        <li>Tapete ou cobertor (Tapete do Reino)</li>
        <li>Luz Amarela (Gatilho de Foco e Imersão)</li>
        <li>Cards dos 5 Guardiões</li>
        <li>Cards dos 5 Locais</li>
    </ul>
    <p style="margin-top:1rem;"><strong><i class="ph-duotone ph-package duotone-gold"></i> Se tiver:</strong></p>
    <ul style="color:#6B7280;">
        <li>Música ambiente suave</li>
    </ul>
</aside>

<!-- Descobertas -->
<p><strong><i class="ph-duotone ph-sparkle duotone-magic"></i> Seu filho vai descobrir:</strong>
    Que existe um Reino especial chamado Reino Contado.
    Que cinco Guardiões vão caminhar com ele nesta jornada.
    Que ele é um <strong>Herdeiro</strong> -- alguém especial, esperado.
</p>

<!-- Segredo do Maravilhamento -->
<p><strong><i class="ph-duotone ph-sparkle duotone-magic"></i> Segredo do Maravilhamento:</strong>
    Não precisa explicar nada. Apenas <strong>viva a narrativa</strong>.
    Se a criança perguntar, sorria e diga: "Você vai descobrir...".
    O <strong>maravilhamento</strong> é mais importante que a compreensão.
</p>

<!-- Nota de Graça -->
<p><strong><i class="ph-duotone ph-heart duotone-heart"></i> Nota de Graça:</strong>
    Se a criança não "entrar" na história hoje, <strong>tudo bem</strong>.
    A semente foi plantada. Amanhã ela pode brotar.
</p>
```

### 6.7 Ritual de Entrada (MONOBLOCO)
```html
<div class="scene-header">
    <i class="ph-duotone ph-film-strip duotone-magic" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Ritual de Entrada
</div>

<!-- Instruction Box -->
<div class="instruction-box">
    <i class="ph-duotone ph-lamp duotone-gold" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    <div>
        <strong>Preparação:</strong>
        <ul style="margin: 0.5rem 0 0 0; padding-left: 1.2rem; font-size: 0.95rem;">
            <li>Tenha a <strong>Luz Amarela</strong> à mão.</li>
            <li>Sentem-se confortavelmente no tapete.</li>
            <li>Ao acender a luz, leia as falas abaixo.</li>
        </ul>
    </div>
</div>

<!-- PORTADOR BLOCK (MONOBLOCO) -->
<div class="script-persona-block portador-block">
    <div class="script-avatar-icon">
        <i class="ph-duotone ph-fire duotone-carmim"></i>
    </div>
    <div class="script-content">
        <div class="script-header">
            <span class="script-name">Portador da Tocha</span>
        </div>
        <div class="script-text">
            <p>"Luz de fora acalma."</p>
            <p>"Sol de dentro acende."</p>
            <p>"Respirem... Estamos no Reino."</p>
            
            <!-- Acting Cue -->
            <p style="color: var(--color-gold); font-style: italic; margin-top: 1rem;">
                [Feche os olhos. Respire fundo...]
            </p>
            
            <p>"Quando abrir os olhos, estaremos em um lugar muito especial...
            O Jardim Central do Reino Contado."</p>
            
            <!-- Card do Local -->
            <div class="card-container" style="margin: 1.5rem 0;">
                <p class="local-label">Mostrar Card</p>
                <img src="../assets/cards/locais/local-jardim-central.png" 
                     style="width: 100%; max-width: 400px; border-radius: 12px; 
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 4px solid var(--color-gold);" 
                     alt="Jardim Central">
                <p style="margin-top: 0.5rem; font-weight: 700; font-size: 1.1rem; 
                          color: var(--color-green); text-align: center;">
                    Jardim Central
                </p>
            </div>
            
            <!-- Imersão Sensorial -->
            <p>"O ar cheira a terra molhada e musgo fresco.
            O sol dourado aquece o rosto. Pássaros cantam ao longe.
            Em um banco de pedra antiga, sentado com as patas cruzadas,
            está um grande Leão de juba dourada. Ele sorri ao ver você chegar."</p>
        </div>
    </div>
</div>
```

### 6.8 A Jornada
```html
<h2><i class="ph-duotone ph-map-trifold duotone-gold" style="margin-right:0.5rem;"></i> A Jornada</h2>

<!-- Cena 1: O Encontro -->
<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-sun duotone-gold" style="font-size:1.5rem; margin-right:0.5rem;"></i>
        O Encontro com Melquior
    </div>
    
    <!-- Card de Melquior -->
    <div class="card-container">
        <p class="local-label">Mostrar Card</p>
        <img src="../assets/cards/guardioes/melquior-leao.png" 
             class="card-visual-asset rotate-left hover-float"
             onError="this.src='../assets/cards/guardioes/placeholder.png'" 
             alt="Melquior, o Leão Dourado">
    </div>
    
    <!-- Script Block de Melquior -->
    <div class="script-persona-block">
        <img src="../assets/cards/guardioes/melquior-leao.png" class="script-avatar" alt="Melquior">
        <div class="script-content">
            <div class="script-header">
                <span class="script-name">Melquior</span>
                <span style="font-style: normal;"><i class="ph-duotone ph-smiley duotone-gold"></i></span>
                (Tom: Acolhedor)
            </div>
            <div class="script-text">
                <p>"Aproxime-se, pequeno Herdeiro.</p>
                <p>Sente-se aqui, no tapete de musgo, sob o brilho da Luz Amarela."</p>
            </div>
        </div>
    </div>
    
    <!-- Continuação... -->
</div>

<!-- Cena 2: Os Quatro Companheiros -->
<!-- ... apresentação de Noé, Celeste, Bernardo, Íris ... -->

<!-- Cena 3: O Convite Final -->
<div class="scene-card">
    <div class="scene-header">
        <i class="ph-duotone ph-hand-heart duotone-gold" style="font-size:1.5rem; margin-right:0.5rem;"></i>
        O Convite Final
    </div>
    
    <div class="instruction-box">
        <i class="ph-duotone ph-hand-pointing duotone-neutral" style="font-size:1.5rem; margin-right:0.5rem;"></i>
        <div>Abrace a criança ou aperte sua mão. Este é o momento de selamento.</div>
    </div>
    
    <div class="script-persona-block">
        <img src="../assets/cards/guardioes/melquior-leao.png" class="script-avatar" alt="Melquior">
        <div class="script-content">
            <div class="script-header">
                <span class="script-name">Melquior</span>
                <span style="font-style: normal;"><i class="ph-duotone ph-shield-check duotone-forest"></i></span>
                (Tom: Solene)
            </div>
            <div class="script-text">
                <p>"Noé, Celeste, Bernardo, Íris... e eu, Melquior.</p>
                <p>Todos nós estamos aqui para caminhar com você.</p>
                <p>Você é o Herdeiro -- alguém que o Rei esperava.</p>
                <p>Amanhã, Celeste vai nos levar à Clareira das Perguntas.</p>
                <p>Ela encontrou algo especial debaixo do carvalho mais velho...</p>
                <p>Três sementes. Três promessas.</p>
                <p>Mas isso é para amanhã.</p>
                <p>Hoje... bem-vindo ao Reino."</p>
            </div>
        </div>
    </div>
</div>
```

### 6.9 O Concreto
```html
<h2><i class="ph-duotone ph-wall duotone-terra" style="margin-right:0.5rem;"></i> O Concreto</h2>

<div class="scene-header">
    <i class="ph-duotone ph-heart duotone-heart" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Momento de Conexão
</div>

<div class="instruction-box">
    <i class="ph-duotone ph-info duotone-neutral" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    <div>
        <p style="margin-bottom: 0.75rem; color: #374151;">
            <strong>Nota:</strong> Esta lição não tem atividade concreta matemática.
            O "concreto" é a experiência sensorial.
        </p>
        <p style="margin-bottom: 0.5rem;"><strong>Sugestões:</strong></p>
        <ul style="padding-left: 1.2rem; line-height: 1.8; margin-bottom: 0.75rem;">
            <li><strong>Passo 1:</strong> Mantenham-se sentados no tapete por um momento em silêncio.
                <br><em>"Vamos guardar esse momento no coração?"</em></li>
            <li><strong>Passo 2:</strong> Pergunte à criança qual guardião ela mais gostou.
                <br><em>"Qual deles você quer conhecer melhor?"</em></li>
        </ul>
        <p style="font-size: 0.9rem; color: #6B7280; font-style: italic;">
            <strong>Norte Absoluto:</strong> O objetivo é SENTIR, não aprender.
            Se a criança estiver encantada, a lição foi perfeita.
        </p>
    </div>
</div>
```

### 6.10 Narramos Juntos
```html
<div class="scene-header">
    <i class="ph-duotone ph-chat-circle-dots duotone-terra" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Narramos Juntos
</div>

<div class="instruction-box">
    <i class="ph-duotone ph-ear duotone-neutral" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    <div>
        Não force perguntas hoje.<br>
        Se a criança quiser falar, ouça.<br>
        Se preferir silêncio, respeite. O coração guardou.
    </div>
</div>

<p><strong>Perguntas do Coração:</strong></p>
<ul style="margin-left:1.5rem; margin-top:0.5rem;">
    <li>O que você achou do Reino Contado?</li>
    <li>Qual guardião você quer conhecer melhor?</li>
    <li>Como é o jardim que você imaginou?</li>
    <li>O que você acha que Celeste encontrou?</li>
</ul>

<p style="font-size: 0.9rem; color: #6B7280; font-style: italic; margin-top: 1rem;">
    <strong>Nota CM:</strong> Esta é uma lição de ATMOSFERA (Charlotte Mason).
    Não avalie. Não corrija. Apenas esteja presente.
</p>
```

### 6.11 Ritual de Fechamento
```html
<div class="scene-header">
    <i class="ph-duotone ph-flag duotone-forest" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Ritual de Fechamento
</div>

<!-- Fala de Melquior -->
<div class="script-persona-block">
    <img src="../assets/cards/guardioes/melquior-leao.png" class="script-avatar" alt="Melquior">
    <div class="script-content">
        <div class="script-header">
            <span class="script-name">Melquior</span>
            <span style="font-style: normal;"><i class="ph-duotone ph-sun duotone-gold"></i></span>
            (Tom: Esperançoso)
        </div>
        <div class="script-text">
            <p>"Herdeiro... obrigado por ter vindo hoje.</p>
            <p>Amanhã Celeste estará esperando na Clareira.</p>
            <p>As três sementes do carvalho estão guardadas para você.</p>
            <p>Descanse bem. O Reino espera seu retorno."</p>
        </div>
    </div>
</div>

<!-- Fala do Portador -->
<div class="script-persona-block portador-block">
    <div class="script-avatar-icon">
        <i class="ph-duotone ph-fire duotone-carmim"></i>
    </div>
    <div class="script-content">
        <div class="script-header">
            <span class="script-name">Portador da Tocha</span>
        </div>
        <div class="script-text">
            <p>"A Luz se apaga, mas o brilho fica no coração."</p>
            <p>"O Reino descansa. Até amanhã, Herdeiro."</p>
        </div>
    </div>
</div>

<!-- Fio de Ouro -->
<div class="instruction-box" style="background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);">
    <i class="ph-duotone ph-link duotone-gold" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    <div>
        <strong>Fio de Ouro:</strong> Amanhã, Celeste nos mostrará as três sementes do carvalho mais velho.
    </div>
</div>
```

### 6.12 Conexão da Jornada
```html
<div class="scene-header">
    <i class="ph-duotone ph-link duotone-indigo" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Conexão da Jornada
</div>

<p>
    <strong>Próxima Lição:</strong>
    <a href="001_trindade_palma.html" style="font-weight: 600; color: var(--color-green);">
        MV-S-001: A Trindade na Palma
        <i class="ph-duotone ph-arrow-right duotone-gold"></i>
    </a>
</p>
<p style="color: #6B7280; font-style: italic;">
    Celeste encontrou três sementes especiais debaixo do carvalho mais velho...
</p>
```

### 6.13 Sementes para o Dia
```html
<div class="scene-header">
    <i class="ph-duotone ph-plant duotone-forest" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Sementes para o Dia
</div>

<div style="background: #F0FDF4; border-radius: 12px; padding: 1.5rem; margin: 1rem 0;">
    <p><strong>Atividades para continuar o encantamento:</strong></p>
    <ul>
        <li><i class="ph-duotone ph-moon duotone-indigo"></i> <strong>Antes de dormir:</strong> Pergunte qual guardião ele quer sonhar.</li>
        <li><i class="ph-duotone ph-sun duotone-gold"></i> <strong>Amanhã de manhã:</strong> "O que você acha que Celeste encontrou?"</li>
        <li><i class="ph-duotone ph-pencil duotone-terra"></i> <strong>Se quiser:</strong> Desenhar o guardião favorito.</li>
        <li><i class="ph-duotone ph-chat duotone-forest"></i> <strong>No jantar:</strong> Contar para a família quem são os Guardiões.</li>
        <li><i class="ph-duotone ph-walk duotone-neutral"></i> <strong>No parque:</strong> Procurar "pistas" dos Guardiões na natureza.</li>
    </ul>
    <p style="font-style: italic; color: #059669; margin-top: 1rem;">
        "O Reino não acaba quando a lição termina. Ele vive no coração do Herdeiro."
    </p>
</div>
```

### 6.14 Formação do Portador
```html
<div class="scene-header">
    <i class="ph-duotone ph-graduation-cap duotone-terra" style="font-size:1.5rem; margin-right:0.5rem;"></i>
    Formação do Portador
</div>

<!-- Por que Importa -->
<div class="cm-box" style="background: #F0F9FF; border-left: 4px solid #0369A1; padding: 1rem; margin: 1rem 0;">
    <p><strong><i class="ph-duotone ph-books duotone-indigo"></i> Por que importa:</strong></p>
    <p>Esta lição não contém matemática -- e isso é intencional.</p>
    <p>Charlotte Mason ensinava que a "atmosfera" é um terço da educação.</p>
    <p>Antes de ensinar QUALQUER coisa, precisamos criar um ambiente de</p>
    <p>maravilhamento, segurança e pertencimento.</p>
</div>

<!-- Método CPA -->
<div class="bruner-box" style="background: #F5F3FF; border-left: 4px solid #7C3AED; padding: 1rem; margin: 1rem 0;">
    <p><strong><i class="ph-duotone ph-brain duotone-indigo"></i> Método CPA:</strong></p>
    <ul>
        <li><strong>Concreto:</strong> Experiência sensorial (luz, tapete, ambiente)</li>
        <li><strong>Pictórico:</strong> Não aplicável (lição litúrgica)</li>
        <li><strong>Abstrato:</strong> Não aplicável</li>
    </ul>
</div>

<!-- Charlotte Mason -->
<div class="cm-box" style="background: #FFFBEB; border-left: 4px solid #D97706; padding: 1rem; margin: 1rem 0;">
    <p><strong><i class="ph-duotone ph-feather duotone-gold"></i> Charlotte Mason (Princípio 6):</strong></p>
    <p><em>"Education is an atmosphere, a discipline, a life."</em></p>
    <p><em>"Educação é atmosfera, disciplina, vida."</em></p>
    <p>Aplicação: Antes de contar, dar. Antes de ensinar, encantar.</p>
</div>

<!-- Currículo Espiral -->
<div class="bruner-box" style="background: #ECFDF5; border-left: 4px solid #059669; padding: 1rem; margin: 1rem 0;">
    <p><strong><i class="ph-duotone ph-spiral duotone-forest"></i> Currículo Espiral:</strong></p>
    <p><strong>Conceito:</strong> Atmosfera sagrada</p>
    <p><strong>Volta Atual:</strong> Sementes -- Primeiro contato com o Reino e os Guardiões</p>
    <p><strong>Próxima Volta:</strong> Raízes -- Revisitamos os Guardiões com novas responsabilidades</p>
</div>

<!-- Reflexão Espiritual -->
<div class="espiritual-box" style="background: #FDF4FF; border-left: 4px solid #A855F7; padding: 1rem; margin: 1rem 0;">
    <p><strong><i class="ph-duotone ph-sparkle duotone-magic"></i> Reflexão Espiritual:</strong></p>
    <p><em>"Tudo o que vê aqui foi feito para seus olhos."</em></p>
    <p>Melquior lembra à criança que ela é esperada, desejada, preparada.</p>
    <p>Em um mundo que muitas vezes diz "você não é suficiente",</p>
    <p>o Reino Contado sussurra: "Você é o Herdeiro."</p>
</div>

<!-- Nota de Graça -->
<div class="graca-box" style="background: #FEF2F2; border-left: 4px solid #EF4444; padding: 1rem; margin: 1rem 0;">
    <p><strong><i class="ph-duotone ph-heart duotone-heart"></i> Nota de Graça:</strong></p>
    <p>Se hoje não "funcionou" como você esperava, respire.</p>
    <p>Algumas crianças precisam de mais tempo para cruzar o portal.</p>
    <p>O convite de Melquior permanece aberto. Volte amanhã com a mesma ternura.</p>
</div>
```

### 6.15 Navigation Footer
```html
<div class="lesson-nav-footer">
    <a href="../index.html" class="nav-btn prev">
        <i class="ph-duotone ph-arrow-left"></i> Dashboard
    </a>
    <a href="001_trindade_palma.html" class="nav-btn next">
        Próxima: A Trindade na Palma <i class="ph-duotone ph-arrow-right"></i>
    </a>
</div>
```

### 6.16 Footer
```html
<footer class="site-footer">
    <p><strong>Matemática Viva</strong> · Histórias que ensinam. Narração que fixa.</p>
    <p style="font-size: 0.85rem; margin-top: 0.5rem;">
        Da Família Rodrigues para outras famílias
    </p>
</footer>
```

---

## 7. CHECKLIST DE VALIDAÇÃO

### 7.1 Estrutura
- [ ] `<head>` completo com fonts, icons, CSS
- [ ] `<body class="clima-0">`
- [ ] Home Button presente
- [ ] Header Navigation com ícone Sementes
- [ ] Hero com meta, título, quote, imagem

### 7.2 Preparação do Portador
- [ ] Scene Header com ícone correto
- [ ] Dica do Coração
- [ ] Materials Box (essencial + opcional)
- [ ] Seu filho vai descobrir
- [ ] Segredo do Maravilhamento
- [ ] Nota de Graça

### 7.3 Ritual de Entrada
- [ ] Scene Header com ícone filme
- [ ] Instruction Box de preparação
- [ ] **MONOBLOCO** do Portador (voz única)
- [ ] Acting Cues em `[ ]` dourado/itálico
- [ ] Card do Local centralizado
- [ ] Imersão sensorial completa

### 7.4 A Jornada
- [ ] H2 com ícone mapa
- [ ] Cena 1: Encontro com Melquior
- [ ] Card de Melquior UMA vez
- [ ] Script Blocks com Tom indicado
- [ ] Cena 2: Os Quatro Companheiros
- [ ] Cards de Noé, Celeste, Bernardo, Íris
- [ ] Cena 3: O Convite Final
- [ ] Instruction Box de selamento

### 7.5 O Concreto
- [ ] H2 com ícone parede
- [ ] Instruction Box com objetivo e sugestões
- [ ] Norte Absoluto presente
- [ ] Adaptação Bernardo (opcional)

### 7.6 Narramos Juntos
- [ ] Scene Header com ícone chat
- [ ] Instruction Box de escuta
- [ ] Perguntas do Coração (lista)
- [ ] Nota CM

### 7.7 Ritual de Fechamento
- [ ] Scene Header com ícone bandeira
- [ ] Fala de Melquior (Script Block)
- [ ] Fala do Portador (Script Block)
- [ ] Fio de Ouro

### 7.8 Conexão da Jornada
- [ ] Scene Header com ícone link
- [ ] Link para próxima lição
- [ ] Teaser narrativo

### 7.9 Sementes para o Dia
- [ ] Scene Header com ícone planta
- [ ] Box verde com 5 atividades
- [ ] Frase de fechamento itálica

### 7.10 Formação do Portador
- [ ] Scene Header com ícone graduação
- [ ] Por que importa (CM box)
- [ ] Método CPA (Bruner box)
- [ ] Charlotte Mason (CM box)
- [ ] Currículo Espiral (Bruner box)
- [ ] Reflexão Espiritual (box)
- [ ] Nota de Graça (box)

### 7.11 Navigation Footer
- [ ] Botões prev/next
- [ ] Footer com identidade

---

## 8. ARQUIVO DE SAÍDA

**Nome:** `L000_PORTAL_REINO_FUSIONADO.html`
**Localização:** `logs/L000_PORTAL_REINO_FUSIONADO.html`
**Encoding:** UTF-8
**Indentação:** 4 espaços

---

## 9. PRÓXIMOS PASSOS

1. **Code Mode**: Gerar o arquivo HTML completo
2. **Validação**: Conferir contra checklist
3. **Revisão Visual**: Verificar se CSS aplica corretamente
4. **Teste**: Abrir em navegador para preview

---

**FIM DA TASK**