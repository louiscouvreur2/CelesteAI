from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

AI = ROOT / "ai"
CONFIG = ROOT / "config"
CORE = ROOT / "core"
GUI = ROOT / "gui"
ENV = ROOT / "env"

MODELS = ROOT / "models"
SAVES = ROOT / "saves"
LOGS = ROOT / "logs"
ASSETS = ROOT / "assets"


def create_directories():
    """Crée automatiquement tous les dossiers nécessaires."""

    for directory in (
        MODELS,
        SAVES,
        LOGS,
        ASSETS,
    ):
        directory.mkdir(exist_ok=True)