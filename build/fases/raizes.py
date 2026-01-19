from pathlib import Path
from core.engine import GutenbergEngine, ForgeLogger
from core.navigation import NavigationService

class RaizesConfig:
    """Configuração ISOLADA da Fase Raízes."""
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    INPUT_DIR = PROJECT_ROOT / "curriculo/02_RAIZES"
    OUTPUT_DIR = PROJECT_ROOT / "site/raizes"
    
    # Templates ISOLADOS por fase
    TEMPLATES_DIR = PROJECT_ROOT / "site/raizes/templates" # Apontando para próprio reino
    TEMPLATE_NAME = "licao.j2"
    
    # Assets ISOLADOS
    ASSETS_DIR = PROJECT_ROOT / "site/assets/raizes"

class RaizesDriver(GutenbergEngine):
    """Driver Específico para Fase Raízes."""
    def __init__(self, dry_run=False):
        super().__init__(RaizesConfig, dry_run)
    
    def render_all(self):
        ForgeLogger.log("🌳 Raízes: Calculando Navegação Linear...", status="🌳")
        self.lessons_index = NavigationService.calculate_links(self.lessons_index)
        ForgeLogger.log(f"🔗 Navegação injetada em {len(self.lessons_index)} lições.", status="🔗")
        
        for item in self.lessons_index:
            if 'prev_licao' in item:
                item['data']['licao']['navegacao_calculada_prev'] = item['prev_licao']
            if 'next_licao' in item:
                item['data']['licao']['navegacao_calculada_next'] = item['next_licao']
        
        super().render_all()

    def validate_lesson(self, fpath, data):
        """Validação Raízes: CPA permitido."""
        if 'licao' not in data:
            ForgeLogger.log(f"❌ {fpath.name}: YAML sem chave 'licao'.", status="⚠️")
            return False
        
        # Diferente de Sementes, Raízes permite Pictórico.
        return True
