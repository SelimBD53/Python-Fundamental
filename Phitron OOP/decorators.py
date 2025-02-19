import math
import time


def timer(funk):
    def inner(*args, **kwargs):
        print("Time Started ")
        start = time.time()
        funk(*args, **kwargs)
        end = time.time()
        print(f"Time Ended. Total Time {end - start}")
    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f"The Number {n} factorial is {result}")
    
# timer(get_factorial)()
get_factorial(n=0)