# 📐 PLANO: [Nome Descritivo]

**Data**: YYYY-MM-DD HH:MM  
**Baseado em**: [_Projeto/pesquisas/arquivo.md]  
**Classificação**: `quick` | `medium` | `strategic`  
**Aprovador requerido**: Humano | Charlotte Mason | N/A

---

## Visão Geral
[O que vamos implementar e por quê — 2-3 parágrafos]

---

## Análise do Estado Atual
[Resumo da pesquisa que embasa este plano]

### Pontos-chave:
- [Descoberta 1 da pesquisa]
- [Descoberta 2 da pesquisa]
- [Limitação atual]

---

## Estado Desejado
[Como ficará o sistema após implementação]

### Critérios de Sucesso:
- [ ] [Critério verificável 1]
- [ ] [Critério verificável 2]
- [ ] [Critério verificável 3]

---

## O que NÃO Estamos Fazendo
> ⛔ Escopo explícito do que está FORA deste plano

- [ ] [Item fora de escopo 1]
- [ ] [Item fora de escopo 2]
- [ ] [Melhoria futura não incluída]

---

## Experts Consultados

| Expert | Posição | Veto? | Justificativa |
|--------|---------|-------|---------------|
| `charlotte_mason` | "..." | ❌ Não | ... |
| `jerome_bruner` | "..." | ❌ Não | ... |
| [externo se strategic] | "..." | ⚠️ WARN | ... |

---

## Fase 1: [Nome Descritivo]

### Objetivo
[O que esta fase alcança — 1-2 frases]

### Arquivos Afetados

| Arquivo | Ação | Descrição |
|---------|------|-----------|
| `path/file.py` | MODIFY | [O que muda] |
| `path/new.yaml` | CREATE | [O que cria] |
| `path/old.md` | DELETE | [Por que remove] |

### Mudanças Específicas

#### `path/file.py`
```python
# ANTES (linha X-Y)
código_antigo()

# DEPOIS
código_novo()
```

#### `path/new.yaml`
```yaml
# Conteúdo do novo arquivo
campo: valor
```

### Verificação Automatizada
- [ ] Comando 1: `python script.py` — Resultado esperado
- [ ] Comando 2: `make check` — Sem erros
- [ ] Comando 3: `yamllint file.yaml` — YAML válido

### Verificação Manual
- [ ] Passo 1: Abrir [URL/arquivo]
- [ ] Passo 2: Verificar [comportamento]
- [ ] Passo 3: Confirmar [resultado esperado]

### ⏸️ Checkpoint
> **PAUSAR AQUI para verificação humana antes da Fase 2**

---

## Fase 2: [Nome Descritivo]

### Objetivo
[...]

### Arquivos Afetados
[...]

### Mudanças Específicas
[...]

### Verificação Automatizada
[...]

### Verificação Manual
[...]

### ⏸️ Checkpoint
[...]

---

## Fase 3: [Nome — se necessário]
[Mesma estrutura...]

---

## Estratégia de Testes

### Testes Automáticos
| Teste | Comando | Critério |
|-------|---------|----------|
| Build | `python build/build.py` | Sem erros |
| Lint | `yamllint .` | 0 warnings |
| [Outro] | `...` | ... |

### Testes Manuais
1. [ ] [Passo de teste 1]
2. [ ] [Passo de teste 2]
3. [ ] [Caso de borda a verificar]

---

## Plano de Rollback
> 🔙 Como reverter se algo der errado

1. [ ] Restaurar `file.py` de backup/git
2. [ ] Deletar arquivos criados: `path/new.yaml`
3. [ ] Comando de verificação pós-rollback

---

## Riscos Identificados

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| [Risco 1] | Baixa | Alto | [Ação] |
| [Risco 2] | Média | Médio | [Ação] |

---

## Referências

| Tipo | Arquivo |
|------|---------|
| Pesquisa | `_Projeto/pesquisas/YYYY-MM-DD_tema.md` |
| LORE | `LORE/north_star.yaml` |
| Workflow | `.bmad/workflows/criar-licao-premium.yaml` |
| Expert | `.bmad/experts/[conselho]/[expert].yaml` |

---

## Histórico de Aprovação

| Data | Aprovador | Status | Notas |
|------|-----------|--------|-------|
| YYYY-MM-DD | [Nome] | ⏳ Pendente | - |

---

> ⚠️ **LEMBRETE**: Este plano só deve ser executado APÓS aprovação.  
> Use `/executar plano.md` quando aprovado.
