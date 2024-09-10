class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} : (fuerza {self.fuerza} velocidad {self.velocidad})"
    
    def __add__(self, otro_pj):
        newName = f"{self.nombre} - {otro_pj.nombre}"
        newFuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.5)
        newVelocidad = round(((self.fuerza + otro_pj.fuerza)/2)**1.5)
        return Personaje(newName, newFuerza, newVelocidad)


personajes = []

def mostrarPersonaje(personajes):
    if not personajes:
        print("aun no hay personajes creados")
    else:
        print("personajes disponibles: ")
        for i,personaje in enumerate(personajes):
            print(f"{i + 1}. {personaje}")

def crearPersonaje():
    name = input("cual es el nombre de tu personaje")
    fuerza = int(input("indica la fuerza de tu persoanje"))
    velocidad = int(input("indica la velocidad de tu persoanje"))
    return Personaje(name,fuerza,velocidad)
    

while True:
    print("\n1. crea un personaje")
    print("\n2. fusionar personaje")
    print("\n3. mostrar personajes")
    print("\n4. salir")
    option = input("elige una opcion")

    if(option == "1"):
        crearPersonaje()
        print("personaje creado con exito")
    elif(option == "2"):
        if(len(personajes) < 2):
            print("debe tener almenos 2 personaje para fusionar")
        else:
            mostrarPersonaje(personajes)
            num_pj1 = int(input("ingrese el numero del primer personaje"))
            num_pj2 = int(input("ingrese el numero del segundo personaje"))

            if (1 <= num_pj1 <= len(personajes) and 1 <=num_pj2 <= len(personajes) and num_pj1 != num_pj2) :
                personaje1 = personajes[num_pj1 - 1]
                personaje2 = personajes[num_pj2 - 1]
                personaje_fusionados = personaje1 + personaje2
                personajes.append(personaje_fusionados)



    


