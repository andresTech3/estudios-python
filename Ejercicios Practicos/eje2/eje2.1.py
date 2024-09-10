#falto el profe  los estudiante van armar la clase
#? range -> se utiliza para generar una secuencia de números
#* pedir el nombre y la edad de los compañeros que vinieron a clase


def get_compañeros(cantidadCompañeros):
    compañeros = []
    for i in range(cantidadCompañeros):
        nombre = input('Ingrese el nombre del compañero')
        edad = int(input('Ingrese la edad del compañero'))
        estudiante = (nombre, edad)
        compañeros.append(estudiante)
    compañeros.sort(key = lambda index : index[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente,profesor = get_compañeros(5) #? desempacando la funcion
print(f' el asistente es : {asistente}')
print(f' el profesor es : {profesor}')
