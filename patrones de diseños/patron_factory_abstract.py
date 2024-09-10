from abc import ABC, abstractmethod, abstractclassmethod

# El patrón de diseño Factory Abstract (Fábrica Abstracta) es un patrón creacional que permite la creación de familias de objetos relacionados sin especificar sus clases concretas. Este patrón utiliza una interfaz común para crear diferentes tipos de objetos, donde cada fábrica derivada puede producir objetos de diferentes tipos pero con temas o propósitos comunes.

#$ una fabrica que permite crear otras fabricas


# class AbstractFactory(ABC):
#     @abstractmethod
#     def create_product_a(self):
#         pass

#     @abstractmethod
#     def create_product_b(self):
#         pass

# class ConcreteFactory1(AbstractFactory):
#     def create_product_a(self):
#         return ProductA1()

#     def create_product_b(self):
#         return ProductB1()

# class ConcreteFactory2(AbstractFactory):
#     def create_product_a(self):
#         return ProductA2()

#     def create_product_b(self):
#         return ProductB2()

# class AbstractProductA(ABC):
#     @abstractmethod
#     def useful_function_a(self):
#         pass

# class ProductA1(AbstractProductA):
#     def useful_function_a(self):
#         return "The result of the product A1."

# class ProductA2(AbstractProductA):
#     def useful_function_a(self):
#         return "The result of the product A2."

# class AbstractProductB(ABC):
#     @abstractmethod
#     def useful_function_b(self):
#         pass

# class ProductB1(AbstractProductB):
#     def useful_function_b(self):
#         return "The result of the product B1."

# class ProductB2(AbstractProductB):
#     def useful_function_b(self):
#         return "The result of the product B2."

# def client_code(factory: AbstractFactory):
#     product_a = factory.create_product_a()
#     product_b = factory.create_product_b()
#     print(product_a.useful_function_a())
#     print(product_b.useful_function_b())

# # Ejemplo de uso
# factory1 = ConcreteFactory1()
# client_code(factory1)

# factory2 = ConcreteFactory2()
# client_code(factory2)


@abstractclassmethod
class IconexionRest(ABC):
    @abstractmethod
    def readUrl(self):
        pass    