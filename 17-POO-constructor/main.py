from coche import Coche

carro1 = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro2 = Coche("Verde", "Seat", "Panda", 240, 200, 4)
carro3 = Coche("Azul", "Citroen", "Xara", 100, 180, 4)
carro4 = Coche("Rojo", "Mercedes", "Clase A", 350, 400, 4)

print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

# Detectar tipado
carro1 = "Aleatorio"
if type(carro1) == Coche:
    print("Es un objeto correcto !!")

else:
    print("No es un objeto")

# Visibilidad
print(carro2.soy_publico)
#print(carro2.__soy_privado)
print(carro2.getPrivado())