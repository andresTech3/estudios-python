# lista (array)________________
#se puden modificar los valores
#no importa los orden de los valores
lista = ["andres", "soy andres", True, 1.56, 21]
print(lista)
print(lista[0])
lista[0] = "felipe" #modificamos el dato
print(lista[0])

#tuplas (array) ________________
#diferencia con las lista es que las tuplas nunca se van a poder modificar las lista si
#se pueden reconstruir
tupla = ("andres", "soy andres", True, 1.56, 21)
print(tupla[1])
# tupla[1] = "nuevo valor" no se puede


#conjunto (set) ________________
#los datos pueden intercambiarce 
#no se puden modificar los valores
#se puede resconstruir el conjunto con nuevos datos
# no podemos haceder por el indice 
# no me permite repetir valores y si hay python me elimina el duplicado
conjunto = {"andres", "soy andres", True, 1.56, 21}
mi_conjunto = set("andres", "soy andres", True) #crea un conjunto
# con set creamos un conjunto
if('soy andres' in conjunto): print("si esta")

#dicionarios (objetos) json (dicts) ________________
#clave : valor
dicionario = {
    'nombre': 'andres',
    'canal': 'andresTech',
    'le gusta programar' : True,
    'altura' : 1.86,
    'datos duplicado': 'andres'
}

print(dicionario['nombre'])
dicionario['canal'] = 'andresWord'
print(dicionario['canal'])