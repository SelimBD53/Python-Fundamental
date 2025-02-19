# Laptop, phone, watch,tablet,
# Base class will have only the common attributes and method
class Device:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
    def re_sale(self):
        print("Ready to sell again")
class Laptop(Device):
    def __init__(self, brand, color, price, disk_size):
        super().__init__(brand, color, price)
        self.disk_size = disk_size
    
    def run(self):
        return "Laptop Open and Runing"
    
    def purchase(self, money):
        if money < self.price:
            return "No Laptop Puchase you"
        else:
            print("Yes Perchase You Laptop")
            return money - self.price
    def __repr__(self):
        return f'Laptop: {self.brand} : {self.price} : {self.color} : {self.disk_size}'

lenavo = Laptop("Lanaveo", "Rad", 20000, "500gb")
# print(lenavo)
# lenavo.re_sale()