INF = 9999

# Input section
n = int(input("Enter number of vertices: "))
graph = []

print(f"\nEnter the {n}x{n} adjacency matrix (row by row):")
for _ in range(n):
    graph.append(list(map(int, input().split())))

# Logic section
selected = [False] * n
selected[0] = True # Starting from the first vertex
total_weight = 0

print("\nMinimum Spanning Tree Edges:")
print("Edge   : Weight")

for _ in range(n - 1):
    minimum = INF
    x = 0 # Source vertex
    y = 0 # Destination vertex

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x, y = i, j

    # Using (x + 1) and (y + 1) to convert 0-indexed logic to 1-indexed display
    print(f"{x + 1} - {y + 1} : {graph[x][y]}")
    selected[y] = True
    total_weight += graph[x][y]

print(f"\nTotal Weight of MST: {total_weight}")