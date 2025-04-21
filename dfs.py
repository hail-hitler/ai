from collections import deque

def dfs(graph, start, n):
    visited = [False] * n
    stack = [start]
    path = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            path.append(node + 1)
            for neighbor in reversed(range(n)):
                if graph[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

    return path


n = int(input("Number of nodes: "))
print("Enter adjacency matrix:")
graph = [list(map(int, input().split())) for _ in range(n)]

start = int(input("Source node: ")) - 1
result = dfs(graph, start, n)

print("DFS Traversal Path:", result)
