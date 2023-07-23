

def add_node(v):
    global node_cout
    if v  in nodes:
        print('node is already in node')
    else:
        node_cout += 1
        nodes.append(v)
    for i in graph:
        i.append(0)
    temp = []
    for i in range(node_cout):
        temp.append(0)
    graph.append(temp)
    
def print_graph(graph):
    for i in range(node_cout):
        for j in range(node_cout):
            print(graph[i][j],end=" ")
        print()
        
def add_edge(v1,v2,el):
    if v1  not in nodes:
        print('no node')
    elif v2 not in nodes:
        print('no node')
    else:
        i1=nodes.index(v1)
        i2 = nodes.index(v2)
        graph[i1][i2]=el
        graph[i2][i1]=el
nodes=[]
graph=[]
node_cout=0
add_node("a")
add_node("b")
add_node("c")
add_edge("a",'b',7)
print(graph)

