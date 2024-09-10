#creando una funcion que nos devuelva los numeros primos

def es_primo(num: int):
    for i in range(2,num-1):
        if num % i == 0 :
            return False
        return True
    
def primos_hasta(num):
    num_primos = []
    for i in range(3,num+1):
        result = es_primo(i)
        if result == True : num_primos.append(i)
    return num_primos
            
print(primos_hasta(100))