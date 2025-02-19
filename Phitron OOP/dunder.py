# dunder Method
# Magic Method
# Special Method


class Person:
    def __init__(self, name, age, money, hight=55):
        self.name = name
        self.age = age
        self.money = money
        self.hight = hight
    def __call__(self):
        print(f"hello {self.money} ")
    
    def __len__(self):
        return self.hight
    
    
    def __eq__(self, value):
        return self.age == value.age
    def __add__(self, other):
        return (self.money + other.money)
    
alim = Person("Alim Ali", 22, 560)
dalim = Person("Dalim Ali", 25, 660)
print(alim + dalim)
print(alim == dalim)
alim()
print(len(alim))