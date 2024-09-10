# son funciones que tiene un nombre inicial reservado comiensan con __ y terminan con __
#$ la sobre carga de operadores y metodos 

class Persona:
    def __init__(self, nombre, edad):  #% __init__ es un metodo especial para crear un constructor
        self.nombre = nombre
        self.edad = edad

    def __str__(self) : #% __str__ nos devuelve una representacion del objeto en una cadena de texto
        return f"persona(nombre = {self.nombre}, edad= {self.edad})"
    
    def __repr__(self): #% es utilizado para definir una representación "oficial" de un objeto, la cual es útil principalmente para depuración y desarrollo 
        return f"Persona(nombre={self.nombre!r}, edad={self.edad!r})"
    
    #$como se va a comportar nuestros objeto cuando utilicemos el operador mas con __add__
    def __add__(self,otro): 
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)
    
andres = Persona("andres", 22)
pedro = Persona("pedro", 26)

resultado = andres + pedro
print(resultado)

# repre = repr(andres) #? repr() está pensada para ser informativa y es principalmente útil para depuración y desarrollo, ya que muestra más detalles sobre el objeto.

# resultado = eval(repre) #? eval() toma un string que contiene una expresión de Python y la evalú


    
