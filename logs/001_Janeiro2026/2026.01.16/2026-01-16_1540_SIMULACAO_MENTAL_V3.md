# SIMULAÇÃO MENTAL: O Teste de Estresse do Plano V3

**Data:** 16/01/2026 15:40
**Objetivo:** Rodar o processo inteiro na "mente da IA" para garantir que o Index vai funcionar na Vercel (`matematicavivav4.vercel.app`).
**Status:** 🧠 Simulação em Andamento (NÃO EXECUTAR CÓDIGO)

---

## 1. O Cenário de Deploy (Vercel)

*   **Fato:** O arquivo `vercel.json` está na raiz e é simples (apenas config de URL).
*   **Fato:** A Vercel geralmente serve a raiz do repositório ou uma pasta `public`/`site` se configurada.
*   **Crítico:** Atualmente, o `forge.py` gera tudo dentro de `site/`.
*   **Risco Detectado na Simulação:** Se a Vercel estiver configurada para ler a raiz `./`, ela vai procurar um `index.html` na RAIZ do projeto, mas nós estamos gerando em `site/index.html`.
*   **Solução Necessária:** Precisamos garantir que nas configurações da Vercel (dashboard) o "Output Directory" esteja definido como `site` OU movermos o output final para a raiz.
    *   *Melhor Prática:* Manter em `site/` (para não sujar a raiz) e configurar Vercel para ler `site`. **(Assumindo que isso já foi feito no deploy anterior que funcionou).**

---

## 2. A Simulação do Build (`forge.py`)

Vamos imaginar o terminal rodando:

### Passo 1: `python build/forge.py --all`
1.  **Fase 1: Sementes Driver**
    *   Lê `curriculo/01_SEMENTES/*.yaml`.
    *   Encontra L001, L002.
    *   Gera `site/sementes/MV-S-001.html`.
    *   *Check:* Arquivos existem. ✅

### Passo 2: `[NOVO] Livros Driver`
1.  Lê `curriculo/90_LIVRO_DOURADO/*.md`.
2.  Usa `site/templates/livro.j2` (Novo).
3.  Gera `site/livros/santos-dumont-cap1.html`.
4.  *Check:* Arquivo existe e é puro HTML. ✅

### Passo 3: `[NOVO] Landing Driver` (O Grande Maestro)
1.  **Scanner:**
    *   Vê `site/sementes/` -> Tem conteúdo? Sim (L001). -> Status **ATIVO**.
    *   Vê `site/raizes/` -> Tem conteúdo? Não. -> Status **EM BREVE**.
    *   Vê `site/livros/` -> Tem conteúdo? Sim. -> Status **ATIVO**.
2.  **Gerador de Index:**
    *   Pega `site/templates/index.j2` (Novo, com a Sidebar completa).
    *   Injeta os dados do Scanner.
    *   Renderiza `site/index.html`.
3.  **Gerador de Placeholders:**
    *   Para cada ciclo vazio (Raízes, Broto...), gera `site/placeholders/raizes.html` usando `placeholder.j2`.

---

## 3. A Experiência do Usuário (Navegação)

1.  **Usuário acessa `matematicavivav4.vercel.app`**
    *   *Vercel:* Serve `site/index.html`.
    *   *Visual:* Vê a Sidebar completa (Brotos até Legado).
2.  **Clica em "Ciclo Sementes"**
    *   Rola até a seção Sementes (já ativa).
    *   Clica em "L001 Trindade". -> Abre `site/sementes/MV-S-001.html`. ✅
3.  **Clica em "Ciclo Raízes"**
    *   Link aponta para `placeholders/raizes.html`.
    *   Abre página bonita: "Urso Bernardo construindo...". ✅
    *   Botão "Voltar". -> Volta para `index.html`. ✅
4.  **Clica em "Livro Dourado"**
    *   Abre seção ou link direto.
    *   Clica em "O Menino Bento". -> Abre `site/livros/santos-dumont.html`.
    *   Design muda: Sem sidebar, foco na leitura (Imersão). ✅

---

## 4. Pontos de Atenção (Fail-safes)

Durante a simulação, identifiquei 3 pontos que precisam de cuidado no código:

1.  **Caminhos Relativos (`../../`):**
    *   O `index.html` está na raiz de `site/`.
    *   As lições estão em `site/sementes/`.
    *   Os Placeholders estarão em `site/placeholders/`.
    *   *Atenção:* O CSS `style.css` está em `site/`.
    *   *Correção:*
        *   Index usa `href="style.css"`
        *   Sementes usa `href="../style.css"`
        *   Placeholders usam `href="../style.css"`
    *   **Veredito:** O template Jinja precisa saber a "profundidade" da página para gerar o link do CSS corretamente.

2.  **Imagens dos Livros:**
    *   Se o markdown do livro tiver `![Imagem](assets/img.png)`, o HTML gerado vai procurar em `site/livros/assets/img.png`.
    *   *Solução:* Centralizar imagens em `site/assets/livros/` e garantir que o `forge.py` substitua os caminhos ou orientar o uso correto no Markdown.

---

## 5. Conclusão da Simulação

**O SITEMA PARA EM PÉ?**
Sim. A lógica é sólida.

**O INDEX VAI APARECER?**
Sim, desde que a Vercel esteja servindo a pasta `site/`. Se a Vercel estiver servindo a raiz do repo, precisaremos configurar o "Root Directory" na Vercel para `site` OU adicionar um script de move para a raiz no final do build (menos elegante).

**Recomendação Final:** Prossiga com o Plano V3. Ele é robusto.

*   *Arquivo de simulação gerado em: `logs/2026-01-16_1540_SIMULACAO_MENTAL_V3.md`*
*   *Pronto para execução.*
