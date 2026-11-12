#datatypes in python
#Numbers Datatypes
#int ,folat, complex
#i) int

# a=10
# print(id(a))#140709363976920
# print(type(a))#<class 'int'>
# b=10
# print(id(b))#140709363976920 same as a
# c= a + b - 10
# print(id(c))#140709363976920

#isinstence() this method is used to validate the type
#syntax isinstence(object,class)
# a=10
# print(type(a))#<class 'int'>
# print(isinstance(a,int))#True
# print(isinstance(a,str))#False

# # Note: bool is a subclass of int class
# is_it=True
# print(type(is_it))#<class 'bool'>
# print(isinstance(is_it,int))#True
# print(isinstance(is_it,bool))#True

#Operations on int
# a=10
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)
# """
# 13
# 7
# 30
# 3.3333333333333335
# 3
# 1
# 1000
# """

#inbuilt methods in int
#  int() => it is use to convert other datatypes to int
# salary = 50000.57
# print(type(salary))
# sal1=int(salary)
# print(type(sal1))

# <class 'float'>
# <class 'int'>

##abs() it will return absolute value or remove -ve and give +ve value
# a=10.5
# b=-10
# print(abs(a))#10.5
# print(abs(b))#10

# ##pow() it iused to provide power
# print(pow(2,3))#8

# ##divmod() it will give both quatient and remainder values
# a=10
# b=3
# print(divmod(a,b))#(3, 1)

#min, max,sum, round
# a=10.7
# print(round(a))
# b=10.3
# print(round(b))
# c=10.5
# print(round(c))

# print(max(10,20,30,33))

# print(min(10,20,30,33))


# print(sum([10,20,30,33]))

# #output
# """11
# 10
# 10
# 33
# 10
# 93"""



"""
Float Numbers
this datatype is used to store decimal values 
we can use both +ve and -ve values in folat
folat is immutable
we cannot store exact values of folat in python because it will be stored in binary format
if we want to use them we need to uses Decimal modules
"""
a=10.5
print(type(a))#<class 'float'>
b=10
print(type(b))#<class 'int'>
print(type(float(b)))#<class 'float'>

#we cannot convert string values into float because they are not number type

# c="varun"
# print(float(c))#ValueError:

#we have specal float values

a=float("inf")
b=float("-inf")
c=float("nan")
print(a)#inf
print(b)#-inf
print(c)#nan

add_a=0.1
add_b=0.2
print(add_a + add_b)#0.30000000000000004 see at the end we are getting 04 it is not correct to over come this we will be using Decimal module

from decimal import Decimal
a=Decimal("0.1")
b=Decimal("0.2")
print(a + b)#0.3