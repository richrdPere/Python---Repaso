"""
Ejercicio 8.
    ¿Cuanto es el X por ciento de X numero?

        20% de 150
"""

nro = int(input("Ingrese un numero: "))
porcentaje = int(input(f"¿Qué porcentaje quieres sacar de {nro}? "))

print(f"El {porcentaje}% de {nro} es {nro*porcentaje/100}")
