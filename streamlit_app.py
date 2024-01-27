import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from src.utils import get_plantilla, to_excel

st.set_page_config(
    page_title="App Comparadora de Precios",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


plantilla = get_plantilla()

with st.sidebar:
    st.download_button("Descarga plantilla", plantilla,  "plantilla_competidores.xlsx", help = "Descarga la plantilla para subir tus precios")
    competencia_raw = st.file_uploader("Precios Competencia", type="csv")

st.title("Price Comparator")
#apply wide mode, make one round of prices to generate ideas of the app, make the download button work and compare.