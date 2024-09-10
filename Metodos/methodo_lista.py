# Crea una lista con list()
lista = ["hola", 24, True]
# nos indica cuanto elementos hay en una lista
recorrido = len(lista)
# agregando elemento a la lista con append
lista.append(22.5)
# agregando elemento a la lista con insert, en un indice espesifico
lista.insert(0,"jajaja")
# agregando elemento a la lista con extend, agregamos varios elementos
lista.extend(["buenos Dias", 3146880954, "andres narvaez"])

#eliminar un elemento de la lista, con los indice negativo (-1,-2 etc) eliminamos de atraz para lante elemento de la lista
lista.pop(0)
#elimina un elemento de la lista indicando el valor espesifico
lista.remove(3146880954)

#eliminando todos los elemento de la lista
#* lista.clear()

lista2 = [23,56,78,3,5,14,16]

#ordena los elemento de la lista
lista2.sort()
lista2.sort(reverse=True) #si utilizamos el parametro reverse = true lo ordena en reversa

#invirte el orden de los elementos de una lista
lista2.reverse()

print(lista2)


print(dir(set('hola')))
