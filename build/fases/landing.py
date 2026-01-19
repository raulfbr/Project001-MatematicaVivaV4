from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from core.logger import ForgeLogger

class LandingDriver:
    """
    O Maestro do Index. 
    Responsável por olhar o Reino (pastas site/) e desenhar o Mapa (index.html).
    """
    def __init__(self, config):
        self.config = config
        self.env = Environment(loader=FileSystemLoader(self.config.TEMPLATES_DIR))
        self.output_dir = self.config.PROJECT_ROOT / "site"

    def scan_sementes(self):
        """Varre as lições e LÊ O YAML ORIGINAL para metadados ricos."""
        sementes_yaml_dir = self.config.PROJECT_ROOT / "curriculo/01_SEMENTESV6"
        lessons = []
        
        # Procura YAMLs, não HTMLs outputados, para garantir Source of Truth
        if not sementes_yaml_dir.exists():
            return []
            
        # Importante: GutenbergEngine importado dentro do metodo para evitar ciclo ou duplicar logica simples load_yaml
        import yaml
        
        # Injeção MANUAL da Lição 000 (O Portal do Reino)
        # Motivo: YAML removido da build para preservar html manual.
        lessons.append({
            "id": "MV-S-000",
            "display_id": "Lição 000",
            "titulo": "O Portal do Reino",
            "desc": "A entrada solene no mundo da Matemática Viva. Conheça os Guardiões e a geografia do Reino.",
            "guardiao": "melquior",
            "guardiao_animal": "leao",
            "objetivo_pedagogico": "Introdução à Narrativa e Geografia",
            "filename": "MV-S-000_O_PORTAL_DO_REINO.html",
            "metadados": {}
        })
        
        # Varre YAMLs
        for f in sorted(sementes_yaml_dir.glob("*.yaml")):
            if f.name.startswith("_"): continue
            
            try:
                with open(f, 'r', encoding='utf-8') as yf:
                    data = yaml.safe_load(yf)
                    
                meta = data.get('licao', {}).get('metadados', {})
                if not meta: continue
                
                # Mapeia para estrutura do index
                # Filename esperado: ID_TITULO_SLUG.html ou similar. 
                # O SementesDriver gera based on ID_TITLE. Vamos reconstruir ou achar o arquivo.
                # Simplificação V3: O driver gera output com nome baseado no YAML.
                # Vamos assumir que titulo -> slug.
                # Mas espera, o index precisa apontar para o arquivo REAL.
                # Melhor estratégia: Listar HTMLs gerados e casar com YAMLs por ID?
                # Ou confiar que o nome gerado segue padrão?
                # Padrão Engine: output_path = output_dir / f"{data['licao']['metadados']['id']}_{slugify(data['licao']['metadados']['titulo'])}.html"
                
                # Para MVP rápido e seguro: Vamos listar os HTMLs existentes e tentar extrair ID deles para match.
                # OU simplesmente confiar pque o build acabou de rodar.
                
                # Vamos reconstruir o nome do arquivo da mesma forma que o Engine faz.
                # Importar slugify é chato aqui.
                # Vamos usar uma abordagem hibrida: Ler YAML, e procurar arquivo HTML que começa com o ID.
                
                lid = meta.get('id')
                
                # Mapeamento de Animais (Hardcoded por enquanto, mas robusto)
                guardian_map = {
                    "celeste": "raposa",
                    "bernardo": "urso",
                    "melquior": "leao",
                    "iris": "passarinho",
                    "noe": "coruja"
                }
                
                guardiao_nome = meta.get('guardiao_lider', 'melquior').lower()
                guardiao_animal = guardian_map.get(guardiao_nome, "leao")

                clean_title = str(meta.get('titulo', 'Sem Título')).replace(' ', '_').upper()
                clean_title = "".join([c for c in clean_title if c.isalnum() or c in ('_', '-')])
                filename = f"{lid}_{clean_title}.html"
                
                # Extraindo objetivo pedagógico (removendo colchetes se houver)
                obj_raw = meta.get('objetivo_pedagogico', 'Fundamentos Gerais')
                obj_clean = obj_raw.replace('[', '').replace(']', '').replace('Foco:', '').strip()
                
                lessons.append({
                    "id": lid,
                    "display_id": lid.replace("MV-S-", "Lição ") if lid else "N/A",
                    "titulo": meta.get('titulo', 'Sem Título'),
                    "desc": data.get('licao', {}).get('para_portador', {}).get('ideia_viva', {}).get('frase', '...'),
                    "guardiao": guardiao_nome,
                    "guardiao_animal": guardiao_animal,
                    "objetivo_pedagogico": obj_clean,
                    "filename": filename,
                    "metadados": meta
                })
                
            except Exception as e:
                ForgeLogger.log(f"Erro lendo metadados de {f.name}: {str(e)}", status="⚠️")
                continue
            
        return lessons

    def scan_livros(self):
        """Varre os MARKDOWNS ORIGINAIS de livros para metadados ricos."""
        livros_md_dir = self.config.PROJECT_ROOT / "curriculo/90_LIVRO_DOURADO"
        livros = []
        
        if not livros_md_dir.exists():
            return []

        import yaml
        
        for f in sorted(livros_md_dir.glob("*.md")):
            if f.name.startswith("_") or f.name.startswith("CONCEITO"): continue
            
            try:
                # Ler Frontmatter
                with open(f, 'r', encoding='utf-8') as mdf:
                    content = mdf.read()
                    
                if content.startswith("---"):
                    try:
                        # Extrai bloco YAML
                        parts = content.split("---", 2)
                        if len(parts) >= 3:
                            meta = yaml.safe_load(parts[1])
                        else:
                            meta = {}
                    except:
                        meta = {}
                else:
                    meta = {}

                # Nome do arquivo HTML gerado (slugify basico igual ao Forge)
                # O forge livros usa o proprio nome do md lower()
                html_filename = f.stem.lower().replace(' ', '_') + ".html"
                
                livros.append({
                    "titulo": meta.get('titulo', f.stem.title()),
                    "desc": meta.get('resumo', 'Uma narrativa visual imersiva das matemáticas vivas.'),
                    "filename": html_filename,
                    "fase": meta.get('fase', 'Ouro'),
                    "guardia": meta.get('guardia', 'Melquior')
                })
                
            except Exception as e:
                ForgeLogger.log(f"Erro lendo livro {f.name}: {str(e)}", status="⚠️")
                continue
                
        return livros

    def generate_placeholders(self):
        """Gera as páginas 'Em Breve'."""
        template = self.env.get_template("placeholder.j2")
        placeholders_dir = self.output_dir / "placeholders"
        
        ciclos = [
            {"id": "brotos", "nome": "Ciclo Brotos", "icon": "🌰"},
            {"id": "raizes", "nome": "Ciclo Raízes", "icon": "🌳"},
            {"id": "logica", "nome": "Lógica & Retórica", "icon": "🦉"},
            {"id": "legado", "nome": "O Legado", "icon": "🏺"}
        ]
        
        for c in ciclos:
            html = template.render(ciclo=c['nome'], icon=c['icon'])
            with open(placeholders_dir / f"{c['id']}.html", 'w', encoding='utf-8') as f:
                f.write(html)
            ForgeLogger.log(f"Placeholder Gerado: {c['id']}.html", status="🚧")

    def build(self):
        ForgeLogger.log("Iniciando Landing Driver...", status="🏠")
        
        # 1. Scan
        sementes = self.scan_sementes()
        livros = self.scan_livros()
        
        # 2. Gera Placeholders
        self.generate_placeholders()
        
        # 3. Define Estado de Navegação (Truth vs Promise)
        navegacao = {
            "brotos": {"ativo": False, "link": "placeholders/brotos.html"},
            "sementes": {"ativo": True, "link": "#sementes"}, # Sempre ativo pois temos lições
            "raizes": {"ativo": False, "link": "placeholders/raizes.html"},
            "logica": {"ativo": False, "link": "placeholders/logica.html"},
            "legado": {"ativo": False, "link": "placeholders/legado.html"},
        }

        # 4. Render Index
        template = self.env.get_template("index.j2")
        html = template.render(
            env_name="Production (Forge V3)",
            build_date=datetime.now().strftime("%d/%m/%Y %H:%M"),
            stats={"total_licoes": len(sementes)},
            sementes_licoes=sementes,
            livros=livros,
            navegacao=navegacao
        )
        
        with open(self.output_dir / "index.html", 'w', encoding='utf-8') as f:
            f.write(html)
            
        ForgeLogger.success("Index.html gerado com sucesso!")
