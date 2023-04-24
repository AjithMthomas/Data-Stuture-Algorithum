import collections

queue = collections.deque()
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.popleft()
queue.popleft()
print(queue)



