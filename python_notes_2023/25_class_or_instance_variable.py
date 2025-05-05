# class Student:
#     section="d"   #class variable is a variable that is defined within a class and outside of any class method

# # constructor function 
#     def __init__(self,roll_no,name,per) :
#         self.roll_no=roll_no    #instance variable
#         self.name=name      #instance variable
#         self.per=per    #instance variable

# # member functions/method
#     def print(self):
#         print(self.roll_no)
#         print(self.name)
#         print(self.per)

# # create instances/objects of class and also setting values using constructor
# s1=Student(335,"muneeb","77.5")  
# s2=Student(337,"obaid",76.7)

# s1.section="b"
# # s1.print()
# # s2.print()
# print(s1.section)
# print(s2.section)

# Student.section="a"
# print(s1.section)
# print(s2.section)

# example 1:
class Employee:
    office_name="cccc"
    def __init__(self) :
        print(Employee.office_name)

xx=Employee()