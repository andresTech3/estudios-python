#polimorfismo es la variacion de un objeto en diferentes caracteristicas o metodos

# class Gato :
#     def sonido(self):
#         return "Miau"

# class Perro :
#     def sonido(self):
#         return "Wou"
    

# gato = Gato()
# perro = Perro()

# print(perro.sonido())

#$ Duck typing -> un objeto para una operación no se basa en su tipo, sino en si puede realizar esa operación específica.

class Pato:
    def sonido(self):
        return "Cua-cua"

class Persona:
    def sonido(self):
        return "Hola"

def hacer_sonar(objeto):
    return objeto.sonido()

pato = Pato()
persona = Persona()

print(hacer_sonar(pato))  # Output: Cua-cua
print(hacer_sonar(persona))

#$ En Python, el enlace estático se refiere a la resolución de referencias a métodos y variables en tiempo de compilación, mientras que el enlace dinámico se refiere a la resolución en tiempo de ejecución.

#*Ejemplo de enlace estático:

class A:
    def foo(self):
        return "Método foo de la clase A"

class B(A):
    def foo(self):
        return "Método foo de la clase B"

obj = B()
print(obj.foo())  # Salida: "Método foo de la clase B"

#*Ejemplo de enlace dinámico:

class A:
    def foo(self):
        return "Método foo de la clase A"

class B(A):
    def foo(self):
        return "Método foo de la clase B"

def llama_foo(obj):
    return obj.foo()

obj = B()
print(llama_foo(obj))  # Salida: "Método foo de la clase B"

#$ En Python, el "tipo real" se refiere al tipo de objeto al que pertenece una variable en tiempo de ejecución, mientras que el "tipo declarado" se refiere al tipo que se especifica al declarar la variable en el código.

class A:
    pass

class B(A):
    pass

obj_real = B()
obj_declarado = A()

print(type(obj_real))  # Tipo real: <class '__main__.B'>
print(type(obj_declarado))  # Tipo declarado: <class '__main__.A'>