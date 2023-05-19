def dfs(node,visited,graph):
    if node not in visited:
        print('node note present')
        return
    if node not in visited:
        visited.add(node)
        for i in graph[node]:
            dfs(node,visited,graph)
        