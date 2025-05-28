from cProfile import label
from email.mime import image
from os import read
from pydoc import text
import tkinter as tk
import pandas as pd
from tkinter import filedialog
from numpy import imag, tile


def abrir_Archivo(): #Falta que abra unicamente archivos .xlsx
    archivos = filedialog.askopenfilename(initialdir="C:\\Users",
                                          filetypes=(("Archivos de Excel", "*.xlsx"),
                                                     ))
    #file = open(archivos, 'r')

    if archivos:
        try:
            df = pd.read_excel(archivos)
            print(df.head())

        except Exception as e:
            print("Error al abrir archivo Excel: ", e)    


def actualizar_entry(entry_widget):
    archivos = abrir_Archivo()
    if archivos:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0,archivos)



appMenu = tk.Tk()

appMenu.geometry("1000x600")
appMenu.configure(bg = "white")

tk.Label(
    appMenu,
    text = "DETECTOR DE MATERIALES",
    font = ("Verdana",25),
    fg = "blue",
    bg = "white",
    justify="center"
).place(x=390, y=0)

frame = tk.Frame(appMenu, width=250,height=600,bg="gray" )
frame.pack()
frame.place(x=0,y=0)

#CHECAR***********************************************************
#cargar imagen del disco
#logo = tk.PhotoImage(file="imagenes/logo_ZF.png")
#label = tk.Label(image=logo)
#label.place(x=10,y=0)



tk.Button(
    appMenu,
    text="Ingresar Base de Datos",
    font=("Verdana",25),
    bg="red",
    fg = "white",
    justify="center",
    command=abrir_Archivo
).place(x=420,y=200)

tk.Label(
    appMenu,
    text = "Base de Datos Existente:",
    font = ("Arial",10),
    fg = "black",
    bg = "white",
    justify="center"
).place(x=260, y=410)

tk.Entry(
    appMenu,
    text = " ",
    bg= "white",
    justify="center",
).place(x=420,y=410, width=400)


tk.Button(
    appMenu,
    text="Aceptar",
    font=("Verdana",15),
    bg="red",
    fg = "white",
    justify="center"
).place(x=520,y=500)


appMenu.mainloop()