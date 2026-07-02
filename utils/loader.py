import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """
    Carga el dataset limpio y lo almacena en caché.
    """
    df = pd.read_csv("../data/ames_housing_clean.csv")
    return df