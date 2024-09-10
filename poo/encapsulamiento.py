# encapsulamiento -> proteger los elementos de una clase tanto propiedades como metodos restringiendo el acceso 
#* la forma de darle a entender a python que estamos creando un atributo privado es con el (_)
#$ la forma de darle a entender a python que estamos creando un atributo muy privado es con el (__)

#? getters y setters -> metodos para hacerder y modificar a las clases privadas con sus propiedades y atributos

class Persona:
    def __init__(self, nombre, edad) :
        self.__nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    



objeto = Persona("Andres", 22)

objeto.set_nombre("francisco")
print(objeto.get_nombre())

