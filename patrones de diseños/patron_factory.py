#El patrón de diseño Factory (Fábrica) es un patrón creacional que proporciona una interfaz para crear objetos en una superclase, pero permite que las subclases alteren el tipo de objetos que se crearán. Este patrón es especialmente útil cuando se necesita desacoplar la creación de un objeto de su implementación.

#$ consiste en devolver instancia de una clase por medio de algun identificador
from abc import ABC, abstractclassmethod

class Dog:
    """Una clase simple para perros."""
    def speak(self):
        return "Woof!"

class Cat:
    """Una clase simple para gatos."""
    def speak(self):
        return "Meow!"

class PetFactory:
    """La fábrica para crear instancias de mascotas."""
    def get_pet(self, pet_type):
        """Método para obtener la instancia de la mascota."""
        pets = dict(dog=Dog(), cat=Cat())
        return pets[pet_type]

# Uso del patrón Factory
factory = PetFactory()
dog = factory.get_pet("dog")
print(dog.speak())  # Output: Woof!

cat = factory.get_pet("cat")
print(cat.speak())  # Output: Meow!

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class IConexion:
    @abstractclassmethod
    def connect(self):
        pass
    
    @abstractclassmethod
    def disconnect(self):
        pass


class ConexionMySql(IConexion):
    def __init__(self):
        self.__host = "localHost"
        self.__port = 8820
        self.__user = "Andres"
        self.__password = "123"

    def connect(self):
        print(f"se acabo de conectar en {self.__host}-{self.__port}-{self.__user}-{self.__password}")
        
    def disconnect(self):
        print("se desconecto de la base de datos")


class ConexionOracle(IConexion):
    def __init__(self):
        self.__host = "localhost"
        self.__port = "7894"
        self.__user = "pamela"
        self.__password = "789"

    def connect(self):
        print(f"se acabo de conectar en {self.__host}-{self.__port}-{self.__user}-{self.__password}")
        
    def disconnect(self):
        print("se desconecto de la base de datos")



class FactoryConexions:
    def getFactoryConexion(self, type_conexion):
        conexions = [ConexionMySql(), ConexionOracle()]

        if type_conexion == "mysql":
            return ConexionMySql()
        elif type_conexion == "oracle":
            return ConexionOracle()
        else :
            print("error en la coneccion, aqui podemos ver los difirentes tipos de coneccion")
            print(f"los tipos de coneccion son los siguientes : ")
            for conexion in conexions:
                print(conexion)

factoryConexions = FactoryConexions()

mysql = factoryConexions.getFactoryConexion("mysql").connect()
oracle = factoryConexions.getFactoryConexion("oracle").connect()

#% beneficio -> no dependemos de una instancia en particular si no solo pasamos por la fabrica, y esta nos dara la implementacion que nosotros necesitamos



