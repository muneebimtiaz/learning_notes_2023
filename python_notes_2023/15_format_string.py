# and close your eyes with holy dread
xx="doors"
yy="water"

print(f"and close your {xx} with holy {yy}")
# postion arguments
print("and close your {} with holy {}".format(xx,yy))
print("and close your {} with holy {}".format(yy,yy))
print("and close your {} with holy {}".format(yy,xx))
# keyword arguments
print("and close your {xx} with holy {yy}".format(xx="doors",yy="water"))

sentence="and close your {} with holy {}"
print(sentence.format(xx,yy))

name="Muneeb"
print("Hello my name is {:10}. YOU WELCOME!!".format(name))
print("Hello my name is {:>10}. YOU WELCOME!!".format(name))
print("Hello my name is {:<10}. YOU WELCOME!!".format(name))
print("Hello my name is {:^10}. YOU WELCOME!!".format(name))
print("Hello my name is {:^10}. YOU WELCOME!!".format(name))


value_of_PI=3.14159
print("PI={:.2f}".format(value_of_PI))
random_number=19000
print("Number={:,}".format(random_number))
print("Number={:b}".format(random_number))
print("Number={:o}".format(random_number))
print("Number={:x}".format(random_number))
print("Number={:e}".format(random_number))





