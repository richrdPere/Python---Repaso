"""
Ejercicio 6.
    Mostrar todas las tablas de multiplicar del 1 al 10.
"""
print("Tablas de Multiplicar del 1 al 10 ")

for i in range(1, 11):
    print(f"Tabla de multiplicar para {i} \n")

    for j in range(21):
        print(f"{i} X {j} = {i*j}")

    print("\n")
