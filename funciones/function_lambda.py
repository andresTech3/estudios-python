# funcion lambda -> es como una funcion flecha en javascript
#?lambda crea funciones anonimas
"""
- lo podemos usar cuando queremos hacer algo sencillo y rapido 
- retorna automaticamente
"""
#*creacion de la funcion lambda
nombre = lambda x: x*2

##########################################################################

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

"""#* creando una funcion que diga si el numero es par o no
def es_par(num):
    if(num%2 == 1):
        return True

#* usando filter para una funcion comun
numerosPares = filter(es_par,numeros)
print(list(numerosPares))

"""

#* creando lo mismo que antes pero con lambda

numeros_pares_lambda = filter(lambda num:num % 2 == 0, numeros)
print(list(numeros_pares_lambda))









