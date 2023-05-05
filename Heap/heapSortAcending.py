import heapq

def heap_sort_ascending(array):
    # Convert the array to a min-heap
    heapq.heapify(array)

    # Extract the minimum value from the heap and place it at the end of the array
    sorted_array = []
    for i in range(len(array)):
        sorted_array.append(heapq.heappop(array))

    return sorted_array

# Test the function
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = heap_sort_ascending(array)
print(sorted_array)   # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
