cad1 = "hola soy andres 5"
cad2 = "bienvenidos"
cad3 = "78542"
cad4 = "hugo, marcos, lorena, sofia"

resultado = cad4.split(',')

dir(cad1) # devuelve la lista de atributos valido del objeto pasado
cad1.upper() #devuleve el texto en mayuscula
cad1.lower() #devuelve el texto pero en minuscula
cad1.capitalize() #devuelve la pimera letra en mayuscula
cad1.find('hola') # ver si en la cadena te texto encontramos los caracteres que le pasemos y me pasa la posicion que lo encuentre y si no encuentra me devuelve -1
cad1.index("andres") #buscamos una cadena dentro de un palabra o frase lo mismo que find a difrencia que no me devuelve -1 si no me lo encuentra una exepcion
cad2.isnumeric() # si es numerico devuelve true y si no false
cad3.isalpha() # si es alphanumerico osea qlos caracteres que van desde la a -> z
cad2.count("n") # busca la cantidad de veses que coincidad segun la cadena que le indicamos
len(cad1) # devuelve la cantidad de caracteres de una cadena
cad1.startswith("a") # verificamos si una cadena empieza con otra cadena dada si es asi retorna true
cad1.endswith("a") # verificamos si una cadena termina con la otra cadena dada si es asi retorna true
cad1.replace("hola", "hi") # remplaza una cadena indicada por otra cadena
cad4.split(",") # nos va a convertir la cadena en una lista y los valores se van separando segun el caracter indicado

print(resultado)