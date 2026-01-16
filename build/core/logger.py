import datetime

class ForgeLogger:
    """Central de Logs com Timestamps (Engenharia: Feedback Rápido)."""
    @staticmethod
    def log(msg, item=None, status="ℹ️"):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        item_str = f" [{item}]" if item else ""
        print(f"[{timestamp}] {status}  {msg}{item_str}", flush=True)

    @staticmethod
    def success(msg): ForgeLogger.log(msg, status="✅ ")
    
    @staticmethod
    def warn(msg): ForgeLogger.log(msg, status="⚠️ ")
    
    @staticmethod
    def error(msg): ForgeLogger.log(msg, status="💥")
