import time
class School:
    # Constructor
    def __init__(self, name, address, principle = ''):
        self.name = name
        self.address = address
        self.principle = principle
        self.gread = []
    
    def add_gread(self, name, teacher):
        new_gread = Gread(name, teacher) 
        self.gread.append(new_gread)
    
# Specificaly delete korar kotha bola decchi.
    def remove_grade(self, name):
        idx = 0
        for i, grade in enumerate(self.gread):
            if grade.name == name:
                idx = i
        del self.gread[idx]        
    def __str__(self):
        return f"{self.name} => {self.principle}"  
    
    
class Gread:
    # Constructor
    def __init__(self, name, teacher):
        self.name = name
        self.students = []
        self.teacher = teacher
        
    def __repr__(self):
        return f"{self.name} == {self.teacher}"
    
# Automatically Delete hoya jaba programm run ses hola.
    def __del__(self):
        print(f"Deleting {self.name} with teacher {self.teacher}")
    
oxford = School("Grren View", "Mirpur", "Selim Reza")
oxford.add_gread("class 23", "Asad")
oxford.add_gread("Class 12", "Razib Sir")
oxford.add_gread("class 4", "Sefat")
  
# print(str(oxford))
print(oxford.gread)
oxford.remove_grade("Class 4")
print("=================")
print(oxford.gread)
print("My code is Done")         # memory thaka auto gurbage collection delete or clean kora deba.
time.sleep(5)