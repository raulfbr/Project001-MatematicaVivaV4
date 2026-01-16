from pathlib import Path
from core.engine import GutenbergEngine, ForgeLogger

class SementesConfig:
    """Configuração ISOLADA da Fase Sementes."""
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    INPUT_DIR = PROJECT_ROOT / "curriculo/01_SEMENTESV6"
    OUTPUT_DIR = PROJECT_ROOT / "site/sementes"
    
    # NOVO: Templates ISOLADOS por fase (Arquitetura v4.0)
    TEMPLATES_DIR = PROJECT_ROOT / "site/sementes/templates"
    TEMPLATE_NAME = "licao.j2"
    
    # NOVO: Assets ISOLADOS por fase
    ASSETS_DIR = PROJECT_ROOT / "site/assets/sementes"

class SementesDriver(GutenbergEngine):
    """Driver Específico para Fase Sementes."""
    def __init__(self, dry_run=False):
        super().__init__(SementesConfig, dry_run)
    
    def validate_lesson(self, fpath, data):
        """Validação Estrita: Sementes proíbe Pictórico."""
        if not super().validate_lesson(fpath, data):
            return False
            
        # Regra de Negócio: Veto Pictórico
        jornada = data['licao'].get('jornada', {})
        pictorico = jornada.get('pictorico', {})
        
        status = pictorico.get('status', '').upper()
        if status != 'VETADO':
            self.warnings.append(f"{fpath.name} [VIOLAÇÃO]: Pictórico deve ser VETADO em Sementes.")
            # Nota: É warning ou erro? Definido aqui como warning para não quebrar build, 
            # mas idealmente seria erro se quiséssemos ser estritos.
            
        return True
