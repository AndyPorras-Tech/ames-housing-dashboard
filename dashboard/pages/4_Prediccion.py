# ==========================================================
# PREDICCIÓN
# Proyecto Final - Analítica de Datos
# ==========================================================

import streamlit as st

from utils.loader import load_data


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="Predicción",
    page_icon="🔮",
    layout="wide"
)


# ==========================================================
# CARGA DEL DATASET
# ==========================================================

df = load_data()


# ==========================================================
# TÍTULO
# ==========================================================

st.title("🔮 Predicción del Precio de una Vivienda")

st.markdown("""
Esta sección permite simular la captura de información de una vivienda
para estimar su precio de venta utilizando el modelo de Machine Learning
desarrollado durante el proyecto.
""")

st.divider()


# ==========================================================
# FORMULARIO
# ==========================================================

st.subheader("🏠 Características de la Vivienda")

col1, col2 = st.columns(2)

with col1:

    gr_liv_area = st.number_input(
        "Área habitable (ft²)",
        min_value=300,
        max_value=6000,
        value=1500
    )

    overall_qual = st.slider(
        "Calidad General",
        1,
        10,
        5
    )

    year_built = st.slider(
        "Año de construcción",
        int(df["Year Built"].min()),
        int(df["Year Built"].max()),
        2000
    )

with col2:

    garage_cars = st.slider(
        "Espacios de garaje",
        0,
        5,
        2
    )

    full_bath = st.slider(
        "Baños completos",
        0,
        5,
        2
    )

    neighborhood = st.selectbox(
        "Vecindario",
        sorted(df["Neighborhood"].unique())
    )


st.divider()


# ==========================================================
# BOTÓN
# ==========================================================

predict = st.button(
    "🔮 Estimar Precio",
    use_container_width=True
)






# ==========================================================
# RESULTADO DE LA PREDICCIÓN
# ==========================================================

if predict:

    st.divider()

    st.subheader("📈 Resultado de la Predicción")

    # ------------------------------------------------------
    # ESTIMACIÓN SIMULADA
    # ------------------------------------------------------

    estimated_price = (
        50000
        + (gr_liv_area * 95)
        + (overall_qual * 22000)
        + (garage_cars * 9000)
        + (full_bath * 7000)
        + ((year_built - 1950) * 350)
    )

    # Evitar valores exagerados
    estimated_price = max(estimated_price, 50000)

    # ------------------------------------------------------
    # MOSTRAR RESULTADO
    # ------------------------------------------------------

    st.metric(
        label="💰 Precio estimado",
        value=f"${estimated_price:,.0f}"
    )

    st.success(
        f"""
El modelo estima que una vivienda con las características seleccionadas
podría tener un precio aproximado de:

# 💲 {estimated_price:,.0f}
"""
    )

    st.info(
        """
Esta predicción es una simulación diseñada para demostrar el
funcionamiento del Dashboard.

En una implementación real, el botón utilizaría el modelo Random Forest
entrenado durante el desarrollo del proyecto para generar la predicción.
"""
    )

    st.divider()

    st.subheader("📋 Características utilizadas")

    col1, col2 = st.columns(2)

    with col1:

        st.write(f"**Área habitable:** {gr_liv_area} ft²")

        st.write(f"**Calidad:** {overall_qual}")

        st.write(f"**Año:** {year_built}")

    with col2:

        st.write(f"**Garajes:** {garage_cars}")

        st.write(f"**Baños:** {full_bath}")

        st.write(f"**Vecindario:** {neighborhood}")








# ==========================================================
# INTERPRETACIÓN DE LA PREDICCIÓN
# ==========================================================

st.divider()

st.subheader("🧠 Interpretación")

st.markdown("""
La estimación presentada representa una simulación del funcionamiento de
un modelo predictivo aplicado al mercado inmobiliario.

El precio estimado depende principalmente de características como:

- Área habitable.
- Calidad general de la construcción.
- Año de construcción.
- Capacidad del garaje.
- Número de baños.
- Ubicación de la vivienda.

Estas variables fueron seleccionadas debido a su influencia sobre el
precio de venta observada durante el análisis exploratorio y el proceso
de entrenamiento del modelo.
""")

st.divider()


# ==========================================================
# RECOMENDACIONES
# ==========================================================

st.subheader("💡 Recomendaciones")

st.info("""
Para obtener predicciones más precisas sería conveniente incorporar
información adicional como:

• Estado de conservación de la vivienda.

• Calidad de acabados interiores.

• Cercanía a escuelas y servicios.

• Tendencias actuales del mercado inmobiliario.

• Indicadores económicos de la zona.
""")

st.divider()


# ==========================================================
# POSIBLES MEJORAS
# ==========================================================

st.subheader("🚀 Mejoras Futuras")

st.markdown("""
En una implementación completa del proyecto podrían incorporarse las
siguientes funcionalidades:

- Conectar el modelo Random Forest entrenado mediante un archivo
  `.joblib`.

- Permitir cargar información desde un archivo CSV.

- Comparar varios modelos de Machine Learning.

- Mostrar el nivel de confianza de la predicción.

- Generar reportes automáticos en formato PDF.
""")

st.divider()


# ==========================================================
# CONCLUSIÓN
# ==========================================================

st.subheader("🎯 Conclusión")

st.success("""
La sección de predicción demuestra cómo un modelo de Machine Learning
puede utilizar las características de una vivienda para estimar su
precio de venta.

Aunque en esta versión se utiliza una simulación para representar el
proceso de inferencia, la estructura de la aplicación está preparada
para integrar un modelo entrenado y realizar predicciones reales en una
implementación futura.
""")