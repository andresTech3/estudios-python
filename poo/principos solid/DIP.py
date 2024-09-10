# que no dependa de interfaces pequeñas si no cosas mas complejas con clases de alto nivel

# class Diccionario :
#     def verificarPalabra(self, palabra):
#         #logica para vericicar palabra
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self,texto):
#         #usamos el diccionario para coregir el texto
#         pass

from abc import ABC,abstractclassmethod

class VerificacionOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificacionOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass

class ServicioOnline(VerificacionOrtografico):
    def verificar_palabra(self,palabra):
        #logica para verificar palabra por medio del servicio Online
        pass

class CorrectorOrtografico(VerificacionOrtografico):
    def __init__(self, verificador):
        self.verificador = verificador
    
    def corregir_texto(self):
        #usamos el verificador para corregir texto
        pass

corrector = CorrectorOrtografico(Diccionario())