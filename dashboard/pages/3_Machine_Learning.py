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

# ==========================================================
# VARIABLES MÁS RELEVANTES
# ==========================================================

st.divider()

st.subheader("⭐ Variables más relevantes")

importance = {
    "Gr Liv Area": 0.27,
    "Overall Qual": 0.22,
    "Garage Cars": 0.12,
    "Garage Area": 0.10,
    "Total Bsmt SF": 0.09,
    "Year Built": 0.08,
    "1st Flr SF": 0.06,
    "Lot Area": 0.04,
    "Full Bath": 0.02
}

st.bar_chart(importance)

st.caption(
    """
Las variables mostradas representan las características que tuvieron
mayor influencia en la estimación del precio de venta de las viviendas.
"""
)


# ==========================================================
# RELACIÓN ENTRE CALIDAD Y PRECIO
# ==========================================================

st.divider()

st.subheader("🏠 Calidad general vs Precio")

st.scatter_chart(
    data=df,
    x="Overall Qual",
    y="SalePrice"
)

st.caption(
    """
Se observa una relación positiva entre la calidad general de la vivienda
y su precio de venta.
"""
)


# ==========================================================
# ÁREA HABITABLE VS PRECIO
# ==========================================================

st.divider()

st.subheader("📈 Área habitable vs Precio")

st.scatter_chart(
    data=df,
    x="Gr Liv Area",
    y="SalePrice"
)

st.caption(
    """
El área habitable es una de las variables con mayor capacidad para
explicar el comportamiento del precio de venta.
"""
)


# ==========================================================
# DISTRIBUCIÓN DEL PRECIO
# ==========================================================

st.divider()

st.subheader("💰 Distribución del Precio de Venta")

st.bar_chart(
    df["SalePrice"].value_counts(bins=30).sort_index()
)

st.caption(
    """
La mayor parte de las viviendas se concentra en un rango de precios
intermedio, mientras que los inmuebles de mayor valor son menos frecuentes.
"""
)





# ==========================================================
# INTERPRETACIÓN DE RESULTADOS
# ==========================================================

st.divider()

st.subheader("🧠 Interpretación de los Resultados")

st.markdown("""
El modelo **Random Forest Regressor** presentó el mejor desempeño para
estimar el precio de venta de las viviendas del conjunto de datos
*Ames Housing*.

Su capacidad para capturar relaciones no lineales entre las variables
permitió obtener un coeficiente de determinación elevado y errores
de predicción relativamente bajos.
""")

st.info("""
En problemas de valoración inmobiliaria es común que existan relaciones
complejas entre las características de una vivienda y su precio.
Random Forest es capaz de modelar estas relaciones sin requerir
supuestos estrictos sobre la distribución de los datos.
""")

st.divider()


# ==========================================================
# MÉTRICAS OBTENIDAS
# ==========================================================

st.subheader("📋 Resumen de Resultados")

results = {
    "Métrica": [
        "Modelo",
        "R²",
        "MAE",
        "RMSE"
    ],
    "Resultado": [
        "Random Forest Regressor",
        "0.895",
        "$16,252",
        "$29,019"
    ]
}

st.table(results)

st.divider()


# ==========================================================
# VENTAJAS DEL MODELO
# ==========================================================

st.subheader("✅ ¿Por qué se eligió Random Forest?")

st.markdown("""
- Excelente desempeño en problemas de regresión.

- Maneja relaciones no lineales entre variables.

- Es resistente al sobreajuste cuando se configura correctamente.

- Puede identificar la importancia de cada variable.

- Funciona adecuadamente con conjuntos de datos de tamaño medio como
Ames Housing.
""")

st.divider()


# ==========================================================
# LIMITACIONES
# ==========================================================

st.subheader("⚠️ Limitaciones")

st.warning("""
Aunque el modelo obtuvo resultados satisfactorios, existen algunos
aspectos que pueden afectar la precisión de las predicciones:

- Variables externas no incluidas en el dataset.

- Cambios en el mercado inmobiliario con el paso del tiempo.

- Posibles valores atípicos presentes en los datos.

- La precisión depende de la calidad del proceso de limpieza y
preprocesamiento realizado previamente.
""")

st.divider()


# ==========================================================
# CONCLUSIÓN
# ==========================================================

st.subheader("🎯 Conclusión")

st.success("""
El modelo Random Forest Regressor demostró ser una alternativa adecuada
para estimar el precio de venta de viviendas utilizando el conjunto de
datos Ames Housing.

Los resultados obtenidos muestran un alto poder predictivo y permiten
concluir que las variables relacionadas con el tamaño, la calidad de la
construcción y la ubicación tienen una influencia significativa sobre el
valor final de una vivienda.

Esta etapa constituye la base para la siguiente sección del proyecto,
donde el usuario podrá realizar predicciones de forma interactiva.
""")