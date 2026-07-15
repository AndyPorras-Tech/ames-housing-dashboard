# ==========================================================
# DASHBOARD PRINCIPAL
# Proyecto Final - Analítica de Datos
# ==========================================================

import streamlit as st

from utils.loader import load_data
from utils.charts import create_histogram


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

fig = create_histogram(df_filtered)

st.plotly_chart(fig)






# ==========================================================
# AGREGAR DESDE AQUÍ
# ==========================================================

st.divider()

# ==========================================================
# PRECIO PROMEDIO POR VECINDARIO
# ==========================================================

st.subheader("🏘️ Precio promedio por vecindario")

avg_price = (
    df_filtered
    .groupby("Neighborhood")["SalePrice"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(avg_price)

st.caption(
    "Se observa el precio promedio de venta para cada vecindario "
    "después de aplicar los filtros seleccionados."
)

st.divider()


# ==========================================================
# ÁREA HABITABLE VS PRECIO
# ==========================================================

st.subheader("📈 Área habitable vs Precio de venta")

st.scatter_chart(
    data=df_filtered,
    x="Gr Liv Area",
    y="SalePrice"
)

st.caption(
    "Existe una tendencia positiva: conforme aumenta el área habitable, "
    "el precio de venta también suele incrementarse."
)

st.divider()


# ==========================================================
# RESUMEN
# ==========================================================

st.subheader("📝 Resumen")

st.success(
    f"""
Se analizaron **{len(df_filtered):,} viviendas** pertenecientes a
**{df_filtered['Neighborhood'].nunique()} vecindarios**.

El precio promedio de las viviendas seleccionadas es de
**${df_filtered['SalePrice'].mean():,.0f}**.

Las visualizaciones permiten identificar rápidamente la distribución
de precios, comparar vecindarios y observar la relación entre el
tamaño de la vivienda y su precio de venta.
"""
)