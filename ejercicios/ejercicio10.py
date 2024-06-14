"""
Ejercicio 10.
    El programa tiene que pedir la nota de 15 alumnos y sacar por pantala cuantos han aprobado y cuantos han suspendido.
"""
aprobados = 0
suspendidos = 0
contador = 1

nro_alumnos = int(input("¿Cauntos alumnos tienes: ?"))
while( contador <= nro_alumnos ):
    nota = float(input(f"Ingrese la nota del alumno {contador}: "))

    if(nota>=13.5):
        print(f"El alumno {contador} esta aprobado...")
        aprobados+=1
    else:
        print(f"El alumno {contador} esta suspendido...")
        suspendidos+=1

    contador+=1

print(f"La cantidad de aprobados = {aprobados} y la cantidad de suspendidos = {suspendidos}")