# 1. if statement

# Executes code when a condition is True.
# syntax: if condition:
           # statement
age=int(input("Enter your age: "))
if age>=18:
    print("you are eligibal for vote")


num=int(input("Enter Number to chech it is +ve or -ve: "))
if num>=0:
    print(f"{num} is +ve")


char=input("Enter char to check it is vowel or not: ")
if char in "aeiouAEIOU":
    print(f"{char} is vowel")