# syntax of print()
# print(object= separator= end= file= flush=)

print("Good Morning!!" ,end=" ")
print("Everything is alright")

print("Good Afternoon!!","Everything is alright",sep=" &*%^ ")


"""
library functions are defined inside the module. And, to use them we must include the module inside our program.
For example, sqrt() is defined inside the math module.
A module is a file containing Python code, definitions of functions, statements, or classes.
module--->built-in python modules
      --->user-defined python modules.
"""

# build-in pyhton modules
import math
square_root=math.sqrt(3)
print(square_root)

power=math.pow(2,3)
# 2*2*2  
print(power)

fact=math.factorial(7)
# 7!=7*6*5*4*3*2*1
print(fact)


"""https://docs.python.org/3/py-modindex.html"""
# help("modules")

# userdefined  python modules
# method 1
import userdefinedmodule
userdefinedmodule.hello_to_user()
userdefinedmodule.bye_to_user()

# method 2
import userdefinedmodule as udm
udm.hello_to_user()
udm.bye_to_user()

#method 3
from userdefinedmodule import hello_to_user,bye_to_user
hello_to_user()
bye_to_user()

# method 4 
from userdefinedmodule import*          #not recommended for large programs
hello_to_user()
bye_to_user()
