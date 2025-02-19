# ai khana polimorphism sound method ka override kora child class a nijar moto implement korcha.
class Animal:
    def __init__(self):
        pass
    def sound(self):
        print("I am Animal")
class Dog(Animal):
    def sound(self):
        print("I am Dog")
class Cat(Animal):
    def sound(self):
        print("I am Cat")
    
obj1 = Dog()
obj1.sound()
obj2 = Cat()

obj2.sound()