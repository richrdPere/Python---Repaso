"""
Proyecto Python y MySQL:
    - Abrir asistente
    - Login o registro
    - Si elegmos registro, creará un usuario en la BD
    - Si elegimos login, identifica al usuario y nos preguntará
    - Crear nota, mostrar notas, borrarlas.
"""

from usuarios import acciones

print("""
Acciones disponibles:
    1.- Registro
    2.- Login
    3.- Salir
      """)

hazEl = acciones.Acciones()
accion = int(input("¿Qué quieres hacer?: "))

if accion == 1:
    hazEl.registro()

elif accion == 2:
   hazEl.login()

elif accion == 3:
    exit()