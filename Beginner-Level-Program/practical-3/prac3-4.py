#Aim : Program to accept year and identify whether it is a leap year or not 

print('Program to identify leap year')
print(25*'*')
year=int(input('Enter a year:'))
if (year%400==0):
    print(year,' is a leap year')
elif (year%100==0):
    print(year,' is not a leap year')
elif (year%4==0):
    print(year,' is a leap year')
else:
    print(year,' is not a leap year')