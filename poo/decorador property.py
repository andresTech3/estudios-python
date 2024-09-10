#$ son propiedades de set , get y delete que podemos establecer algo mas utilizando los decoradores

class Personas:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property  #% decorador especial porque es reservado para las clases donde ya entiende que la funcion es un get  y al llamarlo lo puedo hacer como una propiedad
    def nombre(self):
        return self.__nombre
    
    @nombre.setter #% en este decorador estamos diciendo que se comporte como un setter la funcion de abajo
    def nombre(self,newNombre):
        self.__nombre = newNombre

    @nombre.deleter #%es un operador que nos elimina valores
    def nombre(self):
        return self.__nombre
    

andres = Personas("andres", 22)

andres.nombre = "juan"

# del andres.__nombre

print(andres.nombre)