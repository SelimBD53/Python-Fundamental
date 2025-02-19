# Method OverLoading
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def get_id(self, id=None):       # [Method OverLoading]
#         return f"{self.name} {self.age} {id}"

# obj_1 = Student("Alish", 25)
# print(obj_1.get_id())
# obj_2 = Student("Bob", 33)
# print(obj_2.get_id(2))
# print(type(obj_1))
# print(type(Student))
# print(obj_1 + obj_2)

# num1 = 10
# num2 = 20
# print(num1 + num2)
# print(num1.__add__(num2))


# operator overloading

# + __add__
# - __sub__
# * __mul__
# / __truediv__
# // __floordiv__
# % __mod__
# ** __pow__
# == __eq__
# != __ne__
# > __gt__
# < __lt__

# ai overloading ta buji nai.
class ComplexNubmer:
    def __init__(self, real, img):
        self.real = real  # 2,3
        self.img = img    # 4,5
    def __add__(self, other):
        return (self.real + other.real, self.img + other.img)  # ai ta buji nai.
    
    def __str__(self):
        return f"{self.real} + {self.img}i"

number = ComplexNubmer(2,4)
print(number)
number2 = ComplexNubmer(3,5)
print(number2)
print(number + number2)


# Constractor overloading 
# class ComplexNubmer:
#     def __init__(self, real=None, img=None):    # [Constractor Overloading]
#         self.real = real  # 2,3
#         self.img = img    # 4,5
#     def __add__(self, other):
#         return ComplexNubmer(self.real + other.real, self.img + other.img)  
    
#     def __str__(self):
#         return f"{self.real} + {self.img}i"

# number = ComplexNubmer(2,4)
# print(number)
# number2 = ComplexNubmer(3,5)
# print(number2)
# print(number + number2)

