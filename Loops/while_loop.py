# #print 1 to 10
# num=0
# while num<=10:
#     print(num)
#     num += 1

# #break
# i=1
# while i<=10:
#     print(i)
#     if i==5:
#         break
#     i += 1

#program to undersatnd while and brake in details
# while True:
#     num=int(input("Enter Number to continue iteration || Enter 0 to stop : "))
#     if num==0:
#         print("you enterd 0 so program stop 🥵")
#         break
#     print(f"{num} so continue ⏭️")

# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end="")
#     print()

# for i in range(1,6):
#     print("*" * i)
#     """
#     *
#     **
#     ***
#     ****
#     *****
#     """
# for i in range(6,0,-1):
#     print("*" * i)
"""
*****
****
***
**
*
"""

#continue

# for num in range(1,11):
#     if num%2==0:
#         continue
#     print(num)

# for num in range(1,11):
#     if num%2==1:
#         continue
#     print(num)

#print numbers form 1 to 100 but not numbers divides by 7
n = 1

while n <= 100:
    if n % 7 == 0:
        n += 1
        continue

    print(n)
    n += 1