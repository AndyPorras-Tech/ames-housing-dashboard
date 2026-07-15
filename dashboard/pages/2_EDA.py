# ==========================================================
# ANÁLISIS EXPLORATORIO DE DATOS (EDA)
# Proyecto Final - Analítica de Datos
# ==========================================================

import streamlit as st
import pandas as pd

from utils.loader import load_data


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="EDA",
    page_icon="📈",
    layout="wide"
)


# ==========================================================
# CARGA DEL DATASET
# ==========================================================

df = load_data()


# ==========================================================
# TÍTULO
# ==========================================================

st.title("📈 Análisis Exploratorio de Datos")

st.markdown("""
En esta sección se presentan diferentes visualizaciones que permiten
comprender el comportamiento del mercado inmobiliario antes de la
construcción del modelo de Machine Learning.
""")

st.divider()


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🎛️ Filtros del EDA")

st.sidebar.markdown(
    "Filtra la información para analizar diferentes grupos de viviendas."
)


# ==========================================================
# FILTRO DE VECINDARIO
# ==========================================================

neighborhood = st.sidebar.selectbox(
    "Vecindario",
    ["Todos"] + sorted(df["Neighborhood"].unique().tolist())
)


# ==========================================================
# FILTRO DE AÑO
# ==========================================================

year = st.sidebar.slider(
    "Año de construcción",
    int(df["Year Built"].min()),
    int(df["Year Built"].max()),
    (
        int(df["Year Built"].min()),
        int(df["Year Built"].max())
    )
)


# ==========================================================
# FILTRO DE PRECIO
# ==========================================================

price = st.sidebar.slider(
    "Precio de venta",
    int(df["SalePrice"].min()),
    int(df["SalePrice"].max()),
    (
        int(df["SalePrice"].min()),
        int(df["SalePrice"].max())
    )
)


# ==========================================================
# FILTRADO DEL DATASET
# ==========================================================

df_filtered = df.copy()

if neighborhood != "Todos":
    df_filtered = df_filtered[
        df_filtered["Neighborhood"] == neighborhood
    ]

df_filtered = df_filtered[
    (df_filtered["Year Built"] >= year[0]) &
    (df_filtered["Year Built"] <= year[1])
]

df_filtered = df_filtered[
    (df_filtered["SalePrice"] >= price[0]) &
    (df_filtered["SalePrice"] <= price[1])
]


# ==========================================================
# KPIs
# ==========================================================

st.header("📊 Resumen del Dataset")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🏠 Viviendas",
        f"{len(df_filtered):,}"
    )

with col2:
    st.metric(
        "💰 Precio promedio",
        f"${df_filtered['SalePrice'].mean():,.0f}"
    )

with col3:
    st.metric(
        "📍 Vecindarios",
        df_filtered["Neighborhood"].nunique()
    )

with col4:
    st.metric(
        "📅 Año promedio",
        int(df_filtered["Year Built"].mean())
    )


st.divider()


# ==========================================================
# INTRODUCCIÓN AL EDA
# ==========================================================

st.info(
    """
El Análisis Exploratorio de Datos (EDA) permite comprender la
distribución de las variables, detectar valores atípicos,
identificar relaciones entre variables y obtener información útil
antes del entrenamiento del modelo predictivo.
"""
)




# ==========================================================
# DISTRIBUCIÓN DEL PRECIO DE VENTA
# ==========================================================

st.header("📊 Distribución del Precio de Venta")

st.write(
    """
La siguiente gráfica muestra cómo se distribuyen los precios de las
viviendas seleccionadas después de aplicar los filtros.
    """
)

st.bar_chart(
    df_filtered["SalePrice"].value_counts(bins=30).sort_index()
)

st.divider()


# ==========================================================
# ÁREA HABITABLE VS PRECIO
# ==========================================================

st.header("📈 Área Habitable vs Precio")

st.write(
    """
Existe una relación positiva entre el tamaño de la vivienda y su precio
de venta.
    """
)

st.scatter_chart(
    data=df_filtered,
    x="Gr Liv Area",
    y="SalePrice"
)

st.divider()


# ==========================================================
# PRECIO PROMEDIO POR VECINDARIO
# ==========================================================

st.header("🏘️ Precio Promedio por Vecindario")

avg_price = (
    df_filtered
    .groupby("Neighborhood")["SalePrice"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(avg_price)

st.divider()


# ==========================================================
# ANTIGÜEDAD DE LAS VIVIENDAS
# ==========================================================

st.header("🏠 Año de Construcción")

year_count = (
    df_filtered["Year Built"]
    .value_counts()
    .sort_index()
)

st.line_chart(year_count)

st.divider()


# ==========================================================
# GARAGE CARS VS PRECIO
# ==========================================================

st.header("🚗 Capacidad del Garaje vs Precio")

garage_price = (
    df_filtered
    .groupby("Garage Cars")["SalePrice"]
    .mean()
)

st.bar_chart(garage_price)

st.divider()


# ==========================================================
# SUPERFICIE DEL TERRENO
# ==========================================================

st.header("🌳 Distribución del Área del Terreno")

st.area_chart(
    df_filtered["Lot Area"]
)

st.divider()





# ==========================================================
# CONCLUSIONES DEL ANÁLISIS EXPLORATORIO
# ==========================================================

st.header("📝 Conclusiones del Análisis")

st.markdown(
    """
A partir del análisis exploratorio realizado sobre el conjunto de datos
*Ames Housing* se pueden identificar los siguientes hallazgos:
"""
)

st.markdown(
    f"""
- Se analizaron **{len(df_filtered):,} viviendas** después de aplicar los filtros.

- El precio promedio de venta es de
**${df_filtered['SalePrice'].mean():,.0f}**.

- Los datos pertenecen a
**{df_filtered['Neighborhood'].nunique()} vecindarios**.

- Existe una relación positiva entre el área habitable y el precio de venta.

- Algunos vecindarios presentan precios considerablemente superiores al promedio.

- La mayoría de las viviendas fueron construidas después de la década de 1970.

- Estas tendencias justifican el uso de modelos de Machine Learning para estimar el precio de una vivienda.
"""
)

st.divider()


# ==========================================================
# ESTADÍSTICAS DESCRIPTIVAS
# ==========================================================

st.header("📋 Estadísticas Descriptivas")

st.write(
    """
La siguiente tabla resume las principales estadísticas de las variables
numéricas del conjunto de datos filtrado.
"""
)

st.dataframe(
    df_filtered.describe(),
    use_container_width=True
)

st.divider()


# ==========================================================
# VISTA PREVIA DEL DATASET
# ==========================================================

st.header("🗂️ Vista Previa del Dataset")

st.write(
    """
Las primeras filas del conjunto de datos permiten observar la estructura
general de la información utilizada durante el análisis.
"""
)

st.dataframe(
    df_filtered.head(15),
    use_container_width=True
)

st.divider()


# ==========================================================
# CIERRE
# ==========================================================

st.success(
    """
El Análisis Exploratorio de Datos permitió comprender la distribución
de las variables, identificar patrones importantes y conocer la relación
entre las características de las viviendas y su precio de venta.

La información obtenida servirá como base para la construcción y
evaluación de los modelos de Machine Learning presentados en la
siguiente sección del proyecto.
"""
)