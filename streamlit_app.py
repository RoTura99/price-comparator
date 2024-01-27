import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from src.utils import get_plantilla, clean_list

st.set_page_config(
    page_title="App Comparadora de Precios",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

plantilla_competidores = get_plantilla()
plantilla_propia = get_plantilla(True)

with st.sidebar:
    st.download_button("Plantilla competencia", plantilla_competidores,  "plantilla_competidores.xlsx", help = "Descarga la plantilla para subir los precios de la competencia")
    competencia_raw = st.file_uploader("Precios Competencia", type="csv")
    competidores = clean_list(competencia_raw.columns)
    st.download_button("Plantilla propia", plantilla_propia,  "plantilla_propia.xlsx", help = "Descarga la plantilla para subir tus precios")
    propios_raw = st.file_uploader("Precios Propios", type="csv")
    main_competidor = st.multiselect("Selecciona el competidor principal", competidores)

st.title("Price Comparator")
#make one round of prices to generate ideas of the app, make the download button work and compare.
main_price = 1
average_price = 1
median_price = 1
