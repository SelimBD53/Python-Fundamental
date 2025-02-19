# function Structure
# def function_name(perameter):
#     statement
#     pass
# function call
# function_name(argument)

# def my_name():
#     print("Selim Reza is a loyal Boy")
#     return ("Hello Return")
    
# var = my_name()
# print(var)

# def my_name():
#     print(g)
#     l = "local" #local variable
#     print("Selim Reza is a loyal Boy")
#     return ("Hello Return")
    
# g = "global" # Global Variable
# var = my_name()
# # print(l)
# print(var)

# arg = "arguments" #tuple
# def my_name(*u):
#     print(type(u))
#     return sum(u)
# var = my_name(10, 20, 60)
# print(var)


# kwargs = "keyword argument"  #dictionary

# def my_name(**k):
#     # print(type(k))
#     # print(k)
#     for key, value in k.items():
#         print(key, value)
#     return k

# dict1 = my_name(name ="selim", age=67)
# dict2 = my_name(name ="sara", age=69)
# dict3 = my_name(name ="saba", age=60)

# print(dict1)
# print(dict2)


# def my_name(*agrs, **kwarg):
#     print(agrs)
#     print(kwarg)
#     return kwarg,agrs

# var = my_name(12,13,14,15,16, name="Selim", age=45, sex="male")
# print(var)
# x, y = var
# print(x)
# print(y)

# u = {}        //dictionary user input system.
# i = int(input("Enter The value: "))
# for x in range(i):
#     key = input()
#     value = input()
#     u[key] = value
# print(u)

# function a **kwargs sob sommoy ses a liktha hoba.

# def my_name(a,b,c=0):
#     return a+b+c

# var = my_name(12,10,90)
# var1 = my_name(2,1)
# print(var)
# print(var1)


# Ki dhoronar data type return or data neba sai ta define kora function declare kora.

# def add_sum(num1 : int, num2: int) -> int:
#     return num1+num2



#Generator:  [fibonnachis series problem ]
# def fib(limit):
#     num1, num2 = 0, 1
#     while num1<limit:
#         yield num1
#         num1, num2 = num2, num1+num2

# gen = fib(8)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# def show_employee(name="anonymous", salary=90000):
#     return f"The Employ name is {name} and this salary is {salary}"

# info= show_employee()
# print(info)    




