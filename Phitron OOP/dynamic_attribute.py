class Item:
    all = []
    def __init__(self, ItemName, ItemPrice):
        self.__ItemName = ItemName
        self.ItemPrice = ItemPrice
        self.all.append(self)
        
    def __repr__(self):
        return f"Item({self.ItemName}, {self.ItemPrice})"
        
Item1 = Item("Bowle", 150)
Item2 = Item("Plate", 200)
Item1._Item__ItemName = "Bowl Broken"
Item1._Item__DISCOUNT = "60%"
print(Item1.__dict__)



















# Item1.discount = 60
# Item2.offer = "65%"
# print(Item.all)
# print(Item1.__dict__)
# print(Item2.__dict__)
# Item.all.append(Item1)
# print(Item1.all)
# print(Item2.all)