"""
types of functions
->standard library functions/build-in functions ---> print(),sqrt(),pow()  //// https://docs.python.org/3/library/functions.html
->user-defined functions ---> def
"""

def callMyName(fname="jonny",lname="depp"):    
    print(f"hi {fname} {lname}")
    print("welcome!")

# passing argument to parameter fname,lname
# parameter only exists in scope of the function
# default value of fname->"jonny" & lname->"depp"
callMyName("Muneeb","Imtiaz")  #pass globally
callMyName()
# localvariable<globalvariable

def sumFunction(xx,yy):
    # xx=input("enter int of x:")
    # yy=input("enter int of y:")
    return int(xx)+int(yy)

num1=input("enter the value of num1:")
num2=input("enter the value of num2:")
print(sumFunction(num1,num2))

def squareFunction(num):
    return int(num)*int(num)

abc=input("enter a number whose square you want:")
print("square of that number is:",squareFunction(abc))

# nested function call

