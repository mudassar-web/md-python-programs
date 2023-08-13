#Aim : Program to validate user input using re module

import re

def find():
    str1='SitaRam'
    if re.search('Ram$', str1):
        print("Ram found in end of string")
    else:
        print("Ram not found in end of string")

    if re.search('^Sita', str1):
        print("Sita found in start of string")
    else:
        print("Sita not found in start of string")
        
#"[a-zA-Z0-9(\.|\_)]+@(\w+\.)+(com|org|net|edu|co.in)"
def emailcheck(str):
    emailpattern = "[a-zA-Z0-9(\.|\_)]+@(\w+\.)+(com|org|net|edu|co.in)"
    if(re.match(emailpattern,str)):
        #print(str)
        print("Email format is correct!!!")
    else:
        print("Email is incorrect!!!")

def pincodecheck(str):
    pincodepattern = "\d\d\d\d\d\d"
    if(re.match(pincodepattern,str) and len(str)==6):
        #print(str)
        print("Pincode format is correct!!!")
    else:
        print("Pincode is incorrect!!!")

def phonenocheck(str):
    phonepattern = "\+\d\d\-\d\d\d\d\d\d\d\d\d\d"
    if(re.match(phonepattern,str)):
        #print(str)
        print("Phone number format is correct!!!")
    else:
        print("Phone number is incorrect!!!")

#^(http(s)?)://(www.)([a-zA-Z]){3,}.([a-zA-Z]){2,3}$
def weburlcheck(str):
    pattern = "^(http(s)?)://(www.)([a-zA-Z]){3,}.([a-zA-Z]){2,3}$"
    if(re.match(pattern,str)):
        #print(str)
        print("Web url format is correct!!!")
    else:
        print("Web url is incorrect!!!")

#program
print('Program to use Regular Expression')
find()
str1=input("Enter email id (abc@gmail.com):")
emailcheck(str1)
pincodecheck(input("Enter pincode (401107):"))
phonenocheck(input("Enter phone number (+91-9876543210):"))
weburlcheck(input("Enter web url (http://www.google.com):"))









