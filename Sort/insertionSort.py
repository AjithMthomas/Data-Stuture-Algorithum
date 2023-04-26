a=[87,3,5,9,78,4,100]

for i in range(1,len(a)):
    numberToInsert=a[i]
    j=i-1
    while j>=0 and a[j]>numberToInsert:
        a[j+1] = a[j]
        j = j-1
    a[j+1] =numberToInsert
print(a)