# PROTOCOLO DE REVISAO POR LICAO
Data: 2026-03-10
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

## 2) Ativacao obrigatoria do protocolo
Toda revisao de licao padrao deve ser ativada assim:
1. abrir este protocolo;
2. abrir `004_RUBRICA_PREMIUM_REVISAO.md`;
3. abrir `011_TOPICOS/000_README.md`;
4. abrir os 12 topicos oficiais `001-012`, na ordem;
5. abrir `012_TRANSVERSAIS/000_README.md`;
6. abrir o pacote minimo transversal: `002`, `003`, `005`, `006`, `008`;
7. abrir a licao atual;
8. abrir a licao anterior;
9. abrir a licao seguinte;
10. so depois iniciar diagnostico e patch.

Regra:
1. `topicos relevantes` vale apenas para transversais adicionais;
2. os 12 topicos da licao devem sempre ser auditados.

---

## 3) Ordem obrigatoria de leitura antes de revisar
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
3. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
4. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/000_README.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/001_BASE_E_HERO.md` ate `012_NAVEGACAO_INFERIOR.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/000_README.md`
7. pacote minimo transversal: `002`, `003`, `005`, `006`, `008`
8. licao atual
9. licao anterior
10. licao seguinte

Regra:
1. nao revisar uma licao isoladamente do seu encadeamento;
2. nao pontuar na rubrica antes de fechar a matriz topica e as fronteiras.

---

## 4) Pre-flight obrigatorio
Antes de editar qualquer HTML:

1. confirmar arquivo da licao atual;
2. abrir licao anterior e proxima;
3. confirmar que o arquivo esta em UTF-8;
4. identificar se a licao e `MV-S-000` ou licao padrao;
5. identificar se ha alias legado relevante;
6. abrir os 12 topicos oficiais;
7. abrir o pacote minimo transversal;
8. preparar a matriz `001-012` com `PASS / GAP / BLOCK`;
9. mapear as fronteiras criticas que precisarao ser auditadas depois;
10. confirmar se ha task robusta especifica da licao em andamento.

Checklist:
1. qual e a promessa da licao?
2. qual guardiao lidera?
3. qual local aparece no Ritual?
4. qual conceito concreto precisa ser vivido?
5. qual e o gancho para a proxima?
6. qual e a imagem dominante da licao?
7. onde a licao pode confundir fronteiras entre topicos adjacentes?

Se alguma dessas respostas estiver nebulosa:
1. parar o patch e diagnosticar antes.

---

## 5) Ordem oficial da revisao
Toda licao deve ser revisada nesta ordem:

1. Diagnostico macro
2. Matriz topico por topico
3. Auditoria de fronteiras criticas
4. Patch estrutural
5. Patch narrativo
6. Patch pedagogico
7. Acabamento premium e `TASTE`
8. Reauditoria
9. Validacao final
10. Registro

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

## 7) Passo 2 - Matriz topico por topico
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

## 8) Passo 3 - Auditoria de fronteiras criticas
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

## 9) Passo 4 - Patch estrutural
Corrigir primeiro o que pode reprovar a licao mesmo com texto bom.

Ordem:
1. Base do Documento
2. Header Superior
3. ordem das secoes
4. navegacao inferior
5. labels e classes
6. cards e reveals
7. semantica de links e wrappers

Regra:
1. nao reescrever a narrativa antes de garantir que a arquitetura da pagina esta certa.

---

## 10) Passo 5 - Patch narrativo
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

---

## 11) Passo 6 - Patch pedagogico
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

## 12) Passo 7 - Acabamento premium e Taste
Depois de corrigir o essencial, lapidar.

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
10. pontos em que uma troca pequena de formulacao elevaria muito o `TASTE`.

Objetivo:
1. deixar a licao com aparencia e leitura de produto premium;
2. escolher, entre duas solucoes corretas, a mais clara, viva e usavel.

---

## 13) Passo 8 - Reauditoria
Depois do patch:
1. reabrir os topicos tocados;
2. reabrir os topicos vizinhos impactados;
3. reavaliar as fronteiras criticas afetadas;
4. rerodar sanity check de encoding;
5. so entao fechar os gates finais.

Regra:
1. patch sem reauditoria ainda nao e revisao fechada.

---

## 14) Passo 9 - Validacao final
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
5. entre duas versoes corretas, a escolhida e a mais clara e mais viva.

EM REFINAMENTO quando:
1. a licao funciona;
2. mas ainda falta forca editorial para soar premium.

BLOCK PREMIUM quando:
1. a licao ate passa tecnicamente;
2. mas o texto continua generico, escolar, sem calor ou com drift imagetico.

Regra:
1. `PASS PREMIUM` exige `CT`, `FT`, `NS`, `A`, `B`, `C`, `D`, `E` e `T` aprovados;
2. `PASS ESTRUTURAL` so existe se `CT`, `FT`, `A`, `D` e `E` estiverem em `PASS`, mesmo que `T` ainda esteja em refinamento;
3. qualquer `BLOCK` duro impede fechamento da licao.

---

## 15) Sanity check obrigatorio de encoding
Depois de editar uma licao HTML, rodar:

```powershell
rg -n "\xC3|\xC2|\xE2|\b\w+\?\w+\b" site/sementes/MV-S-00[0-9]*.html
```

Regra:
1. se aparecer sinal de encoding quebrado, corrigir antes de encerrar.

---

## 16) Formato de log por licao
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

## 17) Definition of Ready de uma licao
Uma licao esta pronta para entrar em revisao quando:
1. a licao atual, anterior e proxima estao acessiveis;
2. os 12 topicos oficiais existem e foram abertos;
3. o pacote minimo transversal foi aberto;
4. a excecao do Portal foi considerada, se aplicavel;
5. o objetivo curricular esta minimamente claro;
6. ha espaco para registrar matriz topica e fronteiras.

---

## 18) Definition of Done de uma licao
Uma licao so fecha quando:
1. os 12 topicos tiverem veredito;
2. as fronteiras criticas tiverem sido auditadas;
3. todos os gates duros estiverem em `PASS`;
4. o texto estiver limpo e premium;
5. a pagina estiver coerente com o fluxo do ciclo;
6. o log tiver sido atualizado;
7. o encoding estiver preservado;
8. a resposta para `isso nos aproxima ou afasta do North Star?` for claramente `aproxima`;
9. para `PASS PREMIUM`, o `Gate T - Taste editorial` tambem estiver em `PASS`.

---

## 19) Regra de realimentacao do sistema
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

## 20) Regra de cadencia
Cadencia alvo:
1. `2 licoes por dia`

Mas so depois de:
1. piloto `001-003` validado;
2. topicos essenciais criados e checklistados;
3. rubrica estavel;
4. zero duvida estrutural grande no sistema;
5. protocolo por topicos e fronteiras funcionando sem ambiguidade.
