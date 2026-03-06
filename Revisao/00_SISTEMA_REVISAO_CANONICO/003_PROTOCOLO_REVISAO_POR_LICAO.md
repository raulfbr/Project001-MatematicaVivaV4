# PROTOCOLO DE REVISAO POR LICAO
Data: 2026-03-06
Status: canonico
Escopo: revisao HTML-first de licoes Sementes

---

## 1) Missao deste arquivo
Este protocolo existe para transformar revisao em processo repetivel.

Objetivo:
1. permitir revisao consistente por IA;
2. reduzir retrabalho entre sessoes;
3. separar diagnostico, patch e validacao;
4. sustentar cadencia futura de `2 licoes por dia`.

---

## 2) Ordem obrigatoria de leitura antes de revisar
1. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
2. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
3. topicos relevantes da licao
4. transversais relevantes da licao
5. licao atual
6. licao anterior
7. licao seguinte

Regra:
1. nao revisar uma licao isoladamente do seu encadeamento.

---

## 3) Pre-flight obrigatorio
Antes de editar qualquer HTML:

1. confirmar arquivo da licao atual;
2. abrir licao anterior e proxima;
3. confirmar que o arquivo esta em UTF-8;
4. identificar se a licao e `MV-S-000` ou licao padrao;
5. identificar se ha alias legado relevante (`O Concreto`);
6. consultar os topicos correspondentes.

Checklist:
1. qual e a promessa da licao?
2. qual guardiao lidera?
3. qual local aparece no Ritual?
4. qual conceito concreto precisa ser vivido?
5. qual e o gancho para a proxima?

Se alguma dessas respostas estiver nebulosa:
1. parar o patch e diagnosticar antes.

---

## 4) Ordem oficial da revisao
Toda licao deve ser revisada nesta ordem:

1. Estrutura
2. Navegacao
3. Narrativa
4. Pedagogia
5. Acabamento premium
6. Validacao final
7. Registro

Racional:
1. sem estrutura correta, o refinamento de escrita vira remendo;
2. sem navegacao correta, a jornada curricular quebra;
3. sem pedagogia concreta, a beleza narrativa nao sustenta o objetivo.

---

## 5) Passo 1 - Diagnostico
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
5. atividade concreta abstrata demais para Sementes.

Saida esperada:
1. lista de findings com arquivo e impacto.

---

## 6) Passo 2 - Patch estrutural
Corrigir primeiro o que pode reprovar a licao mesmo com texto bom.

Ordem:
1. Base do Documento
2. Header Superior
3. ordem das secoes
4. navegacao inferior
5. labels e classes
6. cards e reveals

Regra:
1. nao reescrever a narrativa antes de garantir que a arquitetura da pagina esta certa.

---

## 7) Passo 3 - Patch narrativo
Depois da estrutura, revisar a experiencia.

Verificar:
1. Portador com dignidade;
2. guardiao com voz propria;
3. revelacao do local no Ritual;
4. revelacao do guardiao na Jornada;
5. transicoes suaves;
6. tom convidativo, nao militar.

Perguntas de controle:
1. o texto soa como roteiro premium ou como rascunho escolar?
2. o adulto se sente guiado ou sobrecarregado?
3. a crianca e tratada como pessoa capaz?

---

## 8) Passo 4 - Patch pedagogico
Verificar se a licao ensina de verdade.

Checar:
1. concreto no centro;
2. objetivo claro;
3. narracao ajudando a fixar;
4. perguntas de reconto vivas;
5. `Sementes para o Dia` opcionais e uteis;
6. `Formacao do Portador` realmente formativa.

Vetos:
1. abstracao precoce;
2. tarefa fria;
3. explicacao longa substituindo experiencia;
4. extensao extra cansativa.

---

## 9) Passo 5 - Acabamento premium
Depois de corrigir o essencial, lapidar.

Checar:
1. repeticao de frase;
2. excesso de aspas;
3. imperativos duros;
4. blocos longos demais;
5. ritmo visual;
6. clareza de escaneamento no celular.

Objetivo:
1. deixar a licao com aparencia e leitura de produto premium.

---

## 10) Passo 6 - Validacao final
Toda licao deve fechar com estes gates:

### Gate NS - North Star
PASS quando:
1. a licao alivia o adulto;
2. encanta a crianca;
3. honra dignidade, concretude e beleza redentora;
4. ainda soa como Matemática Viva.

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
3. extensoes e formacao coerentes.

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

BLOCK se qualquer gate falhar.

---

## 11) Sanity check obrigatorio de encoding
Depois de editar uma licao HTML, rodar:

```powershell
rg -n "Ã|Â|â|\b\w+\?\w+\b" site/sementes/MV-S-00[0-3]*.html
```

Regra:
1. se aparecer sinal de encoding quebrado, corrigir antes de encerrar.

---

## 12) Formato de log por licao
Registrar sempre:

```md
## MV-S-XXX - [Titulo]

### Findings
- Critico:
- Alto:
- Medio:

### Decisoes
- [...]

### Patch
- Estrutural:
- Narrativo:
- Pedagogico:

### Validacao
- North Star: PASS/BLOCK
- Estrutura: PASS/BLOCK
- Narrativa: PASS/BLOCK
- Pedagogia: PASS/BLOCK
- Navegacao: PASS/BLOCK
- Tecnica: PASS/BLOCK

### Risco residual
- [...]

### Proximo passo
- [...]
```

---

## 13) Definition of Ready de uma licao
Uma licao esta pronta para entrar em revisao quando:
1. a licao atual, anterior e proxima estao acessiveis;
2. o esqueleto e os topicos relevantes existem;
3. a excecao do Portal foi considerada, se aplicavel;
4. o objetivo curricular esta minimamente claro.

---

## 14) Definition of Done de uma licao
Uma licao so fecha quando:
1. todos os gates estiverem em PASS;
2. o texto estiver limpo e premium;
3. a pagina estiver coerente com o fluxo do ciclo;
4. o log tiver sido atualizado;
5. o encoding estiver preservado;
6. a resposta para `isso nos aproxima ou afasta do North Star?` for claramente `aproxima`.

---

## 15) Regra de cadencia
Cadencia alvo:
1. `2 licoes por dia`

Mas so depois de:
1. piloto `001-003` validado;
2. topicos essenciais criados;
3. rubrica estavel;
4. zero duvida estrutural grande no sistema.
