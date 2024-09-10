# si la clase B es una subclase de A entonces A deberia poder utilizarce en todo los lugares donde B pueda utilizarce

#! no se aplica el metodo
# class Padre:
#     def corregir(self):
#         return "te estoy mandandooooo"
    
# class Hijo(Padre):
#     def corregir(self):
#         return "no puedo corregir"
    
# def hacer_corregir(padre : Padre):
#     return padre.corregir()

# print(hacer_corregir(Hijo()))

#* aplicar el metodo correctamente

class Ave:
    pass

class AveVolador(Ave):
    def volar(self):
        return "estoy volando"
    
class aveNoVoladora(Ave):
    pass