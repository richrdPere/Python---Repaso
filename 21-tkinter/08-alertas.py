from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=60)

# 1er Alert
def sacarAlerta():
    MessageBox.showwarning("Alerta", "Hola soy Richard Pereira")

Button(ventana, text="Mostrar alerta!!", command=sacarAlerta).pack()
# 2do Alert
def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutando la aplicación?")

    if resultado != "yes":
        MessageBox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()


Button(ventana, text="Salir", command=lambda: salir("Richard Pereira")).pack()

ventana.mainloop()