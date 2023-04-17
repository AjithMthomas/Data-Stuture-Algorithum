# list1=[1,3,5,6,77,55,5]

# list2 = [i for i in list1 if i%2==0 ]

# list1=[1,3,5,6,77,55,5]

# list2 = [i for i in list1 if i%2==0]
# list1=[i*i for i in range (1,6)]
# print (list1)

list1=[]

for i in range(1,6):
    if i%2==0:
        list1.append(i)
print (list1)