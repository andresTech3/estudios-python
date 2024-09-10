#Clases -> la receta que debemos de seguir un objeto

#Objetos -> la instancia de una clase

#Atributos de instancia -> variables que pertenecen a una clase

#Metodo constructor -> se ejecuta cuando utilizamos la clase

#Metodo -> son funciones o comportamiento que tiene nuestro objeto, tiene que tener el parametro self siempre , ya que hace referencia la objeto

#? self -> forma de hacer referencia al mismo objeto

class Celular :

    def __init__(self, marca, modelo, camara) :
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"estas haciendo un llamado desde un : {self.modelo}")

    def cortarLLamada(self):
        print(f"cortaste la llamada desde tu : {self.modelo}")



celular1 = Celular("sansung", "s23", "42mp")
celular2 = Celular("apple", "phone 15", "96mp")

celular2.llamar()