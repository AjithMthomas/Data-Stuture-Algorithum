graph={}

def add_node(v):
    if v in graph:
        print("node is present")
    else:
        graph[v]=[]
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,'not in graph')
    elif v2 not in graph:
        print(v2,'not in graph')
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)
add_node('a')
add_node('b')
add_node('c')
add_edge('a','b',10)
add_edge('a','c',10)


print(graph)