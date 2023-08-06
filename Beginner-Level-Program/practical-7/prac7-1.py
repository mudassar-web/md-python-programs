"""
Aim : Program to implement functions related to TUPLE
1. Create a tuple tup1 with 1,2,3,4,5,6,7
2.Print 1st element,the range of elements 2-5 and last 3 elements
3.Create a tuple tup2 with elements a,b,c,d,e.
4.Create tup3 by concatenating tup1 and tup2.
5.Delete tup3.
6.Print tup1 4 times.
7.Check if 6 exists in tup1 and 'f' exists in tup2.
8.Print individual elements of tup1 and tup2 in horizontal line. 
9.Find the length of tup1 and tup2
10.Find the maximum and minimum of tup1 and tup2.
"""

print('Program to implement functions related to TUPLE')
print("-"*40)
tup1=(1,2,3,4,5,6,7)
print(tup1)
print("First element:",tup1[0])
print("Element between 2 - 5:",tup1[1:5])
print("Last 3 element:",tup1[-3:])
tup2=('a','b','c','d','e')
print(tup2)
tup3=tup1+tup2
print(tup3)
del(tup3)
print(tup1*4)
print('Elements of tup1:')
for i in tup1:
    print(i)
print('Elements of tup2:')
for i in tup2:
    print(i)
print('6 exists in tup1:',6 in tup1)
print('f exists in tup2:','f' in tup2)
print('Length of tup1:',len(tup1),  \
      '\nlength of tup2:',len(tup2))
print('Minimum of tup1:',min(tup1),  \
      '\nMaximum of tup1:',max(tup1))
print('Minimum of tup2:',min(tup2),  \
      '\nMaximum of tup2:', \
         max(tup2))
print("-*"*20)