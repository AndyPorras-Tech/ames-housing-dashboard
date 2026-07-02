import pandas as pd
import streamlit as st

from config import DATA_PATH


@st.cache_data
def load_data():
    """
    Carga el dataset limpio.
    """

    return pd.read_csv(DATA_PATH)