class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdrow = 100
        self.max_withdrow = 10000
    def get_balance(self):
        return self.balance
    def withdrow(self, amount):
        if amount < self.min_withdrow:
            return f"Tumi Taka withdrow korta parba na , Your Amount is {amount}"
        elif amount > self.max_withdrow:
            return f"Tumi {amount} taka withdrow korta parba na .Maximum Withdrow {self.max_withdrow}"
        elif amount > self.get_balance():
            return f"Tomar Balance Acha {self.get_balance()} Taka AR Basi Do not withdro."
        else:
            self.balance -= amount
            return f"Amount Withdrow successfull {amount}"
    def deposit(self, amount):
        self.balance+=amount
my_bank = Bank(5000)
print(my_bank.withdrow(500))
print(my_bank.get_balance())
my_bank.deposit(1000)
print(my_bank.get_balance())
