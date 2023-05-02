# divide array into 3 and if the sum of each part is true return true else return false
array=[2,4,5,1,3,7]
sum1=0
sum2=0
sum3=0
len=len(array)//3
for i in range(0,len-1):
    sum1+=array[i]
for i in range(len,(len*2)-1):
    sum2+= array[i]
for i in range(len*2,-1):
    sum3+=array[i]
if sum3==sum1==sum2:
    print('true')
else:
    print('false')