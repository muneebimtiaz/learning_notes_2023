"""
funciton arguments --->position arguments
                   --->keyword arguments
"""
# postion arguments
# example 1
def sayMyName(name,age):
    print(f"hello!this is {name}.Nice to meet you")
    print(f"I am {age} years old.")

name=input("enter your name:")
age=input("enter your age:")
sayMyName(name,age)
sayMyName("obaid",22)
sayMyName("taimoor",20)

# example 2
def sum(num1=2,num2=4):
    return int(num1)+int(num2)

num1=input("enter num1:")
num2=input("enter num2:")
print(sum(num1,num2))
print(sum(num1=12))
print(sum())

# keyword argument
# example 3
def info(firstName, lastName):
    print("First Name:", firstName)
    print("Last Name:", lastName)

info(lastName = "Imtiaz", firstName = "Muneeb")

"""
Here, we have assigned names to arguments during the function call.
Hence, firstName in the function call is assigned to firstName in the function definition. Similarly, lastName in the function call is assigned to lastName in the function definition.
In such scenarios, the position of arguments doesn't matter."""

#  Function With Arbitrary Arguments
# *args
def new_sum(*abcd):
    total=0
    for i in abcd:
        total= total + i

    print(total)


new_sum(1,3,4)
new_sum(3,5,6,7)

