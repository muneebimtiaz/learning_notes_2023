from tkinter import *
from tkinter import colorchooser #submodule 

def click():
    color=colorchooser.askcolor()
    colorhex=color[1]
    window.config(bg=colorhex)

window=Tk()
window.geometry("500x500")
button=Button(window,text="Select",command=click)
button.pack()

window.mainloop()