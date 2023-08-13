#Aim : To select a number from spinbox and check whether it appear in any of 3 textbox

from tkinter import *
from random import *

def luck():
    userval=s1.get()    
    v1.set(randint(1, 9))
    v2.set(randint(1, 9))
    v3.set(randint(1, 9))
    
    print(e1.get(),", ",e2.get(),", ",e3.get())
       
    if e1.get()==userval or e2.get()==userval or e3.get()==userval :
        lb1.insert(END," Lucky")
    else :
        lb1.insert(END," UnLucky")

#program
win = Tk()
win.title("Lucky 7 Appilcation")

f1=Frame(win,bd=5,relief=GROOVE)
f1.pack()

l=Label(f1,text="Select your lucky number:")
l.grid(row=0,column=0)

s1=Spinbox(f1, from_=1, to=9)
s1.grid(row=0,column=1)

v1=IntVar()
e1=Entry(f1,textvariable=v1,state=DISABLED)
e1.grid(row=1,column=0)

v2=IntVar()
e2=Entry(f1,textvariable=v2,state=DISABLED)
e2.grid(row=1,column=1)

v3=IntVar()
e3=Entry(f1,textvariable=v3,state=DISABLED)
e3.grid(row=1,column=2)

b1=Button(f1,text="Get Lucky",command=luck)
b1.grid(row=2,columnspan=3)

lb1=Listbox(f1)
lb1.grid(row=3,columnspan=3)

win.mainloop()
