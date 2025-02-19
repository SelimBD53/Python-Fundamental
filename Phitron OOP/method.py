class Phone:
    brand = "Samsung"
    feature = ["Camrea", "Phone Calling", "Reciving Phone"]
    
    def call(self):        # methdo declare system
        print("ring ring ring")
    
    def send_sms(self, number, txt_msg):
        sms = f"Hello My Number is: {number} and I say: {txt_msg}"
        return sms
    
# my_phn = Phone()
# print(my_phn.feature)
# my_phn.call()     # method call system
# sms = my_phn.send_sms("01798653246", "Hello I am Selim.")
# print(sms)


class Calculator:
    brand = "Casino"
    def add(self, a, b):
        return a+b
    def Subtract(self, a, b):
        return a-b
    def Multiply(self, a, b):
        mul = a*b
        return mul
    def divition(self, a, b):
        print(a//b)
    
my_calculator = Calculator()
print(my_calculator.add(10, 20))
print(my_calculator.Subtract(10, 20))
print(my_calculator.Multiply(10, 20))
my_calculator.divition(10, 20)
print(my_calculator.brand)


