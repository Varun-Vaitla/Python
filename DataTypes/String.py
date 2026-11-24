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


# text = "python is easy and python is powerful"

# print(text.find("python"))  # 0
# print(text.rfind("python")) # 19
# print(text.index("python")) # 0
# print(text.rindex("python"))# 19
# print(text.count("python"))# 2

# ## removing spaces and characters method

# #i.. strip()
# sample = "  python  "
# sample1="##python##"
# sample2 = "#  python  "
# sample3="ppythonp"
# print(sample.strip())
# print(sample1.strip("#"))
# print(sample3.strip('py'))

# print("...........")
# print(sample.lstrip())
# print(sample1.lstrip('#'))
# print("...........")
# print(sample.rstrip())
# print(sample1.rstrip('#'))
# print("...........")
# sample4="premidsuff"
# print(sample4.removeprefix("pre"))
# print(sample4.removesuffix("suff"))

# #sting replace methods
# #i.. replace()
# title="this is an python class"
# titleResult = title.replace("a","#")
# titleResult1 = title.replace("a","#",1)
# print(title)
# print(titleResult)
# print(titleResult1)

# #NOTE: using replace we can replace single char or substing at a time but we cannot modify multiple cahr at a time so we need to use marktrans and translate

# #ii.. maketrans() and translate()
# subtitle="i want to become python developer"
# valueToChange={"a":"1" ,"e":"2", "i":"3", "o":"4", "u":"5"}
# #single parameter
# table1=subtitle.maketrans(valueToChange)
# # two parameter
# table2=subtitle.maketrans("aeiou","AEIOU")
# #3parameter
# table3=subtitle.maketrans("aeiou","AEIOU","pd")
# print(table1)#{97: 1, 101: 2, 105: 3, 111: 4, 117: 5} unicode values this the table
# result1=subtitle.translate(table1)
# result2=subtitle.translate(table2)
# result3=subtitle.translate(table3)
# print(result1)#3 w1nt t4 b2c4m2 pyth4n d2v2l4p2r
# print(result2)#I wAnt tO bEcOmE pythOn dEvElOpEr
# print(result3)#I wAnt tO bEcOmE ythOn EvElOEr


## splitting and joining methods

#1.. split() => this method will divide the string into list of elements based on the separator

relation = "varun and sandhya are brother and sisters"
result = relation.split()
print(result)#['varun', 'and', 'sandhya', 'are', 'brother', 'and', 'sisters'] by default whitespace is separator

relation1="varun#and#sandhya#are#brothers"
result1=relation1.split("#")
print(result1)#['varun', 'and', 'sandhya', 'are', 'brothers']

result2= relation1.split('-')
print(result2)#['varun#and#sandhya#are#brothers']

relation2="this?is?to?check"
result4=relation2.rsplit("?",2)
print(result4)#['this?is', 'to', 'check']

##ii.. splitlines()
content="my name is varun \n my age is 25 \n my place is dvg"
result5=content.splitlines()
result6=content.splitlines(keepends=True)
print(result5)#['my name is varun ', ' my age is 25 ', ' my place is dvg']
print(result6)#['my name is varun \n', ' my age is 25 \n', ' my place is dvg']

#iii.. join()
languages=["kannada","telugu","english"]
result7="?".join(languages)
# print(result7)#kannada telugu english
print(result7)#kannada?telugu?english

#iv.. partition() and rpartition() this methods are used to divide the sting into 3 parts and return tuple based on sepatar

friends = "varun naveen are childhood friends and manoj is college friend and uday is j-spider friend"
f1=friends.partition("and")
f2= friends.rpartition("and")
print(f1)
print(f2)
"""
('varun naveen are childhood friends ', 'and', ' manoj is college friend and uday is j-spider friend')
('varun naveen are childhood friends and manoj is college friend ', 'and', ' uday is j-spider friend')
"""


##format_map(): it is used to display object details in string

students=[{"id":1,
           "name":"varun",
           "age":25,
           "place":"DVG"
           },
           {"id":2,
           "name":"Manoj",
           "age":27,
           "place":"BANG"
           }]

for student in students:
 result= "student name: {name}, and his age is:{age} and he is from {place}".format_map(student)
 print(result)

### Boolean methods of string
 string1="varun"
 string2="12345"
 string3="varun12345"
 string4="varun@#$123"

 #1.. isalpha()
 print(string1.isalpha())
 print(string2.isalpha())
 print(string3.isalpha())
 print(string4.isalpha())
"""
True
False
False
False"""

#2..isdigit()
print(string1.isdigit())
print(string2.isdigit())
print(string3.isdigit())
print(string4.isdigit())
"""
False
True
False
False
"""

#3.. isdecimal()

string5="23.4"
print("...................")
print(string1.isdecimal())
print(string2.isdecimal())
print(string3.isdecimal())
print(string4.isdecimal())
print(string5.isdecimal())
"""
False
True
False
False
False
"""
#4 isidentifier()
print("...................")
print(string1.isidentifier())
print(string2.isidentifier())
print(string3.isidentifier())
print(string4.isidentifier())
print(string5.isidentifier())
"""
Rule	Example	Result
Can contain letters	                            "student"	True
Can contain numbers after the first character	"student123"	True
Can start with underscore                      	"_name"	True
Cannot start with a number	                    "123name"	False
Cannot contain spaces	                        "student name"	False
Cannot contain hyphens	                        "student-name"	False
"""

##Alignement and formating methods
#i.. center()
align_str="python"
result=align_str.center(12)
result1=align_str.center(12,"*")
print(result)#   python   
print(result1)#***python***

#ii.. ljust()
res1=align_str.ljust(12,"|")
res2=align_str.rjust(12,"#")
print(res1)#python||||||
print(res2)#######python

#iii.. zfill()
num="201"
num1="-201"
zfill_num=num.zfill(5)
zfill_num1=num1.zfill(6)
print(zfill_num)#00201
print(zfill_num1)#-00201