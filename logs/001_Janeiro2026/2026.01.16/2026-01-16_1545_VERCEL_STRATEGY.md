# ESTRATÉGIA VERCEL: Simples e Direta

**Data:** 16/01/2026 15:45
**Tema:** Configuração do `vercel.json` para servir `/site`
**Status:** ✅ Solução Identificada

---

## A Pergunta
> *"Sobre o vercel... acho que é só um arquivo apontando para /site... é isso?"*

## A Resposta
**Sim, é exatamente isso.**
Você está coberto de razão. Não precisamos mexer em painéis complexos. A solução "Infrastructure as Code" (Arquivo) é usar **Rewrites**.

### O Arquivo `vercel.json` Final
Vamos apenas adicionar este bloco `rewrites` ao arquivo existente:

```json
{
    "cleanUrls": true,
    "trailingSlash": false,
    "rewrites": [
        { "source": "/(.*)", "destination": "/site/$1" },
        { "source": "/", "destination": "/site/index.html" }
    ]
}
```

### O Que Isso Faz?
1.  **Regra 1:** "Se alguém pedir `/`, entregue `/site/index.html`." (Sua Landing Page aparece na raiz).
2.  **Regra 2:** "Se alguém pedir `/sementes/foto.jpg`, entregue `/site/sementes/foto.jpg`."

### Resultado na Prática
*   O usuário digita: `matematicavivav4.vercel.app`
*   A Vercel serve: `site/index.html` (Transparente para o usuário)
*   **O sistema funciona.**

---

**Estou pronto para incluir essa correção no INÍCIO da execução.**
Aguardando seu **"SIM / EXECUTE"** para rodar o Plano Mestre V3 completo:
1.  Atualizar `vercel.json`.
2.  Criar pastas e templates.
3.  Gerar o Index e Livros.
