#Aim : Write a program to accept principle amount, no. of year and rate of interest. Calculate simple interest.

p=int(input('Enter principle amount:'))
n=int(input('Enter no. of year:'))
r=float(input('Enter rate of interest:'))

si=(p*n*r)/100

print("Simple Interest:",si)