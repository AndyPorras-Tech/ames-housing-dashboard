from pathlib import Path

# Carpeta dashboard
DASHBOARD_DIR = Path(__file__).resolve().parent

# Carpeta raíz del proyecto
PROJECT_ROOT = DASHBOARD_DIR.parent

# Dataset
DATA_PATH = PROJECT_ROOT / "data" / "ames_housing_clean.csv"

# Modelos
MODELS_PATH = PROJECT_ROOT / "models"

# Recursos
ASSETS_PATH = DASHBOARD_DIR / "assets"