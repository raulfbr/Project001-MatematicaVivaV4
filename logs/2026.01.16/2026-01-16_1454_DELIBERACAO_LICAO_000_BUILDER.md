# DECISÃO: Lição 000 e Padrão de Onomatopeias

**Data/Hora:** 16/01/2026 15:00
**Status:** ✅ DELIBERAÇÃO AUTÔNOMA CONCLUÍDA
**Referências:** north_star.yaml, engenharia.yaml (SSOT, Clean Code)

---

## DECISÃO 1: Excluir L000 do Build

### ✅ SOLUÇÃO ESCOLHIDA: Mover para pasta separada

**Ação:** Mover `000_PORTAL_REINO.yaml` para `curriculo/01_SEMENTESV6/_MANUAIS/`

**Justificativa (Eric Evans - SSOT/Bounded Contexts):**
- Cria fronteira clara: `_MANUAIS/` = lições atípicas editadas à mão
- Builder ignora `_*` automaticamente (padrão meta-arquivos)
- Preserva o YAML como documentação
- Zero código novo no builder

**Alternativa descartada:** Flag no YAML
- Viola KISS (Keep It Simple)
- Requer código extra no builder

---

## DECISÃO 2: Onomatopeias [entre colchetes]

### ✅ SOLUÇÃO ESCOLHIDA: Campo `pre_instrucao` no script do YAML

**Formato futuro no YAML:**
```yaml
fala_guardiao:
  tom: firme
  pre_instrucao: "Bata os pés no chão imitando passos pesados"
  script: |
    "Ouça o passo firme na terra...
    É o Urso Bernardo!"
```

**Justificativa (Clean Code + YAML Lean):**
- Separação de responsabilidades: instrução ≠ narrativa
- Template renderiza `pre_instrucao` como caixa antes da fala
- Sem parsing complexo de `[...]`
- Explícito > implícito

**Para a L000 (manual):** Ajustar diretamente no HTML já gerado.

---

## DECISÃO 3: Atualizar Template?

### ✅ SOLUÇÃO: Atualizar _TEMPLATE_V6.yaml

Adicionar campo opcional `pre_instrucao` nas falas de guardião.

**Impacto:** Zero nas lições existentes (campo opcional).

---

## AÇÕES A EXECUTAR

1. [ ] Criar pasta `curriculo/01_SEMENTESV6/_MANUAIS/`
2. [ ] Mover `000_PORTAL_REINO.yaml` para `_MANUAIS/`
3. [ ] Adicionar campo `pre_instrucao` ao `_TEMPLATE_V6.yaml`
4. [ ] Testar build para confirmar que L001/L002 ainda funcionam

---

## RESUMO PARA O MAESTRO

| Decisão | Ação | Esforço |
|:---|:---|:---|
| Excluir L000 | Mover para `_MANUAIS/` | ⚡ 1 min |
| Onomatopeias futuras | Campo `pre_instrucao` no YAML | 🔧 5 min |
| L000 onomatopeias | Ajuste manual no HTML | ✋ Manual |

**Posso executar?**
