# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self, balance):
#         if balance < 0:
#             print("Nagetive Balance No add")
#         else:
#             self.__balance += balance
#     def __display_pin(self):
#         print("Pin is 1234")
#     @property
#     def get_pin(self):
#         return self.__display_pin()
# account = BankAccount(1000)
# print(account.get_balance())
# account.set_balance(100)
# print(account.get_balance())
# account.get_pin


# class Atm:
#     def __init__(self, name, age, store_balance, pin):
#         self.name = name
#         self.age = age
#         self.store_balance = store_balance
#         self.__pin = pin
#     def balance_add(self, pin_num, balance):
#         if self.__pin == pin_num:
#             self.store_balance += balance
#             print(f"Balance {balance} Add Successfully.Your Current Balance is {self.store_balance}")
#         else:
#             print("You are not Authenticate User. ")
    
#     def withdrow_balance(self, pin_num, balance):
#         if self.__pin == pin_num:
#             self.store_balance -= balance
#             print(f"Balance {balance} Withdraw Successfully.Your Current Balance is {self.store_balance}")
#         else:
#             print("Your Pin Number is Wrong.")
#     def __desplay_pin(self):
#         print(f"Your Pin Number is: {self.__pin}")
#     @property
#     def get_pin(self):
#         self.__desplay_pin()
    
# user_1 = Atm("Selim", 23, 10000, "1234Dhaka")
# print(user_1.store_balance)
# user_1.balance_add("1234Dhaka", 5000)
# print(user_1.store_balance)
# user_1.withdrow_balance("1234Dhaka", 3000)
# print(user_1.store_balance)
# user_1.get_pin

    