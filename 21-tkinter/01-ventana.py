#Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *

# Crear la ventana raiz
ventana = Tk()

# Titulo de la ventana
ventana.title("Interfaz grafica con Python y Richard Pereira")

# Icono de la ventana
ventana.iconbitmap("../21-tkinter/imagenes/code.ico")

# Cambio en el tamaño de la ventana
ventana.geometry("750x450")

# Bloquear el tamaño de la ventana

#ventana.resizable(1, 1) # Permite la disminucion del tamaño
#ventana.resizable(1, 0) # Permite la disminucion del tamaño horizontalmente
#ventana.resizable(0, 1) # Permite la disminucion del tamaño verticalmente
ventana.resizable(0, 0) # Bloquea la disminucion del tamaño

# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()