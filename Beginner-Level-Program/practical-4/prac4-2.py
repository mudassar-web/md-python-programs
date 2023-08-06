"""Aim : Program to accept a number and print its factorial
	5!=5x4x3x2x1=120
"""

print('Program to calculate factorial of a number')
print('-'*45)
num=int(input('Enter a number:'))
i=num
fact=1
while (i>=1):
        fact=fact*i
        i-=1
print("Factorial of ",num," is ",fact)