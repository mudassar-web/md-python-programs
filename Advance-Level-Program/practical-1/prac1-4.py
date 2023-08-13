#Aim : Write multiple lines to a file

def write_multiple_line(fn):
    fobj=open(fn,"w")
    fobj.write("This file is created by \n \tPYTHON\n")
    fobj.write("File \n \t \t contains multiple lines\n")
    fobj.write("FYBSC \n \tCS Batch 2\n")
    fobj.close()

#program
fname=input("Enter file name:")
write_multiple_line(fname)
print('File created in a Folder')
   
