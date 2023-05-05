class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    
    def remove_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)
    
    def get_adjacent_vertices(self, v):
        return self.adj_list[v]
# create a graph with 5 vertices
graph = Graph(5)

# add some edges
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

# print adjacent vertices of each vertex
for v in range(graph.num_vertices):
    print(f"Adjacent to {v}: {graph.get_adjacent_vertices(v)}")

# remove an edge
graph.remove_edge(1, 4)

# print adjacent vertices of each vertex again
for v in range(graph.num_vertices):
    print(f"Adjacent to {v}: {graph.get_adjacent_vertices(v)}")
