# 📐 PLANO: Pilotagem L001 - Identificando Esquerda e Direita

**Data**: 2026-01-17 04:45
**Baseado em**: `_Projeto/pesquisas/2026-01-17_licao_l001_piloto.md`
**Classificação**: `medium`
**Aprovador requerido**: Charlotte Mason (Simulado pelo Protocolo)

---

## Visão Geral
Conforme validado na fase de pesquisa, implementaremos a **Lição L001 (Identificando Esquerda e Direita)** do 1º Ano (Raízes I). Esta será a primeira lição criada seguindo estritamente o novo "Protocolo de Contexto Limpo" e o workflow `criar-licao-premium` v1.1.

O objetivo é duplo:
1. Entregar a lição L001 com excelência pedagógica (Selo Platinum).
2. Validar o fluxo de trabalho do Protocolo de Contexto Limpo.

---

## Análise do Estado Atual
- **Currículo Mestre**: Define L001 com Guardiã Celeste e foco em "Sentir o calor do sol no braço direito" (Ideia Viva Corporal).
- **Diretório Destino**: `curriculo/02_RAIZES/01_RAIZES_I/` existe e está limpo de arquivos L001.
- **Workflow**: `criar-licao-premium.yaml` disponível.

---

## Estado Desejado
Um arquivo `L001_IDENTIFICANDO_ESQUERDA_DIREITA.yaml` criado em `curriculo/02_RAIZES/01_RAIZES_I/` que:
1. Segue o schema padrão de lição V4.
2. Contém os metadados corretos do Currículo Mestre.
3. Passa na validação do script de build (`build_lessons.py`).
4. É renderizado corretamente no `site/index.html`.

### Critérios de Sucesso:
- [ ] Arquivo YAML criado em `curriculo/02_RAIZES/01_RAIZES_I/`.
- [ ] Build roda sem erros (`python build/build_lessons.py`).
- [ ] Card da lição aparece no `site/index.html` com ícone da Celeste.

---

## O que NÃO Estamos Fazendo
> ⛔ Escopo explícito do que está FORA

- [ ] Não estamos criando L002-L040.
- [ ] Não estamos alterando o `build_lessons.py` (engine), apenas usando-o.
- [ ] Não estamos criando ilustrações reais (usaremos placeholder ou descrição).

---

## Experts Consultados (Simulação)

| Expert | Posição | Veto? | Justificativa |
|--------|---------|-------|---------------|
| `charlotte_mason` | Avaral | ❌ Não | "A lição deve ser corporal, não abstrata. Use o corpo da criança como bússola." |
| `celeste` | Anfitriã | ❌ Não | "Pronta para guiar. O Norte começa no coração." |

---

## Fase 1: Criação Estrutural (YAML)

### Objetivo
Criar o arquivo YAML da lição com a estrutura pedagógica completa (PERD + Narrativa).

### Arquivos Afetados

| Arquivo | Ação | Descrição |
|---------|------|-----------|
| `curriculo/02_RAIZES/01_RAIZES_I/L001_IDENTIFICANDO_ESQUERDA_DIREITA.yaml` | CREATE | Conteúdo completo da lição |

### Mudanças Específicas

#### `L001_IDENTIFICANDO_ESQUERDA_DIREITA.yaml`
```yaml
id: L001
titulo: Identificando Esquerda e Direita
guardiao: celeste
fase: raizes_1
unidade: 1
contexto: "O Norte da Navegadora"
ideia_viva: "O corpo é a bússola: a direita é a mão da força, a esquerda é a mão do coração (para maioria)."
...
```

### Verificação Automatizada
- [ ] `python -c "import yaml; yaml.safe_load(open('.../L001_....yaml'))"` — YAML Válido

### ⏸️ Checkpoint
> Pausa para verificar se o conteúdo YAML está alinhado com o tom da Celeste.

---

## Fase 2: Build e Verificação Visual

### Objetivo
Integrar a lição ao site estático e validar a renderização.

### Ações
1. Rodar `python build/build_lessons.py`.
2. Verificar logs de erro.

### Verificação Automatizada
- [ ] `python build/build_lessons.py` — Sucesso (Exit code 0)

### Verificação Manual
- [ ] Abrir `site/index.html`.
- [ ] Confirmar que L001 aparece na trilha "Raízes I".
- [ ] Confirmar que o card tem a cor/ícone da Celeste (Laranja/Raposa).

---

## Plano de Rollback
1. Deletar `curriculo/02_RAIZES/01_RAIZES_I/L001_IDENTIFICANDO_ESQUERDA_DIREITA.yaml`.
2. Rodar build novamente para limpar `site/index.html`.

---

## Referências
- Pesquisa: `_Projeto/pesquisas/2026-01-17_licao_l001_piloto.md`
- Currículo: `001_..._CURRICULO_MESTRE.md`
