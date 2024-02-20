from abc import ABC, abstractclassmethod #This is the way for make a class to a abstrarct class

class Person(ABC): # Create a New Class
    @abstractclassmethod
    def __init__(self,name,age,gender,activity): # use function initializes a objtect and assign the values
        self.name = name # value inside of the name value in name initialize
        self.age = age 
        self.gender = gender
        self.activity = activity 
        
    @abstractclassmethod #uses as create a abstract class and uses after
    def activity(self):
        pass
    
    def introduce(self):
        print(f"Hi, my name is {self.name} and also i'm {self.age} years old")
        
class Student(Person):
    def __init__(self,name,age,gender,activity):
        super().__init__(name,age,gender,activity) # Super uses for the herency variables in another class
    
    def activity(self): 
        print(f"I am {self.activity}")  

class Worker(Person):
    def __init__(self,name,age,gender,activity):
        super().__init__(name,age,gender,activity)
    
    def activity(self):
        print(f"Im working at: {self.activity}")


enmanuel = Student("Raul", 60, "Men", "Enginner") #create a object Enmanuel with the class student also this have the person class and assing the values
juan = Worker("juancito", 21, "Men", "developer") # Create a object Juan with the class Worker also this have the person class and assing the values

enmanuel.introduce() # Use the object with the class Person introduce function 
enmanuel.activity()# Use the object with the class Student with activity funcion
print()
juan.introduce() # Use the object with the class Worker with introduce funcion
juan.activity() # Use the object with the class Worker with activity funcion
