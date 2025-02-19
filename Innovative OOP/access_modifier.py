# Access Modifier
# _protected, __private, publice

# Private access modifier.
class Car:
    def __init__(self):
        pass
    def drive(self):
        print("driving car")
    def __updatesoftware(self):
        print("Updating Software.")
        
# redcar = Car()
# redcar.drive()
# redcar._updatesoftware()      # not accessable from object.


# Protected access modifier

class Truck(Car):
    def __init__(self):
        pass
    def drive(self):
        print("driving Truck")



# truck = Truck()
# truck.drive()
# truck._updatesoftware()


class Deleta:
    def __init__(self):
        self.__sigma = "hidden"

    
obj = Deleta()
print(obj._Deleta__sigma)

obj.__sigma = "Since"    # [ai ta new variable create hoyacha.]
print(obj.__sigma)



# class Deleta:
#     def __init__(self):
#         self.__sigma = "hidden"

# class Gamma(Deleta):
#     def reveal(self):
#         return self.__sigma   
# obj = Gamma()
# print(obj._Deleta__sigma)





# Home Work
# class Student:
#     def __init__(sef):
#         pass
#     @classmethod
#     def __class_method(cls):    # self used korlaoue kaj kora kno ?
#         print("hello selim")   

# st = Student()
# st._Student__class_method()