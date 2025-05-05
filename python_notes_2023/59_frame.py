# frame is a rectangular containter to group and hold widgets
from tkinter import *
window=Tk()
window.geometry("500x500")

frame=Frame(window,
            bg="orange",
            bd=5,
            relief=SUNKEN)
frame.place(x=100,y=100)
btn=Button(frame,text="Button1",width=10,bd=4).pack(side=TOP)
btn=Button(frame,text="Button2",width=10,bd=4).pack(side=LEFT)
btn=Button(frame,text="Button3",width=10,bd=4).pack(side=RIGHT)
btn=Button(frame,text="Button4",width=10,bd=4).pack(side=BOTTOM)
window.mainloop()