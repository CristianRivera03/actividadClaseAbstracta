from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad, telefono, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.ocupacion = ocupacion
    
    @abstractmethod
    def impresion(self):
        pass
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, telefono, ocupacion, codigo):
        super().__init__(nombre, edad, telefono, ocupacion)
        self.codigo = codigo
        
    def impresion(self):
        return f'''
                    ********************************
                    Ficha Personal
                    Nombre: {self.nombre}
                    Edad: {self.edad}
                    Telefono: {self.telefono}
                    Ocupacion: {self.ocupacion}
                    Codigo: {self.codigo} 
                    ********************************\n'''
                    

class Trabajador(Persona):
    def __init__(self, nombre, edad, telefono, ocupacion, codigo):
        super().__init__(nombre, edad, telefono, ocupacion)
        self.codigo = codigo

    def impresion(self):
        return f'''
                    ********************************
                    Ficha Personal
                    Nombre: {self.nombre}
                    Edad: {self.edad}
                    Telefono: {self.telefono}
                    Ocupacion: {self.ocupacion}
                    Codigo: {self.codigo} 
                    ********************************\n'''
                    

class Nini (Persona):
    def __init__(self, nombre, edad, telefono, ocupacion, codigo):
        super().__init__(nombre, edad, telefono, ocupacion)
        self.codigo = codigo

    def impresion(self):
        return f'''
                    ********************************
                    Ficha Personal
                    Nombre: {self.nombre}
                    Edad: {self.edad}
                    Telefono: {self.telefono}
                    Ocupacion: {self.ocupacion}
                    Codigo: {self.codigo}
                    ********************************\n'''
                    
student = Estudiante('Cristian Rivera' , 19 , 76165646, 'Estudiante' , 'u20220435')
print(student.impresion())
        
worker = Trabajador('Alexander Romero', 19, 76165646, 'Encargado de venta', '21212828')
print(worker.impresion())

nada = Nini('Cris', 19, 76165646, None, None)
print(nada.impresion())
