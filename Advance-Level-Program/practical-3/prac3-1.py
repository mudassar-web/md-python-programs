#Aim : To accepts a number and prints it reciprocal using exception handling

print('Program to calculate reciprocal')
ans='y'
while ans=='y' or ans=='Y':
    try:
        x = int(input("Enter an integer: "))
        r = 1/x
    except ValueError:
        print("Error : Required an integer only.")
        print("Please try again.")
        print()
    except ZeroDivisionError:
        print("Error : Number entered is Zero.")
        print("Please try again.")
        print()
    else:
        print("The reciprocal of ",x," is ",r)
    finally:
        ans=input('Do you want to continue(y|Y):')


#OUTPUT
#Enter an integer: a
#Error : Required an integer only.
#Please try again.

#Enter an integer: 1.2
#Error : Required an integer only.
#Please try again.

#Enter an integer: 0
#Error : Number entered is Zero.
#Please try again.

#Enter an integer: 4
#The reciprocal of 4 is 0.25