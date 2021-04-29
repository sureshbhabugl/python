import threading


def new():
    for x in range(6):
        print("Child Thread is here!")


t1 = threading.Thread(target=new)
t1.start()
t1.join()
print("Main Thread Here!!")
