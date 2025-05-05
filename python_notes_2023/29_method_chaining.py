# method chaining is used to call multiple methods sequentially
class Car:
    def start(self):
        print("car start")
        return self
    def drive(self):
        print("car drive")
        return self
    def brake(self):
        print("car brake")
        return self
    def stop(self):
        print("car stop")
        return self

c1=Car()

# c1.start()
# c1.drive()
# c1.brake()
# c1.stop()

# obj+function=method
c1.start().drive().brake().stop()
# this will not worked because when we call a function it must have returned something but if there is nothing to return then python will return NONE
