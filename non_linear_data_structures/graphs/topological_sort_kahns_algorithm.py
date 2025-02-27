from collections import deque

def kahn_topological_sort(graph):
    # calculating the indegree of each node
    in_degree = {vertex:0 for vertex in graph.graph}
    for vertex in graph.graph:
        for neighbor in graph.graph[vertex]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    queue = deque([vertex for vertex, degree in in_degree.items() if degree == 0])

    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph.graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
