class Student:
# The variables inside a class are called attributes.
    roll_no=None
    name=None
    per=None

# constructor function 
    def __init__(self,roll_no,name,per) :
        self.roll_no=roll_no
        self.name=name
        self.per=per

# member functions/method
    def print_data(self):
        print(self.roll_no)
        print(self.name)
        print(self.per)

# create objects of class and also setting values using constructor
s1=Student(335,"muneeb","77.5")  
s2=Student(337,"obaid",76.7)

s1.print_data()
s2.print_data()

print(s1.roll_no)