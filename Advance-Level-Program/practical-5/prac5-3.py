#Aim : Design a GUI form to accpet 3 subject marks and calculate total, percentage and assign grade

from tkinter import *

def calculate():
    s1=int(e1.get())
    s2=int(e2.get())
    s3=int(e3.get())
    total=s1+s2+s3   
    per=float(total)/3
    grade=""
    if per>=70 :
        grade="O"
    elif per<70 and per>=65 :
        grade="A"
    elif per<65 and per>=55 :
        grade="B"
    elif per<55 and per>=40 :
        grade="C"
    else :
        grade="Fail"
    
    t.set(total)
    p.set(per)
    g.set(grade)


window=Tk()
window.title("Result")

l=Label(window,text="Calculate Percentage and Grade")
l.pack(side=TOP)

#bd means border,releif means border style
f1=Frame(window,bd=2,relief=SOLID)
f1.pack()

l1=Label(f1,text="Subject 1 : ")
l1.pack(side=LEFT)

e1=Entry(f1)
e1.pack(side='left')

f2=Frame(window,bd=2,relief=SOLID)
f2.pack()

l2=Label(f2,text="Subject 2 : ")
l2.pack(side='left')

e2=Entry(f2)
e2.pack(side='left')

f3=Frame(window,bd=2,relief=SOLID)
f3.pack()

l3=Label(f3,text="Subject 3 : ")
l3.pack(side='left')

e3=Entry(f3)
e3.pack(side='left')

f4=Frame(window,bd=2,relief=SOLID)
f4.pack()

l4=Label(f4,text="Total Marks: ")
l4.pack(side='left')

#StringVar() helps to define dynamic variable
#and value to that variable can be set from function

t=StringVar()
e4=Entry(f4,textvariable=t,state=DISABLED)
e4.pack(side='left')

f5=Frame(window,bd=2,relief=SOLID)
f5.pack()

l5=Label(f5,text="Percentage : ")
l5.pack(side='left')

p=StringVar()
e5=Entry(f5,textvariable=p,state=DISABLED)
#state DISABLED means readonly textbox 
e5.pack(side='left')

f6=Frame(window,bd=2,relief=SOLID)
f6.pack()

l6=Label(f6,text="Grade : ")
l6.pack(side='left')

g=StringVar()
e6=Entry(f6,textvariable=g,state=DISABLED)
e6.pack(side='left')

b1=Button(window,text="Calculate",command=calculate)
b1.pack()
window.mainloop()
