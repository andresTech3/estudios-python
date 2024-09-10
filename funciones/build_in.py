# funciones creadas por python
#* encontrando el numero mayor de una lista

numeros = [1,2,3,4,5,6,7,8]
numero_max_alto = max(numeros)
numero_max_bajo = min(numeros)
print(numero_max_bajo)

#redondeado a decimales
numero_redondeado = round(25.387, 1)
print(numero_redondeado)

#bool
# return false -> 0,false,vacio / true -> distinto a cero , true cadena,datos no vacio
resultBool = bool()
#retorna true si todos los valores de adentro de un iterable son verdadero
resultAll = all(["123",True,])

#suma todos los valores de un iterable 
sumaTotal = sum(numeros)