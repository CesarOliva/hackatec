import tkinter as tk
import pandas as pd
from tkinter import filedialog
import pandas as pd
from collections import defaultdict

root = tk.Tk()

width = 1000
height = 600
x_window = root.winfo_screenwidth()//2 - (width//2)
y_window = root.winfo_screenheight()//2 - (height//2)
root.geometry(f"{width}x{height}+{x_window}+{y_window}")
root.resizable(0,0)
root.configure(bg="#85C1E9")

frame = tk.Frame(root, width=300,height=600,bg="white")
frame.place(x=0,y=0)

tk.Label(root, text = "Emisiones de CO2", font=("Verdana",23), fg = "black", bg = "white", justify="center").place(x=500, y=20)

def abrir_Archivo():
    global excel, database, arbol
    excel = filedialog.askopenfilename(filetypes=(("Archivos de Excel", "*.xlsx"),))
    if(excel):
        database = pd.read_excel(excel) #leer el excel
        arbol = createTree(database)
        navegar_arbol(arbol)

def actualizar_entry(entry_widget):
    archivo = abrir_Archivo()
    if archivo:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0,archivo)

tk.Button(root, text="Cargar archivo .xlsx", font=("Verdana",12), bg="#0057B7", fg = "white", justify="center", command=abrir_Archivo).place(x=560,y=100)

logo = tk.PhotoImage(file="imagenes/logo_ZF.png")
label = tk.Label(image=logo)
label.place(x=50,y=50)

#Crea el elemento del arbol
def createTree(dataFrame):
    arbol = defaultdict(lambda: defaultdict(dict)) # Diccionario. no existe la clave la crea
    
    for _, fila in dataFrame.iterrows():
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

root.mainloop()