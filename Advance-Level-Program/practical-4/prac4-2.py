"""
Aim : Program to demonstrate the use of regular expressions

Consider the string str="Global Warming". 
Write statements in python to implement the following:
a. To display the last four characters.
b. To display the substring starting from index 4 and ending at
   index 8.
c. To check whether string has alphanumeric characters or not.
d. To trim the last four characters from the string.
e. To trim the first four characters from the string.
#f. To display the starting index for the substring "Wa".
#g. To change the case of the given string.
h. To check if the string is in title case.
i. To replace all the occurrences of letter "a" in the string with "*".
j. Create a new string which contains
        para="Python RoyalCamp hosted by prof.mudassar ansari.
        Kindly contact us on:
        Teacher Incharge: mudassar.ansari@gmail.com ,
        Dept: rccsdept@gmail.com and 
        Student Coordinator: student@mail.com"
k. Extract the Professor name.
l. Print the email id and count given in paragraph
"""

from re import *

#program
str="Global Warming"
print(str)
print('Last 4 character: ',end='')
last4=findall('\D\D\D\D$',str)
print(last4[0])
#for ch in last4:
#       print(ch,end='')
#print()

print('Character 4th and 8th index: ',end='')
mid=findall('^....(.....)',str,S)
print(mid[0])
#for ch in mid:
#        print(ch,end='')
#print()


print('\nString contain alphanumeric character or not: ',\
      end='')
if(match('^[A-Za-z0-9]*$',str)):
        print('True')
else:
        print('False')
      
print('Trim Last 4 character trim')
str1=sub('\D\D\D\D$','',str)
print(str1)

print('Trim First 4 character trim')
str2=sub('^\D\D\D\D','',str)
print(str2)

"""
print('Index of \'Wa\' in ',str,': ',end='')
i=str.index("Wa")
print(i)

print('Change case to title')
str3=str.title()
print(str3)
"""

print('Check whether string is in title')
if(match('^[A-Z][a-z]*\s[A-Z][a-z]*',str)):
        print(str,'in title case')
else:
        print(str,'not in title case')
  
print("Replace all letter \"a\" in the string with \"*\"")
str4=sub('a','*',str)
print(str4)

print('Paragraph Operations')
para="""Python RoyalCamp hosted by Prof.Mudassar Ansari.
Kindly contact us on:
Teacher Incharge: mudassar.ansari@gmail.com ,
Dept: royalcompsci@gmail.com and 
Student Coordinator: student@mail.com
"""
print('Print the Professor Name')
prof=findall('Prof.[A-Za-z\s]*',para,I)
print(prof[0])

print('Print the email addresses and count')
addresses = findall('[\w\.|\_]+@[\w\.]+[com|co.in]',para)
for address in addresses:
        print(address)
        
print('Total Email Id: ',len(addresses))


"""
m. replace student email id with yours email id

print('Student Email Id')
newemail=sub('student\.|\_]+@[\w\.]+','md@gmail.com',para)
print(newemail)

print('Index of \'Wa\' in ',str,': ',end='')
mid=findall('^.......(..)',str)
i=str.index(str(mid))
print(i)
"""

