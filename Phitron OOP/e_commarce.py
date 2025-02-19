class Shopper:
    def __init__(self, name):
        self.name = name
        self.card = []
        
    def add_to_cart(self, item, price, quantity):
        self.card.append({"item": item, "price": price, "quantity": quantity})
        
    def checkout(self, amount):
        price = 0
        for item in self.card:
            price += item["price"] * item["quantity"]
        if amount < price:
            return f"Here are the more money Please: {price - amount}"
        elif amount > price:
            return f" Here are the items and Back to the Money is: {amount - price}"
        else:
            return f"Here are the items.Thank You"
            
            
shopping = Shopper("Showpno")
shopping.add_to_cart("shirt", 700, 4)
shopping.add_to_cart("shows", 1000, 2)
shopping.add_to_cart("pant", 1400, 4)
reply = shopping.checkout(10400)
print(reply)