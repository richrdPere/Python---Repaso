"""
    Ejercicio 5: Crear una lista con el contenido de esta tabla:

    ACCION      AVENTURA            DEPORTES
    GTA         ASSINS              FIFA 21
    COD         CRASH               PRO 21
    PUGB        Prince o persia     MOTO GP 21

        Mostrar esta información
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSINS", "CRASH", "Prince o persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"------------{categoria['categoria']}-------------------")

    for juego in categoria['juegos']:
        print(juego)
