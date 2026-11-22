#set

"""
set is used to store multiple unique values into an single variables
1.we can store only unique values
2.we can store multiple type data values
3.it will not support indexing and slicing
4.it will not follow order of insertion

"""
# we can  create set in 2 ways
set1={10,20,30,40}
set2=set([10,20,30])
print(set1)
print(set2)
print(type(set1))
print(type(set2))

"""
{40, 10, 20, 30}
{10, 20, 30}
<class 'set'>
<class 'set'>

"""
# set will not support indexing so we need for loop for accessing values
numbers={10,20,30,40,50}
# print(numbers[1])#TypeError: 'set' object is not subscriptable

for num in numbers:
    print(num)
"""
50
20
40
10
30

"""

#add() it is used to add single element into an existing set

names={"varun","naveen","manoj"}
names.add("arjun")
print(names)#{'naveen', 'arjun', 'manoj', 'varun'}