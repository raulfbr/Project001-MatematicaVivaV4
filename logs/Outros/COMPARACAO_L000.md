# Comparação: Lição 000 Existente vs. Gerada
> **Data:** 17/02/2026 | **Análise:** GLM-5 (Code Mode)

---

## 1. Visão Geral

| Aspecto | Versão Existente | Versão Gerada |
|---------|------------------|---------------|
| **Arquivo** | [`curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml`](curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml) | [`logs/L000_PORTAL_REINO_GERADO.yaml`](logs/L000_PORTAL_REINO_GERADO.yaml) |
| **Linhas** | ~300+ | ~200 |
| **Status** | `canonico` | `rascunho_gerado` |
| **Estrutura** | Mista (items/sections + campos) | Template V6.3 puro |

---

## 2. Pontos Fortes da Versão Existente

### 2.1 Narrativa Mais Rica
- **Mais falas do Melquior**: A versão existente tem 5 blocos de fala do Melquior, cada um com mais detalhes
- **Backstory do Reino**: Inclui a história da criação do Reino pelo "Grande Rei"
- **Frase canônica**: Inclui "Eu sabia que você viria" (frase canônica do Melquior de [`LORE/guardioes.yaml`](LORE/guardioes.yaml))

### 2.2 Descrições Sensoriais Mais Detalhadas
```yaml
# Versão Existente
"O ar cheira a terra molhada e musgo fresco. O sol dourado aquece o rosto. 
Pássaros cantam ao longe. Em um banco de pedra antiga, sentado com as patas 
cruzadas, está um grande Leão de juba dourada. Ele sorri ao ver você chegar."
```

### 2.3 Cards dos Locais
- Inclui **Cards dos 5 Locais** como material essencial
- A versão gerada não menciona Cards de Locais

### 2.4 Detalhes dos Guardiões
- **Noé**: "Olhos como duas luas amarelas"
- **Celeste**: "Vulto laranja que corre entre as árvores"
- **Bernardo**: "Tum-tum-arrasta" (som característico da mancadura)
- **Íris**: "Colar de contas brilhando"

---

## 3. Pontos Fortes da Versão Gerada

### 3.1 Auditoria QA Completa
- Seção `auditoria_qa` preenchida com evidências
- Validação contra CM, CPA, Narrativa, Template, Tríade e Inclusão
- Status de cada critério documentado

### 3.2 Estrutura Mais Limpa
- Segue o Template V6.3 de forma mais direta
- Menos aninhamento de estruturas
- Mais fácil de processar programaticamente

### 3.3 Seção `para_familia` Mais Completa
- Inclui `reflexao_espiritual` com conexão teológica
- Inclui `espiral` com progressão K-12
- Inclui `diario_portador` com perguntas de reflexão

### 3.4 Adaptação Bernardo Mais Explícita
- Inclui variações para deficiência visual, auditiva e mobilidade
- Mais alinhado com o "Princípio Bernardo" de inclusão

---

## 4. Diferenças Estruturais

### 4.1 Formato da Jornada

**Versão Existente:**
```yaml
jornada:
  narrativa_principal:
    - section: A Jornada
      items:
        - item: fala_guardiao
          guardiao: melquior
          card_img: melquior-leao.png
          tone: acolhedor
          text: |
            "Aproxime-se..."
```

**Versão Gerada:**
```yaml
jornada:
  narrativa_principal:
    - titulo: 'O Convite de Melquior'
      local: jardim_central
      fala_guardiao:
        guardiao: melquior
        tom: acolhedor
        script: |
          "Aproxime-se..."
```

### 4.2 Clima

| Versão | Clima | Justificativa |
|--------|-------|---------------|
| Existente | `ensolarado` | Clima padrão de alegria |
| Gerada | `primaveril` | "Renovação, novos começos" - mais adequado para primeira lição |

---

## 5. Recomendações de Fusão

### 5.1 Manter da Versão Existente
1. **Narrativa rica** com backstory do Reino
2. **Frase canônica** "Eu sabia que você viria"
3. **Cards dos Locais** como material
4. **Descrições sensoriais** detalhadas
5. **Detalhes dos Guardiões** (olhos de Noé, mancadura de Bernardo, colar de Íris)

### 5.2 Adicionar da Versão Gerada
1. **Auditoria QA** completa
2. **Seção `para_familia`** expandida com reflexão espiritual e espiral
3. **Diário do Portador** com perguntas de reflexão
4. **Adaptação Bernardo** mais explícita
5. **Clima `primaveril`** (mais adequado para "novo começo")

### 5.3 Ajustes Sugeridos
1. **Unificar estrutura**: Usar formato mais limpo da versão gerada, mas manter riqueza narrativa da existente
2. **Adicionar Cards de Locais**: Incluir na seção `preparacao.materiais`
3. **Manter frase canônica**: "Eu sabia que você viria" é essencial para consistência LORE

---

## 6. Checklist de Validação

| Critério | Existente | Gerada | Recomendação |
|----------|-----------|--------|--------------|
| Ideia Viva presente | SIM | SIM | Manter |
| Narração incluída | SIM | SIM | Manter |
| Lição <=20min | SIM | SIM | Manter |
| Concreto presente | SIM (vivência) | SIM (ritual) | Fundir |
| Pictórico vetado | SIM | SIM | Manter |
| Frase canônica | SIM | Parcial | Adicionar |
| Tom Lewis | SIM | SIM | Manter |
| Consistência Tolkien | SIM | SIM | Manter |
| Adaptação Bernardo | Básica | Completa | Usar gerada |
| Auditoria QA | Não | SIM | Adicionar |
| Cards de Locais | SIM | Não | Adicionar |

---

## 7. Próximos Passos

1. **Criar versão fusionada** combinando pontos fortes de ambas
2. **Validar com Maestro** (Raul)
3. **Mover para pasta oficial** se aprovado
4. **Usar como template** para geração de L001-L020

---

## 8. Conclusão

A **versão existente** tem uma narrativa mais rica e detalhada, com elementos sensoriais que criam uma imersão mais profunda. A **versão gerada** tem uma estrutura mais limpa, auditoria QA completa, e melhor documentação para o Portador.

**Recomendação final**: Fundir as duas versões, mantendo a riqueza narrativa da existente e adicionando a estrutura de QA e documentação da gerada.