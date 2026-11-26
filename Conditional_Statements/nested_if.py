"""
4. Nested if statement

An if statement inside another if statement.
syntex: if condition1:
           if condition2:
              statement
"""

#example of star health insurence 
age=int(input("Enter your age: "))
if age<65:
    if age>=55:
       print("your premium is 2500")
    elif age>=40:
        print("your primium is 1800")
    elif age>=25:
        print("your primium is 1000")
    else:
        print("youe primium is 500")

else:
    print("your age is not eligible for Star health insurence")