import customtkinter as CTk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from PIL import Image

app = CTk.CTk()
app.geometry("1000x600")
app.iconbitmap('imagenes/zf.png')

CTk.CTkFrame(master=app, fg_color="#0057B7", width=300, height=600).place(relx=0, rely=0)

def selectArchive():
    excel = filedialog.askopenfilename(filetypes=(("Archivos de Excel", "*.xlsx"),))
    if(excel):
        mostrarElementos()

label = CTk.CTkButton(master=app, text = "CarbonTracker", font=("Verdana",26), hover=False, fg_color="transparent", text_color="black")
label.place(x=545, y=20)

button = CTk.CTkButton(master=app, text="Importar archivo .xlsx", fg_color="#00abe7", font=('Verdana', 16) ,command=selectArchive)
button.place(x=550, y=70)

logo = CTk.CTkImage(light_image=Image.open('imagenes/zf.png'), size=(200,200))
labelImg = CTk.CTkLabel(app, text="", image=logo, fg_color="#0057B7").place(x=50, y=30)

def mostrarElementos():
    sectores = ["Transporte", "Industria", "Energía", "Agricultura", "Residencial"]
    emisiones = [25, 30, 20, 15, 10]
    colores = ["#FF9999", "#66B3FF", "#99FF99", "#FFCC99", "#c2c2f0"]

    # Crear la figura de Matplotlib
    fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(aspect="equal"))
    ax.pie(
        emisiones,
        labels=sectores,
        colors=colores,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True,
        explode=(0.1, 0, 0, 0, 0),  # Destacar el primer sector
    )
    ax.set_title("Distribución de Emisiones de CO2 por Sector")

    # Integrar el gráfico en customtkinter
    frame_grafico = CTk.CTkFrame(master=app, fg_color='transparent', width=200, height=200).place(x=500,y=200)

    # Convertir la figura de Matplotlib a un widget de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().place(x=0, y=0, relwidth=1, relheight=1)  # Ocupa todo el frame

app.mainloop()