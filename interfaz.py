import customtkinter as CTk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
import matplotlib.backends.backend_pdf as pdf
from fpdf import FPDF
import PyPDF2
import os

app = CTk.CTk(fg_color='white')
app.geometry("1000x600")
app.iconbitmap('imagenes/zf.png')

CTk.CTkFrame(master=app, fg_color="#0057B7", width=300, height=600).place(relx=0, rely=0)

def selectArchive():
    excel = filedialog.askopenfilename(filetypes=(("Archivos de Excel", "*.xlsx"),))
    if(excel):
        mostrarElementos()

label = CTk.CTkButton(master=app, text="CarbonTracker", font=("Verdana", 26), hover=False, fg_color="transparent", text_color="black")
label.place(x=545, y=20)

button = CTk.CTkButton(master=app, text="Importar archivo .xlsx", fg_color="#00abe7", font=('Verdana',16), width=120, height=30, command=selectArchive)
button.place(x=550, y=70)

logo = CTk.CTkImage(light_image=Image.open('imagenes/zf.png'), size=(200,200))
labelImg = CTk.CTkLabel(master=app, text="", image=logo, fg_color="#0057B7").place(x=50, y=200)

def mostrarElementos():
    CTk.CTkButton(master=app, text="Ingrese el nivel:", font=("Verdana", 18), hover=False, fg_color="transparent", text_color="black").place(x=350, y=140)
    CTk.CTkEntry(master=app).place(x=515, y=140)
    CTk.CTkButton(master=app, text="Buscar", font=("Verdana", 18), fg_color="#1B76D7", text_color="white", width=80, height=30).place(x=670, y=140)
    GenerarPieChart()
    CTk.CTkButton(master=app, text="Abrir PDF", font=("Verdana", 18), fg_color="red", text_color="white", height=30, command=abrirPDF).place(x=580, y=510)

def GenerarPieChart():
    global output_file
    colores = ["#FF9999", "#66B3FF", "#99FF99", "#FFCC99", "#c2c2f0"]
    sectores = ["Transporte", "Industria", "Energía", "Agricultura", "Residencial"]
    emisiones = [25, 30, 20, 15, 10]
    
    datos_ordenados = sorted(zip(emisiones, sectores), reverse=False)
    emisiones_ordenadas = [dato[0] for dato in datos_ordenados]
    sectores_ordenados = [dato[1] for dato in datos_ordenados]

    fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(aspect="equal"))
    ax.pie( emisiones_ordenadas,labels=sectores_ordenados,colors=colores, autopct='%1.1f%%',startangle=90,shadow=True,explode=(0, 0, 0, 0, 0.1),)
    ax.set_title("Distribución de elementos del nivel: ")

    frame_grafico = CTk.CTkFrame(master=app, fg_color="transparent", width=350, height=350)
    frame_grafico.place(x=450, y=180)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().place(x=0, y=0, relwidth=1, relheight=1)

    # Guardar gráfico temporalmente
    temp_image = "temp_chart.png"
    plt.savefig(temp_image, dpi=300, bbox_inches='tight')
    plt.close()

    # Configurar PDF
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)

    # Título principal
    pdf.cell(0, 20, "Informe de Emisiones de CO2", ln=True, align='C')

    # Insertar gráfico centrado
    pdf.image(temp_image, x=30, y=40, w=150)  # Ajusta posición y tamaño

    # Leyenda (explicación de colores)
    pdf.set_font("Arial", 'B', 12)
    pdf.ln(120)  # Espacio después del gráfico
    pdf.cell(0, 10, "Leyenda:", ln=True)

    pdf.set_font("Arial", size=10)
    for sector, color in zip(sectores, colores):
        pdf.set_fill_color(*[int(color[i:i+2], 16) for i in (1, 3, 5)])  # HEX a RGB
        pdf.cell(10, 6, '', fill=True, border=0)  # Cuadro de color
        pdf.cell(0, 6, f" {sector}: {emisiones[sectores.index(sector)]}%", ln=True)

    # Guardar PDF
    output_file = "Informe_Emisiones_CO2.pdf"
    pdf.output(output_file)
    os.remove(temp_image)
    print(f"✅ PDF generado: {output_file}")

def abrirPDF():
    try:
        with open(output_file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
    except FileNotFoundError:
        print(f"El archivo '{output_file}' no se encontró.")
        exit()
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo: {e}")
        exit()

app.mainloop()