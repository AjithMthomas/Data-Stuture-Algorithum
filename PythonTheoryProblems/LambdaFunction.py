# # we can use map for linking a fuction with a itreble object

# list1=[1,3,4,9]
# # we are going to find the sqare of each element in fuction

# result = list(map(lambda a :a**3,list1))

# print(result)

list1=[1,2,3,4,5]
f= lambda a:a*a
new=[f(a) for a in list1]
print(new)