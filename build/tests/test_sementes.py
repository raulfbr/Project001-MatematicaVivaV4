"""
Testes Básicos para Gutenberg V2.4
Referência: engenharia.yaml (QA: Testes são Documentação)

Uso: python -m pytest build/tests/test_sementes.py
"""
import sys
from pathlib import Path

# Adiciona build/ ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fases.sementes import SementesDriver


def test_sementes_dry_run_no_errors():
    """Verifica que o build Sementes roda sem erros em dry-run."""
    driver = SementesDriver(dry_run=True)
    driver.run()
    
    # Não deve haver erros críticos
    assert len(driver.errors) == 0, f"Erros encontrados: {driver.errors}"


def test_sementes_detects_lessons():
    """Verifica que o driver detecta as lições YAML."""
    driver = SementesDriver(dry_run=True)
    driver.run()
    
    # Deve encontrar pelo menos 1 lição
    assert len(driver.lessons_index) >= 1, "Nenhuma lição encontrada"


def test_sementes_indexes_assets():
    """Verifica que o asset manager indexa arquivos."""
    driver = SementesDriver(dry_run=True)
    driver.run()
    
    # Deve indexar pelo menos 1 asset
    assert len(driver.assets_index) >= 1, "Nenhum asset indexado"


def test_sementes_config_paths_exist():
    """Verifica que os paths configurados existem."""
    from fases.sementes import SementesConfig
    
    assert SementesConfig.INPUT_DIR.exists(), f"INPUT_DIR não existe: {SementesConfig.INPUT_DIR}"
    assert SementesConfig.TEMPLATES_DIR.exists(), f"TEMPLATES_DIR não existe: {SementesConfig.TEMPLATES_DIR}"
    assert SementesConfig.ASSETS_DIR.exists(), f"ASSETS_DIR não existe: {SementesConfig.ASSETS_DIR}"


if __name__ == "__main__":
    # Permite rodar diretamente: python build/tests/test_sementes.py
    test_sementes_dry_run_no_errors()
    print("✅ test_sementes_dry_run_no_errors PASSED")
    
    test_sementes_detects_lessons()
    print("✅ test_sementes_detects_lessons PASSED")
    
    test_sementes_indexes_assets()
    print("✅ test_sementes_indexes_assets PASSED")
    
    test_sementes_config_paths_exist()
    print("✅ test_sementes_config_paths_exist PASSED")
    
    print("\n🎉 Todos os testes passaram!")
