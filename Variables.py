# #python is dynamically typed 
# a=10
# print(type(a))
# name="varun"
# print(type(name))
# isLogedin= True
# print(type(isLogedin))
# salary=30000
# print(type(salary))
# hight=5.7
# print(type(hight))

# """
# output
# <class 'int'>
# <class 'str'>
# <class 'bool'>
# <class 'int'>
# <class 'float'>
# """
# #variables in python is reference of object
# x=10
# y=20
# xx=10
# print(id(x)) #140709623958232 id of x and xx are same because bothe are refcering to the same object that is 10
# print(id(y)) #140709623958552 for y it has diff id
# print(id(xx)) #140709623958232

# # id() and type()
# # id() is used to finf the reference of the object
# #type() is used to find the type id variable 

# """
# rules for variables naming convention
# 1.variable name should be start form letter of _ underscore
# 2. variable name should not start with numbers
# 3.variable name should not contain special char (@,$,-)
# 4. we should not use space
# 5. we cannot use python ketwords
# """

# #in python variables are dynamically typed and strictlly typed so we cannot perform operations between 2 datatypes

# # age=20
# # ageInWords="one"
# # print(age + ageInWords) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# s=10
# t="20"
# print(s + int(t)) #30

# # assigning multipul variables in single line
# sname,sage,smarks="varun",25,60.5
# print(sname)#varun
# print(sage)#25
# print(smarks)#60.5

# #assigning same value for multiple variable
# s1=s2=s3=50
# print(s1)#50
# print(s2)#50
# print(s3)#50

# # mutable and immutable variables
# names1=["varun","tarun","karun"]
# names2=names1
# print(names1)#['varun', 'tarun', 'karun']
# print(names2)#['varun', 'tarun', 'karun']
# names2.append("barun")
# #here we append name2 but name1 is also updated because both are pointing to the same ref
# print(names1)#['varun', 'tarun', 'karun','barun']
# print(names2)#['varun', 'tarun', 'karun','barun']
# #to make a copy are to create shallowcopy use copy()
# names3=names2.copy()
# names3.append("sarun")
# print(names2)#['varun', 'tarun', 'karun', 'barun']
# print(names3)#['varun', 'tarun', 'karun', 'barun', 'sarun']

#scope of variable 
#in python we Have 4 types of scope LEGB
#local scop
# def display():
#     name="varun"
#     print(name)#varun in side the function
# display()
# print(name)# out side the function name error

#global scope
# name="varun"
# def display():
#     print(name)#varun
# display()
# print(name)#varun

#if i want to modify glabal variable inside the function i need to use global keyword
# a=10
# def add():
#     global a
#     a += 10
#     print(a)#20
# add()
# print(a)#20

#encolsed scope it is used in inner and outer function
# def outer():
#     name="varun"
#     def inner():
#         print(name)
#     inner()
#     print(name)
# outer()

#if u want to modify the outer funtion variable form inner function use keword nonlocal
def outer():
    a=10
    def inner():
        nonlocal a
        a += 10
        print(a)#20
    inner()
    print(a)#20
outer()


