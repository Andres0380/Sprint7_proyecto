
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#Datos
df = pd.read_csv('vehicles_us.csv')

st.header("Exploración rápida")

hist_button = st.button("Histograma de odómetro")
if hist_button:
    st.write("Histograma para el odómetro")
    fig = go.Figure(data=[go.Histogram(x=df["odometer"])])
    fig.update_layout(title_text="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button("Dispersión Precio vs Odómetro")
if scatter_button:
    st.write("Diagrama de dispersión Precio vs Odómetro")
    fig = go.Figure(data=[go.Scatter(x=df["odometer"], y=df["price"], mode="markers")])
    fig.update_layout(title_text="Precio vs Odómetro", xaxis_title="Odómetro", yaxis_title="Precio")
    st.plotly_chart(fig, use_container_width=True)

st.title("Análisis de Vehículos")

st.sidebar.header("Opciones de Visualización")

if st.sidebar.button("Histograma de Precio"):
    fig = px.histogram(df, x="price", nbins=50, title="Distribución de Precios de Vehículos")
    st.plotly_chart(fig)

if st.sidebar.button("Dispersión Precio vs Año"):
    fig = px.scatter(df, x="model_year", y="price", title="Precio vs Año del Vehículo", opacity=0.5)
    st.plotly_chart(fig)

st.sidebar.write("Selecciona una opción para visualizar los datos")
