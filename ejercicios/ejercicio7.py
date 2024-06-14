"""
Ejercicio 7.
    Hacer un programa que muestre todos los numeros impares entre dos numeros que eliga el usuario.
"""

nro1 = int(input("Ingrese el primer numero: "))
nro2 = int(input("Ingrese el segundo numero: "))

if(nro1 < nro2):
    print("El rango de numeros impares es: ")

    for i in range(nro1,nro2+1):
        if(i%2 != 0):
            print(i)


else:
    print("El rango de numeros impares es: ")

    for i in range(nro2, nro1 + 1):
        if (i % 2 != 0):
            print(i)