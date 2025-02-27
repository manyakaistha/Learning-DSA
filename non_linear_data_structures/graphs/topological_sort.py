def topological_sort(graph, start_vertex, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    if start_vertex not in graph.graph:
        return []

    visited.add(start_vertex)

    for neighbor in graph.graph[start_vertex]:
        if neighbor not in visited:
           topological_sort(graph, start_vertex, visited, result)

    # result.insert(0, start_vertex) # This works but is ineffecient as we insert at the start of the list
    # return result
    result.append(start_vertex) #jsut append and only reverse the list when the whole graph has been traversed

    if len(result) == len(graph.graph):
        result.reverse()

    return result
