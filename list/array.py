array1 = [1,2,3,4]
array2= [3,5,6,7]
farray=[]

for i in array1:
    farray+=[i]

for i in array2:
    farray+=[i]

print(farray)
sum=0
count=0

for i in farray:
    sum = sum+i
    count +=1
    
print(sum)
print(count)
    