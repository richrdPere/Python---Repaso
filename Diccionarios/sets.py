"""
SET es un tipo de dato, para tener ima colección de valores.
pero no tiene ni indice ni orden.
"""

personas = {
    "victor",
    "manolo",
    "Francisco"
}

personas.add("Paco")
personas.remove("Francisco")


print(type(personas))
print(personas)