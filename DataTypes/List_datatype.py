#list() 
"""
1. insertion order => list follows an order of insertion 
2. mutable=> list is mutable it means we can change the value even after list is created
3. can have duplicate values
4. multiple datatypes => in list we can store multi datatyped values
5. nested list => we have list inside another list
6. we can access the values based on both +ve and -ve index
7. list supports slicing we can extract portion of list
"""
#1. insertion order => list follows an order of insertion 
numbers=[10,20,30,40,50]
print(numbers)#[10, 20, 30, 40, 50]

#2. mutable=> list is mutable it means we can change the value even after list is created
names=["varun","manoj","naveen"]
print(names)#['varun', 'manoj', 'naveen']
names[1]="tarun"#changing value
print(names)#['varun', 'tarun', 'naveen']

#3. can have duplicate values
students_names=["varun","tarun","varun","kiran"]
print(students_names)#['varun', 'tarun', 'varun', 'kiran']

#4.multiple datatypes => in list we can store multi datatyped values
#5. nested list => we have list inside another list
student_details=["varun",25,5.8,["math","science","english"],True]
print(student_details)#['varun', 25, 5.8, ['math', 'science', 'english'], True]

#6. we can access the values based on both +ve and -ve index
num=[10,20,30,40,50]
print(num[0])#10
print(num[1])#20
print(num[-1])#50

#7.list supports slicing we can extract portion of list
full_list=[1,2,3,4,5,6,7,8,9,10]
first_half=full_list[:5]
second_half=full_list[5:]
print(first_half)#[1, 2, 3, 4, 5]
print(second_half)#[6, 7, 8, 9, 10]

#8. we can have empty list
empty_list=[]
print(empty_list)#[]

#9.. 2 lists
text="varun"
one=["varun","naveen","Ajay"]
two=[1,2,3,4,5]
mix=[one ,two]
print(mix)#[['varun', 'naveen', 'Ajay'], [1, 2, 3, 4, 5]]
mix1= one + two
print(mix1)#['varun', 'naveen', 'Ajay', 1, 2, 3, 4, 5]
# mix2=one + text
# print(mix2)


#list built-in methods 

#inserting methods
#1.. append() => this method is used to add one element at end 
numbers=[10,20,30,40]
numbers.append(50)
print(numbers)#[10, 20, 30, 40, 50] 


 