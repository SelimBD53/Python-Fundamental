# class Item:
#     def __init__(self, itemName, itemPrice):
#         assert itemPrice >= 0, f"Error line 3, {itemPrice} is invalid"
#         self.itemName = itemName
#         self.itemPrice = itemPrice
    
    
# item = Item("Plate", 0)
# print(item.itemName, item.itemPrice)

class Person:
    def __init__(self, name, phone, age):
        assert age > 13, f"Only greater than 18 is accepted"
        assert len(phone) == 11, f"Invalid Phone Number"
        self.name = name
        self.phone = phone
        self.age = age
    def __repr__(self):
        return f"{self.name} {self.phone} {self.age}"
    
user = Person("Selim Reza", "01798563479", 15)
print(user)