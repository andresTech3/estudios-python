#utilizando el parametro args -> ase que todos los parametro que pasemos solo sea uno 

def suma(*num):
    result = sum(num)
    return result

print(suma(10,5))