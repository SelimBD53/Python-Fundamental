# def factorial(n):
    
#     if n==1:
#         return 1
#     else:
#         print("n:", n)
#         print("n-1:", n-1)
#         print("=============================")
#         return n*factorial(n-1)
#                # 5* factorial(4) =5*24 =120
#                   # 4* factorial(3) =4*6=24
#                       # 3* factorial(2)  =3*2=6
#                           # 2* factorial(1) =2*1 =2
#                                # return 1

# print(factorial(5))

# def sum_list(l):
#     if len(l) == 1:
#         return l[0]
#     else:
#         return l[0]+sum_list(l[1:])
#            # 1 + sum_list[3,5,7,9] =24+1 = 25[Answer]
#               # 3 + sum_list[5,7,9] =21+3=24
#                 # 5 + sum_list[7,9] =16+5=21
#                   # 7 + sum_list[9]  = 7+9=16
#                       # 9  
# l= [1, 3, 5, 7, 9]
# print(sum_list(l))

# def fibonacci(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         print("n-1:", n-1)
#         print("n-2:", n-2)
#         print("==========================")
#         return fibonacci(n-1)+fibonacci(n-2)
    
# print(fibonacci(6))

