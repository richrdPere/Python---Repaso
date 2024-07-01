import pyodbc

try:
    # Conexion
    # connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-9EN7FOS\SQLEXPRESS;DATABASE=BD_Energias;UID=root;PWD=123456')
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-9EN7FOS\SQLEXPRESS;DATABASE=BD_Energias;Trusted_Connection=yes;')
    print("Conexión exitosa.")

    # Cursor
    cursor = connection.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    #print("Versión del servidor de SQL Server: {}".format(row))

    # Mostrar mediante Consultas
    cursor.execute("SELECT * FROM Energias")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    connection.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")