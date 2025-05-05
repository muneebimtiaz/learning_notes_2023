# class Number:
#     areacode=None
#     exchange=None
#     number=None

#     def input(self):
#         print("Please enter the values:")
#         self.areacode=input("enter area code:")
#         self.exchange=input("enter exchange:")
#         self.number=input("enter number:")
#     def output(self):
#         print(f"{self.areacode}-{self.exchange}-{self.number}")

# n1=Number()
# n2=Number()
# n1.input()
# n2.input()

# n1.output()
# n2.output()

# class Animal:
#     def walk(self):
#         print("walking")
#     def eat(self):
#         print("eating")

# class Dog(Animal):
#     def talk(self):
#         print("bark")
# class Cat(Animal):
#     def talk(self):
#         print("meow")
# class Bear(Animal):
#     def talk(self):
#         print("growl")

# d=Dog()
# c=Cat()
# b=Bear()



# # class Store:
# #     def __init__(self,pn,pp,pq):
# #         self.product_name=pn
# #         self.product_price=pp
# #         self.product_quantity=pq

# #     def t_calculate(self,pp,pq):
# #         return self.product_price*self.product_quantity

# # a=(input("Enter Name of Product:")) 
# # b=(input("Enter Price of Product:"))
# # c=(input("Enter Quantity of Product:")) 
# # p1=Store(a,b,c)

# # print(p1.t_calculate(b,c))


# list_of_even_numbers=[2,4,6,8,10]
# print(len(list_of_even_numbers))

# anime=["attack on titan","monster","onepiece"]
# tv_series=["game of therons","the walking dead","breaking bad"]
# movies=["titanic","endgame","the dark knight"]
# what_to_watch=[anime,tv_series,movies]
# print(len(what_to_watch))

# # example 1
# file=open("practicefile.txt","r")
# y=file.readlines()
# print(y)

# # example 2
# file=open("practicefile.txt","r")
# y=file.readlines()
# list=[]
# for i in y:
#     if i[-1]=="\n":
#         list.append(i[:-1])  #remove \n
#     else:
#         list.append(i)

# print(list)

# example 3
# file=open("practicefile.txt","r")
# y=file.readlines()
# list=[]
# for i in y:
#     list.append(i.strip())

# print(list)

# write in afile
# file=open("practicefile.txt","a")
# file.write("c++")

# print(list)


# sort() or sorted()
# sort() or sorted()
n=int(input("Enter the number of time you want to run the program:"))
j=0
while j<n:
    print("Come On!!!")
    j+=1