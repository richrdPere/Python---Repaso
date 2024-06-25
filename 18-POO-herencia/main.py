# HERENCIA: Es la posibilidad de compartir atributos y metodos
#           entre clases. Y que diferentes clases hereden de otras
import clases

persona = clases.Persona()
persona.setNombre("Richard")
persona.setApellidos("Pereira")
persona.setEdad("24 años")
persona.setAltura("172cm")

print(f"la persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("\n----------------------------------------------------\n")

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martines")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}") 
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("\n----------------------------------------------------\n")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.lenguajes)
