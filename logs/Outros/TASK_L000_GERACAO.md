# TASK: GERAÇÃO DA LIÇÃO 000 - O PORTAL DO REINO
> **Formato:** YAML Lean v1.0 | **Data:** 17/02/2026 | **Status:** PRONTO PARA EXECUÇÃO

---

## SEÇÃO 1: METADADOS DA TASK

```yaml
task:
  id: TASK-L000-GERACAO
  tipo: geracao_licao
  prioridade: ALTA
  status: pronto_execucao
  data_criacao: '2026-02-17'
  responsavel: GLM-5 (Architect Mode)
  validador: Raul (Maestro Fundador)
```

---

## SEÇÃO 2: FONTES DE VERDADE (SSOT)

```yaml
fontes:
  primarias:
    - {arquivo: 'LORE/north_star.yaml', secao: 'identidade + principios_5 + propositos_por_ano.K_sementes'}
    - {arquivo: 'LORE/guardioes.yaml', secao: 'guardioes (todos os 5) + conceitos_por_guardiao'}
    - {arquivo: 'LORE/locais.yaml', secao: 'locais.jardim_central'}
    - {arquivo: 'LORE/climas.yaml', secao: 'climas.primaveril'}
    - {arquivo: 'LORE/artefatos.yaml', secao: 'objetos_rituais.luz_amarela'}
    - {arquivo: 'LORE/viajante.yaml', secao: 'titulos.herdeiro'}
    - {arquivo: 'LORE/evolucao_guardioes.yaml', secao: 'melquior.por_ciclo.sementes'}
  
  templates:
    - {arquivo: 'curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml', secao: 'estrutura completa'}
  
  curriculo_mestre:
    - {arquivo: 'curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md', secao: 'MV-S-000 Hook'}
  
  revisao:
    - {arquivo: 'Revisao/topicos_licao_revisao.md', secao: 'Checklist Estrutura Base'}
    - {arquivo: 'Revisao/revisao_licao003.md', secao: 'Aprendizados Chave'}
    - {arquivo: 'Revisao/padrao_visual_sementes.md', secao: 'Padrão Visual'}
```

---

## SEÇÃO 3: EXPERTS CONSULTADOS

```yaml
experts:
  coordenador:
    id: charlotte_mason
    arquivo: '.bmad/experts/pedagogia/charlotte_mason.yaml'
    role: VETO_FINAL
    foco: [Dignidade, Ideia Viva, Narração, Lição Curta, Things before Signs]
    principios_aplicar: [1, 10, 11, 15]
  
  metodo_cpa:
    id: jerome_bruner
    arquivo: '.bmad/experts/matematica/jerome_bruner.yaml'
    role: PROPOSITIVO
    foco: [Concreto 100%, Enativo, Discovery Learning]
    nota: 'L000 é LITÚRGICA, não conteudista. CPA = Concreto (ritual físico).'
  
  narrativa:
    id: cs_lewis
    arquivo: '.bmad/experts/narrativa/cs_lewis.yaml'
    role: GUARDIAO_DIGNIDADE
    foco: [Tom Nobre, Não Condescender, Supposal não Alegoria]
    citacao_chave: 'Child as reader neither patronized nor idolized'
```

---

## SEÇÃO 4: ESPECIFICAÇÃO DA LIÇÃO 000

```yaml
especificacao:
  tipo: LITÚRGICA_NARRATIVA
  nao_conteudista: true
  objetivo: 'Estabelecer a Atmosfera Sagrada (Charlotte Mason)'
  
  apresentacao:
    - Apresentar os 5 Guardiões (Noé, Celeste, Bernardo, Íris, Melquior)
    - O Convite: Pai/Mãe recebe a Tocha (simbólica)
    - A Criança recebe o Distintivo de Herdeiro
    - Sem Telas: Magia acontece no chão da sala
  
  guardiao_lider: melquior
  local: jardim_central
  clima: primaveril
  virtude: sabedoria
  artefato: luz_amarela
  
  viajante:
    titulo: 'Herdeiro das Promessas'
    idade: '4-6 anos'
    tom: 'RECEPÇÃO: Você é bem-vindo. Isso é SEU.'
```

---

## SEÇÃO 5: ESTRUTURA DA LIÇÃO (Template V6)

### 5.1 Metadados

```yaml
estrutura:
  metadados:
    id: 'MV-S-000'
    titulo: 'O Portal do Reino'
    fase: Sementes
    ciclo: K
    trimestre: 0
    estacao: 0
    tipo: 'Litúrgica/Narrativa'
    tempo_licao: '15-20 min'
    tempo_preparo: '<= 5 min'
```

### 5.2 Para o Portador

```yaml
  para_portador:
    ideia_viva: 'O Reino existe. Você foi convidado.'
    dica_coracao: 'Você não precisa ser perfeito. Apenas presente.'
    filho_descobre: 'Que existe um Reino mágico onde a matemática vive'
    protocolo_impecabilidade: 'NÃO EXPLIQUE, VIVA. Entre na história junto.'
    nota_graca: 'Se a criança não "entrar" hoje, a semente foi plantada.'
    conforto_emocional: 'É normal sentir medo de "atuar". Você é o Portador da Tocha.'
```

### 5.3 Ritual de Abertura

```yaml
  ritual_abertura:
    instrucao_ambiente: 'Tapete do Reino, luz amarela, silêncio'
    local: 'jardim_central'
    clima: 'primaveril'
    virtude: 'sabedoria'
    artefato: 'Luz Amarela (Tocha de Melquior)'
    transicao_reino: 'Olhos fechados, respiração, acender luz'
    fala_portador:
      tom: 'ritual'
      script: 'Luz de fora acalma. Sol de dentro acende. Respirem... Estamos no Reino.'
    abertura_sensorial: 'Luz dourada, cheiro de terra molhada, silêncio sagrado'
```

### 5.4 Jornada - Narrativa Principal

```yaml
  jornada:
    narrativa_principal:
      - titulo: 'O Convite de Melquior'
        local: 'jardim_central'
        fala_melquior:
          tom: 'acolhedor'
          script: |
            "Aproxime-se, pequeno Herdeiro. Sente-se aqui, no tapete de musgo, 
            sob o brilho da Pequena Vela. Eu sou Melquior, o Anfitrião deste Jardim."
        instrucao_portador: 'Mostrar Card do Melquior. Sorrir. Estender a mão.'
      
      - titulo: 'A Apresentação dos Guardiões'
        local: 'jardim_central'
        fala_melquior:
          tom: 'nobre'
          script: |
            "Veja! Ali, no galho mais alto, está a Coruja Noé. Ele guarda o Tempo.
            Sente este vento rápido? É a Raposa Celeste. Ela adora segredos e padrões.
            Ouça o passo firme na terra... É o Urso Bernardo. Ele é forte e gentil.
            E olhe bem de perto para aquela flor... Lá está a Íris. Ela vê o que ninguém mais vê."
        instrucao_portador: |
          Apontar para cada Card de Guardião conforme menciona.
          Pausar entre cada apresentação.
      
      - titulo: 'O Convite Final'
        local: 'jardim_central'
        fala_melquior:
          tom: 'esperançoso'
          script: |
            "Todos nós estamos aqui para caminhar com você.
            O Reino foi feito para você. Vamos começar?"
        instrucao_portador: 'Estender a mão em convite. Aguardar resposta da criança.'
```

### 5.5 Jornada - Concreto

```yaml
    concreto:
      desc: 'Ritual de Entrega da Tocha e Distintivo de Herdeiro'
      metodo: 'mao-na-mao'
      instrucoes_portador:
        - passo: 1
          acao: 'Acender a Luz Amarela junto com a criança'
          fala_sugerida: 'Esta luz é o sinal de que o Reino começou.'
        - passo: 2
          acao: 'Entregar o Distintivo de Herdeiro (pode ser um símbolo, card especial, ou objeto)'
          fala_sugerida: 'Você agora é um Herdeiro das Promessas do Reino.'
        - passo: 3
          acao: 'Fazer um gesto de boas-vindas (abraço, aperto de mão, ou sinal especial)'
          fala_sugerida: 'Bem-vindo ao Reino Contado.'
      norte_absoluto: 'O ritual é o aprendizado. A atmosfera é o conteúdo.'
      adaptacao_bernardo: 'Se a criança não quiser participar do ritual, apenas sente junto e conte a história.'
```

### 5.6 Jornada - Pictórico e Abstrato

```yaml
    pictorico:
      status: VETADO
      motivo: 'Sementes = Concreto. CM Things before Signs.'
    
    abstrato:
      desc: 'Reconhecimento visual dos Guardiões nos Cards'
      nota: 'Ver e tocar os Cards = ENATIVO, conta como Concreto.'
```

### 5.7 Narração

```yaml
  narracao:
    instrucao_portador: 'Guarde os Cards. Olhe nos olhos da criança. Dê tempo.'
    pergunta_principal: 'O que você mais gostou de conhecer hoje?'
    perguntas_coracao:
      - 'Qual Guardião você quer conhecer melhor?'
      - 'O que você sentiu quando a luz acendeu?'
      - 'O que você acha que vamos descobrir no Reino?'
    nota_cm: 'NUNCA interrompa. Espere. Se não quiser falar: Tudo bem, seu coração guardou.'
```

### 5.8 Ritual de Fechamento

```yaml
  ritual_fechamento:
    fala_melquior:
      tom: 'grato'
      script: |
        "Você agora é um Herdeiro do Reino. 
        Toda vez que acendermos a Luz Amarela, estaremos aqui juntos.
        Até a próxima aventura, pequeno Viajante."
    fio_ouro: 'Na próxima lição, vamos descobrir o segredo dos números com Celeste!'
    transicao_volta:
      instrucao: 'Apagar a Luz Amarela juntos'
      fala: 'O Reino descansa. A luz fica no coração. Até amanhã, Herdeiro.'
```

### 5.9 Para a Família

```yaml
  para_familia:
    titulo: 'Entendendo a Jornada de Hoje'
    porque_importa: |
      A Lição 000 é litúrgica, não conteudista. O objetivo não é ensinar matemática,
      mas estabelecer a "Atmosfera Sagrada" (Charlotte Mason). A criança é apresentada
      aos 5 Guardiões e recebe o título de "Herdeiro das Promessas".
      
      Este é o fundamento emocional de toda a jornada. Sem esta lição, as próximas
      não teriam o mesmo impacto. O Reino precisa ser "real" antes de ser "estudado".
    metodo_cpa:
      concreto: 'Ritual físico: acender luz, receber distintivo, tocar os Cards'
      pictorico: 'Vetado em Sementes'
      abstrato: 'Reconhecimento visual dos Guardiões'
      nota: 'CM: Coisas antes de Signos. O ritual É o aprendizado.'
    principio_cm:
      numero: 5
      citacao: 'Education is an atmosphere, a discipline, a life.'
      aplicacao: 'A Atmosfera do Reino foi estabelecida hoje.'
    tgtb_conexao: 'Esta lição é única do Matemática Viva - não há equivalente TGTB.'
    espiral:
      conceito: 'Introdução ao Reino'
      volta_atual: 'Sementes - Maravilhamento puro'
      proxima_volta: 'Raízes - A criança se torna Construtor'
      nota: 'O conceito de "Reino" cresce junto com a criança ao longo de 13 anos.'
    reflexao_espiritual: |
      O Reino Contado é uma metáfora do Reino de Deus. A criança é "Herdeiro" 
      não por mérito, mas por convite. A Luz Amarela simboliza a presença 
      do Rei que nunca se apaga.
    nota_graca: 'Se não saiu como esperava, respire. A semente foi plantada. Volte amanhã com alegria.'
```

### 5.10 Diário do Portador

```yaml
  diario_portador:
    nota: 'Anotações usadas nas revisões trimestrais.'
    perguntas:
      - 'Como meu filho reagiu ao ritual?'
      - 'Qual Guardião mais chamou atenção?'
      - 'O que ajustar para a próxima lição?'
```

### 5.11 Auditoria QA

```yaml
  auditoria_qa:
    cm:
      - {q: 'Criança tratada como pessoa capaz?', status: PENDENTE}
      - {q: 'Ideia Viva presente?', status: PENDENTE}
      - {q: 'Narração incluída?', status: PENDENTE}
      - {q: 'Lição <=20min?', status: PENDENTE}
      - {q: 'Hábito Atenção preservado?', status: PENDENTE}
    cpa:
      - {q: 'Concreto presente (ritual físico)?', status: PENDENTE}
      - {q: 'Pictórico vetado?', status: PENDENTE}
      - {q: 'Abstrato mínimo?', status: PENDENTE}
    narrativa:
      - {q: 'Frase canônica do Guardião usada?', status: PENDENTE}
      - {q: 'Tom Lewis (nobre, não condescendente)?', status: PENDENTE}
      - {q: 'Consistência Tolkien?', status: PENDENTE}
      - {q: 'Cores Potter?', status: PENDENTE}
    template:
      - {q: 'Seções obrigatórias presentes?', status: PENDENTE}
      - {q: 'Linkage com próxima lição?', status: PENDENTE}
      - {q: 'Atmosfera única criada?', status: PENDENTE}
    triade:
      - {q: 'CM OK?', status: PENDENTE}
      - {q: 'CPA OK?', status: PENDENTE}
      - {q: 'TGTB ref válida?', status: N/A}
    inclusao:
      - {q: 'Adaptação Bernardo incluída?', status: PENDENTE}
      - {q: 'Instruções acessíveis?', status: PENDENTE}
```

---

## SEÇÃO 6: CHECKLIST DE VALIDAÇÃO

```yaml
validacao:
  pre_geracao:
    - [x] Fontes SSOT identificadas
    - [x] Experts consultados
    - [x] Especificação completa
    - [x] Estrutura Template V6 mapeada
  
  pos_geracao:
    - [ ] Lição gerada no arquivo YAML
    - [ ] Auditoria QA preenchida
    - [ ] Comparação com L000 existente
    - [ ] Validação do Maestro
```

---

## SEÇÃO 7: PONTOS DE REVISÃO (da pasta Revisao)

### De [`topicos_licao_revisao.md`](Revisao/topicos_licao_revisao.md)

- Scene Headers com ícones temáticos
- Card Container com rotate-left hover-float
- Instruction Box com ph-hand-pointing duotone-neutral
- Script Block com Tom indicado
- Guardião: Card UMA VEZ por lição
- Segredo do Maravilhamento para proteger a magia

### De [`revisao_licao003.md`](Revisao/revisao_licao003.md)

- Local LORE correto (jardim_central para Melquior)
- Metáfora vs. Material: Instrução Técnica (Pai) vs. Fala do Guardião (Imaginação)
- Visual Cues: Ícones apontando para onde devem
- Proteção da Magia: Segredo do Maravilhamento presente
- Estratégias de Resgate: Se criança travar, o que fazer?

---

## SEÇÃO 8: PRÓXIMOS PASSOS

1. **Gerar arquivo YAML completo da Lição 000** (precisa mudar para Code mode)
2. **Salvar em** `logs/L000_PORTAL_REINO_GERADO.yaml`
3. **Comparar com** [`curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml`](curriculo/01_SEMENTESV6/000_PORTAL_REINO.yaml)
4. **Apresentar diferenças e melhorias ao Maestro**
5. **Aprovar e mover para pasta oficial** (se validado)

---

## NOTA IMPORTANTE

> **Para gerar o arquivo YAML final, é necessário mudar para o modo "Code"**, pois o modo Architect só pode editar arquivos Markdown (.md).
>
> A TASK acima contém toda a especificação necessária para gerar a Lição 000 completa no formato YAML Lean v6.3.