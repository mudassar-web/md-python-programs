#Aim : Create a Biodata form in python using GUI 

from tkinter import *

def getData():
    print("---------------------------------")
    print("Name="+e1.get())
    print("Age="+e2.get())
    if gen.get()==1:
        print("Gender=Male")
    elif gen.get()==2:
        print("Gender=Female")
    print("Contact No="+e3.get())
    print("Address="+e4.get())
    strhob=""    
    if read.get()==3:
        strhob=strhob+"Reading,"
    if music.get()==4:
        strhob=strhob+" Music,"
    if internet.get()==5:
        strhob=strhob+" Surfing Internet"          
    print("Hobbies="+strhob)
    print("---------------------------------")



#main program
win=Tk()
win.title("Biodata Example")

f1=Frame(win,bd=5,relief=RAISED)
f1.pack()

l1=Label(f1,text="Name:")
l1.grid(row=0,column=0)

e1=Entry(f1)
e1.grid(row=0,column=1)

l2=Label(f1,text="Age:")
l2.grid(row=1,column=0)

e2=Entry(f1)
e2.grid(row=1,column=1)

lg=Label(f1,text="Gender:")
lg.grid(row=2,column=0)

f2=Frame(f1,bd=3,relief=SOLID)
f2.grid(row=2,column=1)

gen=IntVar()
r1 = Radiobutton(f2,text="Male",variable=gen,value=1)
r1.grid(row=0,column=0)

r2 = Radiobutton(f2,text="Female",variable=gen,value=2)
r2.grid(row=0,column=1)

l3=Label(f1,text="Contact No:")
l3.grid(row=3,column=0)

e3=Entry(f1)
e3.grid(row=3,column=1)

l4=Label(f1,text="Address:")
l4.grid(row=4,column=0)

e4=Entry(f1)
e4.grid(row=4,column=1)

l5=Label(f1,text="Hobbies:")
l5.grid(row=5,column=0)

f3=Frame(f1,bd=3,relief=SOLID)
f3.grid(row=5,column=1)

read=IntVar()
c1=Checkbutton(f3,text="Reading",variable=read,onvalue=3,\
               offvalue=0)
c1.grid(row=0,column=0,sticky=NW)

music=IntVar()
c2=Checkbutton(f3,text="Music",variable=music,onvalue=4,\
               offvalue=0)
c2.grid(row=1,column=0,sticky=W)

internet=IntVar()
c3=Checkbutton(f3,text="Surfing Internet",\
               variable=internet,onvalue=5,offvalue=0)
c3.grid(row=2,column=0,sticky=SW)

b1=Button(f1,text="Click",command=getData)
b1.grid(row=6,column=0,columnspan=2)

win.mainloop()














"""
text = Text(win)
text.configure(font='helvetica 12')
text.pack(side=BOTTOM)

win.mainloop()"""
