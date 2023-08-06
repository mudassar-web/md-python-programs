"""
Aim : To implement different functions related to dictionaries.

1. Create a dictonary studentinfo containing 3 student name and rollno
2. Print only name in sorted order and rollno in sorted order
3. Add new student to studentinfo and print length of studentinfo.
4. Create a dictonary studentinfo1 containing 2 new student name and rollno
5. print all elements of studentinfo using a for loop.
6. Merge studentinfo1 into studentinfo
7. Remove any one element from studentinfo
8. Remove all elements from studentinfo1
9. Delete studentinfo1
"""

print('Program to implement functions related to Dictionaries')
print("-"*40)
studentinfo={'asif':31,'mudassar':30,'talib':27}
print(studentinfo)
print('All Names')
print(studentinfo.keys())
print(sorted(studentinfo.keys()))
print('All Ages')
print(studentinfo.values())
print(sorted(studentinfo.values()))
#studentinfo=
studentinfo.update({'james':27})
print("Total enteries in studentinfo:",len(studentinfo))
studentinfo1={'abdul':31,"kalim":28}
print(studentinfo1)
print('Element in studentinfo:')
for i in studentinfo:
    print(i)
for i in studentinfo.values():
    print(i)
print('Element in studentinfo1:')
for i in studentinfo1:
    print(i)
for i in studentinfo1.values():
    print(i)

studentinfo.update(studentinfo1)
print(studentinfo)

del(studentinfo['abdul'])
print(studentinfo)

studentinfo1.clear()
print('All elements are removed:',studentinfo1)

del(studentinfo1)
#print(studentinfo1)















