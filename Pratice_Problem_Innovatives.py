# Problem 1: Matrix Diagonal Sum 

# num = int(input("Enter The Matris Size: "))
# m= []

# for i in range(num):
#     row = []              # user input in row
#     for j in range(num):
#         x = int(input())          
#         row.append(x)
#     m.append(row)

# primary = 0
# for i in range(num):
#     for j in range(num):
#         if i==j:
#             primary+=m[i][j]

# secondary =0
# for i in range(num):
#     for j in range(num):
#         if (i+j)== (num-1):
#             secondary+=m[i][j]
         
# print("\n")
# print(primary," ", secondary)
  
#  i  j           
# [0,0]  [0,1]  [0,2]   
# 1       2      3
# [1,0]  [1,1]  [1,2]
# 4       5       6
# [2,0]  [2,1]  [2,2]
# 7       8       9

     

# Problem 2 : Fizz Buzz with a Twist 

# N = int(input("Enter The Number: "))

# for i in range(1, N+1):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print("Prime")



# Problem 3 : Palindrome Checker

# def string_plaindrom(s):
#     d=""
#     for i in s:
#         if i!=" " and i!=",":
#             d+=i 
#     p=d.lower()
#     b=p[::-1]
#     if b==p:
#         return "Yes"
#     else:
#         return "No"

# s= input("Enter The String: ")
# print(string_plaindrom(s))


# Problem 4 : Prime Factorization
# number =int(input("Enter the Number: "))
# factorial=[]
# ter = 2

# while number>1:
#     if number%ter==0:
#         factorial.append(ter)
#         number=number/ter
#     else:
#         ter+=1
# print(factorial)

# Problem 5 : Password Validator

# def Password_checker(i):
#     upper = 0
#     lower = 0
#     space = 0
#     num = 0
#     for x in i:
#         if x.isupper():
#             upper += 1
#         elif x.islower():
#             lower += 1
#         elif x.isdigit():
#             num += 1
#         elif x.isspace():
#             space += 1
            
#     if upper >= 1 and lower >= 1 and num >= 1 and space == 0 and len(i) >= 8:
#         return "VALID"
#     else:
#         return "INVALID"
# i = input("Enter The Password: ")
# print(Password_checker(i))    

# Problem 6 : Grade System Using List Comprehension


# gread_number = int(input("Enter The List Number Size: "))
# score=[int(input(f"Enter The {i+1} value: ")) for i in range(gread_number)]
# gread = ["A" if num >= 90 and num <= 100 else
#          "B" if num >= 80 and num <= 89 else 
#          "c" if num >= 70 and num <= 79 else 
#          "D" if num >= 60 and num <= 69 else "F"
#          for num in score]
# print(gread)

    




