# Importa el modulo
import sqlite3

# Conexion
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla 
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "+
    "titulo varchar(255), "+
    "descripcion text, "+
    "precio int(255)"+
")")

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null,'Primer producto', 'Descripcion de mi producto', 550)")

# Guardar cambios
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

#print(productos)
for producto in productos:
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3], "\n")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

# Cerrar conexión
conexion.close()