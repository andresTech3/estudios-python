#creando un conjunto con set
#? los conjunto solo aceptan datos que no se pueden modificar, por ejemplo podemos agrgar una tupla pero no una lista ni los diccionarios

conjunto_datos = set(["d1", "d2"])


#metiendo un conjunto dentro de otro conjunto
#* frozenset (conjunto congelado) -> crea un conjunto inmutable y puede estar congelado para que sea cachable
conj1 = frozenset(["d1", "d2"])
conj2 = {conj1,"d3"}

print(conj2)

#teoria de conjuntos

conjA = {1,3,5,7}
conjB = {2,4,6}

#* issuperset -> (compara los conjunto) y determinando el subconjunto 
#? puedes utilizar los <= o >= para ser la misma comparaciones que utilizando issubset o issuperset

result = conjB.issubset(conjA) 
result2 = conjA.issubset(conjB)

result3 = conjA.issuperset(conjB)
result4 = conjB.issuperset(conjA)

#verificar si hay algun numero en comun en los conjuntos
#* isdisjoint -> comprueba que los conjunto que se esten comparando no tenga ningun valor igual
result5 = conjB.isdisjoint(conjA)

print(result5)