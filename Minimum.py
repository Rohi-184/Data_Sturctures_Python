INF = 9999

n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix: ")
for _ in range(n):
    graph.append(list(map(int, input().split())))

selected = [False] * n
selected[0] = True

print("Edge : Weight")

for _ in range(n - 1):
    minimum = INF
    x = y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x, y = i, j

    print(x, "-", y, ":", graph[x][y])
    selected[y] = True
