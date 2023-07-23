graph ={}

def add_node(v):
    if v in graph:
        print(f'{v} is already in graph')
    else:
        graph[v] = []

def add_edge(v,v2,cost):
    if v not in graph:
        print(f'{v} not in graph')
    elif v2 not in graph:
        print(f'{v2} not in graph')
    else:
        list1 = [v,cost]
        list2 = [v2,cost]
        graph[v].append(list1)
        graph[v2].append(list2)
        
def delete_node(v):
    if v not in graph:
        print(f'{v} not in graph')
    else:
        graph.pop(v)
        for  i in graph:
            list1= graph[i]
            for j in list1:
                if v==j[0]:
                    list1.remove(j)

def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print("no")
    elif v2 not in graph:
        print("no")
    else:
        temp =[v1,cost]
        temp1 =[v2,cost]

        if temp1 in graph [v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)
            print('deleted')
        else:
            print('')


add_node('a')
add_node('b')
add_node('c')
add_edge('a','b',3)
print()
add_edge('a','c',4)
add_edge('b','b',5)
add_edge('b','c',3)


print(graph)