import argparse
import sys
from pathlib import Path

# Adiciona o diretório atual ao path para importações funcionarem
sys.path.append(str(Path(__file__).parent))

from fases.sementes import SementesDriver
from fases.landing import LandingDriver
from fases.livros import LivrosDriver
from core.logger import ForgeLogger

class ForgeConfig:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    TEMPLATES_DIR = PROJECT_ROOT / "site/templates"
    # Configs específicas são herdadas ou definidas aqui se globais

def main():
    parser = argparse.ArgumentParser(description="Forja Gutenberg V3: The Master Builder")
    parser.add_argument("--fase", type=str, choices=['sementes', 'livros', 'all'], default='all',
                        help="Qual fase renderizar (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="Executa verificação sem gravacao")
    
    args = parser.parse_args()
    
    ForgeLogger.log("🔨  FORGE V3 INICIADA", status="🚀")
    
    drivers = []
    
    # 1. Builders de Conteúdo (Geram arquivos que o Index vai ler)
    if args.fase in ['sementes', 'all']:
        drivers.append(SementesDriver(dry_run=args.dry_run))
        
    if args.fase in ['livros', 'all']:
        drivers.append(LivrosDriver(ForgeConfig))

    # Executa Builders
    for d in drivers:
        d.run()

    # 2. Builder do Index (Landing) - Sempre roda se for 'all' ou explícito, 
    # mas precisa rodar DEPOIS do conteúdo estar pronto.
    if args.fase == 'all' and not args.dry_run:
        landing = LandingDriver(ForgeConfig)
        landing.build()

    ForgeLogger.log("🏁  FORGE V3 FINALIZADA", status="DONE")

if __name__ == "__main__":
    main()
