import threading
import time

def workout():
    time.sleep(3)
    print("workout session")

def breakfast():
    time.sleep(5)
    print("eating breakfast")

def goto_work():
    time.sleep(7)
    print("going to office")

# workout()
# breakfast()
# goto_work()

xx=threading.Thread(target=workout,args=())
xx.start()
yy=threading.Thread(target=breakfast,args=())
yy.start()
zz=threading.Thread(target=goto_work,args=())
zz.start()

xx.join()
yy.join()
zz.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())