from tkinter import *

ventana = Tk()
ventana.title("Marcos | Master en Python")
ventana.geometry("700x700")

# 4to cuadro - Marco padre - BOTTOM
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue"
    
    )
marco_padre.pack(side=BOTTOM, fill=X, expand=YES)

# 5to cuadro
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="blue",
    bd=5,
    relief="solid"
    
    )
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="Primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
    height=4,
    width=10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack(fill=Y, expand=YES)

# 6to cuadro
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="orange",
    bd=5,
    relief="solid"
    
    )
marco.pack(side=RIGHT)

# 1er cuadro - Marco Padre
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=5,
    relief="solid"
    
    )
marco.pack(side=LEFT, anchor=SW)

# 2do cuadro
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief="solid"
    
    )
marco.pack(side=RIGHT, anchor=SE)

# 3er cuadro - Marco padre - TOP
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue",
    bd=5,
    relief="solid"
    
    )
marco_padre.pack(side=TOP, fill=X, expand=YES)




ventana.mainloop()