# PLANEJAMENTO MESTRE: Integração do Grande Portal (V3)

**Data:** 16/01/2026 15:30
**Objetivo:** Elaborar o roteiro técnico e estrutural definitivo para o `index.html` e o Livro Dourado, validando a estratégia de automação Python e a diferenciação de formatos.
**Status:** 🚧 Planejamento Final (AGUARDANDO GO - NÃO EXECUTAR)

---

## 1. Visão Geral Validada

O Maestro confirmou a direção:
*   **Index Dinâmico Inteligente:** O script Python vai varrer as pastas e montar o Index baseada na **realidade** (O que está pronto, aparece "Ativo"; o que não está, aparece "Em Breve").
*   **Livro Dourado é "Artefato Atípico":** Não é lição, não segue template padrão. É HTML customizado (Living Book), tratado como uma obra de arte única.
*   **Sidebar Unificada:** Brotos, Sementes, Raízes, Lógica, Legado, Blog, Livros. Tudo acessível.

---

## 2. Detalhamento Técnico das Frentes

### Frente A: O Motor de Landing (`landing_forge.py`)
Criaremos um novo módulo em `build/fases/landing.py` (ou integrado ao `forge.py`) que:

1.  **Escaneamento:**
    *   Lê `curriculo/*` para saber o que *deveria* existir (Meta-dado).
    *   Lê `site/*` para saber o que *realmente* existe (Realidade).
2.  **Lógica de Renderização do Index:**
    *   Se `site/sementes/MV-S-001...html` existe -> Card ganha Link e classe `ativo` (Cor viva).
    *   Se não existe (ex: Raízes) -> Card ganha Link para `placeholders/raizes.html` e classe `em-breve` (Tom pastel/cinza).
3.  **Benefício:** Você nunca precisa editar o `index.html` manualmente para "liberar" uma lição. Buildou? Apareceu.

### Frente B: Estrutura de Pastas & Placeholders
Vamos criar a "Arquitetura da Casa" completa, mesmo que os quartos estejam vazios:

```text
site/
├── index.html (Gerado)
├── placeholders/          <-- [NOVO]
│   ├── brotos.html
│   ├── raizes.html
│   ├── logica.html
│   └── legado.html
├── sementes/ (Lições Reais)
├── blog/ (Artigos Reais)
└── livros/ (Livros Dourados)
```

**Template do Placeholder:**
*   Design limpo, focado no Guardião do ciclo (ex: Coruja para Lógica).
*   Mensagem acolhedora: "O Reino de Lógica está sendo forjado. Aguarde as corujas."
*   Botão "Voltar para o Salão Principal".

### Frente C: O "Livro Dourado" (HTML Puro)
Como é um caso atípico (HTML rico, narrativa visual, não-lição), faremos o seguinte:

1.  **Origem:** `curriculo/90_LIVRO_DOURADO/*.md`
2.  **Processamento:** Um script `build/fases/livros.py` que é mais flexível:
    *   Converte Markdown para HTML.
    *   Permite injeção de classes CSS específicas (ex: `.fundo-sepia`, `.fonte-manuscrita`) direto no Markdown ou via frontmatter.
    *   **Template Especial:** `site/templates/livro.j2` (Sem sidebar de navegação de lição, foco total na leitura imersiva. Tipo "Medium" ou "Substack" mas com estética Belle Époque).
3.  **Resultado:** `site/livros/santos-dumont-cap1.html`.

### Frente D: Alinhamento Narrativo (O 3º Arquivo)
Criaremos `curriculo/90_LIVRO_DOURADO/ALINHAMENTO_TECNICO.md` para unificar a visão do `CONCEITO` e `CONSELHO`:
*   Definir que *tecnicamente* o Livro é um artefato agnóstico de template de lição.
*   Documentar que as imagens misturam Aquarela + Blueprint (CSS classes: `.img-aquarela`, `.img-blueprint`).

---

## 3. O Arquivo de Planejamento (Este Documento)

Esta é a síntese. Se aprovado, a execução seguirá esta ordem exata:

1.  **Criar Pastas:** `site/placeholders`, `site/livros`, `curriculo/00_BROTOS` etc.
2.  **Criar Templates:**
    *   `placeholder.j2` (Simples)
    *   `livro.j2` (Imersivo)
    *   `index.j2` (Dashboard Dinâmico)
3.  **Codar Builders:**
    *   Atualizar `forge.py` para incluir fases `landing` e `livros`.
4.  **Rodar Build:** Ver a mágica acontecer.

---

## 4. Decisão Final

Maestro, o plano **V3** está traçado. Ele respeita a complexidade única do Livro Dourado e a necessidade de automação do Index.

**Posso iniciar a execução pela Criação das Pastas e Templates?**
