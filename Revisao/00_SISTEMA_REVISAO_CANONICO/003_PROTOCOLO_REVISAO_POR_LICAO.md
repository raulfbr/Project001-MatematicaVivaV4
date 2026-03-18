# PROTOCOLO DE REVISAO POR LICAO
Data: 2026-03-17
Status: canonico
Escopo: revisao HTML-first de licoes Sementes

---

## 1) Missao deste arquivo
Este protocolo existe para transformar revisao em processo repetivel, auditavel e premium.

Objetivo:
1. permitir revisao consistente por IA e por humano;
2. reduzir retrabalho entre sessoes;
3. separar diagnostico, patch, reauditoria e validacao;
4. sustentar cadencia futura de `2 licoes por dia`;
5. transformar `TASTE` e `North Star` em criterio operacional real;
6. obrigar revisao por topicos, ponto a ponto, sem pular secoes "obvias".

---

## 2) Autoridade documental
Este arquivo ja nao carrega sozinho a ativacao completa da revisao.

Fonte de verdade:
1. `023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md` = ativacao, ordem de leitura, cerne macro e algoritmo;
2. este `003` = execucao do patch, reauditoria, gates e formato de log;
3. `004_RUBRICA_PREMIUM_REVISAO.md` = pontuacao e veredito.

---

## 3) Ativacao obrigatoria antes deste arquivo
Antes de usar este protocolo, a sessao deve ter sido ativada pelo `023`.

Minimos esperados ao entrar aqui:
1. cerne macro da licao ja preenchido;
2. frase de boca do Portador, pergunta respondivel principal e microfriccoes previsiveis ja registradas;
3. topicos `001-012` ja abertos;
4. pacote minimo transversal ja aberto;
5. licao atual, anterior e seguinte ja lidas no suficiente;
6. escopo da sessao ja congelado.

---

## 4) Pre-flight obrigatorio
Antes de editar qualquer HTML:

1. confirmar arquivo da licao atual;
2. abrir licao anterior e proxima;
3. confirmar que o arquivo esta em UTF-8;
4. identificar se a licao e `MV-S-000` ou licao padrao;
5. identificar se ha alias legado relevante;
6. confirmar que a ativacao oficial do `023` foi seguida;
7. confirmar que o cerne macro da licao foi registrado;
8. preparar a matriz `001-012` com `PASS / GAP / BLOCK`;
9. mapear as fronteiras criticas que precisarao ser auditadas depois;
10. confirmar se ha task robusta especifica da licao em andamento.
11. confirmar se existe caso relevante em `Revisao/FEEDBACK_MAES_REAIS/` para esta licao ou friccao semelhante.
12. se a licao estiver abstrata, distante ou com imagem dominante frouxa, abrir `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/010_LENTE_ENCANTAMENTO_ENCARNADO_E_REVELACAO_MATEMATICA.md` antes do patch narrativo.

Checklist:
1. qual e a promessa da licao?
2. qual guardiao lidera?
3. qual local aparece no Ritual?
4. qual conceito concreto precisa ser vivido?
5. qual e o gancho para a proxima?
6. qual e a imagem dominante da licao?
7. qual e o fruto do dia?
8. qual e a frase de boca que a mae realmente consegue dizer?
9. qual e a pergunta mais respondivel para `4-6 anos`?
10. onde a licao pode confundir fronteiras entre topicos adjacentes?
11. como um irmao menor pode participar sem dissolver o foco de `5-6 anos`?
12. qual e a ancora concreta mais fiel para esta verdade matematica?
13. que microfriccoes previsiveis podem surgir em nomes, comandos, perguntas ou simetrias falsas?

Se alguma dessas respostas estiver nebulosa:
1. parar o patch e diagnosticar antes.
2. quando a nebulosidade for de imagem dominante, ancora concreta ou maravilhamento encarnado, consultar a `TX10`.

---

## 5) Ordem oficial da revisao
Toda licao deve ser revisada nesta ordem:

1. Diagnostico macro
2. Passada premium antecipada
3. Matriz topico por topico
4. Auditoria de fronteiras criticas
5. Patch estrutural
6. Patch narrativo
7. Patch pedagogico
8. Radiacao local dos ajustes
9. Passada premium final de microdetalhes
10. Reauditoria
11. Validacao final
12. Registro

Racional:
1. sem diagnostico macro, a revisao perde o todo;
2. sem matriz topica, o processo vira intuicao parcial;
3. sem auditoria de fronteiras, a licao pode parecer boa e ainda estar mal costurada;
4. sem reauditoria, o patch pode corrigir um bloco e quebrar o vizinho.

---

## 6) Passo 1 - Diagnostico macro
Mapear findings antes de mexer.

Separar em 4 grupos:
1. Estruturais
2. Narrativos
3. Pedagogicos
4. Tecnicos

Classificar severidade:
1. Critico
2. Alto
3. Medio
4. Baixo

Exemplos de critico:
1. secao obrigatoria ausente;
2. navegacao errada;
3. encoding quebrado;
4. guardiao no Ritual de Entrada;
5. atividade concreta abstrata demais para Sementes;
6. fronteira `Jornada -> O Concreto` colapsada;
7. `Formacao do Portador` ausente ou mutilada.

Saida esperada:
1. lista de findings com arquivo, impacto e severidade;
2. resumo da unidade macro da licao;
3. hipotese inicial de quais topicos e fronteiras vao exigir mais trabalho.

---

## 7) Passo 2 - Passada premium antecipada
Antes da matriz, travar os microdetalhes que mais costumam gerar retrabalho depois.

Checar:
1. qual frase realmente cabe na boca da mae;
2. qual pergunta principal a crianca consegue responder sem traducao adulta;
3. se ha um concreto dominante claro, sem simetria falsa com outro concreto;
4. se o comando mais importante esta visivel no ponto certo;
5. se nomes de objetos, numeros, pecas, lugares e gestos ja estao consistentes.

Regra:
1. esta passada acontece antes do primeiro patch forte;
2. se aqui ja houver atrito fino claro, corrigir no plano antes de espalhar o problema pela pagina.

---

## 8) Passo 3 - Matriz topico por topico
Auditar sempre os 12 topicos oficiais.

Para cada topico registrar:
1. `PASS` quando o topico esta funcionalmente alinhado;
2. `GAP` quando o topico existe, mas ainda tem arestas relevantes;
3. `BLOCK` quando o topico reprova estruturalmente ou espiritualmente;
4. observacao curta;
5. referencia de linha, quando houver.

Modelo minimo:
1. `001_BASE_E_HERO`
2. `002_HEADER_SUPERIOR`
3. `003_PREPARACAO_DO_PORTADOR`
4. `004_RITUAL_DE_ENTRADA`
5. `005_A_JORNADA`
6. `006_O_CONCRETO`
7. `007_NARRAMOS_JUNTOS`
8. `008_RITUAL_DE_FECHAMENTO`
9. `009_CONEXAO_DA_JORNADA`
10. `010_SEMENTES_PARA_O_DIA`
11. `011_FORMACAO_DO_PORTADOR`
12. `012_NAVEGACAO_INFERIOR`

Regra:
1. nao pontuar a licao como alinhada sem preencher os 12 itens;
2. nao esconder `GAP` real dentro de elogio geral;
3. se um topico parecer "automatico", ainda assim ele precisa de leitura e veredito.

---

## 9) Passo 4 - Auditoria de fronteiras criticas
Depois da matriz topica, auditar as costuras entre secoes.

Fronteiras obrigatorias:
1. `003 -> 004`: Preparacao orienta sem gastar o portal?
2. `004 -> 005`: Ritual revela local e Jornada revela guardiao, sem vazamento?
3. `005 -> 006`: Jornada prepara a experiencia manual sem consumir o gesto central de `O Concreto`?
4. `006 -> 007`: a experiencia concreta realmente vira linguagem, sem salto seco?
5. `008 -> 009`: o fechamento pousa antes de a conexao olhar para amanha?
6. `009 -> 010`: a conexao fecha a trilha e `Sementes para o Dia` abre extensoes leves, sem mistura?
7. `010 -> 011`: atividades opcionais nao invadem a camada formativa do Portador?
8. `011 -> 012`: a formacao fecha antes da navegacao tecnica, sem competicao visual ou funcional?

Regra:
1. licao com topicos bons e fronteiras fracas ainda nao esta pronta;
2. fronteira ruim gera `GAP` ou `BLOCK`, mesmo que os blocos isolados estejam fortes.

---

## 10) Passo 5 - Patch estrutural
Corrigir primeiro o que pode reprovar a licao mesmo com texto bom.

Ordem:
1. Base do Documento
2. Header Superior
3. ordem das secoes
4. navegacao inferior
5. labels e classes
6. cards e reveals
7. semantica de links e wrappers

Checagem obrigatoria dentro de `labels e classes` + `cards e reveals`:
1. `reveal`, neste sistema, significa o momento em que o local ou o guardiao e mostrado visualmente a crianca, geralmente com o card;
2. se o card exige gesto imediato do adulto, o HTML visivel precisa deixar essa acao clara;
3. quando isso reduzir traducao mental para a mae, preferir o label `Mostre este card a crianca.` no proprio card de reveal;
4. a diferenca entre `local` e `guardiao` continua sendo garantida pela secao e pela arquitetura, nao por um label bonito demais.

Regra:
1. nao reescrever a narrativa antes de garantir que a arquitetura da pagina esta certa.

---

## 11) Passo 6 - Patch narrativo
Depois da estrutura, revisar a experiencia.

Verificar:
1. Portador com dignidade;
2. guardiao com voz propria;
3. revelacao do local no Ritual;
4. revelacao do guardiao na Jornada;
5. transicoes suaves;
6. tom convidativo, nao militar;
7. imagem dominante protegida do Hero ao fechamento.

Perguntas de controle:
1. o texto soa como roteiro premium ou como rascunho escolar?
2. o adulto se sente guiado ou sobrecarregado?
3. a crianca e tratada como pessoa capaz?
4. narrativa e instrucoes parecem parte do mesmo produto?
5. quando ha card de reveal, a mae sabe exatamente quando mostra-lo?

---

## 12) Passo 7 - Patch pedagogico
Verificar se a licao ensina de verdade.

Checar:
1. concreto no centro;
2. objetivo claro;
3. `A Jornada` e `O Concreto` com papeis distintos;
4. narracao ajudando a fixar;
5. perguntas de reconto vivas;
6. `Sementes para o Dia` opcionais e uteis;
7. `Formacao do Portador` realmente formativa;
8. multi-crianca tratada com hospitalidade sem dissolver o foco.

Vetos:
1. abstracao precoce;
2. tarefa fria;
3. explicacao longa substituindo experiencia;
4. extensao extra cansativa;
5. estrategia do mestre virando apenas "mais uma atividade";
6. adaptacao que rebaixa a dignidade da crianca.

---

## 13) Passo 8 - Radiacao local dos ajustes
Depois do patch estrutural, narrativo e pedagogico, irradiar os ajustes para a licao inteira.

Checar:
1. ecos proximos da mesma ambiguidade;
2. mudancas de naming que precisam se repetir em blocos vizinhos;
3. perguntas ou comandos equivalentes que ainda ficaram no modelo antigo;
4. fechamento, conexao e formacao do Portador reabrindo o problema que foi corrigido no centro da pagina.

Regra:
1. nao considerar o problema resolvido se ele foi corrigido no ponto quente e continua vazando em zonas de apoio.

---

## 14) Passo 9 - Passada premium final de microdetalhes
Depois de corrigir o essencial e irradiar, lapidar.

Checar:
1. repeticao de frase;
2. excesso de aspas;
3. imperativos duros;
4. blocos longos demais;
5. ritmo visual;
6. clareza de escaneamento no celular;
7. `metaforas soltas` ou iconografias misturadas;
8. imagem dominante da licao protegida do Hero ao fechamento;
9. trechos tecnicamente corretos, mas sem vida, sem calor ou com cara de material escolar;
10. pontos em que uma troca pequena de formulacao elevaria muito o `TASTE`;
11. pontos em que a mae precisaria traduzir o texto;
12. pontos em que a pergunta parece bonita, mas pouco respondível para `4-6 anos`;
13. pontos em que o bloco nao deixa claro se e para falar, mostrar ou fazer;
14. pontos em que dois concretos diferentes estao sendo tratados como se fossem o mesmo;
15. pontos em que `quem` deveria ser `qual numero`, `qual peca`, `qual lugar` ou formula equivalente mais respondível;
16. pontos em que o nome do objeto, do gesto ou do lugar muda sem necessidade.

Objetivo:
1. deixar a licao com aparencia e leitura de produto premium;
2. escolher, entre duas solucoes corretas, a mais clara, viva e usavel.

---

## 15) Passo 10 - Reauditoria
Depois do patch:
1. reabrir os topicos tocados;
2. reabrir os topicos vizinhos impactados;
3. irradiar os ajustes para ecos proximos da licao inteira;
4. reavaliar as fronteiras criticas afetadas;
5. rerodar sanity check de encoding;
6. so entao fechar os gates finais.

Regra:
1. patch sem reauditoria ainda nao e revisao fechada.

---

## 16) Passo 11 - Validacao final
Toda licao deve fechar com estes gates:

### Gate CT - Cobertura topica
PASS quando:
1. os 12 topicos foram auditados;
2. nao ha topico omitido;
3. nao ha `BLOCK` aberto na matriz.

BLOCK quando:
1. a licao foi julgada sem passar pelos 12 topicos;
2. ha topico sem veredito;
3. ha `BLOCK` ignorado por "sensacao geral".

### Gate FT - Fronteiras topicas
PASS quando:
1. as fronteiras obrigatorias foram auditadas;
2. cada secao cumpre funcao propria;
3. nao ha colapso de reveal, gesto, fechamento ou camada formativa.

BLOCK quando:
1. duas secoes vizinhas fazem o mesmo papel;
2. a progressao da licao fica borrada;
3. a pagina parece boa em partes, mas frouxa no fluxo.

### Gate NS - North Star
PASS quando:
1. a licao alivia o adulto;
2. encanta a crianca;
3. honra dignidade, concretude e beleza redentora;
4. ainda soa como Matematica Viva.

BLOCK quando:
1. a licao pesa sobre a familia;
2. usa medo, culpa ou secura;
3. perde identidade;
4. passa tecnicamente mas trai o espirito.

### Gate A - Estrutura
PASS quando:
1. todas as secoes obrigatorias existem;
2. ordem macro correta;
3. header e footer coerentes.

### Gate B - Narrativa
PASS quando:
1. local, guardiao e fechamento estao bem encadeados;
2. Portador esta digno;
3. tom esta imersivo.

### Gate C - Pedagogia
PASS quando:
1. concreto forte;
2. reconto vivo;
3. `Jornada` e `O Concreto` nao colapsam;
4. extensoes e formacao coerentes.

### Gate D - Navegacao
PASS quando:
1. anterior/proxima no topo corretos;
2. gancho correto;
3. botoes inferiores corretos.

### Gate E - Integridade tecnica
PASS quando:
1. sem encoding quebrado;
2. sem markup grosseiramente inconsistente;
3. sem regressao evidente.

### Gate T - Taste editorial
PASS quando:
1. a imagem dominante da licao se mantem inteira;
2. nao ha `metaforas soltas`;
3. o texto soa vivo, domestico e recognoscivel como `Matematica Viva`;
4. as transicoes parecem organicas, nao coladas;
5. a mae nao precisa traduzir mentalmente o que dizer, mostrar ou fazer;
6. a pergunta mais importante da licao e realmente respondivel para `4-6 anos`;
7. nao ha falsa simetria entre concretos diferentes;
8. entre duas versoes corretas, a escolhida e a mais clara, mais viva e mais usavel.

EM REFINAMENTO quando:
1. a licao funciona;
2. mas ainda falta forca editorial para soar premium.

BLOCK PREMIUM quando:
1. a licao ate passa tecnicamente;
2. mas o texto continua generico, escolar, sem calor ou com drift imagetico;
3. ou continua exigindo traducao adulta recorrente em microdetalhes de uso real.

Regra:
1. `PASS PREMIUM` exige `CT`, `FT`, `NS`, `A`, `B`, `C`, `D`, `E` e `T` aprovados;
2. `PASS ESTRUTURAL` so existe se `CT`, `FT`, `A`, `D` e `E` estiverem em `PASS`, mesmo que `T` ainda esteja em refinamento;
3. qualquer `BLOCK` duro impede fechamento da licao.

---

## 17) Sanity check obrigatorio de encoding
Depois de editar uma licao HTML, rodar:

```powershell
rg -n "\xC3|\xC2|\xE2|\b\w+\?\w+\b" site/sementes/MV-S-00[0-9]*.html
```

Regra:
1. se aparecer sinal de encoding quebrado, corrigir antes de encerrar.

---

## 18) Formato de log por licao
Registrar sempre:

```md
## MV-S-XXX - [Titulo]

### Findings
- Critico:
- Alto:
- Medio:
- Baixo:

### Matriz topica
- 001 Base e Hero:
- 002 Header Superior:
- 003 Preparacao do Portador:
- 004 Ritual de Entrada:
- 005 A Jornada:
- 006 O Concreto:
- 007 Narramos Juntos:
- 008 Ritual de Fechamento:
- 009 Conexao da Jornada:
- 010 Sementes para o Dia:
- 011 Formacao do Portador:
- 012 Navegacao Inferior:

### Fronteiras criticas
- 003 -> 004:
- 004 -> 005:
- 005 -> 006:
- 006 -> 007:
- 008 -> 009:
- 009 -> 010:
- 010 -> 011:
- 011 -> 012:

### Decisoes
- [...]

### Patch
- Estrutural:
- Narrativo:
- Pedagogico:
- Taste:

### Validacao
- Cobertura topica: PASS/BLOCK
- Fronteiras topicas: PASS/BLOCK
- North Star: PASS/BLOCK
- Estrutura: PASS/BLOCK
- Narrativa: PASS/BLOCK
- Pedagogia: PASS/BLOCK
- Navegacao: PASS/BLOCK
- Tecnica: PASS/BLOCK
- Taste editorial: PASS / EM REFINAMENTO / BLOCK PREMIUM
- Status: PASS PREMIUM / PASS ESTRUTURAL / BLOCK

### Risco residual
- [...]

### Proximo passo
- [...]
```

---

## 19) Definition of Ready de uma licao
Uma licao esta pronta para entrar em revisao quando:
1. a licao atual, anterior e proxima estao acessiveis;
2. os 12 topicos oficiais existem e foram abertos;
3. o pacote minimo transversal foi aberto;
4. a excecao do Portal foi considerada, se aplicavel;
5. o objetivo curricular esta minimamente claro;
6. a frase de boca, a pergunta respondivel principal e as microfriccoes previsiveis ja foram registradas;
7. ha espaco para registrar matriz topica e fronteiras.

---

## 20) Definition of Done de uma licao
Uma licao so fecha quando:
1. os 12 topicos tiverem veredito;
2. as fronteiras criticas tiverem sido auditadas;
3. todos os gates duros estiverem em `PASS`;
4. a passada premium antecipada tiver sido concluida;
5. a radiacao local tiver sido concluida;
6. a passada premium final de microdetalhes tiver sido concluida;
7. o texto estiver limpo e premium;
8. a pagina estiver coerente com o fluxo do ciclo;
9. o log tiver sido atualizado;
10. o encoding estiver preservado;
11. a resposta para `isso nos aproxima ou afasta do North Star?` for claramente `aproxima`;
12. para `PASS PREMIUM`, o `Gate T - Taste editorial` tambem estiver em `PASS`.

---

## 21) Regra de realimentacao do sistema
Se a revisao de uma licao revelar:
1. ambiguidade recorrente em topico canonico;
2. fronteira adjacente mal definida pelo sistema;
3. drift entre protocolo, rubrica, topicos e template;
4. checklist faltando em topico ativo;
5. prompt operacional fraco demais para sustentar patch;

entao:
1. registrar o finding no log da licao;
2. abrir task robusta do sistema, se necessario;
3. ajustar o arquivo canonico antes de usar a licao atual como nova referencia.

Regra:
1. nenhuma licao deve virar baseline total enquanto estiver ensinando falhas ao sistema.

---

## 22) Regra de cadencia
Cadencia alvo:
1. `2 licoes por dia`

Mas so depois de:
1. piloto `001-003` validado;
2. topicos essenciais criados e checklistados;
3. rubrica estavel;
4. zero duvida estrutural grande no sistema;
5. protocolo por topicos e fronteiras funcionando sem ambiguidade.
