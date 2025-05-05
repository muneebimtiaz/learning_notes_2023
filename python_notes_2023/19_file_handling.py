# method 1
# read file
# example 1
file=open("file.txt","r")
y=file.readlines()
print(y)

# example 2
file=open("file.txt","r")
y=file.readlines()
list=[]
for i in y:
    if i[-1]=="\n":
        list.append(i[:-1])  #remove \n
    else:
        list.append(i)

print(list)

# example 3
file=open("file.txt","r")
y=file.readlines()
list=[]
for i in y:
    list.append(i.strip())

print(list)

# write file
file=open("file.txt","a")
file.write("c++")

print(list)

# method 2
# open() & read() a file 
try:
    with open("file.txt") as var:
        print(var.read())
except FileNotFoundError:
    print("File Not Found :(")

# open() & write() a file 
data_to_write="\nglory glory manchester\nManchester is Red"
try:
    with open("file.txt","w") as var:
        var.write(data_to_write)
except FileNotFoundError:
    print("File Not Found :(")   



# # copy a file
# import shutil
# shutil.copyfile("copyfrom.txt","copyto.txt")

# # move a file
# import os
# source="moved.txt"
# destinition="C:\\Users\\DELL\\OneDrive\\Documents"

# os.replace(source,destinition)
# print(f"{source} was moved sucessfully")