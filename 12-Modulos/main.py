"""
Modulos: son funcionalidades ya hechas para reutilizar.
    En python hay muchos modulos , que los puedes consultar aqui:
    https://docs.python.org/es/3/tutorial/modules.html

    Podemos consieguir modulos qye ya viennen en el lenguaje,
    modulos en internet, y tambien podemos crear nuestros modulos.
"""

# Importar modulos propios
import miModulo

print(miModulo.holaMundo("Richard"))

# Importar un solo modulo
from miModulo import holaMundo

print(holaMundo("Siwar"))

# Importar varios modulos
from miModulo import *

print(holaMundo("Chispi"))


"""
    MODULO de Fechas
"""
import datetime

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S") # para formatear la fecha
print("Mi fecha personalizada,", fecha_personalizada)

print(datetime.datetime.now().timestamp())

"""
    MODULO de Matematicas
"""
import math

print("Raiz cuadrada de 100: ", math.sqrt(100))
print("numero pi", math.pi)
print("Redondear", math.ceil(6.182526))
print("Redondear", math.floor(6.182526))

"""
    MODULO de Random
"""
import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15,67))