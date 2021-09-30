import threading
import time
'''
def display1():
    for i in range(1,11):
        print("Display function 1")

def display2():
    for i in range(1,11):
        print("Display function 2")

t1=threading.Thread(target=display1)
t2=threading.Thread(target=display2)

t1.start()
t2.start()

for i in range(10):
    print("main thread")

'''
class Mythread(threading.Thread):
    def run(self):
        for i in range(10):
            time.sleep(0.2)
            print("Child Thread")

    def start(self):

        super().start()

t1=Mythread()
t1.start()

for i in range(10):
    time.sleep(0.3)
    print("Main Thread")
