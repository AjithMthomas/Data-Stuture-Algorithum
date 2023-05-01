def missingElement(arry):
    n = len(arry)+1
    totalSum=(n*(n+1))//2
    sumOfArray=sum(arry)
    return totalSum-sumOfArray
arry=[10,12,13]
missingElementInarray=missingElement(arry)
print(missingElementInarray)