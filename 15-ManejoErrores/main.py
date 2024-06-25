# Capturar excepciones y manejar errores en codigo
# suceptible a fallos/errores

"""
try:
    nombre = input("¿Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, escribe bien el nombre...")

else: 
    print("Todo ha funcionado correctamente")

finally:
    print("Fin de la iteración...")
"""


# Multiples excepciones 
"""
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero*numero))

except TypeError:
    print("Debes convertir tus cadenas a enteros..!!")

except ValueError:
    print("Introduce un numero correcto..!!")

except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)
"""

# Excepciones personalizadas o lanzar excepciones

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al Master en Python {nombre} !!")
except ValueError:
    print("Introduce los datos correctamente !!")
except Exception as e:
    print("Existe un error: ", e)