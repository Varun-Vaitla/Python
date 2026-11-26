# for i in range(0,11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# for ch in "varun":
#     print(ch)

# name="varun"
# for ch in range(len(name)):
#     print(name[ch])

# for ch in reversed(name):
#     print(ch)

# name="varun"
# for index,ch in enumerate(name):
#     print(index,ch)

#count number of times the char is occured in str
# text="banana"
# for char in text:
#     print(char," : ",text.count(char))

#revers a string without slicing
text="varun"
result=""
for ch in text:
    result = ch + result
print(result)

#count upper and lower case char in str 
sample="Varun V M"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
count_upper=0
count_lower=0
for ch in sample:
    if ch in lower:
        count_lower+=1
    elif ch in upper:
        count_upper +=1
print(f"uper Case :{count_upper} , lower case :{count_lower}")
#......................................#
sample1="My Name Is Varun"
upper_count=0
lower_count=0
for ch in sample1:
    if ch.isupper():
       upper_count +=1
    elif ch.islower():
        lower_count +=1
print(f" lowecsae char :{lower_count}, uppercase char: {upper_count}")
    