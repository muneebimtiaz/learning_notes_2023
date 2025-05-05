from abc import ABC,abstractmethod
class Vehicle(ABC):
    @ abstractmethod
    def go(self):
        pass
    def stop(self):
        pass
    
class Motorbike(Vehicle):
    def go(self):
        print("riding a motorbike")
    def stop(self):
        print("motorbike stopped")

class Car(Vehicle):
    def go(self):
        print("Driving a car")
    def stop(self):
        print("car stopped")

# v1=Vehicle()  #abstract class doesnot allow to create the object/instance
m1=Motorbike()
c1=Car()

m1.go()
m1.stop()
c1.go()
c1.stop()