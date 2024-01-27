import pandas as pd
from io import BytesIO
import streamlit as st

def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.close()
    
    return output

def get_plantilla(propia=False):
    # Add the standard units to the plantilla
    if propia:
        d = {
        'SKU': ["ALB-20", "ALB-30", "ALB-40", "ALF-20", "ALF-30", "ALF-40", "ALJ-20", "ALJ-30", "ALJ-40", "ALJ-50", 
                "BER-10", "BER-20", "BER-30", "BER-40", "ESC-00", "MEJ-00", "NAV-00", "BOG-11", "BOG-12", "BOG-21", 
                "BOG-22", "BUE-11", "BUE-12", "BUE-21", "BUE-22", "BUE-31", "BUE-32", "CAM-12", "CAM-22", "CAM-32", 
                "CAR-02", "CEA-11", "CEA-12", "CEA-21", "CEA-22", "CEA-31", "CEA-32", "CEO-11", "CEO-12", "CEO-21", 
                "CEO-22", "CEO-31", "CEO-32", "CIG-11", "CIG-12", "CIG-21", "CIG-22", "CIG-31", "CIG-32", "LAA-31", 
                "LAA-32", "LAO-00", "NEC-11", "NEC-12", "NEC-21", "NEC-22", "NEC-31", "NEC-32", "OSR-00", "PAP-02", 
                "PER-11", "PER-21", "PER-31", "VIA-00", "VIE-20", "VIE-30", "VOL-00", "ZAM-00"],
        'Nombre de Producto': ["ALMEJA BABOSA - mediano", "ALMEJA BABOSA - grande", "ALMEJA BABOSA - extra", "ALMEJA FINA - mediano", "ALMEJA FINA - grande", "ALMEJA FINA - extra", "ALMEJA JAPÓNICA - mediano", 
                            "ALMEJA JAPÓNICA - grande", "ALMEJA JAPÓNICA - extra", "ALMEJA JAPÓNICA - especial", "BERBERECHO GALLEGO - pequeño", "BERBERECHO GALLEGO - mediano", "BERBERECHO GALLEGO - grande", 
                            "BERBERECHO GALLEGO - extra", "ESCUPIÑA - ALMEJÓN BOLO -", "MEJILLÓN", "NAVAJAS GALLEGAS", "BOGAVANTE AZUL GALLEGO - vivo, pequeño", "BOGAVANTE AZUL GALLEGO - cocido, pequeño", 
                            "BOGAVANTE AZUL GALLEGO - vivo, mediano", "BOGAVANTE AZUL GALLEGO - cocido, mediano", "BUEY DE MAR - pequeño, vivo", "BUEY DE MAR - pequeño, cocido", "BUEY DE MAR - mediano, vivo", 
                            "BUEY DE MAR - mediano, cocido", "BUEY DE MAR - grande, vivo", "BUEY DE MAR - grande, cocido", "CAMARÓN (COCIDO) - pequeño", "CAMARÓN (COCIDO) - mediano", "CAMARÓN (COCIDO) - grande", 
                            "Carabinero de Huelva", "CENTOLLA DE O GROVE (HEMBRA) - vivo, pequeño", "CENTOLLA DE O GROVE (HEMBRA) - cocido, pequeño", "CENTOLLA DE O GROVE (HEMBRA) - vivo, mediano", 
                            "CENTOLLA DE O GROVE (HEMBRA) - cocido, mediano", "CENTOLLA DE O GROVE (HEMBRA) - vivo, grande", "CENTOLLA DE O GROVE (HEMBRA) - cocido, grande", "CENTOLLO DE O GROVE - pequeño, vivo", 
                            "CENTOLLO DE O GROVE - pequeño, cocido", "CENTOLLO DE O GROVE - mediano, vivo", "CENTOLLO DE O GROVE - mediano, cocido", "CENTOLLO DE O GROVE - grande, vivo", "CENTOLLO DE O GROVE - grande, cocido", 
                            "CIGALA - pequeño, vivo", "CIGALA - pequeño, cocido", "CIGALA - mediano, vivo", "CIGALA - mediano, cocido", "CIGALA - grande, vivo", "CIGALA - grande, cocido", 
                            "LANGOSTA ROJA - GALLEGA - - cocido, Pieza 1-1,5 kg", "LANGOSTA ROJA - GALLEGA - - vivo, Pieza 1-1,5 kg",  "LANGOSTINO CONGELADO COCIDO", "NÉCORA GALLEGA DE O GROVE - pequeño, vivo", 
                            "NÉCORA GALLEGA DE O GROVE - pequeño, cocido", "NÉCORA GALLEGA DE O GROVE - mediano, vivo", "NÉCORA GALLEGA DE O GROVE - mediano, cocido", "NÉCORA GALLEGA DE O GROVE - grande, vivo", 
                            "NÉCORA GALLEGA DE O GROVE - grande, cocido", "OSTRA RIZADA GALLEGA", "PATA DE PULPO COCIDO-500 GR", "PERCEBE GALLEGO - pequeño", "PERCEBE GALLEGO - mediano", "PERCEBE GALLEGO - grande", 
                            "ALBARIÑO DE LAS RÍAS BAIXAS", "VIEIRA GALLEGA - mediano", "VIEIRA GALLEGA - grande", "VOLANDEIRA GALLEGA FRESCA" , "ZAMBURIÑA"],
        'Precios': ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-"]
        }
    else:
        d = {
        'SKU': ["ALB-20", "ALB-30", "ALB-40", "ALF-20", "ALF-30", "ALF-40", "ALJ-20", "ALJ-30", "ALJ-40", "ALJ-50", 
                "BER-10", "BER-20", "BER-30", "BER-40", "ESC-00", "MEJ-00", "NAV-00", "BOG-11", "BOG-12", "BOG-21", 
                "BOG-22", "BUE-11", "BUE-12", "BUE-21", "BUE-22", "BUE-31", "BUE-32", "CAM-12", "CAM-22", "CAM-32", 
                "CAR-02", "CEA-11", "CEA-12", "CEA-21", "CEA-22", "CEA-31", "CEA-32", "CEO-11", "CEO-12", "CEO-21", 
                "CEO-22", "CEO-31", "CEO-32", "CIG-11", "CIG-12", "CIG-21", "CIG-22", "CIG-31", "CIG-32", "LAA-31", 
                "LAA-32", "LAO-00", "NEC-11", "NEC-12", "NEC-21", "NEC-22", "NEC-31", "NEC-32", "OSR-00", "PAP-02", 
                "PER-11", "PER-21", "PER-31", "VIA-00", "VIE-20", "VIE-30", "VOL-00", "ZAM-00"],
        'Nombre de Producto': ["ALMEJA BABOSA - mediano", "ALMEJA BABOSA - grande", "ALMEJA BABOSA - extra", "ALMEJA FINA - mediano", "ALMEJA FINA - grande", "ALMEJA FINA - extra", "ALMEJA JAPÓNICA - mediano", 
                            "ALMEJA JAPÓNICA - grande", "ALMEJA JAPÓNICA - extra", "ALMEJA JAPÓNICA - especial", "BERBERECHO GALLEGO - pequeño", "BERBERECHO GALLEGO - mediano", "BERBERECHO GALLEGO - grande", 
                            "BERBERECHO GALLEGO - extra", "ESCUPIÑA - ALMEJÓN BOLO -", "MEJILLÓN", "NAVAJAS GALLEGAS", "BOGAVANTE AZUL GALLEGO - vivo, pequeño", "BOGAVANTE AZUL GALLEGO - cocido, pequeño", 
                            "BOGAVANTE AZUL GALLEGO - vivo, mediano", "BOGAVANTE AZUL GALLEGO - cocido, mediano", "BUEY DE MAR - pequeño, vivo", "BUEY DE MAR - pequeño, cocido", "BUEY DE MAR - mediano, vivo", 
                            "BUEY DE MAR - mediano, cocido", "BUEY DE MAR - grande, vivo", "BUEY DE MAR - grande, cocido", "CAMARÓN (COCIDO) - pequeño", "CAMARÓN (COCIDO) - mediano", "CAMARÓN (COCIDO) - grande", 
                            "Carabinero de Huelva", "CENTOLLA DE O GROVE (HEMBRA) - vivo, pequeño", "CENTOLLA DE O GROVE (HEMBRA) - cocido, pequeño", "CENTOLLA DE O GROVE (HEMBRA) - vivo, mediano", 
                            "CENTOLLA DE O GROVE (HEMBRA) - cocido, mediano", "CENTOLLA DE O GROVE (HEMBRA) - vivo, grande", "CENTOLLA DE O GROVE (HEMBRA) - cocido, grande", "CENTOLLO DE O GROVE - pequeño, vivo", 
                            "CENTOLLO DE O GROVE - pequeño, cocido", "CENTOLLO DE O GROVE - mediano, vivo", "CENTOLLO DE O GROVE - mediano, cocido", "CENTOLLO DE O GROVE - grande, vivo", "CENTOLLO DE O GROVE - grande, cocido", 
                            "CIGALA - pequeño, vivo", "CIGALA - pequeño, cocido", "CIGALA - mediano, vivo", "CIGALA - mediano, cocido", "CIGALA - grande, vivo", "CIGALA - grande, cocido", 
                            "LANGOSTA ROJA - GALLEGA - - cocido, Pieza 1-1,5 kg", "LANGOSTA ROJA - GALLEGA - - vivo, Pieza 1-1,5 kg",  "LANGOSTINO CONGELADO COCIDO", "NÉCORA GALLEGA DE O GROVE - pequeño, vivo", 
                            "NÉCORA GALLEGA DE O GROVE - pequeño, cocido", "NÉCORA GALLEGA DE O GROVE - mediano, vivo", "NÉCORA GALLEGA DE O GROVE - mediano, cocido", "NÉCORA GALLEGA DE O GROVE - grande, vivo", 
                            "NÉCORA GALLEGA DE O GROVE - grande, cocido", "OSTRA RIZADA GALLEGA", "PATA DE PULPO COCIDO-500 GR", "PERCEBE GALLEGO - pequeño", "PERCEBE GALLEGO - mediano", "PERCEBE GALLEGO - grande", 
                            "ALBARIÑO DE LAS RÍAS BAIXAS", "VIEIRA GALLEGA - mediano", "VIEIRA GALLEGA - grande", "VOLANDEIRA GALLEGA FRESCA" , "ZAMBURIÑA"],
        'Competidor 1': ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-"],
        'Competidor 2': ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
                        "-", "-", "-", "-", "-", "-", "-", "-"],
        }
    df = to_excel(pd.DataFrame(data=d))
    return df

def clean_list(l):
    l.remove("SKU")
    l.remove("Nombre de Producto")
    return l