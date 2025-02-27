# visited set
# result list
def dfs_recursive(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()

    if start_vertex not in graph.graph:
        return []

    visited.add(start_vertex)
    traversal = [start_vertex]

    for neighbor in graph.graph[start_vertex]:
        if neighbor not in visited:
            traversal.extend(dfs_recursive(graph, neighbor, visited))

    return traversal

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    traversal = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)

            #reversed to maintain the order same as recursive
            for neighbor in reversed(graph.graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal

def dfs_path(graph, start_vertex, end_vertex, path=None, visited=None):
    if path is None:
        return []
    if visited is None:
        visited = set()

    path.append(start_vertex)
    visited.add(start_vertex)

    if start_vertex == end_vertex:
        return path

    for neighbor in graph.graph[start_vertex]:
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, end_vertex, path, visited)
            if new_path:
                return new_path
    return None
