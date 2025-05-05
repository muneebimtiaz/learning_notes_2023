
# window
from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)
def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())
def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())

win=Tk()
win.geometry("1000x1000")

win.bind("<Up>",move_up)
win.bind("<Down>",move_down)
win.bind("<Right>",move_right)
win.bind("<Left>",move_left)

icon=PhotoImage(file="C:\\Users\\DELL\\Downloads\\py_out (13).png")
label=Label(win,image=icon)
label.place(x=0,y=0)
win.mainloop()



# canvas
from tkinter import *

def move_up(event):
    cvs.move(cpc,0,-10)
def move_down(event):
    cvs.move(cpc,0,10)
def move_right(event):
    cvs.move(cpc,10,0)
def move_left(event):
    cvs.move(cpc,-10,0)

win=Tk()
cvs=Canvas(win,width=500,height=500)
cvs.pack()


win.bind("<Up>",move_up)
win.bind("<Down>",move_down)
win.bind("<Right>",move_right)
win.bind("<Left>",move_left)

icon=PhotoImage(file="C:\\Users\\DELL\\Downloads\\py_out (13).png")
cpc=cvs.create_image(0,0,image=icon,anchor=NW)

win.mainloop()