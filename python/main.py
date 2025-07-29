import tkinter as tk
from PIL import Image, ImageTk

# VENTANA
ventana = tk.Tk()
ventana.title("SMART CLOTHES")
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

# IMÁGENES DE FONDO
imagen_rosita = Image.open("rosita.png").resize((ancho_pantalla, alto_pantalla))
fondo_rosita = ImageTk.PhotoImage(imagen_rosita)

imagen_azul = Image.open("azul.png").resize((ancho_pantalla, alto_pantalla))
fondo_azul = ImageTk.PhotoImage(imagen_azul)

# Label de fondo
fondo_label = tk.Label(ventana, image=fondo_rosita)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# CONTADORES
contador_guardar = 0
contador_sacar = 0
ultimo_estado = None

# TOOLTIP
class Tooltip:
    def __init__(self, widget, texto_func):
        self.widget = widget
        self.texto_func = texto_func
        self.tooltip = None
        widget.bind("<Enter>", self.mostrar_tooltip)
        widget.bind("<Leave>", self.ocultar_tooltip)

    def mostrar_tooltip(self, event=None):
        if self.tooltip:
            return
        x = self.widget.winfo_rootx() + 60
        y = self.widget.winfo_rooty() + 30
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=self.texto_func(), background="lightyellow",
                         relief="solid", borderwidth=1, font=("Arial", 12))
        label.pack()

    def ocultar_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

# TÍTULO CENTRADO
titulo = tk.Label(ventana, text="SMART CLOTHES", font=("Arial Black", 48), bg="#f5f5f5", fg="#333")
titulo.place(x=ancho_pantalla//2, y=30, anchor="n")  # centrado arriba

# MEDIDAS DE BOTONES
ancho_boton = 350
alto_boton = 80

pos_x = (ancho_pantalla - ancho_boton) // 2 + 200  # más a la derecha
pos_y_sacar = (alto_pantalla // 2) - alto_boton - 30
pos_y_guardar = (alto_pantalla // 2) + 30

# IMÁGENES PARA BOTONES
imagen_boton_original = Image.open("boton.png").resize((ancho_boton, alto_boton))
imagen_boton_azul = Image.open("boton blue.png").resize((ancho_boton, alto_boton))

imagen_boton_tk_original = ImageTk.PhotoImage(imagen_boton_original)
imagen_boton_tk_azul = ImageTk.PhotoImage(imagen_boton_azul)

# FUNCIONES
def sacar_ropa():
    global contador_sacar, ultimo_estado
    if ultimo_estado != "sacar":
        contador_sacar += 1
        ultimo_estado = "sacar"
    fondo_label.configure(image=fondo_rosita)
    boton_sacar.config(image=imagen_boton_tk_original)
    boton_guardar.config(image=imagen_boton_tk_original)

def guardar_ropa():
    global contador_guardar, ultimo_estado
    if ultimo_estado != "guardar":
        contador_guardar += 1
        ultimo_estado = "guardar"
    fondo_label.configure(image=fondo_azul)
    boton_sacar.config(image=imagen_boton_tk_azul)
    boton_guardar.config(image=imagen_boton_tk_azul)

# BOTONES
boton_sacar = tk.Button(
    ventana, text="Sacar ropa", command=sacar_ropa,
    image=imagen_boton_tk_original, compound="center",
    fg="white", font=("Arial", 22), borderwidth=0
)
boton_sacar.place(x=pos_x, y=pos_y_sacar, width=ancho_boton, height=alto_boton)

boton_guardar = tk.Button(
    ventana, text="Guardar ropa", command=guardar_ropa,
    image=imagen_boton_tk_original, compound="center",
    fg="white", font=("Arial", 22), borderwidth=0
)
boton_guardar.place(x=pos_x, y=pos_y_guardar, width=ancho_boton, height=alto_boton)

# BOTÓN INFO
boton_info = tk.Button(ventana, text="ℹ", font=("Arial", 40), bg="white", relief="flat")
boton_info.place(x=50, y=alto_pantalla // 2 - 40, width=80, height=80)

def obtener_estadisticas():
    return f"Guardado: {contador_guardar} veces\nSacado: {contador_sacar} veces"

Tooltip(boton_info, obtener_estadisticas)

ventana.mainloop()


