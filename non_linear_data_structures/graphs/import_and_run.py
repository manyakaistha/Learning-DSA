from list_basic_graph_implementation import Graph

def test_graph():
    # Test undirected graph
    print("Testing Undirected Graph:")
    g = Graph()

    # Test adding vertices and edges
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')

    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    g.add_edge('D', 'A')

    print("Vertices:", g.get_vertices())
    print("Edges:", g.get_edges())

    # Test removing edge and vertex
    g.remove_edge('A', 'B')
    print("\nAfter removing edge A-B:")
    print("Edges:", g.get_edges())

    g.remove_vertex('C')
    print("\nAfter removing vertex C:")
    print("Vertices:", g.get_vertices())
    print("Edges:", g.get_edges())

    # Test directed graph
    print("\nTesting Directed Graph:")
    dg = Graph(directed=True)

    dg.add_vertex('X')
    dg.add_vertex('Y')
    dg.add_vertex('Z')

    dg.add_edge('X', 'Y')
    dg.add_edge('Y', 'Z')
    dg.add_edge('Z', 'X')

    print("Vertices:", dg.get_vertices())
    print("Edges:", dg.get_edges())

if __name__ == "__main__":
    test_graph()
