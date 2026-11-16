##1.. revers an string
text="python"
revers=text[::-1]
print(revers)#nohtyp

##2.. string pallindrom

string1="malayalam"
rev=string1[::-1]
if(string1==rev):
    print("string is pallindrom")#string is pallindrom
else:
    print("string is not pallindrom")

#number of characters
text1="my name is varun"
count_Char = len(text1)
print(count_Char)#15

#remove space form string
text_with_space="this is a text with space"
text_without_space=text_with_space.replace(" ","")
print(text_without_space)

#count vowels ans consonants
mix_text = "my name is varun"

vowels = 0
consonets = 0

for char in mix_text.lower():
    if char in "aeiou":
        vowels += 1

    elif char.isalpha():
        consonets += 1

print("Vowels:", vowels)
print("Consonants:", consonets)

# Find the first and last character	Indexing
exam="a two z"
first_char=exam[0]
last_char=exam[-1]
print("first char: {0} and last_char is {1}".format(first_char, last_char))#first char: a and last_char is z

#Swap first and last characters
name_swamp="Varun T"
swap_res=name_swamp[-1] + name_swamp[1:-1] + name_swamp[0]
print(swap_res)

#Count words in a string
string_names="varun naveen tarun manoj"
words=string_names.split(" ")
print(words)
print(len(words))

#Capitalize the first letter of each word
sub_title="i am learning python"
cap_title=sub_title.title()
print(cap_title)#I Am Learning Python

##Count occurrences of a character
text = "my name is varun"

for char in text:
 result = text.count("a")
 print("Occurrences:", result)#2
    
    