
class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    
    def setApellidos(self, apellidos)    :
        self.apellidos = apellidos
    def getApellidos(self):
        return self.apellidos

    def setAltura(self, altura):
        self.altura = altura
    def getAltura(self):
        return self.altura
    
    def setEdad(self, edad):
        self.edad = edad
    def getEdad(self):
        return self.edad

    # Metodos
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminado"
    
    def dormir(self):
        return "Estoy durmiendo"
    

class Informatico(Persona):
    """
    lenguajes
    experiencia
    """
    def __init__(self):
        self.lenguajes = "HTML, CSS, Javascript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "He reparado tu ordenandor"
    
class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__()
        self.auditarRedes = 'experto'
        self.experienciaRedes = 15

    def auditoria(Self):
        return "Estoy auditando una red"
