"""Aim: Program to accept a number and print its mathematical table.

5 x 1 = 5
5 x 2 = 10
.
.
.
5 x 10 = 50"""

print('Program to print mathematical table')
print('-'*40)
num=int(input('Enter a number:'))
i=1
while (i<=10):
	print(num," x ",i," = ",(num*i))
	i=i+1