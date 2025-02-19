"""Manages Bank Account"""

class Account:
    acc_ID = 1
    def __init__(self, name, age, nid_num, balance):
        self.name = name
        self.age  = age
        self.nid_num = nid_num
        self.balance = balance
        self.account_id = Account.acc_ID
        Account.acc_ID += 1
        
acc_1 = Account("Selim", 23, 235, 4000)
acc_2 = Account("Kona", 25, 579822, 2653)
print(acc_1.account_id)
print(acc_2.account_id)