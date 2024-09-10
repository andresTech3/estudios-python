class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def info(self):
        print(f"hola soy {self.nombre} y tengo {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def myGrado(self):
        print(f"soy {self.nombre} y tengo {self.edad} años y hago grado {self.grado}")


andres = Estudiante("Andres", 22,5)
andres.info()