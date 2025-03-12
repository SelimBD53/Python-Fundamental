import json

class Item:
    all = []
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.all.append(self)
    @staticmethod
    def inicilizer():
        with open("extract.txt", 'r') as file:
            data = file.read()
            js = json.loads(data)
        for item in js:
            Item(
                name = item["name"],
                price = item["price"]
            )
    def __repr__(self):
        return f"Item:({self.name}, {self.price})"
Item.inicilizer()  
print(Item.all)