# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def say_hello(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old")
        
# obj_1 = Human("Selim", 25)
# print(obj_1.name)
# obj_1.say_hello()
# obj_2 = Human("Bob", 33)
# print(obj_2.name)
# obj_2.say_hello()

# class Building:
#     total_area_count = 0
#     def __init__(self,name):
#         self.name = name
#         self.count = 0
#         self.family = []
    
#     def add_family(self, family):
#         self.family.append(family)
#         Building.total_area_count+=1
#         self.count +=1
#         print(f"{self.family} has been added to {self.name}")
        
#     def count_family(self):
#         print(f"{self.name} has {self.count} families")
#     def area_count_fimaly(self):
#         print(f"{Building.total_area_count} has been still fimaly.")

# building_1 = Building("Building 1")
# building_1.add_family("Selim")
# building_1.add_family("Sefat")
# building_1.count_family()
# print(building_1.__dict__)    
# building_1.area_count_fimaly()    


# building_2 = Building("Building 2")
# building_2.add_family("Alish")
# building_2.add_family("Bob")
# building_2.count_family()
# print(building_2.__dict__)  
# building_1.area_count_fimaly()  
# print(Building.total_area_count)   
# print(building_1.total_area_count)
# print(building_2.total_area_count)

# Instance Method
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def say_hello(self):   # Instance Method.
#         print(f"Name: {self.name} age: {self.age}")

# obj_1 = Student("Selim", 22)
# obj_1.say_hello()


# Class Method
# class Student:
#     dept = "CSE"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def say_hello(self):   # Instance Method.
#         print(f"Name: {self.name} age: {self.age}")

#     @classmethod                           # class Method
#     def class_method(cls, instance=None):
#         if instance:
#             print(instance.name)
#         print(f"Hello: {cls.dept}")

# Student.class_method()  # [cls naye Class [Student class ] ka]
# obj_1 = Student("Selim", 22)   # [self naye obj_1 ka]
# # obj_1.say_hello()               # [instance method call]
# obj_1.class_method(obj_1)       # [class method call]




# Static Method
class Student:
    dept = "CSE"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):   # Instance Method.
        print(f"Name: {self.name} age: {self.age}")
    @classmethod                  # Class Method
    def class_method(cls, instance=None):
        if instance:
            print(instance.name)
        print(f"Hello: {cls.dept}")
        
    @staticmethod
    def static_method():
        print("This is Static Method.")
    @staticmethod
    def sum_two(a,b):
        print(a+b)
Student.class_method()  # [cls naye Class [Student class ] ka]
obj_1 = Student("Selim", 22)   # [self naye obj_1 ka]
obj_1.say_hello()           # [instance method call]
obj_1.class_method(obj_1)  # [class method call]
Student.static_method()     # Static Method call
Student.sum_two(5,2)