array = [23,34,3,4,4,4,3,45,5]
for i in range(len(array)):
    for j in range(i+1,len(array)):
        temp =array[i]
        array[i]= array[j]
        array[j] =temp

print(array) 