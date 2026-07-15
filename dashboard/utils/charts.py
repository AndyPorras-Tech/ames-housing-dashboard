import plotly.express as px


def create_histogram(df):
    """
    Histograma del precio de venta.
    """

    fig = px.histogram(
        df,
        x="SalePrice",
        nbins=40,
        title="Distribución del Precio de Venta",
        color_discrete_sequence=["#2563EB"]
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        xaxis_title="Precio",
        yaxis_title="Cantidad de viviendas",
        height=500
    )

    return fig