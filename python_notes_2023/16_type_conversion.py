"""
there are two types of conversions in python
implicit conversion--->automatic type 
explicit conversion--->manual type
"""
# implicit conversion
x=12
y=13.9
print(x,type(x))
print(y,type(y))
z=x+y
print("sum:",z,type(z))

# explicit conversion
xx=23
yy=67.9
print(xx,type(xx))
print(yy,type(yy))
zz=int(xx)+int(yy)
print("sum:",zz,type(zz))
