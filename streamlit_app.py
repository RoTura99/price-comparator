import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from src.utils import get_plantilla, clean_list, to_excel, color_table, clean_output

st.set_page_config(
    page_title="App Comparadora de Precios",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    plantilla_competidores = get_plantilla()
    plantilla_propia = get_plantilla(True)
    st.download_button("Plantilla competencia", plantilla_competidores,  "plantilla_competidores.xlsx", help = "Descarga la plantilla para subir los precios de la competencia")
    competencia_raw = st.file_uploader("Precios Competencia", type="xlsx")
    if competencia_raw is not None:
        competencia_df = pd.read_excel(competencia_raw)
        competidores = clean_list(competencia_df.columns.tolist())
    else:
        competidores = []
    st.download_button("Plantilla propia", plantilla_propia,  "plantilla_propia.xlsx", help = "Descarga la plantilla para subir tus precios")
    propios_raw = st.file_uploader("Precios Propios", type="xlsx")
    if propios_raw is not None:
        propios_df = pd.read_excel(propios_raw)
    main_competidor = st.selectbox("Selecciona el competidor principal", competidores)

# Main App
st.title("Price Comparator")
if competencia_raw is None or propios_raw is None:
    st.write("Sube los archivos para poder comparar")
else:
    if "precios" not in st.session_state:
        st.session_state.precios = pd.merge(propios_df, competencia_df, how = "left", on=["SKU", "Nombre de Producto"])

    if main_competidor == []:
        st.session_state.precios["Precio Principal"] = 0
    else:
        st.session_state.precios["Precio Principal"] = st.session_state.precios[main_competidor]
    st.session_state.precios["Precio Promedio"] = st.session_state.precios[competidores].mean(axis=1)
    st.session_state.precios["Precio Mediano"] = st.session_state.precios[competidores].median(axis=1)
        
    st.session_state.precios = st.data_editor(st.session_state.precios.style.apply(color_table, axis=None), 
                                              height = 800,
                                              column_order = ["SKU", "Nombre de Producto", "Precio Propio", "Precio Principal", "Precio Promedio", "Precio Mediano"] + competidores, 
                                              disabled = ["Precio Principal", "Precio Promedio", "Precio Mediano"] + competidores)

    st.download_button("Descarga los precios", to_excel(clean_output(st.session_state.precios, competidores)),  "precios_final.xlsx", help = "Descarga la hoja de precios final")