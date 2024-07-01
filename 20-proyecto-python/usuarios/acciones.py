import usuarios.usuario as modelo

class Acciones: 
    def registro(self):
        print("\nOK!! Vamos a registrarte en el sistema...")
    
        # Input (Campos)
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email= input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        # Model (Modelo)
        usuario = modelo.Usuario(nombre, apellidos, email, password)

        # Register (Registrar)
        registro = usuario.registrar()

        # Validate (Validar)
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente!!")



    def login(self):
        print("\nVale!! Identificate en el sistema...")

        email= input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")