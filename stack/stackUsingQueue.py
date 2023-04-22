import queue

stack = queue.LifoQueue()

stack.put(10)
stack.put(20)
stack.put(30)
top_item =stack.get(timeout=1)
print(list(stack.queue))
