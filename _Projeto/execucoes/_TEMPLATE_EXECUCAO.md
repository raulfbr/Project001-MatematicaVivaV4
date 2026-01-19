# ⚒️ EXECUÇÃO: [Nome do Plano]

**Data Início**: YYYY-MM-DD HH:MM  
**Data Fim**: [preenchido ao final]  
**Plano Base**: [_Projeto/planos/arquivo.md]  
**Executor**: [Nome IA]

---

## Status Geral

| Fase | Nome | Status | Início | Fim |
|------|------|--------|--------|-----|
| 1 | [...] | ⏳ Pendente | - | - |
| 2 | [...] | ⏳ Pendente | - | - |
| 3 | [...] | ⏳ Pendente | - | - |

**Legenda**: ✅ Completa | 🔄 Em Progresso | ⏳ Pendente | ❌ Bloqueada | 🔙 Rollback

---

## Fase 1: [Nome]

**Status**: 🔄 Em Progresso  
**Início**: YYYY-MM-DD HH:MM

### Ações Planejadas vs Executadas

| # | Ação Planejada | Status | Notas |
|---|----------------|--------|-------|
| 1 | Modificar `file.py` | ✅ | Linhas 23-45 |
| 2 | Criar `new.yaml` | ✅ | 35 linhas |
| 3 | Rodar testes | ❌ | BLOQUEADO: [motivo] |

### Verificação Automatizada

| Teste | Comando | Status | Output |
|-------|---------|--------|--------|
| Build | `python build/build.py` | ✅ | Sem erros |
| Lint | `yamllint .` | ⚠️ | 2 warnings (ignoráveis) |

### Verificação Manual Requerida

> 🔔 **Humano**: Por favor execute:
1. [ ] Abrir `site/index.html` no navegador
2. [ ] Verificar se cards aparecem corretamente
3. [ ] Testar navegação entre lições
4. [ ] Responder abaixo: ✅ OK ou ❌ Problema

**Resposta do Humano**: [aguardando]

### Divergências Encontradas

| # | Esperado (Plano) | Encontrado (Realidade) | Impacto | Ação Tomada |
|---|------------------|------------------------|---------|-------------|
| 1 | Arquivo X existe | Não existia | Médio | Criado novo |
| 2 | Função Y retorna Z | Retorna W | Baixo | Adaptado código |

### Decisões de Implementação

> 💡 Decisões tomadas durante a execução que diferem do plano

1. **[Decisão]**: [Justificativa]
2. **[Decisão]**: [Justificativa]

### Fim Fase 1
**Conclusão**: YYYY-MM-DD HH:MM  
**Status Final**: ✅ Aprovada para prosseguir

---

## Fase 2: [Nome]

**Status**: ⏳ Aguardando Fase 1  
**Início**: -

### Ações Planejadas vs Executadas
[...]

### Verificação Automatizada
[...]

### Verificação Manual Requerida
[...]

### Divergências Encontradas
[...]

### Fim Fase 2
[...]

---

## Fase 3: [Nome — se houver]
[Mesma estrutura...]

---

## Resumo Final

### Métricas

| Métrica | Valor |
|---------|-------|
| Fases completadas | X/Y |
| Tempo total | HH:MM |
| Divergências tratadas | N |
| Rollbacks necessários | 0 |

### Arquivos Modificados

| Arquivo | Ação | Linhas | Commit |
|---------|------|--------|--------|
| `file1.py` | MODIFY | +25, -10 | abc123 |
| `file2.yaml` | CREATE | 35 | abc123 |

### Testes Passados

- [x] Build: `python build/build.py`
- [x] Lint: `yamllint .`
- [x] Manual: Verificação visual OK
- [ ] [Teste pendente]: [motivo]

---

## Próximos Passos

> 📋 Se execução incompleta, o que falta?

1. [ ] [Próximo passo 1]
2. [ ] [Próximo passo 2]
3. [ ] [Ação de follow-up]

---

## Log de Atividades

| Timestamp | Ação | Resultado |
|-----------|------|-----------|
| HH:MM | Iniciada Fase 1 | - |
| HH:MM | Modificado file.py | ✅ |
| HH:MM | Criado new.yaml | ✅ |
| HH:MM | Teste build | ✅ |
| HH:MM | Aguardando verificação humana | ⏳ |

---

## Notas do Executor
[Observações pessoais, aprendizados, sugestões para próxima vez]

---

> ✅ **EXECUÇÃO CONCLUÍDA**: [SIM/NÃO]  
> **Plano atualizado com checkmarks**: [SIM/NÃO]  
> **Pronto para próximo ciclo**: [SIM/NÃO]
