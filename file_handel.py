# File Handeling a two topic importaned 
# 1. Read a File
# 2. Write a File
# open file
# mode: r - read, w - write[create a new file and write this], a - append, x - create [already file exiest then Face the Error], rb - read binary, wb - write binary, ab - append binary, xb - create binary

# write a file
with open('file.txt', 'r') as file:
    # file.write("Hello World")
    # file.writelines("Hello World")
    # file.writelines("Hello World1")
    # file.writelines("Hello World2")
    file.seek(6)             # [seek deya maouse ar karsal ta kotha thaka kothai jaba sai ta bujai. ba kotha thaka suru korbo sai ta bujai]
    print(file.tell())         # [tell bujai ami bortoman a kon position a asi]
    print(file.read())         # read ar moddha integer value dela bujai ami koto thaka read korbo.
    # print(file.readline())
    # print(file.readline())
    # print(file.readlines())
    
    
    
    
    
    
    
# with open('file.pdf', 'r') as file:
#     # file.write("Hello World")
#     print(file.read())