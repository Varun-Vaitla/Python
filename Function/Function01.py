#Function syntax
#local Variable
# def add():
#     a=10
#     b=20
#     return a + b
# print(add())#30

# #Global Variable
# a=10
# b=20
# def add():
#     return a + b
# print(add())#30

# #local and global Variable
# a=10
# b=20
# def add():
#     b=10
#     print(a, " a value in function")
#     print(b, " b value in side function")
#     return a + b
# print(add())
# print(a," a value out side function")
# print(b," b value out side function")

"""
10  a value in function
10  b value in side function
20
10  a value out side function
20  b value out side function

"""
# function with parameter
def squer(num):
    return num**2
print(squer(2))#4


#Named parameter
def welcome(name="user"):
    return "Hello: ",name
print(welcome())##('Hello: ', 'user')
print(welcome("varun"))#('Hello: ', 'varun')

# #return multipel values
# def calculater(num1,num2):
#     add=num1 + num2
#     sub=num1 - num2
#     mul=num1 * num2
#     return add, sub, mul

# a,s,m=calculater(10,5)
# print("addition: ",a," substraction: ",s," multiplication: ",m)#addition:  15  substraction:  5  multiplication:  50


#multiple arguments or *args

def add_numbers(*args):
    print(args)
    summ=0
    for i in args:
        summ += i
    return summ
    


print(add_numbers(1, 2, 3, 4, 5))
print(add_numbers(10, 20, 30, 40, 50))

