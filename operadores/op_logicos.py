#AND -> los 2 valores deben ser verdaderos

result = True & True # devuele True
result2 = True & False # devuele false

#OR -> que alguno de los 2 valores sea falso  o verdadero

result3 = True & True # devuele True
result4 = False & True # devuele True
result5 = False & False # devuele False


#NOT -> cambia el valor contrario del resultado

result6 = not True # devuele False
result7 = not False # devuele True


print(result)
type(result)