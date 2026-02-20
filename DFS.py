def dfs(v):
    visited[v] = True
    print(v, end=" ")
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n = int(input("Enter number of vertices: "))
graph = [[] for _ in range(n)]

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)   # remove this line if graph is directed

visited = [False] * n

start = int(input("Enter starting vertex: "))
dfs(start)
