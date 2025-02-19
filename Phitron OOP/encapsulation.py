class Account:
    def __init__(self, holder, initial_balance):
        self.holder = holder     # Public attribute
        self._account_Number = 165
        self.__balance = initial_balance       # __balance is a private attribute.
        
    def deposit(self, amount):
        print(f"adding {amount} to your account")
        self.__balance += amount
    
    def withdrow(self, amount):
        print(f"Withdrawing {amount} from your account") 
        self.__balance -= amount
    
class StudentAccount(Account):
    def __init__(self, holder, initial_balance, school):
        self.school = school
        super().__init__(holder, initial_balance)
    def get_balance(self):
        return self.__balance
       
Selim = StudentAccount("Selim Reza", 50000, "GUB")

Selim.deposit(20000)
Selim.deposit(35000)
Selim.deposit(15000)
print(Selim.get_balance())
Selim._account_Number = 135
print(Selim._account_Number)
print(Selim.get_balance())