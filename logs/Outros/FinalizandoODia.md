# RESUMO COMPLETO PARA PRÓXIMA CONVERSA

> **Data:** 2026-02-17 (encerramento)
> **Objetivo:** Documentar todo o aprendizado para continuidade na próxima sessão
> **Contexto:** Matemática Viva V4 - Projeto Educacional K-12

---

## 1. O QUE É O PROJETO

### Visão Geral
**Matemática Viva** é uma infraestrutura educacional K-12 que combina:
- **Charlotte Mason** (filosofia): "Children are born persons" - crianças como pessoas completas, não recipientes vazios
- **Jerome Bruner** (metodologia): CPA (Concreto → Pictórico → Abstrato) + Currículo em Espiral
- **Narrativa Imersiva**: O "Reino Contado" - um mundo fantástico onde a matemática é descoberta

### Diferencial
- **Não é Singapura**: Singapura usa repetição; MatViva usa espiral de aprofundamento
- **Não é Khan Academy**: Não é exercício digital; é experiência narrativa
- **É "Abra e Faça"**: 5 minutos de preparo para o pai, 15-20 minutos de lição

### Identidade
- **Slogan**: "Histórias que ensinam. Narração que fixa."
- **Origem**: Da Família Rodrigues para outras famílias
- **Tribo**: "Famílias Pioneiras" - early adopters que co-criam

---

## 2. ESTRUTURA DO REINO CONTADO

### Os 5 Ciclos K-12
| Ciclo | Idade | Título do Viajante | Foco |
|-------|-------|-------------------|------|
| Berço | 0-4 | Broto | Natureza, hábitos, zero matemática formal |
| Sementes | 4-6 | Herdeiro | Maravilhamento, 100% concreto |
| Raízes | 6-10 | Construtor | Aventura construtiva, C+P equilibrado |
| Lógica | 11-14 | Explorador | Investigação intelectual, P+A crescente |
| Legado | 15-18 | Portador da Tocha | Maestria vocacional, Abstrato dominante |

### Os 5 Guardiões
| Guardião | Espécie | Virtude | Domínio | Cor |
|----------|---------|---------|---------|-----|
| **Melquior** | Leão | Sabedoria | O Logos | Dourado |
| **Noé** | Coruja | Paciência | O Tempo | Roxo |
| **Celeste** | Raposa | Curiosidade | O Espaço | Laranja |
| **Bernardo** | Urso | Persistência | A Massa | Marrom |
| **Íris** | Pardal | Atenção | O Detalhe | Rosa |

### Os 5 Locais
| Local | Guardião | Atmosfera |
|-------|----------|-----------|
| Jardim Central | Melquior | Luz dourada, cheiro de terra/musgo |
| Árvore do Silêncio | Noé | Sombra, silêncio, frescor |
| Clareira das Perguntas | Celeste | Sol pleno, flores, aventura |
| Caverna do Recomeço | Bernardo | Brasas, pedra, cedro |
| Ninho Mirante | Íris | Vento, ar puro, visão ampla |

### Os 6 Artefatos
1. **Diário do Reino** (Melquior) - Raízes - Registro do aprendizado
2. **Bússola de Celeste** (Celeste) - Lógica - Direção na exploração
3. **Martelo de Bernardo** (Bernardo) - Quando frustrado - Persistência
4. **Pena de Íris** (Íris) - Descobertas estéticas - Atenção
5. **Ampulheta de Noé** (Noé) - Lógica→Legado - Paciência
6. **Tocha de Melquior** (Melquior) - Encerramento - Legado

---

## 3. ARQUITETURA DE ARQUIVOS

### LORE/ (SSOT Narrativo)
```
LORE/
├── index.yaml          # Navegação central
├── north_star.yaml     # Propósito, princípios, missão
├── guardioes.yaml      # Dados fixos dos 5 Guardiões
├── locais.yaml         # 5 Locais com atmosferas
├── climas.yaml         # 8 Climas + 4 Desafios atmosféricos
├── artefatos.yaml      # 6 Artefatos simbólicos
├── viajante.yaml       # Títulos por ciclo
├── evolucao_guardioes.yaml  # Evolução do tom por ciclo
├── origem_guardioes.yaml    # A Grande Nevasca (backstory)
├── padroes_narrativos.yaml  # Regras de narração
├── curriculo_espiral.yaml   # Progressão espiral K-12
└── toms_de_voz.yaml    # Dicionário de tons
```

### curriculo/ (Conteúdo Pedagógico)
```
curriculo/
├── _SISTEMA/
│   ├── CURRICULOS_MESTRE/    # Scope & Sequence por ano
│   ├── TEMPLATES/            # Templates de lição
│   └── imagens/              # Assets visuais
├── 01_SEMENTESV6/            # Lições Sementes (YAML)
├── 02_RAIZES/                # Lições Raízes
├── 03_LOGICA/                # Lições Lógica
└── 04_LEGADO/                # Lições Legado
```

### site/sementes/ (HTML Final)
```
site/sementes/
├── style.css                 # CSS isolado de Sementes
├── MV-S-000_O_PORTAL_DO_REINO.html
├── MV-S-001_A_TRINDADE_NA_PALMA.html
├── MV-S-002_AS_PEDRAS_DA_FORTALEZA.html
├── MV-S-003_A_ESTRELA_DO_REINO.html
├── MV-S-004_A_ORDEM_DO_DIA.html
└── ...
```

### logs/ (Documentação de Trabalho)
```
logs/
├── Estrutura.md              # Esqueleto canônico de lição (ESTE ARQUIVO)
├── FinalizandoODia.md        # Resumo para próxima conversa
├── 2026.02.17.PRD.md         # PRD consolidado
├── AprofundamentoIdadeCedo.md # Defesa pedagógica
├── ChatGPTPRD01.md           # PRD do ChatGPT v1
├── ChatGPTPRD02.md           # PRD do ChatGPT v2
├── TASK_L000_GERACAO.md      # TASK para gerar L000
├── L000_PORTAL_REINO_GERADO.yaml
├── COMPARACAO_L000.md
├── TASK_FUSAO_HTML_L000.md
└── L000_PORTAL_REINO_FUSIONADO.html
```

---

## 4. FORMATO YAML LEAN V6.3

### Estrutura de uma Lição YAML
```yaml
# METADADOS
id: MV-S-XXX
titulo: "[TÍTULO]"
ciclo: Sementes
guardiao_principal: [GUARDIÃO]
foco: [NÚMEROS/CONCEITOS]
tempo: "15-20 min"

# PREPARAÇÃO DO PORTADOR
preparacao_portador:
  dica_coracao: |
    [Mensagem de encorajamento]
  materiais:
    essencial:
      - item: [ITEM]
        qtd: [QTD]
    opcional:
      - item: [ITEM]
  descobertas:
    - [O que a criança vai descobrir]
  segredo_maravilhamento: |
    [Como criar o momento "uau"]
  protocolo_impecabilidade: |
    [Regras de execução]
  nota_graca: |
    [Permissão para errar]

# RITUAL DE ENTRADA
ritual_entrada:
  bastidores: |
    [Preparação do ambiente]
  monobloco_portador: |
    [Script de transição para o Reino]
  local: [LOCAL]
  clima: [CLIMA]

# A JORNADA
jornada:
  cenas:
    - titulo: "[TÍTULO CENA]"
      guardiao: [GUARDIÃO]
      instrucao: |
        [O que o pai faz]
      tom: "[TOM]"
      dialogo: |
        [Diálogo do Guardião]

# O CONCRETO
concreto:
  passo_a_passo:
    - acao: |
        [Ação 1]
      fala_sugerida: |
        "[FALA]"
    - acao: |
        [Ação 2]
      fala_sugerida: |
        "[FALA]"

# NARRAMOS JUNTOS
narramos_juntos:
  perguntas:
    - "[Pergunta aberta 1]"
    - "[Pergunta aberta 2]"

# RITUAL DE FECHAMENTO
ritual_fechamento:
  instrucao: |
    [Como encerrar]
  despedida_guardiao: |
    [Frase de despedida]

# FORMAÇÃO DO PORTADOR
formacao_portador:
  estrategia_mestre:
    titulo: "[TÍTULO]"
    explicacao: |
      [Teoria pedagógica]
    acao: |
      [Como aplicar]

# AUDITORIA QA
auditoria_qa:
  evidencia: |
    [Como foi validado]
  checklist: [lista de verificação]
```

---

## 5. ESTRUTURA HTML CANÔNICA

### Seções Obrigatórias
1. **HEAD**: charset, viewport, CSS, fonts, icons, favicon
2. **BODY**: classe de clima (`clima-0` para L000, `clima-1` para demais)
3. **HERO**: meta-tag, título, citação, imagem do guardião
4. **NAVEGAÇÃO**: anterior/próxima lição
5. **Preparação do Portador**: 7 elementos obrigatórios
6. **Ritual de Entrada**: bastidores + monobloco + local
7. **A Jornada**: múltiplas cenas com cards
8. **O Concreto**: passo a passo
9. **Narramos Juntos**: perguntas abertas
10. **Ritual de Fechamento**: encerramento
11. **Formação do Portador**: estratégia pedagógica

### Classes CSS Principais
```css
.lesson-container    /* Container principal */
.lesson-hero         /* Seção hero */
.lesson-meta-tag     /* Tag de metadados */
.hero-title          /* Título da lição */
.hero-quote          /* Citação temática */
.hero-guardian       /* Imagem do guardião */
.scene-card          /* Card de seção */
.scene-header        /* Título da seção */
.instruction-box     /* Caixa de instrução */
.materials-box       /* Lista de materiais */
.script-persona-block /* Bloco de diálogo */
.portador-block      /* Monobloco do Portador */
.script-avatar       /* Avatar do guardião */
.script-name         /* Nome do guardião */
.script-text         /* Texto do diálogo */
.card-visual-asset   /* Imagem de card */
.local-label         /* Label "Mostrar Card" */
```

### Ícones Phosphor por Seção
| Seção | Ícone | Cor |
|-------|-------|-----|
| Preparação | `ph-clipboard-text` | `duotone-terra` |
| Ritual Entrada | `ph-film-strip` | `duotone-magic` |
| Jornada | `ph-map-trifold` | `duotone-gold` |
| Concreto | `ph-wall` | `duotone-terra` |
| Narração | `ph-chat-circle-text` | `duotone-indigo` |
| Fechamento | `ph-sun-horizon` | `duotone-gold` |
| Formação | `ph-graduation-cap` | `duotone-forest` |

---

## 6. PRINCÍPIOS PEDAGÓGICOS

### Charlotte Mason (VETO FINAL)
1. **Children are born persons** - Crianças são pessoas completas
2. **Living Ideas** - Ideias vivas, não informação seca
3. **Narração** - A criança reconta para fixar
4. **Lições curtas** - 15-20 min para Sementes
5. **Things before Signs** - Concreto antes de abstrato
6. **Atmosphere, Discipline, Life** - O ambiente educa

### Jerome Bruner (PROPOSITIVO)
1. **CPA**: Concreto → Pictórico → Abstrato
2. **Espiral**: Conceitos retornam com maior profundidade
3. **Scaffolding**: Suporte que diminui com o tempo
4. **Enactive-Iconic-Symbolic**: Estágios de representação

### Princípios do North Star
1. **Qualidade Não é Negociável** - 3 impecáveis > 10 boas
2. **A Família é o Centro** - Serve a família, não o contrário
3. **Foco no Positivo** - Nunca vender pelo medo
4. **Identidade Tribal** - "People like us do things like this"
5. **Unidade Familiar** - Um Reino para TODOS (0-18 + pais)
6. **Norte Seguro + Flexibilidade** - Core fixo, caminhos flexíveis
7. **Soberania Intelectual** - Mirar global, BNCC é consequência
8. **Beleza Redentora** - Estética cura
9. **Transcendência** - Imago Dei em toda criança

---

## 7. TRABALHO REALIZADO HOJE

### Arquivos Criados
1. **`logs/TASK_L000_GERACAO.md`** - TASK completa para gerar Lição 000
2. **`logs/L000_PORTAL_REINO_GERADO.yaml`** - Lição 000 em YAML Lean v6.3
3. **`logs/COMPARACAO_L000.md`** - Análise comparativa das versões
4. **`logs/TASK_FUSAO_HTML_L000.md`** - TASK para fusão HTML
5. **`logs/L000_PORTAL_REINO_FUSIONADO.html`** - HTML fusionado (~700 linhas)
6. **`logs/Estrutura.md`** - Esqueleto canônico de lição
7. **`logs/FinalizandoODia.md`** - Este resumo

### Análises Realizadas
- Leitura completa do LORE (12 arquivos YAML)
- Análise do North Star (missão, princípios, roadmap)
- Estudo do Currículo Mestre Sementes
- Comparação de Template V6.3 com lições existentes
- Análise de padrões visuais e narrativos
- Síntese de PRDs anteriores (ChatGPT + manual)

### Decisões Tomadas
1. **Fusão como abordagem**: Combinar riqueza narrativa existente com estrutura QA
2. **Voz Única**: Guardião fala, Portador conduz (não competem)
3. **Estrutura de 7 elementos**: Preparação do Portador padronizada
4. **Classe de clima**: `clima-0` para L000, `clima-1` para demais

---

## 8. PRÓXIMOS PASSOS RECOMENDADOS

### Imediato (Próxima Sessão)
1. **Auditar lições existentes** usando `logs/Estrutura.md`
2. **Identificar lacunas** em cada lição (L001-L025)
3. **Padronizar estrutura** em todas as lições
4. **Criar template HTML** reutilizável

### Curto Prazo
1. **Completar Sementes** (L001-L025) com estrutura canônica
2. **Validar com famílias pioneiras**
3. **Documentar feedback** e iterar
4. **Preparar Raízes I** (piloto)

### Médio Prazo
1. **Expandir para Raízes** (6-10 anos)
2. **Criar sistema de geração** semi-automatizada
3. **Desenvolver app/web** para distribuição
4. **Onboarding de famílias**

---

## 9. FONTES E REFERÊNCIAS

### SSOT (Single Source of Truth)
- `LORE/north_star.yaml` - Propósito e princípios
- `LORE/guardioes.yaml` - Dados dos Guardiões
- `LORE/locais.yaml` - Locais do Reino
- `LORE/artefatos.yaml` - Artefatos simbólicos
- `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md` - Currículo
- `curriculo/_SISTEMA/TEMPLATES/000_TEMPLATE_SEMENTES_V3-6_GOLD.md` - Template

### Referências Externas
- Charlotte Mason: "Home Education" (Vol. 1)
- Jerome Bruner: "The Process of Education" (1960)
- Singapore Math: CPA Framework
- Finlândia: PISA Rankings, modelo educacional

### Arquivos de Apoio
- `logs/2026.02.17.PRD.md` - PRD consolidado
- `logs/AprofundamentoIdadeCedo.md` - Defesa pedagógica completa
- `Revisao/padrao_visual_sementes.md` - Padrões visuais

---

## 10. COMO COMEÇAR A PRÓXIMA CONVERSAA

### Prompt Sugerido
```
Leia o arquivo logs/FinalizandoODia.md para entender o contexto completo do projeto.
Depois, leia logs/Estrutura.md para ver o esqueleto canônico de uma lição.
Me ajude a [TAREFA ESPECÍFICA].
```

### Tarefas Possíveis
1. **Auditar lição existente**: "Audite a lição MV-S-001 usando o esqueleto"
2. **Gerar nova lição**: "Crie a lição MV-S-005 seguindo o esqueleto"
3. **Corrigir lição**: "Corrija a lição MV-S-XXX para seguir o esqueleto"
4. **Criar template**: "Gere um template HTML reutilizável baseado no esqueleto"
5. **Documentar**: "Crie documentação para [aspecto específico]"

---

## 11. NOTAS FINAIS

### O Que Funcionou
- Estrutura YAML Lean v6.3 é clara e completa
- Fusão de narrativa rica com estrutura QA
- Padrão visual consistente (Phosphor Icons, cores litúrgicas)
- Princípios pedagógicos bem definidos

### O Que Precisa Atenção
- Algumas lições existentes podem não seguir o esqueleto
- Necessário validar com famílias reais
- Sistema de geração ainda é manual
- Distribuição ainda não definida

### Lembrete Importante
> "O medo acaba em você. O encantamento começa neles."
> 
> O objetivo não é criar matemáticos perfeitos, mas crianças que amam aprender.

---

**Fim do Resumo**
*Gerado em: 2026-02-17*
*Para: Próxima sessão de trabalho*
