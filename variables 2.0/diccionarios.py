#creando diccionario con dict

diccionario = dict(nombre= "andres", apellido = "narvaez")

# las lista no pueden ser claves pero las tuplas si y utilizamos frozenset para meter conjuntos
diccionario = {("nombre", "apellido"):"jajaja"}

#creando un diccionario con fromkeys(insertamos claves)
#* fromkeys -> permkite insertar claves a nuestro diccionario
#? si le pasamos el fromkeys y pasamos un solo key nos itera la key por caracter teniendo sus valores en none
diccionario = dict.fromkeys(["nombre", "apellido","edad"])
#? 1 dato -> un iterable 2 dato -> el valor que se igualara con cada iterable 
dicionario2 = dict.fromkeys("ABCDE", "igualdad")
print(dicionario2)