#* metodo de resolucion de orden -> el orden en que python busca los metodos y atributo entre las clases cuando hay herencia multiples


class A:
    def hablar(self):
        print("hola desde A")

class B(A):
    def hablar(self):
        print("hola desde B")

class C(A):
    def hablar(self):
        print("hola desde C")

class D(B,C):
    pass

# print(D.mro()) podemos saber como esta el orden de gerarquia de las clases

d = D()
B.hablar(d) # de esta forma puedo haceder a los metodos de una clase superior segun el orden gerarquico