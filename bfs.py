from collections import deque

def bfs(graph, start, n):
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    path = []

    while queue:
        node = queue.popleft()
        path.append(node + 1)

        for neighbor in range(n):
            if graph[node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return path


n = int(input("Number of nodes: "))
print("Enter adjacency matrix:")
graph = [list(map(int, input().split())) for _ in range(n)]

start = int(input("Source node: ")) - 1
result = bfs(graph, start, n)

print("BFS Traversal Path:", result)
