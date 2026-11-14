# ##string formatting or using variables in string
# name="varun"
# age=25
# #there are 3 ways
# #1.. formate()
# message="my name is {} and my age is {}".format(name,age)
# print(message)
# message1="my name is {1} and my age is {0}".format(name,age)
# print(message1)#we can specifie the order also

# #2.. by using f string
# message2=f"my name is{name} and my age is{age}"
# print(message2)

# c=10
# d=20
# add=f"addition of c and d is {c+d}"
# print(add)

# #3.. by using % formatting
# #this is the old way and not recomended

# message3="my name is %a and my age is %d ...."%(name,age)
# print(message3)

# ##string methods###
 
#  ##1. case methods
# sample_text="i am am Python Developer"
# print(sample_text.upper())
# print(sample_text.lower())
# print(sample_text.capitalize())
# print(sample_text.title())
# print(sample_text.swapcase())

# """I AM AM PYTHON DEVELOPER
# i am am python developer
# I am am python developer
# I Am Am Python Developer
# I AM AM pYTHON dEVELOPER"""

# #2.. searching and finding methods 

# #i.. find() => this method id udes to find the first occurence of the sub string, if the stind is found it will return index of first occurence if not found it will return -1
# text="this is a sample text, this text is used for executing"
# #syntax => string.find(substring, start, end)


# #ii..rfind() => it will return index of last occurence of the substing 


# #iii.. index() => it will work  similer to the find but if substing is not present in sub string it will return valueError not -1


# #iv.. rindex => it will return the index of last occrence of substring 


# #v.. count() => it is used to count the number of times the substring is repeted in the string and it return 0 if the substring is not there


text = "python is easy and python is powerful"

print(text.find("python"))  # 0
print(text.rfind("python")) # 19
print(text.index("python")) # 0
print(text.rindex("python"))# 19
print(text.count("python"))# 2

## removing spaces and characters method

#i.. strip()
sample = "  python  "
sample1="##python##"
sample2 = "#  python  "
sample3="ppythonp"
print(sample.strip())
print(sample1.strip("#"))
print(sample3.strip('py'))

print("...........")
print(sample.lstrip())
print(sample1.lstrip('#'))
print("...........")
print(sample.rstrip())
print(sample1.rstrip('#'))
print("...........")
sample4="premidsuff"
print(sample4.removeprefix("pre"))
print(sample4.removesuffix("suff"))

#sting replace methods
#i.. replace()
title="this is an python class"
titleResult = title.replace("a","#")
titleResult1 = title.replace("a","#",1)
print(title)
print(titleResult)
print(titleResult1)

#NOTE: using replace we can replace single char or substing at a time but we cannot modify multiple cahr at a time so we need to use marktrans and translate

#ii.. maketrans() and translate()
subtitle="i want to become python developer"
valueToChange={"a":"1" ,"e":"2", "i":"3", "o":"4", "u":"5"}
#single parameter
table1=subtitle.maketrans(valueToChange)
# two parameter
table2=subtitle.maketrans("aeiou","AEIOU")
#3parameter
table3=subtitle.maketrans("aeiou","AEIOU","pd")
print(table1)#{97: 1, 101: 2, 105: 3, 111: 4, 117: 5} unicode values this the table
result1=subtitle.translate(table1)
result2=subtitle.translate(table2)
result3=subtitle.translate(table3)
print(result1)#3 w1nt t4 b2c4m2 pyth4n d2v2l4p2r
print(result2)#I wAnt tO bEcOmE pythOn dEvElOpEr
print(result3)#I wAnt tO bEcOmE ythOn EvElOEr
