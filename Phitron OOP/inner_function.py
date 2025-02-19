# def do_somthing(work):
#     print("Start The Work")
#     work()
#     print("Done The Work")
    
# def partice_problem():
#     print("Pratice the problem Python")
    
# def learning_python():
#     print("Learning The Python")
# do_somthing(partice_problem)
# do_somthing(learning_python)


# def do_somthing():
#     print("Learning Python")
#     def Inner_function():
#         print("Inner Function Call")
#     Inner_function()
# do_somthing()

def First_function():
    print("First Function call")
    def Second_function():
        print("Second Function Call")
    return Second_function
# first = First_function()
# first()
# First_function()()