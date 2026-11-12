##string formatting or using variables in string
name="varun"
age=25
#there are 3 ways
#1.. formate()
message="my name is {} and my age is {}".format(name,age)
print(message)
message1="my name is {1} and my age is {0}".format(name,age)
print(message1)#we can specifie the order also

#2.. by using f string
message2=f"my name is{name} and my age is{age}"
print(message2)

c=10
d=20
add=f"addition of c and d is {c+d}"
print(add)

#3.. by using % formatting
#this is the old way and not recomended

message3="my name is %a and my age is %d ...."%(name,age)
print(message3)