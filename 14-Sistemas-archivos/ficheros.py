from io import open
import pathlib
import shutil

# Abrir archivo
#archivo = open("14-Sistemas-archivos/fichero_texto.txt", "a+")

# ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# print(ruta)

# archivo = open(ruta, "a+") #Crea un archivo


# # Escribir en un archivo
# archivo.write("**** Soy un Texto metido desde Python ********\n")

# # cerrar archivo
# archivo.close()


"""

"""

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r") # Abrir y leer contenido

# Leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

# for frase in lista:
#     if not frase.isnumeric():
#         print("- " + frase.upper())

for frase in lista:
    #lista_frase = frase.split()
    #print(lista_frase)
    #print("- " + frase.capitalize())
    print("- " + frase.center(100))

# Copiar
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_Alternativa = "../07-ejercicios/fichero_copiado77.txt"

shutil.copyfile(ruta_original, ruta_Alternativa)
"""

# Mover
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
"""

# Eliminar 
"""
import os

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)

"""

# Comprobar si existe
"""
import os.path

#print(os.path.abspath("../"))
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
ruta_comprobar = "./ficheros.py"

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")
"""
