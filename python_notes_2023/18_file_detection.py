import os
# example 1
path="C:\\Users\\DELL\\OneDrive\\Documents\\My Notes"
if os.path.exists(path):
    print("File Detection Successful")
else:
    print("File Detection Unsuccessful")


# example 2    
path="C:\\Users\\DELL\\OneDrive\\Documents\\My Notes\\New folder"
if os.path.exists(path):
    print("Location Exists")
    if os.path.isfile(path):
        print("Location Exists as a file/txt")
    elif os.path.isdir(path):
        print("Location Exists as a Folder/Directory")
else:
    print("Location oesnot Exists")


# example 3
path1="C:\\Users\\DELL\\OneDrive\\Documents\\My Notes\\New Text Document.txt"
if os.path.exists(path1):
    print("Location Exists")
    if os.path.isfile(path1):
        print("Location Exists as a file/txt")
    elif os.path.isdir(path1):
        print("Location Exists as a Folder/Directory")
else:
    print("Location doesnot Exists")

