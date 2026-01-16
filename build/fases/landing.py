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
        """Varre as lições JÁ BUILDADAS em site/sementes."""
        sementes_dir = self.output_dir / "sementes"
        lessons = []
        
        if not sementes_dir.exists():
            return []

        # Procura arquivos HTML reais (exceto index se houver)
        for f in sorted(sementes_dir.glob("MV-S-*.html")):
            # Extrai metadados simples do nome ou poderia ler um .meta.json se tivéssemos
            # Por simplicidade V3: infere do nome MV-S-001_A_TRINDADE...
            parts = f.stem.split('_')
            lid = parts[0].replace('MV-S-', '') # 001
            
            # Tenta mapear Guardião rapidinho (Hardcoded MVP, ideal seria ler YAML original)
            # Mapa rápido de ID -> Guardião (Baseado no index.html original)
            guardiao_map = {
                "000": ("melquior", "leao", "O Início de Tudo"),
                "001": ("celeste", "raposa", "A Trindade na Palma"),
                "002": ("bernardo", "urso", "As Pedras da Fortaleza"),
                "003": ("iris", "passarinho", "A Estrela do Reino"),
                "004": ("noe", "coruja", "O Ritmo do Criador")
            }
            
            g_data = guardiao_map.get(lid, ("melquior", "leao", "Lição do Reino"))
            
            lessons.append({
                "id": f"LIÇÃO {lid}",
                "guardiao": g_data[0],
                "guardiao_animal": g_data[1],
                "titulo": g_data[2], # Título bonitinho do mapa
                "desc": "Uma aventura no Reino Contado.", # Placeholder desc
                "filename": f.name
            })
            
        return lessons

    def scan_livros(self):
        """Varre livros em site/livros."""
        livros_dir = self.output_dir / "livros"
        livros = []
        if livros_dir.exists():
            for f in livros_dir.glob("*.html"):
                livros.append({
                    "titulo": f.stem.replace('-', ' ').title(),
                    "desc": "Narrativa Visual Vivente.",
                    "filename": f.name
                })
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
