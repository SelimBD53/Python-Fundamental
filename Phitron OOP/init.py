class Phone:
    manufacturer = "Chain"    # Class Attributs
    def __init__(self, brand, price, color):    # Auto call Constractor.
        self.brand = brand      # instance attribute / variable
        self.price = price
        self.color = color
        
    def send_sms(self):
        print("dong dong dong.")
        
my_phone = Phone("oppo", 28000, "Pink")  # object ka bola hoccha instance. 
my_phone.send_sms()
print(my_phone.price)

her_phone = Phone("Samsung", 25000, "black")

print(her_phone.price, my_phone.manufacturer)

dad_phone = Phone("Vivo", 30000, "White")
dad_phone.send_sms()
print(my_phone.price, her_phone.price, dad_phone.price)