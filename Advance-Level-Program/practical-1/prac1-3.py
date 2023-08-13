#AIM : Reading multiple lines from a file

def read_multiple_lines(fn,num):
    count=1
    fobj=open(fn,"r")
    lines=fobj.readlines()
    fobj.close()
    for line in lines:
        print(line)
        if count==num:
            break
        count+=1
        
#program
print('Program to read multiple lines from file')
fname=input("Enter a file name:")
no=int(input("Enter no. of lines to be read:"))
read_multiple_lines(fname,no)





