import heapq

list1=[2,3,5,34,3,6]

negativeList =[-x for x in list1]

heapq.heapify(negativeList)
maxheap = [-x for x in negativeList]
print(maxheap)