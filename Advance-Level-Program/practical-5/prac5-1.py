#Aim : Create window with Button widget, when user click the button a message box should appear on the screen

import tkinter
#import tkinter.messagebox

def helloCallBack():
   tkinter.messagebox.showinfo("Hello Python",\
               "Hello World")

#program   
top = tkinter.Tk()
top.title('Button Click Window')

B=tkinter.Button(top,text ="Click Me to See Message",\
            command = helloCallBack)

B.pack()

top.mainloop()


