# Decorator

# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Somthing Say!")
#         func(*args,**kwargs)
#         print("Another Somthing Say!")
#     return wrapper

# Development Side a Decorator used Hoy authentication and authorization side a.

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Say Somthing!")
#         func(*args, **kwargs)
#         # func(*args,**kwargs)
#         print("Another Say Somthing!")
#     return wrapper
# @my_decorator

# def say_hello(name):
#     print(f"Hello {name}")
    
# say_hello("Selim")
# s=my_decorator(say_hello("Selim"))

# def decorator(v):
#     print("Function is call First")
#     def wrapper(*args, **kwargs):
#         print(f"Function is {v.__name__} called.")
#         v(*args, **kwargs)
#         print(f"Function is {v.__name__} finished.")
#         # return s
#     print(wrapper)
#     print("Wrapper is returned.")
#     return wrapper  # [ai khana pura function ta ka return kora deccha.]
# @decorator

# def multiply(d,f):
#     print(d*f)

# multiply(5,10)
# print("=============================")
# mul = decorator(multiply(5,10))
# print(mul)


# def repeat(num):
#     def decorator(funk):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 funk(*args, **kwargs)
#         return wrapper
#     return decorator
        
# @repeat(5)
#                 #[Kono akta function 5 hour por por check dak.]
# def time_check():
#     print("time is checked!")

# time_check()



def decorator(funk):
    def wrapper(*args, **kwargs):
        print("Starting")
        funk(*args, **kwargs)
    print("===================")
    return wrapper

@decorator       # [@ deya mainly wrapper function ta ka call daya hoccha.]
def check(name):
    print(f"{name} Entered! ")

# m =decorator(check("selim"))
# check("Selim")
# check("Selim1")



# map 

# l = [1, 2, 3, 4, 5, 6]

# m = map(lambda x: x**2, l)
# print(list(m))

# filter
# m = filter(lambda x: x%2 ==1, l)
# print(list(m))

#reduce
# from functools import reduce
# m = reduce(lambda x, y: x*y, l)
# print(m)
