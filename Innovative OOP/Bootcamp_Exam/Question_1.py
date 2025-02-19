def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Insufficient funds")
    else:
        new_balance = balance - amount
        return f"New Balance: {new_balance}"
try:
    balance = int(input("Enter The Balance: "))
    amount = int(input("Enter The Amount: "))
    print(withdraw(balance, amount))
except Exception as g:
    print(g)        
    
