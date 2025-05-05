# example 1
happy=True
print(happy)
# same code with walrus operator
print(happy:=True)


# example 2
list=[]
while True:
    food=input("Enter the food you like:")
    if food=="quit":
        break 
    list.append(food)
# same code with walrus operator
list=[]
while food:=input("Enter the food you like:") !="quit":
    list.append(food)