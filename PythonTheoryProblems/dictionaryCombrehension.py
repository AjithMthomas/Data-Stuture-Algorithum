list1 = [1,3,4,56,6,54]
dictionary={i:i*i for i in list1}
print(dictionary)

new ={i:i*i for i in list1 if i%2==0}
print(new)