#Aim : Program to accept a 3 number and find greatest number out of them.

print('Program to find greatest of 3 number.')
print('*'*40)

a=int(input('Enter number 1:'))
b=int(input('Enter number 2:'))
c=int(input('Enter number 3:'))

if(a>b and a>c):
        print(a,' is greatest of ',b,' and ',c)
elif (b>a and b>c):
        print(b,' is greatest of ',a,' and ',c)
else:
        print(c,' is greatest of ',a,' and ',b)
