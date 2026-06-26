import streamlit as st

st.set_page_config(
    page_title="Ames Housing Dashboard",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Ames Housing Dashboard")

st.subheader("Proyecto de Analítica de Datos")

st.write(
    """
    Bienvenido.

    Este dashboard presenta el análisis exploratorio,
    los indicadores principales y los modelos predictivos
    desarrollados sobre el conjunto de datos Ames Housing.
    """
)