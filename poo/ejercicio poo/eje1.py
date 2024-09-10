class Estudiante :
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")


name = input("ingrese su nombre: ")
age = input("ingrese su edad: ")
grade = input("ingrese su grado: ")

alumno = Estudiante(name, age, grade)

print(f"""
    Datos del Estudiante :\n
    Nombre : {alumno.nombre}
    Edad : {alumno.edad}
    Grado : {alumno.grado}
    """)


while True:
    estudiar = input()
    if(estudiar.lower() == "estudiar"):
        alumno.estudiar()
        break
