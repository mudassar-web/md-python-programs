#Aim : Create different shapes on Canvas using python GUI

from tkinter import *

top=Tk()
top.title("Canvas Example")

C=Canvas(top, bg="aqua", height=250, width=400)

coord=10, 50, 250, 210
arc=C.create_arc(coord, start=0, extent=180, fill="green")

line=C.create_line(10,10,250,250,fill="black")

rect=C.create_rectangle(50, 25, 150, 75, fill="orange")

oval=C.create_oval(10, 10, 50, 50, fill="red")

points=[150, 100, 200, 120, 240, 180, 210,\
        200, 150, 150, 100, 200]
poly=C.create_polygon(points, outline='black', \
                    fill='gray', width=2)

C.pack()

top.mainloop()