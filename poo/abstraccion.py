# atraccion -> manenejando la complejidad ocultando todos los detalles imnesesarios al programador o al usuario dandole solo las funcionalidades relevantes



#$ crear una interfaz simple que oculte una interfaz mas compleja 

class Auto:
    def __init__(self):
        self.estado = "apagado"
    
    def encender(self):
        self.estado = "encendido"
        print(f"el auto esta {self.estado}")

    def conducir(self):
        if (self.estado == "apagado"):
            self.encender()
            
        print("conduciendo el Auto")

myAuto = Auto()
myAuto.conducir()
