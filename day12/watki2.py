import threading

def thread_id():
    print("thread_id: ", threading.get_ident())

def worker(number):
    print("Worker: ", number)
    thread_id()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Worker:  0
# thread_id:  10904
# Worker:  1
# thread_id:  23200
# Worker:  2
# thread_id:  23824
# Worker:  3
# thread_id:  5228
# Worker:  4
# thread_id:  11716
