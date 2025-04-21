import heapq

def a_star(graph, heuristics, start, goal):
    open_set = [(heuristics[start], 0, start, [start])]
    visited = set()

    while open_set:
        f_cost, g_cost, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g_cost

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g_cost + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float("inf")



# Define the graph (node: [(neighbor, cost)])
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

# Heuristic estimates to goal 'G'
heuristics = {
    'A': 7, 'B': 6, 'C': 5,
    'D': 4, 'E': 3, 'F': 6,
    'G': 0
}

start_node = 'A'
goal_node = 'G'

path, cost = a_star(graph, heuristics, start_node, goal_node)
print("A* Path:", " -> ".join(path))
print("Total Cost:", cost)
