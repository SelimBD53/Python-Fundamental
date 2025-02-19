class Laptop:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def incress_age(self, age=1):
        self.last_age = self.age
        self.age = self.age + age
    def repair(self, life_incress= -5):
        self.incress_age(life_incress)

my_laptop = Laptop("HP", 5)
my_laptop.incress_age()
my_laptop.incress_age()
# my_laptop.incress_age()
# my_laptop.incress_age()
# my_laptop.age = 17
print(my_laptop.last_age,"->", my_laptop.age)

my_laptop.repair()
print(my_laptop.age)