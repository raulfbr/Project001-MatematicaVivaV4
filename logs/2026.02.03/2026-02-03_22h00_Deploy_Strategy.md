# 🌍 Estratégia de Deploy: Manter Link Vercel Vivo + Sincronizar V4
**Data:** 03/02/2026 — 22:00
**Contexto:** Famílias usando link ativo (`matematicavivav4.vercel.app`) ligado ao repo `matematica-viva`. Trabalho local sendo feito no repo `Project001...`.

---

## 1. O Cenário Atual

| Componente | Status | Link/Conexão |
|------------|--------|--------------|
| **Link das Famílias** | 🟢 ONLINE de `matematica-viva` | `https://matematicavivav4.vercel.app/manual-portador` |
| **Repo Local** | 💻 Onde estamos trabalhando | `Project001-MatematicaVivaV4` |
| **Repo Remoto 1** | `origin` (Atual Vercel) | `github.com/raulfbr/matematica-viva` |
| **Repo Remoto 2** | `origin_v4` (Futuro Oficial) | `github.com/raulfbr/Project001-MatematicaVivaV4` |

## 2. O Problema
Você precisa atualizar o **Manual do Portador** (adicionar o trecho "Tribo vs Audiência") e garantir que:
1.  O link da Vercel (que as famílias já têm) seja atualizado.
2.  O repositório novo (`Project001`) não fique defasado.

## 3. Análise dos Arquivos
Preciso verificar o `manual-portador.html` local para ver onde inserir o texto "Tribo vs Audiência".

## 4. A Estratégia Sugerida (Dual Push)

Não precisamos "migrar" o Vercel agora se o risco for quebrar o link. Podemos simplesmente alimentar **os dois** repositórios simultaneamente.

## 5. Discussão: Mudar Vercel ou Dual Push? (Análise Aprofundada)

Você perguntou: *"Seria talvez eu fazer esse projeto ir para o repositorio V4? e já resolveria?"*

**Análise dos Caminhos:**

### Caminho A: Migração Vercel (O "Oficial")
- **Ação:** Reconfigurar o painel da Vercel para ler o repo `Project001...`.
- **Pró:** Limpeza total. Um repo único.
- **Contra:** Risco de downtime se a configuração de pastas (`root directory`) estiver diferente. Exige acesso ao painel.

### Caminho B: Dual Push (O "Espelho Mágico" - RECOMENDADO AGORA) 🏆
- **Ação:** Enviar o código local (que já está perfeito) para o repo antigo (`matematica-viva`).
- **Pró:** Zero risco. A Vercel nem percebe que mudamos de máquina. O site atualiza instantaneamente.
- **Contra:** Mantemos um vínculo com o repo antigo (mas apenas como "canal de transmissão").

**Por que recomendo B agora?**
Porque seu objetivo imediato é *atualizar o conteúdo* sem dor de cabeça técnica. Podemos fazer a migração oficial (A) num segundo momento, com calma.

---

## 🚀 Plano de Ação Imediata (Status: PRONTO)
O arquivo `manual-portador.html` local já está **superior** ao que está online:
1.  ✅ **Bússola Rápida:** Integrada.
2.  ✅ **Seção Tribo:** Integrada.
3.  ✅ **Correções Técnicas:** Scripts adicionados.

**Só falta apertar o botão:**
1.  `git commit` (Salvar este estado perfeito).
2.  `git push` (Enviar para o mundo).

Estamos aguardando seu "Sinal Verde" para executar. 🟢

---

## 🚧 Próximos Passos para Execução
1.  [x] Ler `site/manual-portador.html` atual.
2.  [x] Adicionar/Ajustar o bloco inicial "Tribo vs Audiência". (Inserido com sucesso!)
3.  [ ] Confirmar se o visual está quebrado ou se precisa de CSS. (A classe `ph-bold` existe?)
4.  [ ] Executar o Push Duplo.

---

## 💬 Espaço para Discussão
(Aguardando sua confirmação sobre o texto exato da "Tribo" ou ordem dos passos)
