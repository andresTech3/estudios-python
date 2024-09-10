# las clases solo deben tener una unica funcion y encargarse solo de esa funcion
class Auto :
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        

    def mover(self, distancia):
        if(self.tanque.obtener_combustible() >= distancia/2):
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("haz movido el auto exitosamente")
        else :
            print("no tienes suficiente combustible")
    
    def obtener_posicion(self):
        return self.posicion
    

    
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustibles(self,cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad


tanque = TanqueDeCombustible()
autico = Auto(tanque)


print(autico.obtener_posicion())
print(autico.mover(50))
print(autico.obtener_posicion())
