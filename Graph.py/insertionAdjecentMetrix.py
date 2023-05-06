

def add_node(v):
    global node_count

    if v in nodes:
        print('node already pressent')
    else:
        node_count += 1
        nodes.append(v)
    for i  in graph:
        i.append(0)
    temp = []
    for i in range(node_count):
        temp.append(0)
    graph.append(temp)
    
def print_graph(graph):
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()

nodes = []
graph = []
node_count = 0        
add_node('a')
add_node('b')
add_node('c')
print_graph(graph)

