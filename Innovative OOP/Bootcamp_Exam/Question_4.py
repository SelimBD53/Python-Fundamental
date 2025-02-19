from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def introduce(self):
        print( "I am a person.")

class Student(Person):
    def introduce(self):
        print("I am a student.")
        
student1 = Student()
student1.introduce()

