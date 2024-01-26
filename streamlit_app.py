import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from src.utils import get_plantilla, to_excel


plantilla = get_plantilla()

with st.sidebar:
    st.download_button("Descarga plantilla", plantilla,  "plantilla_competidores.xlsx", help = "Descarga la plantilla para subir tus precios")
    competencia_raw = st.file_uploader("Precios Competencia", type="csv")

st.title("Price Comparator")
