# lamda functions are those functions that are written in one line using lamda keyword
# lambda parameter : expression

sum=lambda x,y:x+y
print(sum(5,7))

name=lambda f_name,l_name:f_name+" "+l_name
# name=lambda f_name,l_name:f"{f_name} {l_name}"
print(name("muneeb","imtiaz"))


# age=int(input("enter age:"))
# if age>=18:
#    True
# else:
#     False

chk=lambda age:True if age>=18  else False
age=int(input("enter age:"))
print(chk(age))