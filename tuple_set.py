# tuple1=(1,2,3,4,5,6)
# v=8
# f=tuple1+(v,)
# print(f)

# List1 = [1,2,3,4,5,6]
# List1.append(9)
# print(List1)

# set1={1,2,3,4,5,6}
# set1.add(9)
# print(set1)
# for i in set1:
#     print(i)
    
# set convert to list
# list=[1,2,3,3,4,5]
# d=set(list)
# k=[*d]
# print(k)

# dict1 = {
#     "key": "value",
#     "name": "Selime Reza",
#     "age": 23
# }
# dict1["sex"]="male"
# for i, j in dict1.items():
#     print(i,j)



# list1 = [1,2,3,4,5,6]
# print(list1)
# print(list1[0])
# print(list1[:3]) #print(list1[:(n-1)])
# print(list1[-1:-4:-1])
# print(list1[-1::1])


# start : end : step

# start = null = 0
# end =null = len(list1)
# step = null = 1



# set ar moddha dublicate value raka jaba na. alwayes unique value raktha hoba.
# set a order maintain kora na. unorder obostai thaka.
# tuple hoccha emutable. mana tuple ka change korta parbo na.value assing or delete kora jai na.

# tp = 10,2,3,4,45
# tp =([12,23,45],[54,66])
# tp[1]=55
# tp[0][1]= 55
# print(tp)





#Dictonary

# dt = {"bangla": 55, "english": 66, "math":65}
# dt['ML'] = 85
# dt['op'] = 88
# dt_key = dt.keys()
# dt_values = dt.values()
# print(dt_key)
# print(dt_values)
# print(dt.pop("ML"))
# dt.clear()
# del dt["math"]
# print(dt)
# print(dt.items())



# dt = {"bangla": 55, "english": 66, "math":65}
# for mark in dt:
#     val = dt[mark]
#     print(mark, val)
# for subjet, mark in dt.items():
#     print(subjet, mark)



# Dictionary Comprehension
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# Keys to extract
# keys = ["name", "salary"]

# for key, value in sample_dict.items():
#     for i in keys:
#         if i==key:
#             print({i,value})
            

# d={i:value for key, value in sample_dict.items() for i in keys  if i==key}
# print(d) 


# list1 = ["M", "na", "i", "Bo"]
# list2 = ["y", "me", "s", "nd"]
# new_list=[]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if i==j:
#             v=list1[i]+list2[j]
#             new_list.append(v)
# print(new_list)


# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# l=list2[::-1]
# x=zip(list1,l)
# for i in x:
#     print(i)

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# re = {}
# for i in range(len(keys)):
#     for j in range(len(values)):
#         if i==j:
#             re[keys[i]]=values[j]


# print(re)













