# #creating new window
# from tkinter import *

# def create_window():
#     # first method
#     new_window=Toplevel() #create a new window on top of other window ,linked with base window
#     # second method
#     new_window=Tk() #create a new independent window


# window=Tk()  #obj=constructor()

# btn=Button(window,text="create new window",width=25,command=create_window)
# btn.pack()
# window.mainloop()


# creating tabs on a window
from tkinter import *
from tkinter import ttk

window=Tk()  
window.geometry("500x500")
note=ttk.Notebook(window)
tab1=Frame(note)
tab2=Frame(note)

note.add(tab1,text="tab1")
note.add(tab2,text="tab2")

Label(tab1,text="tab1 information",height=25,width=50).pack()
Label(tab2,text="tab2 information",height=25,width=50).pack()


note.pack(expand=True,fill="both")

window.mainloop()


