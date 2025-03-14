def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph.graph}
    distances[source] = 0
    predecessors = {vertex: None for vertex in graph.graph}

    unvisited = set(graph.graph.keys())

    while unvisited:
        current = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current] == float('inf'):
            break

        unvisited.remove(current)

        for neighbor, weight in graph.graph[current]:
            if neighbor in unvisited:
                distance = distances[current] + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current

    return distances, predecessors

def get_shortest_path(predecessors, target):
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = predecessors[current]

    return path[::-1]
