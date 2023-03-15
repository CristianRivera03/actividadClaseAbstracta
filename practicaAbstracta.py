from abc import ABC, abstractmethod

class Figura(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
#Creando clases dependientes de figura

class Cuadrado(Figura):
    def __init__ (self, lado):
        self.lado = lado
        
    def area(self):
        return self.lado * self.lado 
    
    def perimetro(self):
        return self.lado * 4

class Circulo(Figura):
    def __init__(self, radio):
        self.radio =  radio
        
    def area(self):
        return 3.1416 * self.radio * self.radio
    
    def perimetro(self):
        return 2*3.1416 * self.radio
    
#Creando clases del las clases hijas de la clase abstracta 

square = Cuadrado(5)
print('El area es: ', square.area())
print('El perimetro es: ' , square.perimetro())

circle = Circulo(2)
print('El area es: ' ,circle.area())
print("El perimetro es: ",circle.perimetro())