# from tkinter import *
# window=Tk()

# menubutton=Menubutton(window,text="options")
# menubutton.menu=Menu(menubutton,tearoff=0)
# menubutton["menu"]=menubutton.menu
# menubutton.grid()
# window.mainloop()



from tkinter import *
window=Tk()
# creating the menubar in the main window
menubar=Menu(window)
window.config(menu=menubar)

# creating file heading in the menubar
fileheading=Menu(menubar,tearoff=0)    #tearoff is used to erase the dashed line
menubar.add_cascade(label="File",menu=fileheading)
fileheading.add_command(label="New Text File")
fileheading.add_command(label="New File")
fileheading.add_command(label="New Window")

# creating edit heading in the menubar
editheading=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editheading)
editheading.add_command(label="Undo")
editheading.add_command(label="Redo")
# editheading.add_separator()
editheading.add_command(label="Cut")

# creating selection heading in the menubar
selectionheading=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Selection",menu=selectionheading)
selectionheading.add_command(label="Select All")
selectionheading.add_command(label="Expand Selection")
selectionheading.add_command(label="Shrink Selection")

window.mainloop()
