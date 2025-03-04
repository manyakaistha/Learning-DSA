from list_basic_graph_implementation import UnweightedGraph as Graph

def create_simple_graph():
    """Returns a simple undirected graph with 5 vertices"""
    g = Graph()
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A'), ('B', 'E')]
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_complex_graph():
    """Returns a more complex undirected graph with 8 vertices"""
    g = Graph()
    edges = [
        ('1', '2'), ('1', '3'), ('2', '4'), ('2', '5'),
        ('3', '5'), ('4', '6'), ('5', '6'), ('5', '7'),
        ('6', '8'), ('7', '8'), ('7', '3')
    ]
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_directed_acyclic_graph():
    """Returns a directed acyclic graph (DAG)"""
    g = Graph(directed=True)
    edges = [
        ('A', 'B'), ('A', 'C'), ('B', 'D'),
        ('C', 'D'), ('D', 'E'), ('C', 'F'),
        ('F', 'E')
    ]
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_cyclic_directed_graph():
    """Returns a directed graph with cycles"""
    g = Graph(directed=True)
    edges = [
        ('1', '2'), ('2', '3'), ('3', '4'),
        ('4', '2'), ('3', '5'), ('5', '6'),
        ('6', '3')
    ]
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g

def create_weighted_graph():
    """Returns a weighted graph (represented as tuples of (vertex1, vertex2, weight))"""
    edges = [
        ('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1),
        ('B', 'D', 5), ('C', 'D', 8), ('C', 'E', 10),
        ('D', 'E', 2), ('D', 'F', 6), ('E', 'F', 3)
    ]
    return edges

def create_large_graph():
    """Returns a large graph for stress testing"""
    g = Graph()
    # Create a graph with 20 vertices and multiple connections
    vertices = [str(i) for i in range(1, 21)]
    for i in range(len(vertices)):
        for j in range(i + 1, min(i + 5, len(vertices))):
            g.add_edge(vertices[i], vertices[j])
    return g

def create_disconnected_graph():
    """Returns a graph with multiple disconnected components"""
    g = Graph()
    # Component 1
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    # Component 2
    g.add_edge('D', 'E')
    g.add_edge('E', 'F')
    # Component 3
    g.add_edge('X', 'Y')
    # Isolated vertex
    g.add_vertex('Z')
    return g
