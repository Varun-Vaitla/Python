#range is built in type of python we need to use range() to create range object
#syntax(start,stop,step)
"""
1.it starts form 0
2.it will exclude ending value
3.it will not store its values in memory
4it is mainly used in for loop

"""
for i in range(11):
    print(i)
    """
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    """
#for printing odd and even numbers

#odd
for o in range(1,10,2):
    print(o)
    """
    1
    3
    5
    7
    9
    """
#even
for e in range(0,11,2):
    print(e)
    """
    2
    4
    6
    8
    10
    """