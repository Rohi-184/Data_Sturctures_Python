def dfs(v, n, matrix, visited):
    visited[v] = True
    print(v, end=" ")

    # Iterate through all possible nodes i
    for i in range(n):
        # Check if there is an edge AND if it hasn't been visited
        if matrix[v][i] == 1 and not visited[i]:
            dfs(i, n, matrix, visited)


n = int(input("Enter number of vertices: "))
print(f"\nEnter the {n}x{n} adjacency matrix (row by row):")

# Initialize and fill the matrix
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

visited = [False] * n
start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
dfs(start, n, matrix, visited)