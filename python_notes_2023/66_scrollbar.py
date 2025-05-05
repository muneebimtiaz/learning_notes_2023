# error fixed

from tkinter import *
window=Tk()


scrollbar=Scrollbar(window)
listbox=Listbox(window,yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT,fill=Y)
for i in range(100):
    listbox.insert(END,"line number is" + str(i))
scrollbar.config(command=listbox.yview)
listbox.pack(side=LEFT,fill=BOTH)


window.mainloop()