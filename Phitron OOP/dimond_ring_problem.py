                #     A
                #   /   \ 
                #  B     C
                #  \     /
                #     D
                
# A k B and C inherite kora D hoccha B and C ka inherite kora
"""Dimond Ring Problem"""

class A:
    def print_somthing(self):
        print("I am A")
class B(A):
    # def print_somthing(self):
    #     print("I am B")
    pass
class C(A):
    # def print_somthing(self):
    #     print("I am C")
    pass        
class D(B,C):
    # def print_somthing(self):
    #     print("I am D")
    pass 
obj_1 = A()
obj_2 = B()
obj_3 = C()
obj_4 = D()

# obj_1.print_somthing()
# obj_2.print_somthing()
# obj_3.print_somthing()
obj_4.print_somthing()