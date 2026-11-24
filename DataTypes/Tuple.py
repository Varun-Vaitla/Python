#tuple is used to store multiple values in single variable

"""
1.tu[le is represented by ()
2.in tuple we can store duplicate values
3.in tuple ve can store multiple data typed values
4. it folloes oerder of insertion
5. it suports +ve and -ve indexing and slicing
6. it is immutable
7. comma(,) seprated values are considered as tuple

"""
#we can create tuple in many ways
n1=(10,20,30)
print(type(n1))#tuple
n2=10,20,30
print(type(n2))#tuple
n3=tuple([10,20,30,40])
print(type(n3))#tuple

n4=(10)
print(type(n4))#<class 'int'> because there is no comma

#if you want to store single value in tuple use ( , )
n5=(10,)
print(type(n5))#<class 'tuple'>

