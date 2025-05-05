# class Rectangle:
#     pass
# class Square(Rectangle):
#     def __init__(self,lenght,width):
#         self.lenght=lenght
#         self.width=width
#     def area(self):
#         return self.width*self.lenght

# class Cube(Rectangle):
#     def __init__(self,lenght,width,height):
#         self.lenght=lenght
#         self.width=width
#         self.height=height
#     def volume(self):
#         return self.height*self.width*self.lenght


# s1=Square(2,2)
# print(s1.area())
# c1=Cube(2,2,2)
# print(c1.volume())

# doing this program using  super function
class Rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width

class Square(Rectangle):
    def __init__(self,lenght,width):
        super().__init__(lenght,width)
    def area(self):
        return self.width*self.lenght

class Cube(Rectangle):
    def __init__(self,lenght,width,height):
        super().__init__(lenght,width)
        self.height=height
    def volume(self):
        return self.height*self.width*self.lenght


s1=Square(2,2)
print(s1.area())
c1=Cube(2,2,2)
print(c1.volume())
