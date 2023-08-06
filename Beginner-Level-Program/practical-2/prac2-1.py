#Aim : Write a program to accept 5 integer and print average of 3 and 5 number independently.

a=int(input('Enter number1:'))
b=int(input('Enter number2:'))
c=int(input('Enter number3:'))
d=int(input('Enter number4:'))
e=int(input('Enter number5:'))

avg3=(a+b+c)/3

avg5=(a+b+c+d+e)/5

print(25*"*")
print('Average of 3 number=',avg3)
print('Average of 5 number=',avg5)
print(25*"*")