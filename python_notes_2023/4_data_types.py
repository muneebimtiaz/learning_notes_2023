"""
numeric----> int,float,complex
string---->str
sequence---->list,tuple,range
mapping---->dict
boolean---->bool
set---->set,frozeenset
"""

# numeric data types
num1=23
print(num1,"has type of",type(num1))
num2=43.99
print(num2,"has type of",type(num2))
# one way
num3=5+6j
print(num3,"has type of",type(num3))
# another way
num4=complex(4,6)
print(num4,"has type of",type(num4))


# string datatype
message="hello,world"
print(message,"has type of",type(message))


# sequence datatype-->list
""" 
lists are used to store multiple data at once. For example,
Suppose we need to record the ages of 5 students. Instead of creating 5 separate variables, we can simply create a list
"""
languages=["python","java","javascript"]
print(languages[0])
languages[0]="go"
print(languages[0])
print(languages[2])


# sequence datatype-->tuple
# tuples are ordered and immutable(unchangable)
product=("Xbox 360","playstation",499.9)
print(product[0])
# product[0]="nintendo" there is no way to change a tuple a error message will show
print(product[0])
print(product[2])


# mapping datatype-->dict
capital_city={"Pakistan":"Islamabad","England":"London","Japan":"Tokyo"}
print(capital_city)
print("Capital city of Pakistan is:",capital_city["Pakistan"])
print("Capital city of Japan is:",capital_city["Japan"])


# set datatype-->set
# sets have unordered,unindexed or no dublicate values
student_id={23,44,55,6,73,11}
print(student_id,"has type of",type(student_id))
for i in student_id:                       
    print(i)

# student_id={23,44,55,6,73,11,11,11,11}     no dublicate values it will print only 1 time "11"

student_id.add("hello")
print(student_id)
student_id.remove(44)
print(student_id)
student_id.clear()
print(student_id)


set1={2,4,6,8}
set2={1,3,5,7,9}
print(set1.union(set2))