str = "helloworld"

count = {char:str.count(char) for char in str}

print(count)


str = "my name is is ajith ajith"
list1 = str.split(" ")
dict1 = {i:list1.count(i) for i in list1}
print(dict1)

def dictionay(n):
    dict1 ={i:i*'a' for i in range(1,n+1)}
    return dict1

a = dictionay(5)
print(a)
