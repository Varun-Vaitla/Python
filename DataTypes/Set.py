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

#update() it is used to add multiple elements into an set using iteratables such as list,tuple,string,set etc

numbers1={10,20,30}
numbers1.update([40,50,60])
print(numbers1)#{40, 10, 50, 20, 60, 30}

#update using string
chars={"a","b","c"}
chars.update("defghijklmnopqrstuvwxyz")
print(chars)#{'g', 'o', 'p', 'i', 'a', 'c', 'h', 'u', 'f', 'x', 'm', 'k', 'v', 's', 't', 'd', 'n', 'z', 'y', 'b', 'j', 'q', 'w', 'l', 'e', 'r'}

#remove is used to remove one element from set
s1={10,20,30,40,50}
s2=s1.remove(10)

# print(s1)#{50, 20, 40, 30}
# print(s2)#None
# s1.remove(60)
# print(s1)#keyerror if the value is not present we will get keyerror

#discard() it works similar to the remove method but if the element is not present it will not give keyerror
s3={10,20,30,40}
s3.discard(60)
print(s3)# no error

#clear() it is used to clear the set elements
s4={100,200,300,400}
print(s4)
s4.clear()#{200, 100, 400, 300}
print(s4)#set()

#del
# s5={1,2,3,4,5}
# print(s5)#{1, 2, 3, 4, 5}
# # del s5
# print(s5)#NameError: name 's5' is not defined. Did you mean: 's1'?

#union it will combain 2 set and remove all duplicate values
s6={10,20,30,40}
s7={30,40,50,60}
s8=s6.union(s7)
print(s8)#{40, 10, 50, 20, 60, 30}
s9=s6 | s7
print(s9)#{40, 10, 50, 20, 60, 30}

#intersection() it is used to print only duplicate values
s10=s6.intersection(s7)
print(s10)#{40, 30}
s11= s6 & s7
print(s11)#{40,30

#difference(): it will print elements present in first set and those elemnts should not be in second set
# s1={10 ,20 ,30, 40, 50}
# s2={        30, 40,   ,60}
# s3={10 ,20 ,0 , 0,  50 }
se1={10,20,30,40,50}
se2={30,40,60}
result=se1.difference(se2)
print(result)#{50, 10, 20}

#symmentric_difference() prints all elements except comman elements

se3={10,20,30,40,50}
se4={40,50,60,70}
result=se3.symmetric_difference(se4)
print(result)#{70, 10, 20, 60, 30}

#issubset() checks all set1 elements are present in set2 elements
set1={10,20,30,40,50}
set2={10,20,30,40,50}
set3=set1.issubset(set2)
print(set3)#True

set4={40,50}
set5=set1.issuperset(set4)
print(set5)#True

