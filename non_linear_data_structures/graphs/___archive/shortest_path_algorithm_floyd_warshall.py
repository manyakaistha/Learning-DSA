def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm for finding all-pairs shortest paths.
    Can handle negative edge weights but not negative cycles.
    
    Time Complexity: O(V^3)
    Space Complexity: O(V^2)
    
    Args:
        graph: WeightedGraph instance
    
    Returns:
        tuple: (distances, predecessors)
            - distances: Dictionary of dictionaries containing shortest distances between all pairs of vertices
            - predecessors: Dictionary of dictionaries containing predecessors in shortest paths
    """
    vertices = graph.get_vertices()
    
    # Initialize distances and predecessors
    distances = {}
    predecessors = {}
    
    for u in vertices:
        distances[u] = {}
        predecessors[u] = {}
        for v in vertices:
            if u == v:
                distances[u][v] = 0
            else:
                weight = graph.get_weight(u, v)
                distances[u][v] = weight if weight is not None else float('inf')
                predecessors[u][v] = u if weight is not None else None
    
    # Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distances[i][k] != float('inf') and distances[k][j] != float('inf'):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
                        predecessors[i][j] = predecessors[k][j]
    
    # Check for negative cycles
    for v in vertices:
        if distances[v][v] < 0:
            return None, None
    
    return distances, predecessors

def get_shortest_path_floyd_warshall(predecessors, start, end):
    """
    Reconstruct the shortest path between two vertices using Floyd-Warshall predecessors.
    
    Args:
        predecessors: Dictionary of dictionaries from floyd_warshall()
        start: Start vertex
        end: End vertex
    
    Returns:
        list: Path from start to end vertex, or None if no path exists
    """
    if predecessors is None or start not in predecessors or end not in predecessors[start]:
        return None
    
    path = [start]
    current = start
    
    while current != end:
        current = predecessors[current][end]
        if current is None:
            return None
        if current in path:
            return None  # Cycle detected
        path.append(current)
    
    return path