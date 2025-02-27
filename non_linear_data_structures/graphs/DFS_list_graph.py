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

def dfs_iterative(graph, start_index):
    visited = set()
    stack = [start_index]
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
