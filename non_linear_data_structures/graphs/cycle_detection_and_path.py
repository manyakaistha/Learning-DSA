def is_cyclic(graph, start_vertex, visiting=None, visited=None):
    if visiting is None:
        visiting = set()
    if visited is None:
        visited = set()

    visiting.add(start_vertex)

    for neighbor in graph.graph[start_vertex]:
        if neighbor in visiting:
            return True
        if neighbor not in visited:
            if is_cyclic(graph, neighbor, visiting, visited):
                return True

    visiting.remove(start_vertex)
    visited.add(start_vertex)
    return False

def cycle_path(graph, start_vertex):
    visited = set()
    stack = []
    parent = {start_vertex: None}

    def dfs_cycle(vertex):
        visited.add(vertex)
        stack.append(vertex)

        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                parent[neighbor] = vertex
                return True
            elif neighbor in stack:
                cycle = []
                current = vertex
                while current != neighbor:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(neighbor)
                cycle.append(vertex)
                # print(f"Cycle found: {' -> '.join(cycle)}")
                # return True
                return cycle

        stack.pop()
        return False

    return dfs_cycle(start_vertex)
