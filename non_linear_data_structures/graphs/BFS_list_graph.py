from collections import deque

def bfs(graph, start_vertex):
    if start_vertex not in graph.graph:
        return []

    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    traversal_order = []

    while queue:
        vertex = queue.popleft()
        traversal_order.append(vertex)

        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

def bfs_level_order(graph, start_vertex):
    if start_vertex not in graph.graph:
        return {}

    levels = {start_vertex: 0}
    queue = deque([start_vertex])

    while queue:
        vertex = queue.popleft()
        current_level = levels[vertex]

        for neighbor in graph.graph[vertex]:
            if neighbor not in levels:
                levels[neighbor] = current_level + 1
                queue.append(neighbor)

    return levels
