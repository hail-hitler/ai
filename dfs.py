def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")

    for neighbor, is_adjacent in enumerate(graph[start]):
        if is_adjacent == 1 and neighbor not in visited:
            dfs(graph, neighbor, visited)

# --- Main Program ---
n = int(input("Enter the number of vertices: "))
graph = []

print("Enter the adjacency matrix (0 for no edge, 1 for edge):")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start_vertex = int(input(f"Enter the starting vertex (0 to {n-1}): "))
print("DFS Traversal starting from vertex", start_vertex, ":")
dfs(graph, start_vertex)
