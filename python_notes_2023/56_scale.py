# from tkinter import *
# window=Tk()
# scale=Scale(window,from_=0,to=100).pack()
# window.mainloop()


from tkinter import *

def submit():
    x=str(scale.get())
    print("volume of device is "+x)

window=Tk()

scale=Scale(window,
            from_=100,
            to=0,
            orient=VERTICAL,
            troughcolor="gray",
            label="Volume",
            font=("impact",20),
            tickinterval=10,  #add numeric indicators for value
            # sliderlength=10,
            length=600)
scale.pack()


button=Button(window,text="submit",width=25,command=submit)
button.pack()

window.mainloop()