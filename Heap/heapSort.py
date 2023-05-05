import heapq

def heap_sort_max(array):
    # Convert the array to a max-heap
    heap = []
    for item in array:
        heapq.heappush(heap, -item)

    # Extract the maximum value from the heap and place it at the end of the array
    for i in range(len(array)):
        array[i] = -heapq.heappop(heap)

    return array

# Test the function
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = heap_sort_max(array)
print(sorted_array)   # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
