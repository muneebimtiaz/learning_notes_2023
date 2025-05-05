# taking input from user and then store the input in a variable
name=input("what is your name?")

# to remove widespaces 
name=name.strip()
# to capitilize the first name
name=name.capitalize()
# to capitilize the surname 
name=name.title()

# instead of calling function one by one we can chain the functions together as well
name=name.strip().title()

# instead of calling function one by one we can chain the functions together on input file as well
name=input("what is your name?").strip().title()

# split user input into first name or last name
first,last=name.split(" ")

print("your name is",name)
# cancadinating strings
print("your name is "+name)
# format string or fstring
print(f"your first name is {first}")
print(f"your surname is {last}")


# to compare two strings
str1 = "attack on titan"
str2 = "monster"
str3 = "attack on titan"
print(str1 == str2)
print(str1 == str3)


# escape sequence \
print("football club \"Manchester United\".\nname \"Muneeb Imtiaz\"")

fff="Manchester United"
print(fff[0])
print(fff[3])


# string slicing
print(fff[1:4])

# find(),count()


"""
List of Escape Sequence Available in Python
\'	Single quote
\\' Double quote
\\	Backslash
\n	Newline
\r	Carriage Return
\t	Horizontal Tab
\b	Backspace
\f	Formfeed
\v	Vertical Tab
\0	Null Character
"""

