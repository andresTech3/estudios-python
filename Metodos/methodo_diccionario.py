diccionario = {
    "name": "andres",
    "last_name": "narvaez",
    "email": "andres@gmail.com",
    "subs" : 350
}

# Devuelve la cantidad de elementos (pares clave-valor) en el diccionario. 
print(len(diccionario))

#Devuelve el valor asociado a la clave especificada. Si la clave no existe, se generará un error
print(diccionario["email"])

#Devuelve el valor asociado a la clave especificada. Si la clave no existe, en lugar de generar un error, devuelve el valor predeterminado especificado. 
print(diccionario.get('name'))

# Devuelve una lista con todas las claves del diccionario. 
clave = diccionario.keys()
print(clave)

#Devuelve una lista con todos los valores del diccionario.
print(diccionario.values())

#Devuelve una lista de tuplas, donde cada tupla contiene un par clave-valor del diccionario. 
tupla = diccionario.items()
print(tupla)

#Elimina el par clave-valor asociado a la clave especificada y devuelve el valor eliminado. Si la clave no existe, se generará un error. 

diccionario.pop("subs")
print(diccionario)

#eliminar todo el diccionario
diccionario.clear()
print(diccionario)

#Elimina y devuelve un par clave-valor arbitrario del diccionario como una tupla. Si el diccionario está vacío, se generará un error. 
tupla2 = diccionario.popitem()
print(diccionario)
print(tupla2)