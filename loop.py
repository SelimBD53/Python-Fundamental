# s = '12345'
# i = 0
# while i<len(s):
#     print(s[i])
#     i+=1

# for i in range(6)[1::]:
#     print(i)
# break, continue, pass

# for i in "12345":
#     if i == '3':
#         break
#     print(i)
# print("????????????????????????")
# for i in "12345":
#     if i == '3':
#         continue
#     print(i)
# print("/////////////////////////")
# for i in "12345":
#     if i == '3':
#         pass
#     print(i)
# print("====================")
# for i in '12345':
#     print(i)
# else:
#     print("loop Completed")

# list1 = ["apple", "bannana", "cherry"]
# for i in list1:
#     print(i)
    
# tuple1 = ("apple", "bannana", "cherry")
# for i in tuple1:
#     print(i)

# dict1 = {"name": "selim", "age": "23"}
# for i in dict1.items():
#     print(i)
#     for j in i:
#         print(j)

# list comprehension // set and tuple comprehension same as list.
# list2 = [b for i in ("apple", "bannana", "cherry") for b in i ]
# print(list2)
# list3 = [x**2 for x in range(5)]
# print(list3)

# list1 = "12345"  # ["apple", "bannana", "cherry"]
# for i, j in enumerate(list1):
#     print(i)
#     print(j)
# l = ["apple", "bannana", "cherry"]
# s = ["red", "yellow", "black"]
# for i, j in zip(l, s): # data track raktha zip used kori.
#     print(i, j)

# dictonary Comprehension
# dict1 = {key: value for key, value in [("name", "selim"), ("age", 29)] if key != "name"}  # use in list of tuple
# print(dict1)


tuple1 = ("apple", "bannana", "cherry")
print(type(tuple1))
# print(next(tuple1))

tuple1 =(i for i in ("apple", "bannana", "cherry")) # onek boro data neya kaj kora hoy generator.
print(type(tuple1))
print(tuple1)
print(next(tuple1))


