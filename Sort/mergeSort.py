
def mergeSort(list1):
    if  len(list1)>1:
        mid = len(list1)//2
        left_side = list1[:mid]
        rigt_side = list1[mid:]
        mergeSort(left_side)
        mergeSort(rigt_side)
        i=0
        j=0
        k=0
        while i<len(left_side) and j<len(rigt_side):
            if left_side[i]<rigt_side[j]:
                list1[k]=left_side[i]
                i=i+1
                k=k+1
            else:
                list1[k]=rigt_side[j]
                j=j+1
                k=k+1
        while i<len(left_side):
            list1[k]=left_side[i]
            i=i+1
            k=k+1
        while j<len(rigt_side):
            list1[k]=rigt_side[j]
            j=j+1
            k=k+1
list1=[1,2,3,4,5]
mergeSort(list1)
print(list1)

    