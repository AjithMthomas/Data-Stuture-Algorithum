# list1=['aji','arun','ajul']
# tuple2=('kiran','athul','abin')
# set1={'emy','sara'}
# dict1={'name':'febin'}

# # new  =list1+list(tuple2)+list(set1)+[dict1.items()]
# # new = tuple(list1)+ tuple2 + tuple(set1),(dict1)
# new=set(list1)|set(tuple2)|set1|{frozenset (dict1.items())}
# even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]

list2=[1,3,5,6,77,55,5]
list3=[]
for i in   list2:
    if i%2==0:
        list3.append(i)
print(list3)
