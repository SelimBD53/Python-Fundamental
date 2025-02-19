# 1: Shape Area Calculator

# class Shape:
#     pi = 3.1416
#     def __init__(self, name, *agrs):
#         self.name = name
#         self.values = agrs
#         # print(self.values)
#     def area(self):
#         if self.name == "Circle":
#             return Shape.pi * self.values[0]**2 
#         elif self.name == "Rectangle":
#             return self.values[0] * self.values[1]
#         elif self.name == "Triangle":
#             return 0.5 * self.values[0] * self.values[1]
        
        
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle", radius)
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__("Rectangle", width, height)
# class Triangle(Shape):
#     def __init__(self, base, height):
#         super().__init__("Triangle", base, height)
    
# circle = Circle(5)
# print(circle.area())
# rectangle = Rectangle(5,10)
# print(rectangle.area())
# tringle = Triangle(5, 6)
# print(tringle.area())

# 2: Employee Management System

# class Employee:
#     def __init__(self, name, employee_ID, salary):
#         self.name = name
#         self.employee_ID = employee_ID
#         self.salary = salary
    
# class Full_Employee(Employee):
#     def __init__(self, name, employee_ID, salary):
#         super().__init__(name, employee_ID, salary)
#     def calculate_salary(self):
#         return self.salary

# class Contract_Employee(Employee):
#     def __init__(self, name, employee_ID, salary, projet_num):
#         super().__init__(name, employee_ID, salary)
        
#         self.project_num = projet_num
#     def calculate_salary(self):
#         return self.salary * self.project_num
    
# e1 = Full_Employee("Alice", 101, 5000)  
# e2 = Contract_Employee("Bob", 102, 2000, 3)  
# print(e1.calculate_salary())
# print(e2.calculate_salary())


# 3: Online Shopping System

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def reduce_stock(self, quentity):
        self.stock -= quentity
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []
    def add_to_cart(self, product, quentity):
        self.cart.append((product, quentity))
        
    def Checkout(self):
        total_cost = 0
        for product, quentity in self.cart:
            total_cost += product.price * quentity
            product.reduce_stock(quentity)
        return f"Total Cost: ${total_cost}"
            
product_1 = Product("Laptop", 1000, 5)
product_2 = Product("Phone", 500, 10)
customer = Customer("Selim")
customer.add_to_cart(product_1, 2)
customer.add_to_cart(product_2, 1)
print(customer.Checkout())
print(product_1.stock)
print(product_2.stock)