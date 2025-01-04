
# Problem 1
# userinput = float(input("Enter The Number: "))

# print(f"This {userinput} Number Floor is {int(userinput)}")
# print(f"This {userinput} Number Ceil  is {int(userinput+1)}")

# Problem 2

# x = int(input("Enter The 1st Number: ")) 
# y = int(input("Enter The 2nd Number: ")) 
# z = int(input("Enter The 3rd Number: ")) 

# c = x if x>=0  else x*-1
# print(c)
# v = y if y>=0 else y*-1
# print(v)
# b = z if z>=0 else z*-1
# print(b)

# Problem 3

# player1=input("Enter The Player-1 Name:")
# player2=input("Enter The Player-2 Name:")

# if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "rock"):
#     print("Player 1 is winner")
# elif (player1 == "paper" and player2 == "rock") or (player1 == "rock" and player2 == "paper"):
#     print("Player 1 is winner")
# elif (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "scissors"):
#     print("Player 1 is winner")
 
 
# # Problem 4 
# while True:
#     user = input("Enter The Number: ")
#     if user =="Quit":
#         print("Stop The Program.")
#         break
#     elif int(user) ==0:
#         print("User input is ZERO.")
#     elif int(user)>0:
#         print(f"{user} is the Positive Number")
#     elif int(user)<0:
#         print(f"{user} is the Negative Number.")
    
    
# Problem 5
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)

# d = 'pHitrOn.iO presents "Python COuRSe"'
# k= ""
# for i in d:
#     if i==i.lower():
#         k+=i.upper()
#     elif i==i.upper():
#         k+=i.lower()
#     elif i=='"':
#         k+=i
# print(k)

# 1
# def two_sum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             print(i, i+1)
#             print("=================")
#             if nums[i] + nums[j] == target:
#                 return [i,j]


# nums = [3,2,4]
# target=6
# print(two_sum(nums, target))




# 2 
# def two_sum(nums,target):
#     for i in range(len(nums)):
#         second_num = target - nums[i] 
#         if second_num in nums[i+1:]:
#             return [i, nums.index(second_num)]

# nums = [3, 3]
# target=6
# print(two_sum(nums, target))


#3[Acceptaed]
# class Solution:
# def twoSum(nums, target):
#     seen = {}  
#     for i in range(len(nums)):
#         second_num = target - nums[i]
#         if second_num in seen:
#             return [i, seen[second_num]]
#         seen[nums[i]] = i
        
# nums = [3,3]
# target=6
# print(two_sum(nums, target))

# 1. first bujbo ki input dela ki output chacca
# 2. first chinta korbo brout force deya solve korar.
# 3. tarpor chinta korbo na hola onno way kojar.
# 4. Brout force deya solve korla visulation ta clear hoba.
# 5. data visualization korat hoba.