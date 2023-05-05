import heapq

heap=[1,3,46,64,7,87]
# adding new element to the heap
heapq.heappush(heap,19)
heapq.heappush(heap,1)
# to remove the smallest element from heap
heapq.heappop(heap)

# to making the list to heap
heapq.heapify(heap)
# to push element and remove the smallest element from the heap
# heap.heappushpop(heap,29)

# to find the n small small elements from the heap
s=heapq.nlargest(1,heap)

print(s)