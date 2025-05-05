from tkinter import *
window=Tk()

cvs=Canvas(window,width=500,height=500)
# # line
# cvs.create_line(0,500,500,0,fill="blue",width=5)
# cvs.create_line(0,0,500,500,fill="red",width=5)
# cvs.create_line(200,100,400,300,fill="green",width=5)
# cvs.create_line(100,200,300,400,fill="green",width=5)
# cvs.create_line(100,100,400,400,fill="green",width=5)

# rectangle
cvs.create_rectangle(100,100,300,200,fill="purple",width=5)


cvs.pack()

window.mainloop()