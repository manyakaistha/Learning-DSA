import heapq

def prims_mst(graph):
    if graph.directed:
        raise ValueError("Prim's algorithm works only for undirected graphs")

    if not graph.graph:
        return [], 0

    # Start from first vertex
    start_vertex = next(iter(graph.graph))

    # Track visited vertices and MST edges
    visited = set()
    mst_edges = []
    total_weight = 0

    # Priority queue: (weight, vertex, parent)
    pq = [(0, start_vertex, None)]

    while pq and len(visited) < len(graph.graph):
        weight, current, parent = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if parent is not None:
            mst_edges.append((parent, current, weight))
            total_weight += weight

        # Add all edges from current vertex to unvisited neighbors
        for neighbor, edge_weight in graph.graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor, current))

    return mst_edges, total_weight
