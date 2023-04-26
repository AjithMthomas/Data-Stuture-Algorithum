a=[6,2,7,4,8,8,5]

for i in range (len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            mi = a[i]
            a[i] = a[j]
            a[j] = mi
print(a)