import usuarios.usuario as modelo
import notas.acciones

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

        try:
            # Input (Campos)
            email= input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            
            # Model (Modelo)
            usuario = modelo.Usuario('', '', email, password)

            # Login (Logearse)
            login = usuario.identificar()

            # Validate (Validar)
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"El login incorrecto!! Intentalo más tarde")
        
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
            1.- Crear nota (crear)
            2.- Mostrar tus notas (mostrar)
            3.- Eliminar nota (eliminar)
            4.- Salir (salir)
              """)
        
        accion = int(input("¿Qué quieres hacer?: "))
        hazEl = notas.acciones.Acciones()

        if accion == 1:
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == 2:
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 3:
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 4:
            print(f"\nOk {usuario[1]}, hasta pronto!!")
            exit()

        return None