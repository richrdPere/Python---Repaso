"""
Ejercicio 5.
    Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario.
"""

nro1 = int(input("Ingrese el primer numero: "))
nro2 = int(input("Ingrese el segundo numero: "))


if(nro1 < nro2):
    print("El rango de numeros es: ")

    for i in range(nro1,nro2+1):
        print(i)

else:
    print("El rango de numeros es: ")

    for i in range(nro2, nro1 + 1):
        print(i)