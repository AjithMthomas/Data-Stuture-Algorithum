import queue
queue1 = queue.Queue()
queue1.put(10)
queue1.put(20)
queue1.put(30)
queue1.put(40)
queue1.get()
while queue1 is not None:
    print(queue1.get())