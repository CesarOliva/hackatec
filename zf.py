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