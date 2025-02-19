class Shope:
    cart = []
    def __init__(self,byer):
        self.byer = byer
        
    def add_to_cart(self, item):
        self.cart.append(item)

Shopper_1 = Shope("Selim")
Shopper_1.add_to_cart("t-sirt")
print(Shopper_1.cart)

Shopper_2 = Shope("Alim")
Shopper_2.add_to_cart("Pant")
print(Shopper_2.cart)
