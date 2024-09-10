animales = list(["perro","gato","loro", "cocodrilo"])
numeros = [10,12,54,34]

for animal in animales :
    print(animal)
    
for numero in numeros :
    print(numero * 2)
    
    
#iterar ambas lista juntas en python pueden 2 o mas listas
#* las listas debe tener las misma cantidad de elementos
#? zip(listas)-> recorremos 2 o mas lista al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(animal)
    print(numero)
    
#iterar segun el indice y el elemento

for indice, element in enumerate(animales):
    print(f"indice : {indice} , element : {element}")
    
#iterar segun el rango
#? range() -> permite definir un rango inicial y final

#! forma no optima de recorrer una lista (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#* forma correcta de recorrer lista con su indice
for num in enumerate(numeros):
    print(num[1])   
    

#utilizando el for else
#? los else dentro de los for se ejecuta siempre al finalizar el for siempre y cuando no aya un break
for numero in numeros:
    print("ejecutando el ultimo bucle, valor actual : " ,numero)
else:
    print("el bucle termino")
    
#* todo lo anterior funciona exactamente para tuplas, listas y conjuntos