#Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path

class Programa:

    def __init__(self):
        self.title = "Master en Python con Richard Pereira"
        self.icon = "../imagenes/code.ico"
        self.icon_alt = "../21-tkinter/imagenes/code.ico"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Titulo de la ventana
        ventana.title(self.title)

        # Comprobar si existe un archivo 
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)


        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()


        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana

        #ventana.resizable(1, 1) # Permite la disminucion del tamaño
        #ventana.resizable(1, 0) # Permite la disminucion del tamaño horizontalmente
        #ventana.resizable(0, 1) # Permite la disminucion del tamaño verticalmente
        #ventana.resizable(0, 0) # Bloquea la disminucion del tamaño

        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

        # Arrancar y mostrar la ventana hasta que se cierre
        #ventana.mainloop()

    def addTexto(self):
        texto = Label(self.ventana, text="Hola desde un metodo...")
        texto.pack() # Carga en la aplicacion

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()



# Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto()
programa.mostrar()