# from tkinter import *
# window=Tk()

# var=IntVar()
# radiobutton=Radiobutton(window,text="attack on titan",variable=var,value=1).grid(row=0)
# radiobutton=Radiobutton(window,text="monster",variable=var,value=2).grid(row=1)

# window.mainloop()



from tkinter import *

demonslayer=["Tanjiro Kamado","Zenitsu Agatsuma","Nezuko kamado","Inosuke Hashibira","Kyojuro Rengoku"]

window=Tk()

# tanjiro=PhotoImage(file="C:\\Users\\DELL\\Downloads\\py_out (11).png")
# zenitsu=PhotoImage(file="C:\\Users\\DELL\\Downloads\\py_out (3).png")
# nezuko=PhotoImage(file="C:\\Users\\DELL\\Downloads\\py_out (2).png")
# inosuke=PhotoImage(file="C:\\Users\\DELL\\Downloads\\py_out (1).png")
# rengoku=PhotoImage(file="C:\\Users\\DELL\\Downloads\\py_out (4).png")
# slayer_image_list=[tanjiro,zenitsu,nezuko,inosuke,rengoku]

x=IntVar()
for i in range(len(demonslayer)):
    radiobutton=Radiobutton(window,
                            text=demonslayer[i],
                            # image=slayer_image_list[i],
                            variable=x,
                            value=i,
                            activebackground="green",
                            activeforeground="white",
                            font=("Impact",25),
                            command=LEFT,
                          # indicatoron=0, #eliminate circle indicators
                    )
    radiobutton.pack(anchor=W)


window.mainloop()