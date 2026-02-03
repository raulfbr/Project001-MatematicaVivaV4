# DELIBERAÇÃO: Apresentação do Manual para Famílias Pioneiras

**Data:** 2026-01-22 13:36 (Revisado 13:38)  
**Tema:** Integrar Manual do Portador da Tocha no site existente  
**Status:** EM DELIBERAÇÃO (REFINADO)  
**Modo:** REUNIAO (Orchestrator v1.5)

---

## Contexto

O Manual do Portador da Tocha está completo (425 linhas, ~20KB). 

**Descoberta:** Já existe um `site/index.html` completo! É um dashboard bonito com:
- Sidebar com navegação por ciclos
- Seção "Família Pioneira" 
- Cards para lições
- Livros Dourados
- Blog

**Estrutura existente:**
```
site/
├── index.html (Dashboard principal)
├── style.css (Estilos)
├── assets/ (Imagens)
├── sementes/ (Lições HTML)
└── placeholders/ (Páginas em construção)
```

---

## Nova Abordagem: Integrar no Site Existente

### Estratégia

1. **Criar página HTML para o Manual** (`site/manual-portador.html`)
2. **Adicionar link na sidebar** como primeiro item (antes das lições)
3. **Seguir o mesmo estilo** do site existente

---

## Plano de Implementação

### Fase 1: Criar manual-portador.html
- [ ] Criar arquivo `site/manual-portador.html`
- [ ] Usar template do site existente (mesmo header, sidebar, footer)
- [ ] Converter conteúdo do Markdown para HTML
- [ ] Estilizar com CSS existente

### Fase 2: Atualizar index.html
- [ ] Adicionar link para Manual na sidebar (seção "Família Pioneira")
- [ ] Posicionar ANTES das lições (como primeiro passo)
- [ ] Usar ícone apropriado (🔥 tocha ou 📖 manual)

### Fase 3: Verificação
- [ ] Testar navegação
- [ ] Verificar responsividade (mobile)
- [ ] Verificar links internos

---

## Estrutura Proposta da Sidebar

```html
<!-- SEÇÃO FAMÍLIA PIONEIRA -->
<div class="nav-section">Família Pioneira</div>

<!-- NOVO: Manual do Portador (primeiro!) -->
<a href="manual-portador.html" class="nav-link">
    <span>🔥</span> Manual do Portador
</a>

<!-- Ciclos existentes -->
<a href="#sementes" class="nav-link active">
    <span>🌱</span> Ciclo Sementes
</a>
...
```

---

## Design da Página do Manual

### Layout Sugerido

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manual do Portador da Tocha | Matemática Viva</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Mesma sidebar do index.html -->
    <nav class="sidebar">...</nav>
    
    <main class="main-content">
        <header>
            <div class="role-badge">Manual do Portador</div>
            <h1>🔥 Manual do Portador da Tocha</h1>
            <p class="subtitle">Um guia para você que vai conduzir a jornada do seu filho pelo Reino Contado</p>
        </header>
        
        <!-- Conteúdo do Manual convertido -->
        <article class="manual-content">
            <!-- Partes 1-8 + Comunidade + Pioneiras + Fechamento -->
        </article>
    </main>
</body>
</html>
```

### Estilos Adicionais (style.css)

```css
/* Estilos específicos para o Manual */
.manual-content {
    max-width: 800px;
    margin: 0 auto;
    line-height: 1.8;
}

.manual-content h2 {
    color: var(--primary);
    border-bottom: 2px solid var(--accent);
    padding-bottom: 0.5rem;
    margin-top: 3rem;
}

.manual-content h3 {
    color: var(--text);
    margin-top: 2rem;
}

.manual-content blockquote {
    background: #FDF8F3;
    border-left: 4px solid var(--accent);
    padding: 1rem;
    margin: 1rem 0;
}

.manual-content table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
}

.manual-content th, .manual-content td {
    border: 1px solid #E5E7EB;
    padding: 0.75rem;
    text-align: left;
}
```

---

## Checklist de Execução

| # | Tarefa | Detalhes | Status |
|---|--------|----------|--------|
| 1 | Criar `manual-portador.html` | Template base + conteúdo convertido | ⏳ |
| 2 | Adicionar CSS para manual | Estilos específicos em style.css | ⏳ |
| 3 | Atualizar sidebar no index.html | Adicionar link para o Manual | ⏳ |
| 4 | Atualizar sidebar no manual-portador.html | Manter consistência | ⏳ |
| 5 | Testar navegação | Desktop + Mobile | ⏳ |

---

## Fluxo da Família Pioneira

```
1. Família recebe link do site
2. Abre index.html
3. Vê "📖 Manual do Portador" como PRIMEIRO item
4. Lê o manual completo
5. Volta para as lições (🌱 Ciclo Sementes)
6. Começa pela Lição 000
```

---

## Decisão

**Status:** ⏳ AGUARDANDO APROVAÇÃO DO MAESTRO

**Perguntas:**
1. Aprovar integração no site existente?
2. Ícone 🔥 (tocha) ou 📖 (livro) para o Manual?
3. Criar também versão PDF para download?

---

*Deliberação conduzida pelo Orchestrator v1.5*
