# from tkinter import *
# window=Tk()

# var1=IntVar()
# chk_btn=Checkbutton(window,text="man",variable=var1).grid(row=0,sticky=W)
# # chk_btn.grid()
# var2=IntVar()
# chk_btn=Checkbutton(window,text="women",variable=var2).grid(row=1,sticky=W)
# # chk_btn.grid()

# window.mainloop()


from tkinter import *
def disp():
    if (xx.get()==1):       # xx.get()==Yes,Not need to say T/F it return the value anyways
        print("You agreed with us :)")
    elif (xx.get()==0):     # xx.get()==No,
        print("You didnot agreed with us :(")

win=Tk()
xx=IntVar()
# xx=StringVar()
# xx=BooleanVar()
chk=Checkbutton(win,text="attack on titan is the goat anime🐐",
                variable=xx,
                onvalue=1, #for string "Yes",#for boolean True
                offvalue=0,#for string "No",#for boolean False
                 
                 
                command=disp,
                activebackground="green",
                activeforeground="white",
                font=("Comic Sans",15),
                # width=15,
                # height=2,
                )

chk.pack()
win.mainloop()