from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader
from core.engine import ForgeLogger

class LivrosDriver:
    """
    O Bibliotecário.
    Transforma Markdown puro (Livros Dourados) em HTML Imersivo.
    """
    def __init__(self, config):
        self.config = config
        self.env = Environment(loader=FileSystemLoader(self.config.TEMPLATES_DIR))
        self.input_dir = self.config.PROJECT_ROOT / "curriculo/90_LIVRO_DOURADO"
        self.output_dir = self.config.PROJECT_ROOT / "site/livros"

    def run(self):
        ForgeLogger.log("Iniciando Driver de Livros...", status="📖")
        
        if not self.input_dir.exists():
            ForgeLogger.log("Pasta de Livros Dourados não encontrada.", status="⏭️")
            return

        # Garante output
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)

        md_files = list(self.input_dir.glob("*.md"))
        if not md_files:
            ForgeLogger.log("Nenhum Livro Dourado encontrado (.md).", status="search")
            return

        template = self.env.get_template("livro.j2")

        for md_file in md_files:
            # Ignora arquivos de sistema/meta
            if md_file.name.startswith("_") or "CONCEITO" in md_file.name or "CONSELHO" in md_file.name:
                continue

            with open(md_file, 'r', encoding='utf-8') as f:
                text = f.read()
                
            # Parse MD -> HTML
            html_content = markdown.markdown(text)
            
            # Render Final
            final_html = template.render(
                titulo=md_file.stem.replace('_', ' ').replace('-', ' ').title(),
                conteudo=html_content
            )
            
            out_file = self.output_dir / f"{md_file.stem.lower()}.html"
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(final_html)
                
            ForgeLogger.success(f"Livro publicado: {out_file.name}")
