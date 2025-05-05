# from tkinter import *
# window=Tk()

# listbox=Listbox(window)
# listbox.insert(1,'attack on titan')
# listbox.insert(2,'onepiece')
# listbox.insert(3,'naruto shippuden')
# listbox.insert(4,'demon slayer')
# listbox.pack()

# window.mainloop()


from tkinter import *

def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

def submit():
    print("You have ordered:")
    print(listbox.get(listbox.curselection()))

window=Tk()

listbox=Listbox(window,
                bg="yellow",
                font=("Arial",15))

listbox.insert(1,'Pizza')
listbox.insert(2,'Burger')
listbox.insert(3,'Icecream')
listbox.insert(4,'Chicken Biryani')
listbox.insert(5,'Stake')
listbox.config(height=listbox.size())
listbox.pack()

entry=Entry(window)
entry.pack()
button=Button(window,text="Add",command=add)
button.pack()
button=Button(window,text="Delete",command=delete)
button.pack()
button=Button(window,text="Submit",command=submit)
button.pack()


window.mainloop()