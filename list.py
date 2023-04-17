animals =['hen','horse','zebra','chicken']
# animals.append('man')
# animals.insert(2,'man')
# animals.pop()
# animals.sort()
numbers = [1,3,4,5]
# numbers.reverse()
new = numbers.index(4)

# new = [str(x) for x in numbers] + animals
# x=10
# list1=[ x for x in range(10) if x %2 ==0]
nmnber = int(input("Enter an integer: "))

# a=[]
# for x in number
#       a.append(x)

list1=[1,2,3,4,5]
tuple1=(4,5,6,7,8)
set1={7,8,9,10}


new_list = list1+list(tuple1)+list(set1)
new_set= set(new_list)
new =[]
sum=0
for i in new_list:
    sum+=i

print(sum)


print(new)
