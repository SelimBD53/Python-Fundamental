"""Problem 1: Secure Bank Account"""

class BankAccount:
    def __init__(self, account_number, balance_amount):
        self.__account_number = account_number
        self.__balance_amount = balance_amount
    def get_balance(self, amount):
        return self.__balance_amount + amount
class OneBank(BankAccount):
    def __init__(self, account_number, balance_amount):
        super().__init__(account_number, balance_amount)
        
    def add_amount(self, amount):
        if amount > 0:
            # self.__balance_amount += amount
            print(self.get_balance(amount))
            
bank = OneBank("1235fg", 1000)
print(bank.__account_number)
bank.add_amount(200)