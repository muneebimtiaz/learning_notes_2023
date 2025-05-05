# from tkinter import *
# window=Tk()
# btn=Button(window,text="Stop",width=25)
# btn.pack()
# window.mainloop()


from tkinter import *

def click():
    print("You clicked the button")

win=Tk()

# icon=PhotoImage(file="C:\\Users\\DELL\\Downloads\\out.png")
btn=Button(win,text="Click Me",
          activebackground="red",
          activeforeground="blue",
          command=click,
          font=("Comic Sans",10),
          bg="purple",
          bd=4,
        # width=15,
        # height=2,
        # image=icon,
        # padx=25,
        # pady=25,
        # compound="bottom",
          relief=RAISED)

btn.pack()
win.mainloop()