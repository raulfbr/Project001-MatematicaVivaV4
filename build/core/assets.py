import time
from pathlib import Path
from .logger import ForgeLogger

class AssetManager:
    """Gerenciador de Assets Visuais (Single-Pass)."""
    def __init__(self, assets_dir: Path):
        self.assets_dir = assets_dir
        self.index = {}

    def index_assets(self):
        """Phase 1: Asset Inventory (Single-Pass V2.2)."""
        ForgeLogger.log("Indexando Assets Visuais (Single-Pass)...")
        start = time.time()
        
        valid_extensions = {'.png', '.jpg', '.jpeg', '.svg', '.webp'}
        found_count = 0
        
        if not self.assets_dir.exists():
             ForgeLogger.error(f"Assets dir not found: {self.assets_dir}")
             return self.index

        # V2.2: Single-Pass Scan (Otimizado para OneDrive)
        for asset_path in self.assets_dir.rglob('*'):
            if asset_path.is_file() and asset_path.suffix.lower() in valid_extensions:
                try:
                    rel_path = asset_path.relative_to(self.assets_dir)
                    key = str(rel_path).replace('\\', '/')
                    self.index[key] = asset_path
                    found_count += 1
                except ValueError:
                    continue
        
        elapsed = time.time() - start
        ForgeLogger.success(f"Indexados {found_count} assets ({elapsed:.3f}s).")
        return self.index
