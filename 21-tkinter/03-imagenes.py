from tkinter import *
from PIL import Image, ImageTk  #pip install --upgrade --force-reinstall pillow


ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola, soy Richard!!").pack(anchor=W)

imagen=Image.open('../21-tkinter/imagenes/sven.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()

