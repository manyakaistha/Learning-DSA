def is_cyclic(graph, start_vertex, visiting=None, visited=None, parent=None):
    if visiting is None:
        visiting = set()
    if visited is None:
        visited = set()
    if parent is None:
        parent = None

    visiting.add(start_vertex)

    neighbors = graph.graph[start_vertex]
    for neighbor in neighbors:
        # Handle both weighted and unweighted graphs
        if isinstance(neighbor, tuple):
            neighbor_vertex = neighbor[0]
        else:
            neighbor_vertex = neighbor

        #skips the edge back to parent if undirected graph
        if not graph.directed and neighbor_vertex == parent:
            continue

        if neighbor_vertex in visiting:
            return True
        if neighbor_vertex not in visited:
            if is_cyclic(graph, neighbor_vertex, visiting, visited, start_vertex):
                return True
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

        neighbors = graph.graph[vertex]
        for neighbor in neighbors:
            # Handle both weighted and unweighted graphs
            if isinstance(neighbor, tuple):
                neighbor_vertex = neighbor[0]
            else:
                neighbor_vertex = neighbor

            #skips the edge back to parent if undirected graph
            if not graph.directed and neighbor_vertex == parent_vertex:
                continue

            if neighbor_vertex not in visited:
                parent[neighbor_vertex] = vertex
                result = dfs_cycle(neighbor_vertex, vertex)
                if result:
                    return result
            elif neighbor_vertex in stack:
                cycle = []
                current = vertex
                while current != neighbor_vertex:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(neighbor_vertex)
                cycle.append(vertex)
                return cycle

        stack.pop()
        return False

    return dfs_cycle(start_vertex)
