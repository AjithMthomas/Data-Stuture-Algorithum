import heapq

# def heap_sort_max(array):
#     # Convert the array to a max-heap
#     heap = []
#     for item in array:
#         heapq.heappush(heap, -item)

#     # Extract the maximum value from the heap and place it at the end of the array
#     for i in range(len(array)):
#         array[i] = -heapq.heappop(heap)

#     return array
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
n= len(array)
sortd=heapq.nsmallest(n,array)

# Test the function
print(sortd)