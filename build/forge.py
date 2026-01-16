import argparse
import sys
from pathlib import Path

# Adiciona o diretório atual ao path para importações funcionarem
sys.path.append(str(Path(__file__).parent))

from fases.sementes import SementesDriver

def main():
    parser = argparse.ArgumentParser(description="Forja Gutenberg V2: Modular Build System")
    parser.add_argument("--fase", type=str, required=True, choices=['sementes'], 
                        help="Qual fase do currículo renderizar")
    parser.add_argument("--dry-run", action="store_true", help="Executa verificação sem gravacao em disco")
    
    args = parser.parse_args()
    
    print(f"🛠️  Gutenberg V2: Iniciando driver para fase '{args.fase.upper()}'...")
    
    if args.fase == 'sementes':
        forge = SementesDriver(dry_run=args.dry_run)
        forge.run()

if __name__ == "__main__":
    main()
