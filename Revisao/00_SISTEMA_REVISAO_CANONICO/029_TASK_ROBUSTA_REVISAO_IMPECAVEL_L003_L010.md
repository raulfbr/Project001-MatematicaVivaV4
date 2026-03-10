# TASK ROBUSTA - REVISAO IMPECAVEL L003 A L010
Data: 2026-03-10
Status: ativa para execucao em ondas
Escopo: revisar profundamente `MV-S-003` ate `MV-S-010` pelo protocolo central, com validacao humana posterior
Insumo-base: `logs/2026-03-10_REVIEW_L003_L004.md`

---

## 1) Objetivo desta task
1. abrir uma frente unica e disciplinada para `L003-L010`;
2. impedir revisao por impulso, memoria difusa ou patch isolado;
3. usar `L001-L002` como baseline de contrato, e nao como teto criativo;
4. entregar `L003-L010` alinhadas ao protocolo central e prontas para validacao humana posterior.

---

## 2) Decisao desta rodada
1. a validacao humana da Familia Rodrigues para `Manual`, `L001` e `L002` continua pendente, mas fica adiada para depois desta rodada;
2. por decisao explicita da sessao de `2026-03-10`, o lote `L003-L010` entra agora em revisao profunda por IA;
3. `L003` e `L004` ja receberam uma primeira passada forte nesta sessao e entram nesta task como baseline provisoria, nao como lote fechado;
4. `L005-L010` entram com sinais claros de modelo legado e exigem revisao completa;
5. esta task governa a cadencia e a integridade do lote, sem reescrever a governanca que ja mora em `023`.

---

## 3) Arquivos em escopo
1. `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html`
2. `site/sementes/MV-S-004_A_ORDEM_DO_DIA.html`
3. `site/sementes/MV-S-005_O_ESCONDERIJO_DA_GLÓRIA.html`
4. `site/sementes/MV-S-006_O_DESENHO_DO_REI.html`
5. `site/sementes/MV-S-007_A_COROA_DA_SEMANA.html`
6. `site/sementes/MV-S-008_O_PAR_PERFEITO.html`
7. `site/sementes/MV-S-009_O_CELEIRO_DE_NOÉ.html`
8. `site/sementes/MV-S-010_A_FILA_DA_PROVIDÊNCIA.html`

Fora de escopo desta task:
1. `Manual do Portador`;
2. revisao humana da Familia Rodrigues;
3. mudanca de governanca em `023`, `003`, `004`, `011_TOPICOS/` ou `012_TRANSVERSAIS/`, exceto se surgir contradicao dura.

---

## 4) Fontes obrigatorias
1. `README.md`
2. `Revisao/README.md`
3. `Revisao/000_COMECAR_AQUI.md`
4. `Revisao/001_CONTEXTO_DETALHADO_PROXIMA_SESSAO.md`
5. `Revisao/00_SISTEMA_REVISAO_CANONICO/015_ESTADO_REAL_DO_PROJETO_E_DIRECAO_HTML_FIRST.md`
6. `Revisao/00_SISTEMA_REVISAO_CANONICO/005_STATUS_REVISAO_SEMENTES.md`
7. `Revisao/00_SISTEMA_REVISAO_CANONICO/023_GUIA_CENTRAL_ATIVACAO_REVISAO_TOPICO_A_TOPICO.md`
8. `Revisao/00_SISTEMA_REVISAO_CANONICO/002_ESQUELETO_GERAL_LICAO_SEMENTES.md`
9. `Revisao/00_SISTEMA_REVISAO_CANONICO/003_PROTOCOLO_REVISAO_POR_LICAO.md`
10. `Revisao/00_SISTEMA_REVISAO_CANONICO/004_RUBRICA_PREMIUM_REVISAO.md`
11. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/000_README.md`
12. `Revisao/00_SISTEMA_REVISAO_CANONICO/011_TOPICOS/001_BASE_E_HERO.md` ate `012_NAVEGACAO_INFERIOR.md`
13. `Revisao/00_SISTEMA_REVISAO_CANONICO/012_TRANSVERSAIS/000_README.md`
14. pacote minimo transversal: `002`, `003`, `005`, `006`, `008`
15. `logs/2026-03-10_REVIEW_L003_L004.md`
16. a licao anterior e a proxima de cada pagina auditada

Regra:
1. ativar sempre a ordem de leitura oficial de `023`;
2. nenhuma licao entra por intuicao frouxa ou por espelhamento superficial com `L001-L002`.

---

## 5) Diagnostico de entrada do lote
### `L003-L004`
1. receberam reescrita forte em `2026-03-10`;
2. passaram na checagem estrutural rapida e nos anti-patterns mais visiveis;
3. ainda precisam de reauditoria em lote, especialmente nas fronteiras `002 -> 003`, `003 -> 004` e `004 -> 005`;
4. entram como referencia de direcao, nao como artefatos definitivamente fechados.

### `L005-L010`
1. compartilham um pacote legado claro: `[Foco:`, `Ritual de Abertura`, `Atividade Concreta`, `div onclick` e `Para a Familia`;
2. a estrutura `001-012` esta so parcialmente refletida no naming atual;
3. ha sinais explicitos de encoding ruim em trechos de titulo, hero, navegacao e links internos;
4. o risco nao e apenas cosmetico: link com nome corrompido pode quebrar continuidade curricular e auditoria tecnica;
5. o lote pede migracao disciplinada para o contrato canonico, nao remendo topico avulso.

---

## 6) Fios condutores obrigatorios do lote
1. pensar primeiro no macro da licao, antes de mexer nos blocos;
2. proteger a imagem dominante de cada pagina;
3. impedir colapso de fronteiras entre secoes adjacentes;
4. manter `O Concreto` como nucleo pedagogico vivido;
5. honrar `Narramos Juntos` como reconto real, nao interrogatorio;
6. manter `Sementes para o Dia` como opcionalidade leve e domestica;
7. usar `Formacao do Portador` para restaurar confianca e criterio, nao para despejar teoria;
8. preservar uso real em celular e casa cansada, inclusive com mais de uma crianca;
9. tratar encoding, links e semantica como parte do premium, nao como detalhe tecnico secundario.

---

## 7) Cerne minimo esperado por licao
### `MV-S-003`
1. proteger o cerne `4 guardam as bordas / 1 acende o centro`;
2. garantir que a estrela seja descoberta viva, e nao mero arranjo decorativo.

### `MV-S-004`
1. proteger o cerne `ordem estavel de 1 a 5, do primeiro ao ultimo`;
2. manter a ordem como claridade, nao como controle escolar.

### `MV-S-005`
1. tratar posicao espacial como experiencia viva: `em cima`, `embaixo`, `atras`, `na frente`;
2. impedir que a licao vire vocabulario abstrato de localizacao.

### `MV-S-006`
1. tratar o numero como desenho proprio e reconhecivel;
2. impedir que a licao deslize para treino escolar de traco.

### `MV-S-007`
1. proteger a passagem para `6` e `7` com clima de coroa e semana viva;
2. impedir que a pagina vire apenas contagem ampliada sem imagem dominante.

### `MV-S-008`
1. proteger a correspondencia um-a-um e a ideia de par vivo;
2. impedir colapso entre emparelhamento, organizacao e teste escolar.

### `MV-S-009`
1. proteger a entrada de `8` e `9` com peso de celeiro, espera e provisao;
2. impedir redundancia cansada com a licao anterior.

### `MV-S-010`
1. proteger ordinais ate `5o` como experiencia concreta de fila e providencia;
2. impedir que a licao vire nomenclatura seca de `primeiro`, `segundo` e `terceiro`.

Regra:
1. cada licao precisa preencher o cerne macro completo de `023` antes de qualquer patch.

---

## 8) Ondas obrigatorias de execucao
### Onda 1 - consolidacao de `L003-L004`
1. reabrir cerne macro das duas paginas;
2. reexecutar matriz `001-012`;
3. auditar fronteiras `002 -> 003`, `003 -> 004` e `004 -> 005`;
4. confirmar se o `PASS PREMIUM por IA` resiste ao lote.

### Onda 2 - migracao premium de `L005-L006`
1. revisar `L005` e `L006` como primeiro par legado;
2. patchar estrutura, naming, semantica, encoding e fronteiras;
3. proteger a diferenca entre posicao espacial e forma numerica;
4. auditar `004 -> 005`, `005 -> 006` e `006 -> 007`.

### Onda 3 - migracao premium de `L007-L008`
1. revisar `L007` e `L008` como segundo par legado;
2. proteger a passagem de quantidade ampliada para correspondencia um-a-um;
3. auditar `006 -> 007`, `007 -> 008` e `008 -> 009`.

### Onda 4 - migracao premium de `L009-L010`
1. revisar `L009` e `L010` como terceiro par legado;
2. corrigir com atencao redobrada links internos e nomes corrompidos;
3. auditar `008 -> 009`, `009 -> 010` e `010 -> 011`.

### Onda 5 - auditoria transversal do lote
1. reler `L003-L010` em sequencia;
2. verificar progressao curricular, respiracao entre paginas e integridade tecnica;
3. decidir se o lote fecha como `PASS PREMIUM por IA` ou se exige nova passada de patch.

---

## 9) Algoritmo obrigatorio por licao
1. ativar a leitura minima oficial de `023`;
2. congelar escopo da passada;
3. preencher o cerne macro da licao;
4. preencher a matriz `001-012` com `PASS / GAP / BLOCK`;
5. auditar fronteiras criticas da pagina;
6. classificar findings por severidade;
7. patchar primeiro estrutura, naming, semantica, links e encoding;
8. patchar depois narrativa, pedagogia e `Taste`;
9. reauditar topicos tocados e vizinhos imediatos;
10. fechar a rubrica de `004`;
11. registrar risco residual honesto;
12. marcar a licao como pronta para validacao humana posterior, se passar.

Regra:
1. nenhuma licao avanca de onda com `BLOCK` duro aberto;
2. se um patch mudar a promessa macro da licao, voltar ao cerne macro antes de seguir.

---

## 10) Gates obrigatorios por licao
### Gate de entrada
1. arquivo correto identificado;
2. licao anterior e seguinte abertas;
3. cerne macro preenchido;
4. topicos `001-012` abertos;
5. pacote minimo transversal aberto;
6. escopo congelado.

### Gate de saida
1. matriz `001-012` completa;
2. fronteiras criticas auditadas;
3. `BLOCK` duro inexistente;
4. sem labels legadas como `Ritual de Abertura`, `Atividade Concreta` e `Para a Familia`;
5. sem `div onclick` em CTA estrutural;
6. sem corrupcao evidente `Ã`, `Â`, `â` ou `ðŸ`;
7. navegacao anterior/proxima coerente com os nomes reais dos arquivos;
8. pronta para validacao humana posterior.

---

## 11) Registro obrigatorio por onda
Usar sempre:

```md
## Onda X - [Par ou etapa]

### Licao
- Arquivo:
- Estado de entrada:
- Cerne macro:
- Fronteiras criticas:

### Findings
- Critico:
- Alto:
- Medio:

### Patch
- Estrutural:
- Narrativo:
- Pedagogico:
- Tecnico:
- Taste:

### Validacao
- Matriz `001-012` fechada: SIM/NAO
- Fronteiras passaram: SIM/NAO
- Encoding passou: SIM/NAO
- Veredito da rubrica:

### Risco residual
- [...]

### Proximo passo
- [...]
```

Regra:
1. `L003-L004` precisam de registro proprio de reauditoria, mesmo ja tendo log preliminar;
2. a Onda 5 deve fechar com veredito do lote inteiro.

---

## 12) Criterio de fechamento desta task
Esta task so fecha quando:
1. `L003-L010` tiverem passado pela matriz `001-012`;
2. `L003-L004` tiverem sido revalidadas no contexto do lote;
3. `L005-L010` tiverem sido migradas ao contrato canonico atual;
4. as fronteiras `002 -> 003` ate `010 -> 011` estiverem respirando;
5. nao restarem anti-patterns legados nem corrupcao tecnica evidente;
6. o lote soar como uma trilha una, e nao como paginas corretas porem desconectadas;
7. o resultado final esteja pronto para validacao humana posterior da Familia Rodrigues.

---

## 13) Artefatos esperados ao final
1. `029_TASK_ROBUSTA_REVISAO_IMPECAVEL_L003_L010.md`
2. logs operacionais por onda
3. `site/sementes/MV-S-003_A_ESTRELA_DO_REINO.html`
4. `site/sementes/MV-S-004_A_ORDEM_DO_DIA.html`
5. `site/sementes/MV-S-005_O_ESCONDERIJO_DA_GLÓRIA.html`
6. `site/sementes/MV-S-006_O_DESENHO_DO_REI.html`
7. `site/sementes/MV-S-007_A_COROA_DA_SEMANA.html`
8. `site/sementes/MV-S-008_O_PAR_PERFEITO.html`
9. `site/sementes/MV-S-009_O_CELEIRO_DE_NOÉ.html`
10. `site/sementes/MV-S-010_A_FILA_DA_PROVIDÊNCIA.html`
11. atualizacao coerente do quadro de status, quando o lote avancar.
