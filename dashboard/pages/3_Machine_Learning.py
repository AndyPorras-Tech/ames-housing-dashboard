# ==========================================================
# MACHINE LEARNING
# Proyecto Final - Analítica de Datos
# ==========================================================

import streamlit as st

from utils.loader import load_data


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="Machine Learning",
    page_icon="🤖",
    layout="wide"
)


# ==========================================================
# CARGA DEL DATASET
# ==========================================================

df = load_data()


# ==========================================================
# TÍTULO
# ==========================================================

st.title("🤖 Modelo de Machine Learning")

st.markdown("""
En esta sección se presentan los resultados obtenidos durante el
entrenamiento y evaluación del modelo predictivo utilizado para estimar
el precio de venta de las viviendas del conjunto de datos Ames Housing.
""")

st.divider()


# ==========================================================
# MODELO UTILIZADO
# ==========================================================

st.subheader("🏆 Modelo Seleccionado")

st.success(
    """
Después de evaluar diferentes alternativas, el modelo seleccionado fue
**Random Forest Regressor**, debido a su capacidad para modelar relaciones
no lineales entre las variables y ofrecer un excelente desempeño en la
predicción del precio de las viviendas.
"""
)

st.divider()


# ==========================================================
# MÉTRICAS DEL MODELO
# ==========================================================

st.subheader("📊 Métricas de Evaluación")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="R²",
        value="0.895"
    )

with col2:
    st.metric(
        label="MAE",
        value="$16,252"
    )

with col3:
    st.metric(
        label="RMSE",
        value="$29,019"
    )

st.info(
    """
Estas métricas indican que el modelo logra explicar aproximadamente el
89.5 % de la variabilidad del precio de venta, obteniendo errores
promedio relativamente bajos para un problema de regresión inmobiliaria.
"""
)

st.divider()


# ==========================================================
# RESUMEN DEL MODELO
# ==========================================================

st.subheader("📌 Resumen")

st.markdown("""
- **Algoritmo:** Random Forest Regressor

- **Tipo de problema:** Regresión

- **Variable objetivo:** SalePrice

- **Dataset utilizado:** Ames Housing

- **Objetivo:** Predecir el precio de venta de una vivienda a partir de
sus características físicas y de ubicación.
""")