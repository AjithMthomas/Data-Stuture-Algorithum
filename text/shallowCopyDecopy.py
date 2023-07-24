import copy

name = 'ajit'
name1 = name
name2 = copy.deepcopy(name)

print(f'{id(name)},{id(name1),id(name2)}')