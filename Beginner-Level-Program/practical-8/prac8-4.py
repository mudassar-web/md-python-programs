#Aim : Program to print all even number till n terms using functions

def myeven(n):
    for i in range(1,n+1):
        if (i%2==0):
            print(i,end=' ')

print("Even number list")
n=int(input("Enter number:"))
myeven(n)