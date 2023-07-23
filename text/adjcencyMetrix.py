node = []
graph = []
node_cout =0

def add_node(v):
    global node_cout
    if v in node:
        print('present')
    else:
        node_cout+=1
        node.append(v)
        for i in graph:
            i.append(0)
        temp = []
        for i in range(node_cout):
            temp.append(0)
        graph.append(temp)
def metrix_representation():
    for i in range(node_cout):
        for j in range(node_cout):
            print(graph [i][j],end=" ")
        print()

def add_edge(v1,v2,cost):
    if v1 not in node :
        print(f'{v1} is not present ')
    elif  v2 not in node :
        print(f'{v2} is not present ')

    else:
        index1 = node.index(v1)    
        index2 = node.index(v2)
        graph [index1][index2] = cost
        graph [index2][index1] = cost

def delete(v):
    global node_cout
    if v not in node:
        print(f'{v} not in graph')
    else:
        index = node .index(v)
        node.remove(v)
        graph.pop(index)
        node_cout -= 1
        for i in graph:
            i.pop(index)

def delete_edge(v,v1):
    if v  not in node:
        print(f'{v} not in garaph')
    elif v1 not in node:
        print(f'{v1} not in graph')
    else:
        index = node.index(v)
        index1 = node.index(v1)
        graph[index][index1] = 0
        graph[index1][index] = 0



add_node('a')
add_node('b')
add_node('v')
add_edge('a','b',10)

print(node)
print(graph)
metrix_representation()
