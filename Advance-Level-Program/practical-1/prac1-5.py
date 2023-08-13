#Aim : Working with path and directory functions 

from os import *

#To Print Current working direcorty
print("Current working directory=",path.abspath(""))
print("Current working directory=",getcwd())
print()

#To Print Contents of directory
print("Print Contents of directory")
d=getcwd()
for name in listdir(d):
    print(path.join(d,name))
print()

#To change directory
chdir("C:\\Python34")
print("Current working directory=",getcwd())
#To Print Contents of directory new directory
print("Print Contents of new directory")
d=getcwd()
for name in listdir(d):
    print(path.join(d,name))


#OUTPUT
#Current working directory= C:\Python34\Sem2
#Current working directory= C:\Python34\Sem2
#
#Print Contents of directory
#C:\Python34\Sem2\lamb.txt
#C:\Python34\Sem2\mary.txt
#C:\Python34\Sem2\P1A.py
#C:\Python34\Sem2\P1B.py
#C:\Python34\Sem2\P2A.py
#C:\Python34\Sem2\P2B.py
#
#Current working directory= C:\Python34
#Print Contents of new directory
#C:\Python34\DLLs
#C:\Python34\Doc
#C:\Python34\Exception
#C:\Python34\include
#C:\Python34\Lib
#C:\Python34\libs
#C:\Python34\LICENSE.txt
#C:\Python34\mdexception.py