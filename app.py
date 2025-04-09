import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Producción", layout="wide")
st.title("📊 Dashboard de Producción de Cilindros Hidráulicos")

# Cargar archivo
@st.cache_data
def cargar_datos():
    return pd.read_excel("FORMATO TIEMPOS.xlsx")

df = cargar_datos()

# Filtros
empleados = df["Empleado"].unique()
items = df["Item"].unique()

col1, col2 = st.columns(2)

with col1:
    empleado = st.selectbox("Seleccionar empleado", empleados)

with col2:
    item = st.selectbox("Seleccionar ítem", items)

# Gráfico: Tiempo por OP del empleado
df_emp = df[df["Empleado"] == empleado]
fig1 = px.bar(df_emp, x="OP", y="Tiempo", color="Item",
              title=f"Tiempo por OP - {empleado}", labels={"Tiempo de mecanizado (en minutos)": "Tiempo (min)"})
st.plotly_chart(fig1, use_container_width=True)

# Gráfico: Tiempo por empleado del ítem
df_item = df[df["Item"] == item]
fig2 = px.bar(df_item, x="Empleado", y="Tiempo", color="OP",
              title=f"Tiempo por Empleado - Ítem: {item}", labels={"Tiempo de mecanizado (en minutos)": "Tiempo (min)"})
st.plotly_chart(fig2, use_container_width=True)

# Tabla
st.subheader("📋 Datos completos")
st.dataframe(df)
