# from tkinter import *
# window=Tk()
# message=Message(window,text="this is our message")
# message.config(bg="lightgreen")
# message.pack()
# window.mainloop()


from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showerror(title="Error message box",message="Gui not responding!")
    # messagebox.showinfo(title="Info message box",message="Aot is the goat🐐")
    messagebox.showwarning(title="Warning message box",message="Earthquake magnitude 7.1")

window=Tk()

message=Message(window,
                text="Click button and check which message appears",
                bg="lightgreen").pack()

button=Button(window,
              text="Click",
              command=click).pack()

window.mainloop()