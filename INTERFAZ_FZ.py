import tkinter as tk
import customtkinter as Ctk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
Ctk.set_default_color_theme("blue")

width = 1000
height = 600
x_window = root.winfo_screenwidth()//2 - (width//2)
y_window = root.winfo_screenheight()//2 - (height//2)
root.geometry(f"{width}x{height}+{x_window}+{y_window}")
root.resizable(0,0)
root.configure(bg="#85C1E9")

frame = Ctk.CTkFrame(master=root,bg_color="#FFF").geometry("300x600+0+0")

tk.Label(root, text = "Emisiones de CO2", font=("Verdana",23), fg = "black", bg = "white", justify="center").place(x=500, y=20)

def abrir_Archivo():
    global excel, database, arbol
    excel = filedialog.askopenfilename(filetypes=(("Archivos de Excel", "*.xlsx"),))
    if(excel):
        database = pd.read_excel(excel) #leer el excel

tk.Button(root, text="Cargar archivo .xlsx", font=("Verdana",12), bg="#0057B7", fg = "white", justify="center", command=abrir_Archivo).place(x=560,y=100)

logo = tk.PhotoImage(file="imagenes/zf.png")
label = tk.Label(image=logo)
label.place(x=50,y=50)

root.mainloop()