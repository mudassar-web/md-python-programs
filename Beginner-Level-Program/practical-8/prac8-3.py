#Aim : Program to use math module and create square function and its implementation.

import math
def mysqr(num):
    return (math.pow(num,2))

print('Program related to function')
print('-'*25)
n=int(input('Enter a number:'))
print("Square of ",n,"=",mysqr(n))