import threading
import os

event=threading.Event()

def func():
    event.wait()
    a=input("\nName of the folder?")
    os.mkdir(f"C:/Users/vasu1/OneDrive/Desktop/Python/Intermediate/{a}")
t1=threading.Thread(target=func)
t1.start()
ask=input("Want to make the respective folder?  Y/N\n")
if(ask=='Y'):
    event.set()
