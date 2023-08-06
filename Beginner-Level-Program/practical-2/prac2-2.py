#Aim : Write a program to accept 3 subject marks and print total and percentage. [Marks are considered out of 100]

sub1=int(input("Enter marks of subject1:"))
sub2=int(input("Enter marks of subject2:"))
sub3=int(input("Enter marks of subject3:"))

total=sub1+sub2+sub3
percent=(total/3)

print("Total:",total)
print("Percentage:",percent,"%")