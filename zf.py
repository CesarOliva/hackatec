#importar librerias
from openpyxl import load_workbook

#abre el archivo
excel = load_workbook('prueba.xlsx')
worksheet = excel.active

data = []

def addToData(column):
    global celdaInicio, celdaFin
    for cell in column:
        if(cell.value != None):
            celdaFin = cell.coordinate
            if(cell.value not in data):
                data.append(cell.value)
                celdaInicio = cell.coordinate

column = worksheet['E']
addToData(column)

for cell in data:
    print(f'{cell}')

print("celda inicio "+celdaInicio+", celda fin: "+celdaFin)

import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Análisis de CO2", layout="wide")
st.title("Análisis Jerárquico de Emisiones de CO₂")

uploaded_file = st.file_uploader("Sube tu archivo .xlsx", type=["xlsx"])

if uploaded_file:
    try:
        excel_file = pd.ExcelFile(uploaded_file)
        df = pd.read_excel(excel_file, sheet_name='Product example ', skiprows=3)

        df = df.rename(columns={
            'Unnamed: 2': 'Parte',
            'Unnamed: 3': 'Componente',
            'Unnamed: 4': 'Subcomponente',
            'Unnamed: 5': 'Material',
            'Unnamed: 6': 'Submaterial',
            'Flows': 'CO2'
        })

        df = df.fillna(method='ffill')

        df = df[df['CO2'].notna()]

        if st.checkbox("Mostrar datos procesados"):
            st.dataframe(df)

        niveles = ['Submaterial', 'Material', 'Subcomponente', 'Componente', 'Parte']

        nivel = st.selectbox("Selecciona el nivel jerárquico para agrupar y analizar", niveles)

        resultado = df.groupby(nivel)['CO2'].sum().sort_values(ascending=False).reset_index()

        st.subheader(f"Top emisores de CO₂ a nivel de: {nivel}")
        st.dataframe(resultado)

        st.bar_chart(resultado.set_index(nivel))

    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
else:
    st.info("Por favor, sube un archivo .xlsx con la estructura jerárquica esperada.")
