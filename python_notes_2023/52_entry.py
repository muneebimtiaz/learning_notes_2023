# from tkinter import *
# window=Tk()
# label=Label(window,text="f_name",width=10).grid(row=0,column=0)
# label=Label(window,text="l_name",width=10).grid(row=1,column=0)
# entry=Entry(window).grid(row=0,column=1)
# entry2=Entry(window).grid(row=1,column=1)
# window.mainloop()


from tkinter import *

def submit():
    type=entry_box.get()
    print(type)
def delete():
    entry_box.delete(0,END)
def backspace():
    entry_box.delete(len(entry_box.get())-1,END)   # DMAS Rule


win=Tk()
# entry box
entry_box=Entry(win,
        font=("Arial",14),
        fg="black",
        # bg="grey"
        )
# entry_box.insert(0,"hello")
# entry_box.config(show="*")
# entry_box.config(state=DISABLED)

entry_box.pack(side=LEFT)

# button
b=Button(win,text="Submit",activebackground="red",activeforeground="black",command=submit,font=("Arial",10),bg="gray",bd=4,relief=RAISED)
b.pack(side=RIGHT)
b=Button(win,text="Delete",activebackground="red",activeforeground="black",command=delete,font=("Arial",10),bg="gray",bd=4,relief=RAISED)
b.pack(side=RIGHT)
b=Button(win,text="Backspace",activebackground="red",activeforeground="black",command=backspace,font=("Arial",10),bg="gray",bd=4,relief=RAISED)

b.pack(side=RIGHT)
win.mainloop()