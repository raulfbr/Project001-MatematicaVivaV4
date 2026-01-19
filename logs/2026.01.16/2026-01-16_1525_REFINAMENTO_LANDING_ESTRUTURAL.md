# REFINAMENTO INTEGRAL: O Grande Portal do Reino (V2)

**Data:** 16/01/2026 15:25
**Tema:** Expansão Estrutural Completa (Brotos, Sementes, Raízes, Lógica, Legado + Acervo)
**Status:** 🚧 Planejamento Refinado (NÃO EXECUTAR)
**Referência:** `.bmad/orchestrator.yaml`

---

## 1. Diretriz: "A Roda Já Gira"

O Maestro foi claro: **Não reinventar a roda.** O design atual está aprovado. O objetivo é pegar essa estrutura ("Sidebar Esquerda" + "Conteúdo Main") e expandi-la para abraçar todo o universo Matemática Viva, sem quebrar o que já funciona.

### Visão do Orchestrator (Engenharia + Design)
*   **Identidade Visual:** Manter o layout atual. Sidebar escura, emojis/ícones, área de conteúdo limpa.
*   **Arquitetura:** Index Estático (Promessa) vs Index Dinâmico.
    *   *Decisão Refinada:* Vamos criar **PLACEHOLDERS funcionais**. Em vez de 404, os links levam a páginas "Em Breve" bonitas com a identidade do ciclo. Isso mantém a "Promessa" visível mas sem ser quebrada (Impecabilidade).

---

## 2. A Nova Estrutura de Navegação (Sidebar)

A barra lateral será o mapa completo do Reino. Proposta de estrutura hierárquica:

### 🏰 Reino Contado (O Currículo)
*   **🌰 Ciclo Brotos (0-4 anos)**
    *   *Ícone:* Semente pequena / Bebê
    *   *Status:* Em Breve (Placeholder)
*   **🌱 Ciclo Sementes (5-6 anos)**
    *   *Ícone:* Broto verde
    *   *Status:* **ATIVO** (L000-L002)
*   **🌳 Ciclo Raízes (7-10 anos)**
    *   *Ícone:* Árvore robusta
    *   *Status:* Em Breve (Placeholder)
*   **🦉 Lógica & Retórica (11+ anos)**
    *   *Ícone:* Coruja / Pergaminho
    *   *Status:* Em Breve (Placeholder)

### 📜 Acervo Real (Conteúdo Rico)
*   **📝 Blog & Ensaios**
    *   *Status:* Ativo (2 artigos prontos para migrar)
    *   *Conteúdo:* "A Mentira de Exatas", "Por que seu filho não ama..."
*   **📖 Livros Dourados**
    *   *Status:* Ativo (Santos Dumont)
    *   *Formato:* Leitura Nobre (Artigo longo com imagens)

### 🏛️ Arquivos Antigos
*   **🏺 O Legado**
    *   *Status:* Arquivo Morto (Acesso somente leitura)
    *   *Conteúdo:* Material das versões anteriores (v1-v3)

---

## 3. Estratégia de Implementação (Passo a Passo)

Como solicitado, **NÃO executaremos agora**, mas este é o roteiro para quando o sinal verde for dado:

### Fase 1: Fundação de Diretórios (Estrutura)
Criar as pastas físicas para que o site reflita a realidade, mesmo que vazias:
*   `curriculo/00_BROTOS/`
*   `curriculo/02_RAIZES/`
*   `curriculo/03_LOGICA/`
*   `curriculo/99_LEGADO/`

### Fase 2: Templates de Placeholder ("Em Breve")
Criar um `placeholder.html` genérico mas bonito que recebe o nome do Ciclo e o Guardião responsável.
*   *Ex:* Ao clicar em "Raízes", vê-se uma página com o Urso Bernardo dizendo: "Estamos construindo as fundações..."

### Fase 3: Landing Page (Index.html)
Editar o `index.html` atual para incluir todos os links da Sidebar nova.
*   Manter o estilo CSS atual.
*   Adicionar as seções "Brotos", "Raízes", "Lógica" apenas como cards de chamada na home (ou manter foco em Sementes e deixar os outros só na sidebar).

### Fase 4: Integração de Conteúdo Real (Blog + Livros)
*   Usar o `forge.py` para gerar HTML estático dos markdowns do Blog e Livro Dourado.
*   O Index ganha uma seção "Últimas do Blog".

---

## 4. O Que Precisa Ser Decidido (Checklist do Maestro)

Para transformarmos este plano em código, confirme:

1.  **Sidebar Completa:** Aprova a lista (Broto, Semente, Raiz, Lógica, Legado, Blog, Livros)?
2.  **Abordagem "Em Breve":** Concorda em criar páginas de placeholder para os links não terem erro 404?
3.  **Livros Dourados:** Podemos tratar como um "Artigo Especial" (semelhante ao Blog, mas com design mais nobre)?

---

**Arquivo de Planejamento Gerado.** Aguardando ordem para início da construção.
