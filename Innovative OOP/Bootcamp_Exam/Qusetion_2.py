"""Calculator"""
def calculate(num_1, num_2, operator):
    if operator == "+":
        return num_1+num_2
    elif operator == "-":
        return num_1-num_2
    elif operator == "*":
        return num_1*num_2
    elif operator == "/":
        return num_1/num_2


num_1 = int(input("Enter The Number 1 : "))
num_2 = int(input("Enter The Number 2 : "))
operation = input("Which operation do you want to perform?(+, -, *, /) : ")
print("Result: ", calculate(num_1, num_2, operation))

