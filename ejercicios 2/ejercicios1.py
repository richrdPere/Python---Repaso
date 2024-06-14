"""
Ejercicio 1.
    Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
        - Recorrer la lista y mostrarla
        - Crea una funcion que recorra la lista y devuelva un string
        - Ordenarla y mostrarla
        - Mostrar su logitud
        - Buscar algun elemento (que el usuario pida por teclado)
"""

numeros = [1,2,4,5,7,8,9,6]

#Crea una funcion que recorra la lista y devuelva un string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Element: " + str(elemento)
        resultado += "\n"

    return resultado


# Recorrer la lista
print(mostrarLista(numeros))
# print("Recorrer la lista")
# for numero in numeros:
#     print(numero)

# Ordenar y mostrarlo
print("Lista ordenada")
numeros.sort()
print(numeros)

# Tamaño de la Lista
print("Tamaño de la Lista")
print(len(numeros))

# Ingrese algun elemento

elem=input("Ingrese un numero: ")

if(numeros.index(elem)):
    print("Ese elemento si existe en la lista")

else:
    print("Este elemento no existe en la lista")