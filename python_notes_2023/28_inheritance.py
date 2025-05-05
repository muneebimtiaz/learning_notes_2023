# # inheritance
# class Animal:
#     alive=True
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class Dog(Animal):
#     def eat(self):
#         print("Dog eats meat")

# class Cat(Animal):
#     def drink(self):
#         print("Cat drinks milk")

# class Lion(Animal):
#     def attack(self):
#         print("Lion attack others as their prey")

# d1=Dog("harbar",12)
# c1=Cat("Lexie",6)
# l1=Lion("Leo",11) 

# d1.eat()
# c1.drink()
# l1.attack()


# # multilevel inheritance
# class Employee:
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id

# class Staff(Employee):
#     def tot_staff(self):
#         print("Total Staff members are 54")

# class Writer(Staff):
#     def tot_writer(self):
#         print("Out of 54 only 4 are writers")

# s1=Employee
# w1=Employee


# s1=Staff("Muneeb",21,505)
# w1=Writer("Jason",23,457)

# w1.tot_staff()
# w1.tot_writer()

# multi inheritance
class Prey:
    def flee(self):
        print("this animal is fleeing")
class Predator:
    def hunt(self):
        print("this animal is hunting")
class Rabbit:
    pass
class Lion:
    pass
class Fish(Prey,Predator):
    pass

r1=Rabbit()
l1=Lion()
f1=Fish()

f1.flee()
f1.hunt()
