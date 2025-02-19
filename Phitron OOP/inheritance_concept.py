# Multi-LEVEL inheritance  (grandpa --> parent --> child)
# class Vechile:
#     def __init__(self, name, licence, price, color):
#         self.name = name
#         self.licence = licence
#         self.price = price
#         self.color = color
#         print("Vechile init call.")
        
# class Bus(Vechile):
#     def __init__(self, name, licence, price, color):
#         super().__init__(name, licence, price, color)
#         self.color = color
#         print("Bus init call.")
        
# class Mini(Bus):
#     def __init__(self):
#         super().__init__("selim", "DH123", 12000, "Red")
#         print("Mini bus Call")
        
# mini = Mini()
# print(mini.name)

    
# MultiPle inheritance   (father, mother: child --> (father, mother))

class School:
    def __init__(self, school_name):
        self.school_name = school_name
        print("School init Called")
        
class Gread:
    def __init__(self, gread_name):
        self.gread_name = gread_name
        print("Gread init Called")
        
class Student(School, Gread):
    def __init__(self, name, gread_name, school_name):
        self.name = name
        School.__init__(self, school_name)
        Gread.__init__(self, gread_name)
        print("Student init Called")
        
# mimi = Student("Selim", "A+", "Green View")
# print("========")
# print(mimi.name)
  
# Hierarchical Inheritance (father: father --> you, father --> brother, father --> sister)
# Hybrid Inheritance
# DRY == Do Not Repeat Yourself.
      