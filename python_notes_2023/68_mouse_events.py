from tkinter import *
from tkinter import colorchooser #submodule 

def click(event):
    print("you type return keyword" + event.keysym)
    # label.config(text=event.keysym)

window=Tk()
# window.bind("<Return>",click) 
window.bind("<Button-1>",click) 
label=Label(window,font=("impact",100))
label.pack()

window.mainloop()