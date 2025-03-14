#!/usr/bin/env python3

"""Graph Shortest Path Algorithms Demonstration

This module demonstrates various shortest path algorithms including basic shortest path,
Dijkstra's algorithm, Bellman-Ford algorithm, and Floyd-Warshall algorithm.
"""

# Import test graphs
from .._test_graph import create_weighted_graph
from ..list_basic_graph_implementation import WeightedGraph

# Import graph algorithms
from ..shortest_path_algorithm import shortest_path
from ..shortest_path_algorithm_dijkstras_algorithm import dijkstra, get_shortest_path
from ..shortest_path_algorithm_bellman_ford import bellman_ford, get_shortest_path_bellman_ford
from ..shortest_path_algorithm_floyd_warshall import floyd_warshall, get_shortest_path_floyd_warshall


def print_subsection_header(title):
    """Print a formatted subsection header"""
    print("\n" + "-" * 60)
    print(f" {title} ".center(60, "-"))
    print("-" * 60)


def demonstrate_shortest_path():
    """Demonstrate shortest path algorithms"""
    # Create weighted graph
    weighted_edges = create_weighted_graph()
    weighted_graph = WeightedGraph()
    for v1, v2, weight in weighted_edges:
        weighted_graph.add_edge(v1, v2, weight)
    
    # Basic Shortest Path
    print_subsection_header("Basic Shortest Path")
    path, distance = shortest_path(weighted_graph, 'A', 'F')
    print(f"Shortest path from 'A' to 'F': {path} (distance: {distance})")
    
    # Dijkstra's Algorithm
    print_subsection_header("Dijkstra's Algorithm")
    distances, predecessors = dijkstra(weighted_graph, 'A')
    print("Distances from 'A' to all vertices:")
    for vertex, distance in distances.items():
        print(f"  {vertex}: {distance}")
    
    path = get_shortest_path(predecessors, 'F')
    print(f"Shortest path from 'A' to 'F': {path} (distance: {distances['F']})")


def demonstrate_advanced_shortest_path():
    """Demonstrate advanced shortest path algorithms (Bellman-Ford and Floyd-Warshall)"""
    # Create weighted graph with negative edges
    weighted_edges = create_weighted_graph()
    weighted_graph = WeightedGraph()
    for v1, v2, weight in weighted_edges:
        weighted_graph.add_edge(v1, v2, weight)
    
    # Add some negative edges for demonstration
    weighted_graph.add_edge('A', 'B', -2)
    weighted_graph.add_edge('B', 'C', -3)
    
    # Bellman-Ford Algorithm
    print_subsection_header("Bellman-Ford Algorithm")
    distances, predecessors, has_negative_cycle = bellman_ford(weighted_graph, 'A')
    
    if has_negative_cycle:
        print("Graph contains a negative cycle!")
    else:
        print("Distances from 'A' to all vertices (Bellman-Ford):")
        for vertex, distance in distances.items():
            print(f"  {vertex}: {distance}")
        
        path = get_shortest_path_bellman_ford(predecessors, 'F')
        print(f"Shortest path from 'A' to 'F': {path}")
    
    # Floyd-Warshall Algorithm
    print_subsection_header("Floyd-Warshall Algorithm")
    distances, predecessors = floyd_warshall(weighted_graph)
    
    if distances is None:
        print("Graph contains a negative cycle!")
    else:
        print("All-pairs shortest distances:")
        for u in weighted_graph.get_vertices():
            for v in weighted_graph.get_vertices():
                print(f"  {u} -> {v}: {distances[u][v]}")
        
        path = get_shortest_path_floyd_warshall(predecessors, 'A', 'F')
        print(f"Shortest path from 'A' to 'F': {path}")