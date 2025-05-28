#IMPORTAR LIBRERIAS
import pandas as pd
from collections import defaultdict

excel = 'BDD.xlsx' # ARCHIVO QUE SUBA LA PERSONA

database = pd.read_excel(excel) # LEE EL EXCEL

def crear_arbol_jerarquico(df):
    arbol = defaultdict(lambda: defaultdict(dict))
    
    for _, fila in df.iterrows():
        niveles = []
        for valor in fila:
            if pd.notna(valor) and valor != '':
                niveles.append(valor)
        
        # Construir el árbol nivel por nivel
        nivel_actual = arbol
        for nivel in niveles:
            if nivel not in nivel_actual:
                nivel_actual[nivel] = defaultdict(dict)
            nivel_actual = nivel_actual[nivel]
    
    return arbol

def navegar_arbol(arbol, nivel_actual=None):
    if nivel_actual is None:
        nivel_actual = arbol
    
    opciones = list(nivel_actual.keys())
    
    if not opciones:
        print("No hay más niveles disponibles.")
        return
    
    print("\nOpciones disponibles:")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    
    print("0. Volver al nivel anterior")
    print("q. Salir")
    
    seleccion = input("\nSelecciona una opción: ")
    
    if seleccion == 'q':
        return
    elif seleccion == '0':
        return  # Volverá al nivel anterior por recursión
    elif seleccion.isdigit() and 1 <= int(seleccion) <= len(opciones):
        opcion_seleccionada = opciones[int(seleccion)-1]
        navegar_arbol(arbol, nivel_actual[opcion_seleccionada])
    else:
        print("Opción no válida. Intenta de nuevo.")
        navegar_arbol(arbol, nivel_actual)

arbol = crear_arbol_jerarquico(database)

# Iniciar la navegación
print("Navegación jerárquica - Comienza desde el primer nivel:")
navegar_arbol(arbol)