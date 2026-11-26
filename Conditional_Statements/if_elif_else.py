"""
3. if-elif-else statement

Checks multiple conditions.

syntax: if condition1:
          statement
        elif condition2:
          statement
        else:
          statement
"""
marks=float(input("Enter your Marks: "))
if marks>=90:
    print(f"Grade A: you have got {marks} marks")
elif marks>=75:
    print(f"Grade B: you have got {marks} marks")
elif marks>=60:
    print(f"Grade C: you have got {marks} marks")
elif marks>=35:
    print(f"Grade D: you have got {marks} marks")
else:
    print(f"Fale😂: you have got {marks} marks")