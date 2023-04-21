array=[1,2,3,4,5]
n=input('limit:')
for i in n:
    temp = array[0]
    for j in range(len(array)-1):
        array[j] = array[j+1]
    array[-1] = temp
print(array)
