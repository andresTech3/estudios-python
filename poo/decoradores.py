#$ decoradores -> es una funcionalidad que permite agregar mas funcionalidad a un metodo independintemente del la funcionalidad actual , si lo queremos antes o despues

#$ 1 - tima una funcion como entrada, 2 - le agrega una funcionalidad extra , 3 devuelve como salida la funcion modificada

"""
    *en que se puede utilizar
    % manejo de exepciones
    % validacion de entrada
    % medicion de tiempo de ejecucuiones
    % etc
"""

def decorador(funcion):
    def funcion_modificada(): #%creando una funcion 
        print("antes de llamar a la funcion") #% definiendo una duncionalidad antes de la funcion a pasar
        funcion()
        print("despues de llamar a la funcion") #%definiendo una funcionalidad despues de la funcion a pasar
    return funcion_modificada #$retornamos la funion nueva modificada

#* codigo normal que se puede utilizar para usar el decorador
# def saludo():
#     print("hola mundo")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

#* codigo optimo para utilizar el decorador

@decorador #? definimos el decorador con el @ y el nombre del decorador que creamos
def saludo():
    print("hola soy andres")

saludo() #$es una funcion modificada