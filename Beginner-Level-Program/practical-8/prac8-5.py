#Aim : Program to accept number and print the factorial using user define functions.

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return(fact)

print("Factorial Program:")
n=int(input("Enter number:"))
print("Factorial of ",n," is ",factorial(n))