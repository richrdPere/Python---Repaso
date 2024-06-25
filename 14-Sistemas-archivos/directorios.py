import os, shutil
import pathlib

# Crear carpeta 
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")

# Copiar directorio
"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"

shutil.copytree(ruta_original, ruta_nueva)
"""

# Eliminar 
os.rmdir('./mi_carpeta_COPIADA')

# Listar archivos de un directorio
print("Contenido de mi carpeta: ")
contenido = os.listdir("./mi_carpeta")

for fichero in contenido:
    print("Fichero: " + fichero)