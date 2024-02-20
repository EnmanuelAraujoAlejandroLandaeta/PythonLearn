from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,name,age,gender,activity):
        self.name = name
        self.age = age
        self.gender = gender
        self.activity = activity 
        
    @abstractclassmethod
    def actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, Me llamo {self.name} y tengo {self.age} años")
        
        
class Estudiante(Persona):
    def __init__(self,name,age,gender,activity):
        super().__init__(name,age,gender,activity)
    
    def actividad(self):
        print(f"Estoy Estudiando: {self.activity}")


class Trabajador(Persona):
    def __init__(self,name,age,gender,activity):
        super().__init__(name,age,gender,activity)
    
    def actividad(self):
        print(f"Estoy trabajandor en el rubro de: {self.activity}")


enmanuel = Trabajador("Raul", 60, "Men", "Enginner")
juan = Estudiante("juancito", 21, "Men", "developer")

enmanuel.presentarse()
enmanuel.actividad()
print()
juan.presentarse()
juan.actividad()