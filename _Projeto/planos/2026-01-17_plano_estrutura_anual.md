# 📐 PLANO IMPECÁVEL: Arquitetura K-12 Explícita (13 Anos)

**Data**: 2026-01-17
**Status**: Pronto para Execução (Aguardando Retorno do Usuário)
**Estratégia**: Arquitetura Explícita + Migração Direta (Com Backup)
**Objetivo**: Garantir independência total de configuração e lógica para cada um dos 13 anos do currículo.

---

## 🏗️ O Conceito: Arquitetura Explícita ("What You See Is What You Isolate")

Para atender ao requisito *"Cada ano é diferente"*, abandonamos qualquer tentativa de configuração genérica ("mágica").
Adotamos a **Explicitação Total**.

### A Regra de Ouro
> **Se existe um Ano no Currículo, existe um Arquivo Python exclusivo para ele.**

Isso garante que:
1.  **Independência**: Editar o `ano9.py` (Legado) jamais quebrará o `ano1.py` (Raízes).
2.  **Legibilidade**: O programador futuro não precisa adivinhar onde a configuração está; ela está no arquivo do ano.
3.  **Evolução**: Se o 5º Ano precisar de uma regra nova (ex: "Sem imagens"), basta adicionar um método no `ano5.py`.

---

## 🗺️ O Mapa da Mina (Estrutura de Diretórios To-Be)

```text
build/
  fases/
    # --- FASE 1: RAÍZES (Anos 1-5) ---
    raizes/
       __init__.py
       base.py    (CLASSE ABSTRATA: Lógica compartilhada de navegação e Jinja)
       ano1.py    (CLASSE CONCRETA: Config exclusiva do Ano 1)
       ano2.py    (Futuro...)
       ...
    
    # --- FASE 2: LÓGICA (Anos 6-9) ---
    logica/
       base.py
       ano6.py
       ...

    # --- FASE 3: LEGADO (Anos 10-12) ---
    legado/
       base.py
       ano10.py   (Implementa Protocolo Dual Printing)
```

---

## 🛡️ Execução: A Migração do Raízes 1 (Passo a Passo)

> [!CRITICAL]
> **SEGURANÇA**: O usuário confirmou que fará um **BACKUP MANUAL** antes desta execução.
> Isso nos permite migrar a estrutura `raizes.py` diretamente, sem criar pastas temporárias.

### Passo 1: Criação da Infraestrutura de Pacotes
O arquivo atual `build/fases/raizes.py` contém lógica mista (configuração + motor). Vamos separá-lo.

1.  **Criar Pasta**: `build/fases/raizes/`
2.  **Converter em Base**: Mover o atual `raizes.py` para `build/fases/raizes/base.py`.
3.  **Refatorar Base**: Renomear a classe `RaizesDriver` para `RaizesBaseDriver` e remover quaisquer caminhos hardcoded (`INPUT_DIR`, etc.). Ela deve se tornar uma classe puramente lógica.

### Passo 2: O Nascimento do Ano 1
Criaremos o primeiro "cidadão" dessa nova arquitetura.

1.  **Criar Arquivo**: `build/fases/raizes/ano1.py`
2.  **Implementar**:
    ```python
    from .base import RaizesBaseDriver
    
    class Raizes1Driver(RaizesBaseDriver):
        """
        Driver exclusivo para o 1º Ano (Raízes I).
        Regra: Apenas configura os caminhos. A lógica vem da Base.
        """
        def __init__(self, dry_run=False):
            super().__init__(dry_run=dry_run)
            self.input_dir = "curriculo/02_RAIZES/01_RAIZES_I"
            self.output_dir = "site/raizes/ano1"
            self.templates_dir = "site/raizes/templates/ano1"
    ```

### Passo 3: Atualização da Forja (CLI)
O `forge.py` precisa saber que o "Raízes" agora é específico.

1.  **Atualizar Import**: De `from fases.raizes import RaizesDriver` para `from fases.raizes.ano1 import Raizes1Driver`.
2.  **Atualizar Chamada**: Instanciar `Raizes1Driver`.

### Passo 4: Migração de Ativos (Templates)
Para garantir isolamento visual (atmosfera):

1.  **Criar Pasta**: `site/raizes/templates/ano1/`
2.  **Mover Templates**: Transferir todos os `.j2` atuais para essa nova pasta.

---

## 🧪 Verificação de Sucesso (Definition of Done)

Ao rodar `python build/forge.py --fase raizes`:
1.  **Leitura**: O sistema deve ler `L001` da pasta `01_RAIZES_I`.
2.  **Escrita**: O site deve ser gerado em `site/raizes/ano1/`.
3.  **Visual**: O HTML deve abrir corretamente, carregando CSS e imagens (ajustar caminhos relativos se necessário).

---

## 🔮 Visão de Futuro (Escalabilidade)

Para adicionar o **Raízes 2** amanhã, você fará apenas:
1.  Criar `build/fases/raizes/ano2.py`.
2.  Criar `site/raizes/templates/ano2/`.
3.  Pronto. O Ano 1 permanece intocado e seguro.

Este é o **Padrão de Ouro** para a arquitetura K-12.
Bom descanso. Estamos prontos para executar quando voltar. 😴🦅
