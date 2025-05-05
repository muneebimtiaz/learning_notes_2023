class car:
    color=None

class truck:
    color=None

def change_color(obj,color):
    obj.color=color


c1=car()
t1=truck()

print(c1.color)
print(t1.color)

change_color(c1,"Red")
change_color(t1,"black")

print(c1.color)
print(t1.color)
