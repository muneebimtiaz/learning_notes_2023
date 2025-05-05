# from tkinter import *
# window=Tk()
# label=Label(window,text="muneebimtiaz6@gmail.com").pack()
# label=Label(window,text="muneebimtiaz6@outlook.com").pack()
# window.mainloop()


from tkinter import *
win=Tk()
icon=PhotoImage(file="C:\\Users\\DELL\\Downloads\\py_out (10).png")
label=Label(text="You are Hacked",
          bg="black",
          fg="green",
          font=("impact",40),
          relief=RAISED,
          bd=5,
          padx=20,
          pady=20,
          image=icon,
          compound=BOTTOM)
label.pack()
# label.place(x=0,y=0)
win.mainloop()