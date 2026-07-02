import streamlit as st

from utils.loader import load_data

# ---------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------

st.set_page_config(
    page_title="Ames Housing Dashboard",
    page_icon="🏠",
    layout="wide"
)


# ======================================================
# CARGA DEL DATASET
# ======================================================
df = load_data()

    """
    Lee el archivo CSV y devuelve un DataFrame.
    Streamlit almacenará el resultado en caché para
    evitar leer el archivo en cada actualización.
    """
    df = pd.read_csv("data/ames_housing_clean.csv")
    return df







# ---------------------------------------------------
# TÍTULO
# ---------------------------------------------------

st.title("🏠 Ames Housing Dashboard")

st.subheader("Proyecto Final de Analítica de Datos")

st.markdown("---")

st.write(
    """
Dashboard interactivo para el análisis y predicción del precio de viviendas utilizando el dataset Ames Housing.
"""
)


# Cargar el dataset
df = cargar_datos()






# ======================================================
# KPIs PRINCIPALES
# ======================================================

st.markdown("---")
st.header("📊 Indicadores Principales")

# Crear cuatro columnas
col1, col2, col3, col4 = st.columns(4)

# KPI 1
with col1:
    st.metric(
        label="💰 Precio Promedio",
        value=f"${df['SalePrice'].mean():,.0f}"
    )

# KPI 2
with col2:
    st.metric(
        label="🏠 Total de Viviendas",
        value=len(df)
    )

# KPI 3
with col3:
    st.metric(
        label="📍 Vecindarios",
        value=df["Neighborhood"].nunique()
    )

# KPI 4
with col4:
    st.metric(
        label="🤖 Mejor R²",
        value="0.911"
    )