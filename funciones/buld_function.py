import random
# para decir que vamos acrear una funcion se utiliza def


def saludar(nombre):
    print(f'hola {nombre} como estas? ')
    

saludar('raul')

#funciones con mas parametros y parametros opcional

def presentation(sexo, nombre="andres"):
    sexo = sexo.lower() #? convierte texto en minuscula
    if(sexo == 'mujer'):
        abjetivo = 'Reina'
    elif(sexo == 'hombre'):
        abjetivo = 'Titan'
    else:
        abjetivo = 'crack'
    
    print(f'hola {nombre} , mi {abjetivo} como andas?')
    

presentation('hombre')
presentation('mujer', 'maria')




#funciones que retorna valores
def createPasswordRandom(num):
    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    num_entero = str(num)
    numInt = int(num_entero[0])
    c1 = numInt- 2
    c2 = numInt
    c3 = numInt- 5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{numInt *2}"
    print(password)
    



def createPasswordRandomOrigin(numCont):
    chars = "abcdefghijklmnopqrstuvwxyz1234567890$#"
    createpass = ""
    cont = 0
    while(cont < numCont):
        numberRandom = random.randint(0,len(chars))
        char = chars[numberRandom]
        createpass += char
        cont += 1
    return (createpass,numCont) #? podemos retonar varios valores


password,oneNumeric = createPasswordRandomOrigin(5)
print(f'tu contraseña es : {password}')
print(f'el numero que utilizaste es : {oneNumeric}')




