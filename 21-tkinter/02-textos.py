from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    
    fg="white",  #fg: (Fore Ground, color del texto)
    bg="#000000",  #bg: (Back ground, color del fondo)
    padx=20,    #padx: (padding)
    pady=20,
    font=("Consolas", 30),     #Font de texto
    ) 
texto.pack()

# Funcion Pruebas
def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text=pruebas(nombre="Richard", apellidos="Pereira", pais="Perú"))
texto.config(
    #justify=RIGHT
    #width=400,
    height=3,
    bg="orange",
    font=("Arial", 14),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(anchor=SE) # Ver la imagen imagen_Orientacion



texto = Label(ventana, text=pruebas(nombre="Richard", apellidos="Pereira", pais="Perú"))
texto.config(
    #justify=RIGHT
    #width=400,
    height=3,
    bg="green",
    font=("Arial", 14),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(anchor=NW) # Ver la imagen imagen_Orientacion

ventana.mainloop()