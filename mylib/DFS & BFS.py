'''   __ A __
     /       \
    C       __B__
    |      /     \
    |     D       E
     \           /
      \         /
        F _____/
'''
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print("Graph:           {}".format(graph))

# DFS iterative visited nodes
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
print("DFS visited:     {}".format(dfs(graph, 'A')))

# DFS resursive visited nodes
visited = set()
def dfs_resursive(graph, start):
    visited.add(start)
    for next_vertex in graph[start] - visited:
        dfs_resursive(graph, next_vertex)
dfs_resursive(graph, 'A')
print("DFS(r) visited:  {}".format(visited))

# BFS visited nodes
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
print("BFS visited:     {}".format(bfs(graph, 'A')))

# DFS iterative all paths
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    res = []
    while stack:
        vertex, path = stack.pop()
        if vertex == goal:
            res.append(path)
        for v in graph[vertex] - set(path):
            stack.append((v, path + [v]))
    return res
print("DFS paths:       {}".format(dfs_paths(graph, 'A', 'F')))

# DFS resursive all paths
res = []
def dfs_paths_recursive(graph, start, goal, path):
    if start == goal:
        res.append(path)
    for vertex in graph[start] - set(path):
        dfs_paths_recursive(graph, vertex, goal, path + [vertex])
dfs_paths_recursive(graph, 'A', 'F', ['A'])
print("DFS(r) paths:    {}".format(res))

# BFS all paths
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    res = []
    while queue:
        vertex, path = queue.pop(0)
        if vertex == goal:
            res.append(path)
        for v in graph[vertex] - set(path):
            queue.append((v, path + [v]))
    return res
print("BFS paths:       {}".format(bfs_paths(graph, 'A', 'F')))

# BFS shortest path
def shortest_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        if vertex == goal:
            return path
        for v in graph[vertex] - set(path):
            queue.append((v, path + [v]))
    return []
print("BFS shortest:    {}".format(shortest_path(graph, 'A', 'F')))
