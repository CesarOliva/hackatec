from fpdf import FPDF
import matplotlib.pyplot as plt
import os
import pandas as pd
import customtkinter as CTk

app = CTk.CTk(fg_color='white')
app.geometry("1000x600")

def generar_pdf():
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