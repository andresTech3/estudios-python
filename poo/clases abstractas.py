#*clases abstractos -> es una clase que no podemos instanciar, es una especie de plantilla para que podamos crear clases apartir de esa plantilla

#* metodo abstracto es el que esta declarado en una clase abstracta solo que no tiene ninguna implementacion

#%al hacer una clase abstrata estas obligando a la otra clase que era de esta ah implemnetar sus metodos y propiedades

from abc import ABC, abstractclassmethod #$ importando una clase y un decorador 

# esto seria una plantilla

class Persona(ABC): #% ya estamos haciendo que esto sea una clase abstracta
    @abstractclassmethod #? estamos diciendo que vamos a crear un metodo abstracto
    def __init__(self, nombre, edad, sexo, actividad) :
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def realizar_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

#andres = Persona("andres",22, "M", "programador" ) #! no podemos instanciar la clase porque es una clase abstracta

class Estudiante(Persona):
    def __init__(self,nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def realizar_actividad(self):
        print(f"estoy estudiando : {self.actividad}")


class Trabajador(Persona):
    def __init__(self,nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def realizar_actividad(self):
        print(f"actualmente estoy trabajando en el rubro de : {self.actividad}")



andres = Estudiante("andres", 22,"M", "programacion")
pedro = Trabajador("pedro", 26,"M", "programacion")

andres.presentarse()
andres.realizar_actividad()

pedro.presentarse()
pedro.realizar_actividad()