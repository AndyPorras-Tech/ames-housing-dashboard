import streamlit as st

# ---------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------

st.set_page_config(
    page_title="Ames Housing Dashboard",
    page_icon="🏠",
    layout="wide"
)

# ---------------------------------------------------
# TÍTULO
# ---------------------------------------------------

st.title("🏠 Ames Housing Dashboard")

st.subheader("Proyecto Final de Analítica de Datos")

st.markdown("---")

st.write(
    """
Este dashboard presenta el análisis realizado sobre el conjunto de datos
**Ames Housing**, incluyendo:

- Exploración de datos (EDA)
- Indicadores principales (KPIs)
- Visualizaciones interactivas
- Modelos de Machine Learning
- Predicción del precio de viviendas
"""
)