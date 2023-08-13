"""Aim : Write a GUI program in Python. To accept name and 
age from user in entry box and check whether user is eligible for voting or not"""

from tkinter import *
#import tkinter.messagebox

def fetch():
    name=ent.get()
    age=int(ent1.get())
    if(age>=18 and age<=110):
        str1=name+" Eligible for Voting"
        messagebox.showinfo("Info",str1)
    else:
        str1=name+" Not Eligible for Voting"
        messagebox.showinfo("Info",str1)    


#program
root = Tk()
root.title('Voting Age Eligibility')

l=Label(root,text="Enter name")
l.pack(anchor=W)
ent = Entry(root)         
ent.pack(anchor=W)

l1=Label(root,text="Enter age")
l1.pack(anchor=W)
ent1 = Entry(root)         
ent1.pack(anchor=W)

btn = Button(root, text='Eligibility', command=fetch) 
btn.pack(anchor=CENTER)

root.mainloop()

