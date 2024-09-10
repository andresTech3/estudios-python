
class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        """ Método estático de acceso a la instancia única """
        if Singleton._instance == None:
            Singleton._instance = Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("Esta clase es un singleton!")
        else:
            Singleton._instance = self

# Crear una instancia
s = Singleton.getInstance()

 # Intentar crear otra instancia. Esto levantará una excepción.
# s2 = Singleton()

"""
El patrón Singleton es un patrón de diseño que restringe la instanciación de una clase a un solo objeto. Esto es útil cuando se necesita exactamente un objeto para coordinar acciones en todo el sistema. El patrón Singleton garantiza que una clase tenga solo una instancia y proporciona un punto de acceso global a esa instancia
"""


#* ejemplo -> base de datos

class Conexion:
    _instancia = None

    @staticmethod
    def getInstance(self):
        if Conexion._instancia == None:
            Conexion._instancia = Conexion()
        return Conexion._instancia
    
    def __init__(self):
        if Conexion._instancia != None:
            raise Exception("no se puede crear otra instancia de esta clase")
        else:
            Conexion._instancia = self

    def conectarDB(self, barrio):
        print(f"conectado a la base de datos Barrios {barrio}")
    
    def desconectarDB(self, barrio):
        print(f"desconectando la base de datos Barrios {barrio}")


dbBarrios = Conexion()

dbPiñalito = dbBarrios.conectarDB("piñalito")
dbPorvenir = dbBarrios.conectarDB("porvenir")
dbParaiso = dbBarrios.conectarDB("paraiso")

