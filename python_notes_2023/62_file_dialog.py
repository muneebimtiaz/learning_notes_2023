# error 

from tkinter import *
from tkinter import filedialog

window=Tk()
def open():
    filepath=filedialog.askopenfilename(initialdir="C:\\Users\\DELL\\OneDrive\\Desktop")
# open()  write()/read()  close()
    fff=open(filepath,"r")
    print(fff.read())
    fff.close()
button=Button(window,text="open",command=open)
button.pack()
window.mainloop()