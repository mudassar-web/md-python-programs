#Aim : To read the content from one file and write it to another file

def make_anothertext_file(f1,f2):
    fone=open(f1,'r')
    data=fone.read()
    fone.close()
    ftwo=open(f2,'w')
    ftwo.write(data)
    ftwo.close()
    
import os
print('File copy program')
s=""
file1=""
file2=""
while s!=".txt":
    file1=input("Enter a file name:")
    fext=os.path.splitext(file1)
    s=fext[1]
    if s==".txt":
        break
    else:
        print("Enter only text file (.txt)")
        
if os.path.isfile(file1):
    print(file1," exists.")
    s=""
    while s!=".txt":
        file2=input("Enter a new file name:")
        fext=os.path.splitext(file2)
        s=fext[1]
        if s==".txt":
            break
        else:
            print("Enter only text file (.txt)")

    #creating a new text file
    make_anothertext_file(file1,file2)
    print(file2," created in python folder")         
else:
    print(file1," not exists.")

#OUTPUT
#Enter a file name:mary.txt
#mary.txt  exists.
#Enter a new file name:lamb.txt
#lamb.txt  created in python folder
    

