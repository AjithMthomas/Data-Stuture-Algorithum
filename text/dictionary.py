dict1 = {5:'a',
         2:'aa',
         3:'aaa'}
new ={}
for key,value in dict1.items():
    new[value] = key
print(new)

new1={i:dict1[i] for i in dict1 if i%2 ==0}
print(new1)


dictionary ={dict1[i]:i for i in dict1}
print(dictionary)

