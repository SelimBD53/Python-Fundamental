from functools import partial
def get_number(a, b, c, d):
    return a*1000 + b*100 + c*10 +d
    
get_number(4, 5, 3, 2)
fourth = partial(get_number, b=0, c=0, d=0)
print(fourth(4))
