## MV-S-003 - A Estrela do Reino

### Cerne macro
- TGTB ref e papel no curriculo: `000-L3`, composicao visual de `4` e `5`
- Promessa pedagogica: ver o cinco como estrutura viva, nao so como sequencia
- Guardiao e lugar: Iris no Ninho Mirante
- Conceito vivo e concreto: borda, centro e forma revelada
- Imagem dominante: a estrela que nasce quando a moldura recebe o centro
- Fruto do dia esperado: a crianca monta e reconhece `quatro ao redor + um no centro`

### Findings
- Critico:
- Iris falava dos quatro lados antes do material chegar a crianca.
- `Narramos Juntos` ainda pedia reconto amplo demais para `4-6` anos.
- Alto:
- perguntas de reconto e coracao ainda exigiam traducao adulta em varios pontos.
- `Sussurro do Mirante` repetia funcao e ocupava espaco ritual sem ganho proporcional.
- Medio:
- uma fala de `O Concreto` ainda colocava poesia em slot funcional.
- o fechamento do Portador ainda podia pousar melhor.
- Baixo:
- `Sementes para o Dia` e `Formacao do Portador` precisavam apenas de microafinacao.

### Matriz topica
- 001 Base e Hero: PASS
- 002 Header Superior: PASS
- 003 Preparacao do Portador: PASS
- 004 Ritual de Entrada: GAP -> PASS apos corte do sussurro redundante
- 005 A Jornada: BLOCK -> PASS apos reordenar gesto e fala
- 006 O Concreto: GAP -> PASS apos ancorar melhor fala de apoio e ponte
- 007 Narramos Juntos: BLOCK -> PASS apos concretizar pergunta inicial e reconto
- 008 Ritual de Fechamento: GAP -> PASS apos oralizacao do Portador
- 009 Conexao da Jornada: PASS
- 010 Sementes para o Dia: PASS
- 011 Formacao do Portador: PASS
- 012 Navegacao Inferior: PASS

### Fronteiras criticas
- 003 -> 004: PASS
- 004 -> 005: PASS apos o Ritual parar de competir com a Jornada
- 005 -> 006: PASS apos a Jornada voltar a preparar e o Concreto voltar a encarnar
- 006 -> 007: PASS apos o reconto nascer do gesto visivel
- 008 -> 009: PASS
- 009 -> 010: PASS
- 010 -> 011: PASS
- 011 -> 012: PASS

### Deliberacao dos experts
- Charlotte Mason: aprovou quando a licao voltou a honrar gesto, atencao curta e narracao viva sem prova oral precoce.
- Jerome Bruner: aprovou quando a ordem voltou a ser `objeto na mao -> acao -> nomeacao`.
- Susan Macaulay: aprovou a reducao de frases que obrigavam a mae a traduzir.
- Mae Ansiosa: vetava a versao anterior no ponto `eu preciso improvisar o que dizer`; este veto caiu com o patch.
- Mae Veterana: pediu que o encanto continuasse; isso foi preservado pela manutencao da imagem dominante.
- Beatrix Potter: apoiou retirar excesso em vez de inflar a cena com nova explicacao.
- Design: sem alteracao estrutural ruidosa; layout e escaneabilidade preservados.
- Engenharia: patch pequeno, localizado e auditavel.

### Decisoes
- cortar `Sussurro do Mirante`
- inverter a ordem funcional da moldura
- reescrever o centro da maca para observacao guiada, nao interpretacao forcada
- reescrever abertura e perguntas de `Narramos Juntos`
- simplificar a fala de apoio em `O Concreto`
- dividir melhor o fechamento do Portador
- incorporar a heuristica `mostrar -> entregar -> agir -> nomear -> perguntar` em `Formacao do Portador`

### Patch
- Estrutural: remocao de bloco ritual redundante; reordenacao de gesto e fala na Jornada
- Narrativo: Iris segue doce e observadora; suspense da maca preservado
- Pedagogico: reconto ficou respondível por gesto, apontamento ou frase curta
- Taste: reducao forte de traducao mental e de abstração precoce

### Validacao
- Cobertura topica: PASS
- Fronteiras topicas: PASS
- North Star: PASS
- Estrutura: 5/5
- Narrativa: 4/5
- Pedagogia: 5/5
- UX do Portador: 5/5
- Navegacao: 5/5
- Tecnica: PASS
- Taste editorial: PASS
- Status: PASS PREMIUM

### Risco residual
- a nova versao ainda precisa de validacao humana em uso real para confirmar ritmo, especialmente na passagem maca -> concreto;
- o terminal deste ambiente ainda pode mostrar mojibake em algumas leituras, entao encoding deve ser sempre conferido no arquivo final.

### Proximo passo
- validar a `L003` com familia real
- observar se as novas perguntas realmente saem sem traducao
- usar a heuristica desta licao como lente de revisao para `L004+`, sem canonizacao precoce
