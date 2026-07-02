# ==========================================================
# DASHBOARD PRINCIPAL
# Proyecto Final - Analítica de Datos
# ==========================================================

import streamlit as st

from utils.loader import load_data


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)


# ==========================================================
# CARGA DE DATOS
# ==========================================================

df = load_data()


# ==========================================================
# TÍTULO
# ==========================================================

st.title("🏠 Ames Housing Dashboard")

st.markdown("""
Dashboard interactivo para el análisis del mercado inmobiliario utilizando el dataset **Ames Housing**.
""")

st.divider()


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🎛️ Filtros")

st.sidebar.markdown("Selecciona los filtros que deseas aplicar.")

# Vecindario
neighborhood = st.sidebar.selectbox(
    "Vecindario",
    ["Todos"] + sorted(df["Neighborhood"].unique().tolist())
)

# Calidad General
overall_quality = st.sidebar.slider(
    "Calidad General",
    int(df["Overall Qual"].min()),
    int(df["Overall Qual"].max()),
    (
        int(df["Overall Qual"].min()),
        int(df["Overall Qual"].max())
    )
)

# Año de construcción
year = st.sidebar.slider(
    "Año de Construcción",
    int(df["Year Built"].min()),
    int(df["Year Built"].max()),
    (
        int(df["Year Built"].min()),
        int(df["Year Built"].max())
    )
)


# ==========================================================
# FILTRADO
# ==========================================================

df_filtered = df.copy()

# Vecindario
if neighborhood != "Todos":
    df_filtered = df_filtered[
        df_filtered["Neighborhood"] == neighborhood
    ]

# Calidad
df_filtered = df_filtered[
    (df_filtered["Overall Qual"] >= overall_quality[0]) &
    (df_filtered["Overall Qual"] <= overall_quality[1])
]

# Año
df_filtered = df_filtered[
    (df_filtered["Year Built"] >= year[0]) &
    (df_filtered["Year Built"] <= year[1])
]


# ==========================================================
# KPIs
# ==========================================================

st.header("📊 Indicadores Principales")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Precio Promedio",
        f"${df_filtered['SalePrice'].mean():,.0f}"
    )

with col2:
    st.metric(
        "🏠 Viviendas",
        len(df_filtered)
    )

with col3:
    st.metric(
        "📍 Vecindarios",
        df_filtered["Neighborhood"].nunique()
    )

with col4:
    st.metric(
        "🤖 Mejor Modelo",
        "Random Forest"
    )

st.divider()

st.info("✅ Dashboard listo para agregar visualizaciones.")