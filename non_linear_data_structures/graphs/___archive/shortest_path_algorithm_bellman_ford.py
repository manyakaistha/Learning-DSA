def bellman_ford(graph, start):
    """
    Bellman-Ford algorithm for finding shortest paths from a source vertex to all other vertices.
    Can handle negative edge weights and detect negative cycles.
    
    Time Complexity: O(VE)
    Space Complexity: O(V)
    
    Args:
        graph: WeightedGraph instance
        start: Starting vertex
    
    Returns:
        tuple: (distances, predecessors, has_negative_cycle)
            - distances: Dictionary of shortest distances from start to each vertex
            - predecessors: Dictionary of predecessors in shortest paths
            - has_negative_cycle: Boolean indicating if a negative cycle exists
    """
    if start not in graph.graph:
        return None, None, False

    # Initialize distances and predecessors
    distances = {vertex: float('inf') for vertex in graph.graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph.graph}
    
    # Relax edges |V| - 1 times
    V = len(graph.graph)
    edges = graph.get_edges()
    
    for _ in range(V - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
    
    # Check for negative cycles
    has_negative_cycle = False
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            has_negative_cycle = True
            break
    
    return distances, predecessors, has_negative_cycle

def get_shortest_path_bellman_ford(predecessors, end):
    """
    Reconstruct the shortest path from the start vertex to the end vertex.
    
    Args:
        predecessors: Dictionary of predecessors from bellman_ford()
        end: End vertex
    
    Returns:
        list: Path from start to end vertex, or None if no path exists
    """
    if predecessors is None or end not in predecessors:
        return None
        
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = predecessors[current]
        
        # Check for cycles
        if current in path:
            return None
            
    return path[::-1] if path else None