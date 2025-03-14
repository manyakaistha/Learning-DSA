def shortest_path(graph, start, end):
    if start not in graph.graph or end not in graph.graph:
        return None, float('inf')

    distances = {vertex: float('inf') for vertex in graph.graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph.graph}

    pq = [(0, start)]
    visited = set()

    while pq:
        current_distance, current_vertex = min(pq)
        pq.remove((current_distance, current_vertex))

        if current_vertex == end:
            break

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.graph[current_vertex]:
            if neighbor in visited:
                continue

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                pq.append((distance, neighbor))

    if distances[end] == float('inf'):
        return None, float('inf')

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]

    return path[::-1], distances[end]
