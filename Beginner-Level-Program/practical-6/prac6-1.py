"""
Aim : Program related to study of List functions
1. Create a list lst1 with elements 1,2,3,4,5,6,7
2. Print 1st element,the range of elements 2-5 and last 3 elements.
3. Create a list lst2 with elements a,b,c,d,e.
4. Concatenate lst1 with lst2 and save it in lst3.
5. Change the 2nd value of lst3 to 4.
6. Delete the 3rd value from lst3.
7. Print lst3 4 times.
8. Check if 3 is present in lst3.
9. Display the count of number 4 in lst3.
10.Append 8 to lst3.
11.Insert character 'a' at 5th position.
12.Print individual elements of lst3.
13.Print reverse and length of the lst3.
14.Sort the list lst1 and lst2.
15.Find the maximum and minimum of lst1 and lst2.
"""

print('program related to study of List functions')
print('-'*40)
lst1=[1,2,3,4,5,6,7]
print(lst1)
print('1st element of lst1:',lst1[0])
print('Range of element from 2 - 5:',lst1[1:5])
print('Last 3 element of lst1:',lst1[4:])
print('Last 3 element of lst1:',lst1[-3:])
lst2=['a','b','c','d','e']
print(lst2)
lst3=lst1+lst2
print(lst3)
lst3[1]=4
print(lst3)
del(lst3[2])
print(lst3)
print(lst3*4)
for i in lst3:
    print(i)
print('3 exists in lst3:',3 in lst3)
print('Count of 4:',lst3.count(4))
lst3.append(8)
print(lst3)
lst3.insert(5,'a')
print(lst3)
lst3.reverse()
print(lst3)
print('Length of lst3:',len(lst3))
lst1.sort()
print('Sorted lst1:',lst1)
lst2.sort()
print('Sorted lst2:',lst2)
print('Minimum of lst1:',min(lst1),'\nMaximum of lst1:',max(lst1))
print('Minimum of lst2:',min(lst2),'\nMaximum of lst2:',max(lst2))