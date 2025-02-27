def is_cyclic(graph, start_vertex, visiting=None, visited=None, parent=None):
    if visiting is None:
        visiting = set()
    if visited is None:
        visited = set()
    if parent is None:
        parent = None

    visiting.add(start_vertex)

    for neighbor, _ in graph.graph[start_vertex]:
        #skips the edge back to parent if undirected graph
        if not graph.directed and neighbor == parent:
            continue

        if neighbor in visiting:
            return True
        if neighbor not in visited:
            if is_cyclic(graph, neighbor, visiting, visited, start_vertex):
                return True

    visiting.remove(start_vertex)
    visited.add(start_vertex)
    return False

def cycle_path(graph, start_vertex):
    visited = set()
    stack = []
    parent = {start_vertex: None}

    def dfs_cycle(vertex, parent_vertex=None):
        visited.add(vertex)
        stack.append(vertex)

        for neighbor, _ in graph.graph[vertex]:
            #skips the edge back to parent if undirected graph
            if not graph.directed and neighbor == parent_vertex:
                continue

            if neighbor not in visited:
                parent[neighbor] = vertex
                result = dfs_cycle(neighbor, vertex)
                if result:
                    return result
            elif neighbor in stack:
                cycle = []
                current = vertex
                while current != neighbor:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(neighbor)
                cycle.append(vertex)
                return cycle

        stack.pop()
        return False

    return dfs_cycle(start_vertex)
