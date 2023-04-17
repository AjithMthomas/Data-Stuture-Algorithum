# finding two numbers whose sum is 10 from an array
# a=[1,2,6,3,4,7,9]
# for i in range(len(a)   ):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==10:
#             print(a[i],a[j])
# count=0
# for i in a:
#     count+=1
# for i in range(count):
#     for j in range(i+1,count):
#         if a[i] + a[j] ==10:
#             print(a[i],a[j])

# --------------------------------------------------------
# 2.from an arry bring all particular number to the end of the array
# array=[1,2,4,4,5,6,7]
# 1 method
# array =[i for i in array if i!=4]+[j for j in array if j==4]
# print(array)
# 2nd method 
# count=array.count(4)
# array =[ i for i in array if i!=4]
# array+=[4]*count
# print(array)
# -----------------------------------------------------------
# # adding element to the middle of the array
# a=[1,4,6,5,6,7]
# b=[8,10]
# pos = len(a)//2
# for i in b:
#     a.insert(pos,i)
# print(a)
# ------------------------------------------------------------
#adding many element in the end of array
a=[1,4,6,5,6,7]
b=[1,2,3,4]
for i in b:
    a+=[i]
print(a)



     
    

