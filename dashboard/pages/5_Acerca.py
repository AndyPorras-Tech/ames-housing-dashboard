# ==========================================================
# ACERCA DEL PROYECTO
# Proyecto Final - Analítica de Datos
# ==========================================================

import streamlit as st


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="Acerca del Proyecto",
    page_icon="📄",
    layout="wide"
)


# ==========================================================
# TÍTULO
# ==========================================================

st.title("📄 Acerca del Proyecto")

st.markdown("""
Este Dashboard fue desarrollado como proyecto final de la materia
**Analítica de Datos**, utilizando el conjunto de datos **Ames Housing**.

La aplicación integra técnicas de análisis exploratorio de datos,
visualización de información y Machine Learning para analizar y estimar
el precio de venta de viviendas.
""")

st.divider()


# ==========================================================
# OBJETIVOS
# ==========================================================

st.header("🎯 Objetivos")

st.markdown("""
### Objetivo General

Desarrollar un Dashboard interactivo que permita analizar las
características del mercado inmobiliario y mostrar los resultados
obtenidos mediante un modelo de Machine Learning.

### Objetivos Específicos

- Explorar el comportamiento del conjunto de datos.

- Identificar relaciones entre las variables.

- Visualizar indicadores relevantes.

- Presentar el desempeño del modelo predictivo.

- Simular la predicción del precio de una vivienda.
""")

st.divider()


# ==========================================================
# TECNOLOGÍAS
# ==========================================================

st.header("🛠️ Tecnologías Utilizadas")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### Lenguajes

- Python 3

### Librerías

- Pandas
- NumPy
- Streamlit
""")

with col2:

    st.markdown("""
### Machine Learning

- Scikit-learn

### Visualización

- Plotly
- Streamlit
""")

st.divider()


# ==========================================================
# FLUJO DEL PROYECTO
# ==========================================================

st.header("📊 Flujo de Trabajo")

st.markdown("""
1. Obtención del conjunto de datos.

2. Limpieza y preparación de la información.

3. Ingeniería de características.

4. Análisis Exploratorio de Datos (EDA).

5. Entrenamiento del modelo de Machine Learning.

6. Evaluación del modelo.

7. Desarrollo del Dashboard interactivo.
""")

st.divider()


# ==========================================================
# DATASET
# ==========================================================

st.header("🏠 Dataset Utilizado")

st.info("""
**Ames Housing Dataset**

Este conjunto de datos contiene información detallada de viviendas
ubicadas en Ames, Iowa (Estados Unidos).

Incluye variables relacionadas con:

- Área construida.
- Calidad de construcción.
- Número de habitaciones.
- Garaje.
- Año de construcción.
- Vecindario.
- Precio de venta.

Es uno de los datasets más utilizados para problemas de regresión y
predicción de precios inmobiliarios.
""")

st.divider()


# ==========================================================
# AUTOR
# ==========================================================

st.header("👨‍💻 Autor")

st.markdown("""
**Proyecto desarrollado por:**

Andy Porras

Materia:

**Analítica de Datos**

Universidad:

*UNIVER*

Periodo:

*5*
""")

st.divider()


# ==========================================================
# AGRADECIMIENTOS
# ==========================================================

st.header("🙏 Agradecimientos")

st.success("""
Se agradece al docente de la asignatura por la orientación durante el
desarrollo del proyecto, así como a la comunidad de software libre por
las herramientas utilizadas para la implementación del Dashboard.
""")

st.divider()


# ==========================================================
# CIERRE
# ==========================================================

st.markdown(
    """
<div style='text-align:center;'>

### 🏠 Ames Housing Dashboard

Proyecto Final de Analítica de Datos

Desarrollado con ❤️ utilizando Python y Streamlit.

</div>
""",
unsafe_allow_html=True
)