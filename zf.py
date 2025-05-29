import customtkinter as CTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Configuración inicial de la ventana
app = CTk.CTk()
app.title("Gráfico de Pastel - Emisiones de CO2")
app.geometry("800x600")

# Datos de ejemplo (emisiones de CO2 por sector)
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
frame_grafico = CTk.CTkFrame(master=app)
frame_grafico.pack(pady=20, padx=20, fill="both", expand=True)

# Convertir la figura de Matplotlib a un widget de Tkinter
canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

# Botón de ejemplo (opcional)
boton = CTk.CTkButton(
    master=app,
    text="Actualizar Gráfico",
    command=lambda: print("Gráfico actualizado"),
)
boton.pack(pady=10)

app.mainloop()