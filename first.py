a = int(input("Enter the first Number: "))
c = input("Enter the operation(+,-,*,/,%): ")
b = int(input("Enter the second Number: "))

if c == '+':
    x = a+b
    print(f"The sum is {x}")
elif c == '-':
    x = a-b
    print(f"The sub is {x}")
elif c == '*':
    x = a*b
    print(f"The Multiply is {x}")
elif c == '/':
    x = a/b
    print(f"The Division  is {x}")  
elif c == '%':
    x = a%b
    print(f"The Dividends is {x}")
else:
    print("Invalid Number.")