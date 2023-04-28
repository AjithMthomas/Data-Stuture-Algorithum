def findPivot(list1,first,last):
    pivot = list1[last]
    left = first
    right = last-1
    while True:
        while left<=right and list1[left]<=pivot:
            left = left+1
        while left<=right and list1[right]>=pivot:
            right = right-1
        if left>right:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[last],list1[left] = list1[left],list1[last]
    return last
def quicksort(list1,first,last):
    if first<last:
        p = findPivot(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)
list1=[76,76,38,7,69,3]
quicksort(list1,0,len(list1)-1)
print(list1)