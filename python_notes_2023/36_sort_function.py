"""
sort()--> method .. it works on lists only
sort()--> function .. it works with iterables 
"""

# # for lists
# list=["jonny depp","leonardo dicaprio","the rock","cole sprouse","amanda seyfried","jennifer lawrence"]
# list.sort()
# # list.sort(reverse=True)
# for i in list:
#     print(i)


# # for iterables
# tuple=("jonny depp","leonardo dicaprio","the rock","cole sprouse","amanda seyfried","jennifer lawrence")
# xx=sorted(tuple)
# # xx=sorted(tuple,reverse=True)
# for i in xx:
#     print(i)



list_of_students=[("jonny depp","A",55),
                  ("leonardo dicaprio","B",57),
                  ("the rock","D",50),
                  ("cole sprouse","F",31),
                  ("amanda seyfried","B",34),
                  ("jennifer lawrence","C",32)]

# for i in range(len(list_of_students)):
#     for j in range(len(list_of_students[i])):
#         print(list_of_students[i][j])


# # sort according to name  (index 0)
# def name_print(name):
#     return name[0]
# list_of_students.sort(key=name_print)

# # sort according to grade (index 1)
# def grade_print(grade):
#     return grade[1]
# list_of_students.sort(key=grade_print)
# list_of_students.sort(key=grade_print,reverse=True)

# # sort according to marks (index 2)
# def marks_print(marks):
#     return marks[2]
# list_of_students.sort(key=marks_print)


for i in list_of_students:
    print(i)


