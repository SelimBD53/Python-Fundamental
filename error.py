# if(1):
#   print("Testing purpose")
#     print("Hello")  

# SyntaxtError**
# print("Hello"
# # NameError
# if True:
#     x=0
# print(x)
# # TypeError**
# print("hello"+1)
# # IndentationError**
# if True:
# print("Hello")
# KeyError
# ValueError
# ZerodivitationERROR
# print(10/0) 


# error handling
# try: 
#     print(10/2)
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")

# try:
#     if False:
#         x=0
#     print(x)
# except Exception as e:
#     print(str(e))
#     print(type(e))

# koto Number Line a Error asa sai ta dakar jonno ai vaba try, exceptation used kora.
# import traceback
# try:
#     print(10/0)
# except Exception as e:
#     tb =traceback.format_exc()
#     print(tb)   # developer ka show korar jonno
#     print("Zero Not diviede.") # user ka show korar jonno


# Raise Error: developer nijar moto kora user ka error mssage dakata chai:

# a = int(input("Enter The Number: "))
# if a<0:
#     raise Exception("Sorry, this is Nagative Number. ")
    # raise NameError("Sorry, this is Nagative Number. ")  #  jai rokom error dakata chai sai rokom error dakata para jai.
    # raise ZeroDivisionError("Sorry, this is Nagative Number. ")
    # raise CustomError("Sorry, this is Nagative Number. ")        