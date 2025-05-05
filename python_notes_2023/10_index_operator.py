"""
by using index operator we can easily access the sequene(str,list,tuple) items
The index operator (Python uses square brackets to enclose the index) selects a single character from a string.
In strings, the characters are accessed by their position or index.
In lists and tuples, items are accessed by their position or index.
Characters are indexed left to right from position '0' to position '13'. Positions are also named from right to left using negative numbers, where -1 is the rightmost index and so on."""

myname="muneeb imtiaz"

if myname[0].islower():
    myname=myname.capitalize()
    print(myname) 

fname=myname[:6].upper()
lname=myname[7:].lower()
print(fname,lname)