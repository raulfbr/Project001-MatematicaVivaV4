# ORGANIZACAO DA PASTA REVISAO
Data: 2026-03-04 21:14 (America/Sao_Paulo)

---

## 1) Decisao adotada
Limpeza **não destrutiva** da pasta `Revisao`:
1. manter apenas arquivos ativos (SSOT + checklist + framework),
2. mover conteúdos avulsos para arquivo histórico em `logs/Outros/Revisao_Legado/`.

Motivo:
1. reduzir ruído operacional,
2. evitar apagar conhecimento histórico,
3. preservar compatibilidade com template e padrões atuais.

---

## 2) Estado final de `Revisao`
Arquivos ativos:
1. `Revisao/padrao_visual_sementes.md`
2. `Revisao/topicos_licao_revisao.md`
3. `Revisao/framework_estrategia_mestria.md`
4. `Revisao/README.md` (novo guia de organização)

Arquivos movidos para legado:
1. `Revisao/anuncio_whatsapp_maes.md` -> `logs/Outros/Revisao_Legado/anuncio_whatsapp_maes.md`
2. `Revisao/revisao_licao003.md` -> `logs/Outros/Revisao_Legado/revisao_licao003.md`

---

## 3) Ajustes de governança
1. `INICIAR_AQUI` atualizado para incluir `Revisao/README.md` e `Revisao/framework_estrategia_mestria.md` na ordem obrigatória de leitura.

---

## 4) Risco evitado
Nenhum arquivo referenciado pelo template ativo foi removido.
`framework_estrategia_mestria.md` foi mantido por dependência explícita em:
1. `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml`
2. `Revisao/padrao_visual_sementes.md`
