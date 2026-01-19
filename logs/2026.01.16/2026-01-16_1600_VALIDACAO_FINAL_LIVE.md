# VALIDAÇÃO FINAL: V4 vs FORJA VIVA (Execution Masterplan)

**Data:** 16/01/2026 16:00
**Referência:** `https://forja-viva.vercel.app/` (O Padrão Ouro Visual)
**Status:** 🟢 EM EXECUÇÃO

---

## 1. O Padrão Visual (A Promessa)
O objetivo é replicar **exatamente** a experiência estética do dashboard atual, porém com um backend inteligente.

*   **Design:** Mantido 100% (Sidebar escura, Cards elegantes, Tipografia clássica).
*   **UX:** Mantida 100% (Navegação rápida, Links diretos).
*   **Impecabilidade:** Zero links quebrados. Se não existe, é "Em Breve" (Placeholder).

## 2. A Arquitetura Invisível (A Solução)

Para entregar esse visual sem trabalho manual, implementaremos o seguinte sistema:

### A. Infraestrutura Vercel (`vercel.json`)
Configuração de **Rewrites** para servir a pasta `/site` como raiz. Simples, limpo, robusto.

### B. O Motor de Construção (`forge.py`)
O Python se torna o "Arquiteto" que monta o HTML line-by-line:
1.  **Landing Driver:** Lê o estado real do projeto e desenha o `index.html`.
2.  **Livros Driver:** Transforma os Markdowns do Livro Dourado em páginas HTML "Living Books".
3.  **Placeholders:** Garante que cada botão da Sidebar leve a um destino válido.

### C. Estrutura de Pastas (O Reino)
```text
site/
├── index.html          <-- Gerado dinamicamente (Dashboard)
├── sementes/           <-- Lições Reais (L000-L002)
├── placeholders/       <-- Páginas "Em Breve" (Brotos, Raízes...)
├── livros/             <-- O Menino Bento (HTML Imersivo)
└── assets/             <-- Imagens e Estilos centralizados
```

## 3. Roteiro de Execução Imediata

1.  **Config**: Atualizar `vercel.json`.
2.  **Skeleton**: Criar pastas `curriculo/00_BROTOS`, `site/placeholders`, etc.
3.  **Templates**: Criar `index.j2` (baseado no HTML atual), `livro.j2` e `placeholder.j2`.
4.  **Code**: Implementar `landing.py` e `livros.py`.
5.  **Deploy**: Rodar Build e Validar.

---

**CONFIRMADO:** O design será preservado. A automação será total.
**INICIANDO EXECUÇÃO.**
