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



