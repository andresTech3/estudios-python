frutas = ["banana", "manzana", "ciruela","pera", "naranja","granada","durazno"]


#? continue pasa la condicion y sigue su siclo de ejecuccion normal
for fruta in frutas:
    if fruta == "granada" or fruta == "manzana":
        continue;
    print(f"me voy a comer {fruta}")
else:
    print("terminaste de comer !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#? breack cuando llega a la condicion detiene el bucle y no se sigue ejecutando
for fruta in frutas:
    if fruta == "naranja":
        break;
    print(f"me voy a comer {fruta}")
    
    
# recorrer una cadena de texto
cadena = "hola soy andres, mucho gusto"

for recor in cadena:
    print(recor)
    
#el bucle for en una sola linea de codigo


numeros = [2,4,7,13,5,8]
num_duplicados = list()

#! forma larga
for num in numeros:
    num_duplicados.append(num * 2)

print(num_duplicados)

#* forma mas corta
""" 
?1 -> expresion matematica alante
?2 -> todo lo demas, ya sea un for o otras funciones
"""
num_duplicados2 = [x*2 for x in numeros]
print(num_duplicados2)






