#Aim : Program to calculate square of a number using function

def square(n):
    return(n**2)

print("""program to calculate square
      of a number""")
num=int(input("Enter number:"))
print("Square of ",num," is ",square(num))

s=square(8)
print('square of 8=',s)