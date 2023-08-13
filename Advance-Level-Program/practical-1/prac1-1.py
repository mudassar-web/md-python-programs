#Aim : To accepts text from user and write that contents to a file

import os

def make_text_file(fn):
    fo=open(fn,'w')
    data=input("Enter content:")
    fo.write(data)
    fo.close()

#program
print('Program to accept contents from user '\
      'and write that content in file')
s=""
fname=""
while s!=".txt":
    fname=input("Enter a new file name:")
    fext=os.path.splitext(fname)
    print(fext)
    s=fext[1]
    if s==".txt":
        break
    else:
        print("Enter only text file (.txt)")

make_text_file(fname)
print("file created in python folder")


#OUTPUT
#Enter a new file name:mary.jpg
#Enter only text file (.txt)
#Enter a new file name:mary.doc
#Enter only text file (.txt)
#Enter a new file name:mary.txt
#Enter content:mary had a little lamb
#file created in python folder
