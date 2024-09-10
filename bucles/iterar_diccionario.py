diccionario = {
    "nombre": "andres",
    "apellido" : "narvaez",
    "subs" : 1000000
}

#opteniendo solo las claves
for key in diccionario:
    print(key)

#opteniendo las claves y valor
#? items() -> nos sirve para iterar todo el diccionario en key:value y poder haceder a sus datos
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"{key} : {value}")