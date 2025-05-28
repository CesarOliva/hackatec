#importar librerias
from openpyxl import load_workbook

#abre el archivo
excel = load_workbook('prueba.xlsx')
worksheet = excel.active

data = []

def addToData(column):
    global celdaInicio, celdaFinal
    for cell in column:
        if(cell.value != None):
            if(cell.value not in data):
                data.append(cell.value)

column = worksheet['E']
addToData(column)
for cell in data:
    print(f'{cell}')