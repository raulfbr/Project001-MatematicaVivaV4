# PLANEJAMENTO INTEGRADO: O Grande Portal Matemática Viva

**Data:** 16/01/2026 15:20
**Tema:** Unificação Impecável do Index, Blog e Currículos Expandidos
**Status:** 🚧 Aguardando Decisão (NÃO EXECUTAR)

---

## 1. O Objetivo: "Uma Única Casa"

Atualmente, o `index.html` é um painel estático manual. O objetivo é transformá-lo no **Grande Portal do Reino**, gerado dinamicamente ou estruturado para acomodar:
1.  **Ciclo Sementes** (Já ativo: L000-L002)
2.  **Blog/Ensaios** (Atualmente placeholder)
3.  **Livros Dourados** (Santos Dumont)
4.  **Novas Fronteiras** (Brotos, Raízes, Lógica, Legado)

---

## 2. A Visão dos Especialistas

### 🏛️ Charlotte Mason (Pedagogia)
> *"Education is an Atmosphere."*
>
> 1.  **O Index não pode ser um "painel administrativo".** Ele deve ser o **Saguão do Reino**. A criança (ou pai) deve sentir que está entrando em um lugar vivo.
> 2.  **Blog como "Educação de Pais":** Os artigos "Por que seu filho não ama matemática" são fundamentais para educar os pais (Princípio: Parents and Children). Eles devem ter destaque nobre, não rodapé.
> 3.  **Livros Dourados:** A biografia de Santos Dumont é "Living Idea" pura. Deve ser apresentada como um tesouro, um livro na estante, não apenas um link.

### ⚙️ Engenharia & BMAD (Técnica)
> *"Single Source of Truth & Automation"*
>
> 1.  **O Index atual mente:** Ele lista lições (003-015) que *não existem* no build atual. Isso viola a integridade.
> 2.  **Proposta de Automação:** O `forge.py` deve ter um módulo `LandingForge` que lê o que *realmente foi buildado* e gera o `index.html`. Se a lição não existe, ela não aparece (ou aparece como "Coming Soon" sem link quebrado).
> 3.  **Arquitetura do Blog:** Tratar Artigos como "Lições de Texto". Parsear Markdown -> HTML usando o mesmo CSS base, mas com layout de leitura (sem sidebar de navegação de lição).

---

## 3. Inventário do Que Temos

| Seção | Estado Atual | Ação Necessária |
|:---|:---|:---|
| **Sementes** | 3 lições prontas (L000, L001, L002) | Automatizar listagem no Index. |
| **Blog** | 2 arquivos MD (`ama-matematica`, `mentira-exatas`) | Criar `blog_forge.py` para gerar HTML. |
| **Livros Dourados** | 1 arquivo MD (`SANTOS_DUMONT`) | Definir template "Livro" e gerar HTML. |
| **Brotos** | Inexistente (Pasta física) | Criar estrutura `curriculo/00_BROTOS`? |
| **Raízes/Lógica** | Pastas vazias em `site/` | Definir se exibimos "Em Breve" ou ocultamos. |
| **Legado** | Pasta com templates | Decidir o que migrar ou linkar. |

---

## 4. O Plano de Batalha (Draft)

Se aprovado, executaremos em 4 ondas:

### Onda 1: O Motor de Blog & Livros
*   Criar `build/fases/blog.py`: Lê `blog/*.md`, aplica template de leitura, gera `site/blog/*.html`.
*   Criar `build/fases/livros.py`: Lê `curriculo/90_LIVRO_DOURADO/*.md`, gera páginas de "Livro Vivo".

### Onda 2: A Verdade do Index
*   Criar template `site/templates/index.j2`.
*   Atualizar `forge.py`: Ao final do build, ele escaneia todas as pastas `site/*` (sementes, blog, livros) e gera o `index.html` com links REAIS.
*   **Resultado:** Nunca mais teremos links quebrados.

### Onda 3: Expansão de Estrutura
*   Criar pastas oficiais para `curriculo/00_BROTOS`, `curriculo/03_LOGICA`.
*   Adicionar placeholders simples nessas pastas (ex: `000_INTRO.md`) só para "povoar" o site.

### Onda 4: Estética Impecável (Charlotte Mason)
*   Revisar o CSS do Index/Blog para garantir que não pareça um "painel de controle", mas sim uma **Biblioteca Viva**.

---

## 5. Perguntas para o Maestro (VOCÊ DECIDE)

Para prosseguir com o "Não Execute Nada, Apenas Planeje", preciso das suas diretrizes sobre estes pontos cruciais:

**Q1. Index: Verdade ou Promessa?**
*   (A) **Dinâmico (Verdade):** O Index só mostra o que *realmente existe* e foi buildado (L000-L002, 2 posts). Links garantidos.
*   (B) **Estático (Promessa):** Mantemos o Index manual atual visualizando o futuro (L000-L015), mesmo que os links 003+ dêem 404 por enquanto.
*   *Recomendação Engenharia: A (Impecabilidade).*

**Q2. Livros Dourados (Santos Dumont):**
*   Ele deve ser lido como um **Artigo** (texto corrido) ou como uma **Lição** (com passos, atividades, guardiões)?
*   Se for Lição, preciso de um YAML para ele. Se for Texto, uso o Markdown direto.

**Q3. Brotos & Legado:**
*   Brotos é prioridade agora? Devo criar a pasta `curriculo/00_BROTOS`?
*   O que fazemos com o Legado? Apenas um link para "Arquivos Antigos" ou vamos importar conteúdo?

**Q4. Blog:**
*   Posso usar o layout padrão `base.j2` (cabeçalho, rodapé) para o Blog, ou você quer um design distinto (tipo "Jornal" ou "Carta")?

---

**Aguardando suas ordens.** O arquivo de log foi gerado. Nada foi executado.
