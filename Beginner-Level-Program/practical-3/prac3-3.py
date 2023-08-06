#Aim : Write a python program to accept a number and print its absolute value.

print('Program to find absolute value of number')
print('*'*45)

num=int(input('Enter a number:'))
if (num<0):
        print('Absolute of ',num,'=',(num*-1))
else:
        print('Absolute of ',num,'=',num)