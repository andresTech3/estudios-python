# que que una clase herede la clase hijo de la clase padre, propiedades y metodos etc

class Personas:
    def __init__(self, nombre,edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def habla(self):
        print("Todas las Personas hablamos")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrarHabilidad(self):
        print(f"mi habilidad es {self.habilidad}")
    

#% de esta forma heredamos los metodos y propiedades de la clase persona
class Empleado(Personas):
    def __init__(self,nombre,edad, nacionalidad,trabajo, salario):
        super().__init__(nombre,edad,nacionalidad) #definir que quiero que erede de la clase Personas
        self.trabajo = trabajo
        self.salario = salario

    def presentacion(self):
        print(f"hola mi nombre es {self.nombre}, tengo {self.edad} y soy de {self.nacionalidad}, mi profecion personal es {self.trabajo}, y gano actualmente {self.salario}$")

    def habla(self):
        print("Todos los Empleamos debemos de hablar")


class Estudiantes(Personas):
    def __init__(self,nombre,edad, nacionalidad,notas, universidad):
        super().__init__(nombre,edad,nacionalidad) #definir que quiero que erede de la clase Personas
        self.notas = notas
        self.universidad = universidad

    def presentacion(self):
        print(f"hola mi nombre es {self.nombre}, tengo {self.edad} y soy de {self.nacionalidad}, mi notas son {self.notas}, y estudio en {self.universidad}")

    def habla(self):
        print("Todos los Estudiante deberia de hablar")

#*Herencias Multiples -> cuando heredamos de 2 o mas clases 


class EmpleadoArtista(Personas, Artista): #hereda todas las 2 clases 
    def __init__(self, nombre = "andres", edad = 20 , nacionalidad = "", habilidad = "Artista", salario = 20000, empresa = "andresTech"):
        Personas.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario  
        self.empresa = empresa

    def presentar(self):
        return super().mostrarHabilidad()
    
andres = EmpleadoArtista()
andres.presentar()

#$ para saber si una clase hereda de una clase superior
herencia = issubclass(EmpleadoArtista, Artista) #? 1 - clase que quiere verificar , 2 - la clase superior
#$ para ver si un objeto es una instancia de una clase
instancia = isinstance(andres,EmpleadoArtista) #? 1 - el objeto a evaluar, 2 - la clase a determinar 

print(instancia)








