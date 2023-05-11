graph={}
visited = set()

def add_node(v):
    if v in graph:
        print('already present')
    else:
        graph[v]=[]
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print('node not in graph')
    elif v2 not in graph:
        print('node not in graph')
    else:
        list1=[v2,cost]
        graph[v1].append(list1)
def DFS(node,visited,graph):
    if node not in graph:
        print("node is not in graph")
        return
    if node not in visited:
        print(node)
        visited.append(node)
        for i in graph[node]:
            DFS(i,visited,graph)
add_node('a')
add_node('b')
add_node('c')
add_edge('a','c',10)
graph = DFS()
print(graph)