# from collections import deque

# def bfs(graph, source_node, num_nodes):
#     visited = [False] * num_nodes
#     queue = deque([source_node])
#     visited[source_node] = True
#     traversal_path = []

#     while queue:
#         current_node = queue.popleft()
#         traversal_path.append(current_node + 1)

#         for neighbor in range(num_nodes):
#             if graph[current_node][neighbor] == 1 and not visited[neighbor]:
#                 visited[neighbor] = True
#                 queue.append(neighbor)
    
#     return traversal_path

# def main():
#     num_nodes = int(input("Enter the number of nodes in the graph: "))

#     print("Enter the adjacency matrix (row by row, space-separated values):")
#     graph = []
#     for i in range(num_nodes):
#         row = list(map(int, input().split()))
#         graph.append(row)

#     source_node = int(input("Enter the source node: ")) - 1

#     traversal_path = bfs(graph, source_node, num_nodes)

#     print("BFS Traversal Path:", traversal_path)

# if __name__ == "__main__":
#     main()


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
