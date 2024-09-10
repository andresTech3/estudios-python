
class Animal:
    def comer(self):
        print("tel animal esta comiendo")


class Mamifero(Animal):
    def amamantar(self):
        print("el animal esta amamntando")


class Ave(Animal):
    def volar(self):
        print("el animal esta volando")

class Murcielago(Mamifero, Ave):
    pass



murcielago = Murcielago()
murcielago.volar()
murcielago.comer()
murcielago.amamantar()

print(Murcielago.mro())

