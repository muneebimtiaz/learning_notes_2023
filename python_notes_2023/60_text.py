# from tkinter import *
# window=Tk()
# text=Text(window,height=2,width=30)
# text.insert(END,"hello my name is muneeb")
# text.pack()
# window.mainloop()


from tkinter import *

def submit():
    print(text.get("1.0",END))  #get(starting index in floats,ending index)

window=Tk()
text=Text(window,
          height=10,
          width=50,
        # bg="yellow",
        # fg="orange",
        # font=("Ink Free",25)
          )
          
text.pack()
button=Button(window,text="Submit",command=submit)
button.pack()
window.mainloop()