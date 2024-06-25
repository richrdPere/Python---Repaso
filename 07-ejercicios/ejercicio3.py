"""
Ejercicio 3.
    Escribir un programa que muestre los cuadrados de los 60 primeros numeros naturales.
    Resoolverlo con for y con while
"""

# While
contador = 1

# while contador <=60:
#     print(f"el cuadrado de {contador} es {contador*contador}")
#     contador+=1

# For

for contador in range(1, 61):
    print(f"el cuadrado de {contador} es {contador*contador}")
