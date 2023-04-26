a=[87,3,5,9,78,344,83,3,2,1,555,1,550]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)