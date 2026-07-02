from pathlib import Path

import pandas as pd
import streamlit as st


# Ruta de la carpeta raíz del proyecto
BASE_DIR = Path(__file__).resolve().parents[2]

# Ruta del dataset
DATA_PATH = BASE_DIR / "data" / "ames_housing_clean.csv"


@st.cache_data
def load_data():
    """
    Carga el dataset limpio y lo almacena en caché.
    """
    df = pd.read_csv(DATA_PATH)
    return df