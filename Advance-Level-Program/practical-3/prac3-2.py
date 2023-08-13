#Aim :To accept positive number using Exception handling with Raise

def positive_num(n):
    if n<0:
        raise Exception(n)
    return n

#program
print('Program to accept postive number using Exception handling with Raise')
try:
    num=int(input('Enter a positive number:'))
    no=positive_num(num)
except Exception as e:
    print('You entered ',e.args[0],' which is an invalid input.')
else:
    print('Number:',no)
    
"""
#program
print('Program to accept postive number using Exception handling with Raise')
num=int(input('Enter a positive number:'))
no=positive_num(num)
print('Number:',no)
"""  
