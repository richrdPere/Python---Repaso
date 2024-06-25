"""
Ejercicio 1.
    Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
        - Recorrer la lista y mostrarla
        - Crea una funcion que recorra la lista y devuelva un string
        - Ordenarla y mostrarla
        - Mostrar su logitud
        - Buscar algun elemento (que el usuario pida por teclado)
"""

"""
numeros = [13, 64, 52, 73, 21, 7, 91, 63]

#Crea una funcion que recorra la lista y devuelva un string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Element: " + str(elemento)
        resultado += "\n"

    return resultado


# Recorrer la lista
print("######### Mostrar Lista ###############")
print(mostrarLista(numeros))
# print("Recorrer la lista")
# for numero in numeros:
#     print(numero)

# Ordenar y mostrarlo
print("######### Ordenar Lista ###############")
print("Lista ordenada")
numeros.sort()
print(numeros)

# Tamaño de la Lista
print("######### Tamaño de la Lista ###############")
print(len(numeros))

# Si existe un elemento en la lista
print("######### Busqueda en la lista ###############")
busqueda = int(input("Introduce el numero: "))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el numero: "))

else:
    print(f"Has introducido el {busqueda}")

print(f"######## Buscar en la lista el número {busqueda} ############")

try:
    search = numeros.index(busqueda)
    print(f"El numero buscado existe en la lista, es el indice: {search}")

except:
    print("El numero no esta en la lista, lo siento!!")

"""
# Multiples excepciones 

try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero*numero))

except TypeError:
    print("Debes convertir tus cadenas a enteros..!!")

except ValueError:
    print("Introduce un numero correcto..!!")
    

