from tkinter import *

ventana = Tk()
#ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    
    fg="white",  #fg: (Fore Ground, color del texto)
    bg="#000000",  #bg: (Back ground, color del fondo)
    padx=20,    #padx: (padding)
    pady=20,
    font=("Consolas", 30),     #Font de texto
    ) 
texto.pack(side=TOP)

# Funcion Pruebas
texto = Label(ventana, text="Soy Richard Pereira")
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
texto.pack(side=TOP, fill=X, expand=YES) # Para que cubra en la secion x, y se expanda


# 1 text
texto = Label(ventana, text="Basico 1")
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
texto.pack(side=LEFT, fill=X, expand=YES) # Ver la imagen imagen_Orientacion

# 2 text
texto = Label(ventana, text="Basico 2")
texto.config(
    #justify=RIGHT
    #width=400,
    height=3,
    bg="red",
    font=("Arial", 14),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES) # Ver la imagen imagen_Orientacion

# 3 text
texto = Label(ventana, text="Basico 3")
texto.config(
    #justify=RIGHT
    #width=400,
    height=3,
    bg="pink",
    font=("Arial", 14),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES) # Ver la imagen imagen_Orientacion

ventana.mainloop()