#Aim: Program to print fibonacci series upto n term

print('Program to print fibonacci series upto n terms')
n=int(input('Enter number of terms:'))
a=0
b=1
c=1
print(a,b,end=' ')
for i in range(3,(n+1)):
    c=a+b
    print(c,end=' ')
    a=b
    b=c