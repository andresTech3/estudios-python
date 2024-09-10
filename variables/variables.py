#variables
a = 2
b = 3
c = a + b

#redefiniendo variables
nombre = "andres" 
nombre = "felipe"
print(c)
print(nombre)

numero = 10
numero += 5
numero -= 5
print(numero)

#concatenar 

nombre = "andres"
bienvenido = "hola " + nombre + " ¿como estas?"
#la f adelante combierte lso datos en texto 
welcome = f"hola {nombre} ¿como estas?" 
del welcome #del es un operador para borrar datos en la memoria
print(welcome)

# son sencible a mayuscula o minuscula
hola = " hola como has estado"
print("hola" in hola) # in me busca una palabra en una frace y si esta me dice true y si no false
print ("hola" not in hola) # not in me dice si la palabra no esta si no es true pero si esta es false
