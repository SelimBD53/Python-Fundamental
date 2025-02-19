# # Single Inheritance
# class Parents:
#     def __init__(self):
#         print("Parents Class Constructor")
    
#     def parents_methos(self):
#         print("Parents Method")
        
# class Child(Parents):
#     def __init__(self):
#         print("child Class Constructor")
    
#     def child_methos(self):
#         print("Child Method")
  
# child = Child()
# child.child_methos()
# child.parents_methos()

# Parent = Parents()
# Parent.parents_methos()    
# Parent.child_methos()       # AttributeError: 'Parents' object has no attribute 'child_methos'


# Multiple Inheritance        : basi used hoy Bank a. 
# class Flyable:
#     def fly(self):
#         print("Flying")
        
# class Swimmable:
#     def swim(self):
#         print("Swimming")

# class Duck(Flyable, Swimmable):
#     pass

# duck = Duck()
# duck.fly()
# duck.swim()

# Multilevel Inheritance 
# class Animal:
#     def eat(self):
#         print("Eating")
        
# class Dog(Animal):
#     def bark(self):
#         print("Barking")
        
# class BabyDog(Dog):
#     def weep(self):
#         print("weeping")
    
# bay_dog = BabyDog()
# bay_dog.weep()
# bay_dog.bark()
# bay_dog.eat()

# dog = Dog()
# dog.eat()



# Hierachical Inheritance
# class Animal:
#     def eat(self):
#         print("Eating")
        
# class Dog(Animal):
#     def bark(self):
#         print("Barking")
        
# class Cat(Animal):
#     def meow(self):
#         print("Meowing")
    
    
# dog = Dog()
# dog.eat()
# dog.bark()

# cat = Cat()
# cat.eat()
# cat.meow()



# Hybrid Inheritance
# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def Bark(self):
#         print("Barking")

# class germanShepherd(Dog, Animal):
#     def color(self):
#         print("Black")
        
# obj_1 = germanShepherd()
# obj_1.eat()
# obj_1.Bark()

# dog = Dog()
# dog.eat()


# Super Method
# class Cat:
#     def __init__(self):
#         print("Cat Class Constructor")
    
#     def sound(self):
#         print("Meow")
  
# class Tiger(Cat):
#     def __init__(self):
#         print("Tiger Class Constructor")
    
#     def sound(self):
#         # Cat.sound(self)        # sound ka chnaiya deta hoccha self mana current object a pass hocche.
#         super().sound()      # it self baki sob kishu ka handel kora fala.
#         print("Roar")
         
# tiger = Tiger()
# tiger.sound()

# Supwr Method Pratice 
# class Parent:
#     def __init__(self, name):
#         print("Parent Class Constructor")
#         self.parent_name = name

    
# class Child(Parent):
#     def __init__(self, parent_name, name, age):
#         print("child Class Constructor")
#         super().__init__(parent_name)
#         self.name = name
#         self.age = age

        
#     def display(self):
#         print("Parent Name:", self.parent_name)
#         print("Name: ", self.name)
#         print("Age: ", self.age)


# child = Child("Parent", "Child", 25)     # Super method ta kono kishu ka override korta help korcha.
# child.display()

# class Parent:
#     def display(self, child):
#         print("Parent Name:", child.parent_name)
#         print("Age: ", child.age)
#         print("Name: ", child.name)
    
# class Child(Parent):
#     def __init__(self, parent_name, name, age):
#         print("Child class Constructor")
#         self.parent_name = "Selim"
#         self.name = name 
#         self.age = age
#         super().display(self)
        
# child = Child("parent", "child", 20)
# child.display()


# Composition = Has a Relation
# class Engine:
#     def __init__(self):
#         print("Engine Class Constructor")
    
#     def start(self):
#         print("Engine Started")

# class Car:

#     def __init__(self, engine):      # used composition
#         print("Car Class Constructor")
#         self.engine = engine

#     def drive(self):
#         self.engine.start()         # used composition
#         print("Driving Start")
        
# engine = Engine()
# car = Car(engine)           # used composition
# print("============")
# car.drive()
    
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         print("Book Class")
    
#     def display(self):
#         print(self.title)
#         print(self.author)

# class Library(Book):
#     def __init__(self, name, title, author):
#         super().__init__(title, author)
#         self.name = name
#         self.books = [self]
    
#     def display(self):
#         if self.books:
#             for book in self.books:
#                 print(book.title)
#                 print(book.author)
               
#         else:
#             print("No Book Available")
#         super().display()
    
#     def add_book(self, book):
#         self.books.append(book)
        
# library = Library("Rokomary", "Guido van Rossum", "O'Reilly")
# library.display()

# print("********************************")

# book1 = Book("Python", "Selim Reza")
# library.add_book(book1)
# library.display()




class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def display(self):
        print(self.title)
        print(self.author)
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def display(self, book):
        if self.books:
            book.display()
        else:
            print("No Book Available")
    def add_book(self, book):
        self.books.append(book)
lib = Library("Rokomary")
book1 = Book("Python", "Selim Reza")
lib.add_book(book1)
book2 = Book("Java", "Sefat")
lib.add_book(book2)   
lib.display(book1)   