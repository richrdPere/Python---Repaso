"""
LISTAS (array)
Son colencciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice numerico
"""

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jennifer Lopez'))
years = list(range(2020, 2050))
variada = ["vixtor", 30, 4.4, True, "texto"]

# print(peliculas[1])
# print(cantantes[-1])
# print(years[1:3])
# print(variada)


# Añadir elementos a una lista
cantantes.append("Kase O")

print(cantantes)

# Recorrer y mostrar los elementos de una lista
# nueva_pelicula = ""
#
# while (nueva_pelicula != "parar"):
#     nueva_pelicula = input("Introduce la nueva pelicula: ")
#     peliculas.append(nueva_pelicula)
#
#
# for pelicula in peliculas:
#     print(f"{peliculas.index(pelicula) +1 } - {pelicula}")


# Listas Multidimencionales
"""
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'salvador',
        'salvador@salvador.com'
    ]
]
print(contactos)

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")
"""

# Funciones y metodos para las listas
cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1, 5, 2, 6, 4, 5, 8, 7]

# Ordenar
print(numeros)
numeros.sort()

print(numeros)

# Añadir elementos
cantantes.append("Natos y Waor")
cantantes.insert(1, "David Bisbal")
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove('Bad Bunny')
print(cantantes)

# Dar la vuelta
numeros.reverse()
print(numeros)


# Buscar dentro de una lista
print('Drake' in cantantes)   # True

# Contar elementos
print(cantantes)
print(len(cantantes))   # 4

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8)) #2

# Conseguir indice
print(cantantes.index("Drake"))

# Unir listas
cantantes.extend(numeros)

print(cantantes)
