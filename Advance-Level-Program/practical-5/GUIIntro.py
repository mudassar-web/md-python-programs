#Aim: Introduction to GUI Programming

#program
import tkinter #tkinetr module used for GUI 

root=tkinter.Tk()  #Main Window Screen
root.title('My First GUI Application')
# Title set on window

L1=tkinter.Label(root,text='Introduction to GUI Programming',bg='Blue',fg='White')
L1.pack()
# pack() is used to add widgets on main window

root.mainloop()
#mainloop() which accepts user interaction
