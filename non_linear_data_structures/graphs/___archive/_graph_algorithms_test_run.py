# this file was not created by me but generated using AI as I had already tested all the files before but wanted to have a sigle file to see them all at once

#!/usr/bin/env python3

"""
Graph Algorithms Demo

This script demonstrates the various graph algorithms implemented in the DSA project.
It imports test graphs from _test_graph.py and runs different algorithms on them.
"""

# Import test graphs
from tests._test_graph import (
    create_simple_graph,
    create_complex_graph,
    create_directed_acyclic_graph,
    create_cyclic_directed_graph,
    create_weighted_graph,
    create_large_graph,
    create_disconnected_graph
)

# Import graph algorithms
from BFS_list_graph import bfs, bfs_level_order
from DFS_list_graph import dfs_recursive, dfs_iterative, dfs_path
from cycle_detection_and_path_directed_graph import is_cyclic as is_cyclic_directed, cycle_path as cycle_path_directed
from cycle_detection_and_path_undirected_graph import detect_cycle_undirected, find_cycle_path_undirected
from cycle_detection_universal import is_cyclic as is_cyclic_universal, cycle_path as cycle_path_universal
from list_basic_graph_implementation import WeightedGraph
from minimum_spanning_tree_prims_algorithm import prims_mst
from shortest_path_algorithm import shortest_path
from shortest_path_algorithm_dijkstras_algorithm import dijkstra, get_shortest_path
from shortest_path_algorithm_bellman_ford import bellman_ford, get_shortest_path_bellman_ford
from shortest_path_algorithm_floyd_warshall import floyd_warshall, get_shortest_path_floyd_warshall
from topological_sort import topological_sort
from topological_sort_kahns_algorithm import kahn_topological_sort
from minimum_cost_spanning_tree_kruskals_algorithm import kruskals_mst, kruskals_mst_union_find


def print_section_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 80)
    print(f" {title} ".center(80, "="))
    print("=" * 80)


def print_subsection_header(title):
    """Print a formatted subsection header"""
    print("\n" + "-" * 60)
    print(f" {title} ".center(60, "-"))
    print("-" * 60)


def demo_traversal_algorithms():
    """Demonstrate BFS and DFS traversal algorithms"""
    print_section_header("Graph Traversal Algorithms")
    
    # Create test graphs
    simple_graph = create_simple_graph()
    complex_graph = create_complex_graph()
    
    # BFS Traversal
    print_subsection_header("BFS Traversal")
    print("Simple Graph BFS from 'A':", bfs(simple_graph, 'A'))
    print("Complex Graph BFS from '1':", bfs(complex_graph, '1'))
    
    # BFS Level Order
    print_subsection_header("BFS Level Order")
    print("Simple Graph BFS Level Order from 'A':")
    levels = bfs_level_order(simple_graph, 'A')
    for vertex, level in levels.items():
        print(f"  {vertex}: Level {level}")
    
    # DFS Recursive
    print_subsection_header("DFS Recursive Traversal")
    print("Simple Graph DFS Recursive from 'A':", dfs_recursive(simple_graph, 'A'))
    print("Complex Graph DFS Recursive from '1':", dfs_recursive(complex_graph, '1'))
    
    # DFS Iterative
    print_subsection_header("DFS Iterative Traversal")
    print("Simple Graph DFS Iterative from 'A':", dfs_iterative(simple_graph, 'A'))
    print("Complex Graph DFS Iterative from '1':", dfs_iterative(complex_graph, '1'))
    
    # DFS Path
    print_subsection_header("DFS Path Finding")
    path = dfs_path(simple_graph, 'A', 'D', [], set())
    print("Path from 'A' to 'D' in Simple Graph:", path)
    path = dfs_path(complex_graph, '1', '8', [], set())
    print("Path from '1' to '8' in Complex Graph:", path)


def demo_cycle_detection():
    """Demonstrate cycle detection algorithms"""
    print_section_header("Cycle Detection Algorithms")
    
    # Create test graphs
    simple_graph = create_simple_graph()
    complex_graph = create_complex_graph()
    dag = create_directed_acyclic_graph()
    cyclic_directed = create_cyclic_directed_graph()
    
    # Undirected Cycle Detection
    print_subsection_header("Undirected Cycle Detection")
    print("Simple Graph has cycle:", detect_cycle_undirected(simple_graph))
    print("Complex Graph has cycle:", detect_cycle_undirected(complex_graph))
    
    # Undirected Cycle Path
    print_subsection_header("Undirected Cycle Path")
    cycle = find_cycle_path_undirected(simple_graph)
    print("Cycle in Simple Graph:", cycle)
    cycle = find_cycle_path_undirected(complex_graph)
    print("Cycle in Complex Graph:", cycle)
    
    # Directed Cycle Detection
    print_subsection_header("Directed Cycle Detection")
    print("DAG has cycle:", is_cyclic_directed(dag, list(dag.graph.keys())[0]))
    print("Cyclic Directed Graph has cycle:", is_cyclic_directed(cyclic_directed, '1'))
    
    # Directed Cycle Path
    print_subsection_header("Directed Cycle Path")
    cycle = cycle_path_directed(cyclic_directed, '1')
    print("Cycle in Cyclic Directed Graph:", cycle)
    
    # Universal Cycle Detection
    print_subsection_header("Universal Cycle Detection")
    print("Simple Graph (undirected) has cycle:", is_cyclic_universal(simple_graph, list(simple_graph.graph.keys())[0]))
    print("DAG (directed) has cycle:", is_cyclic_universal(dag, list(dag.graph.keys())[0]))
    print("Cyclic Directed Graph has cycle:", is_cyclic_universal(cyclic_directed, '1'))
    
    # Universal Cycle Path
    print_subsection_header("Universal Cycle Path")
    cycle = cycle_path_universal(cyclic_directed, '1')
    print("Cycle in Cyclic Directed Graph (universal):", cycle)


def demo_shortest_path():
    """Demonstrate shortest path algorithms"""
    print_section_header("Shortest Path Algorithms")
    
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


def demo_minimum_spanning_tree():
    """Demonstrate minimum spanning tree algorithms"""
    print_section_header("Minimum Spanning Tree Algorithms")
    
    # Create weighted graph
    weighted_edges = create_weighted_graph()
    weighted_graph = WeightedGraph()
    for v1, v2, weight in weighted_edges:
        weighted_graph.add_edge(v1, v2, weight)
    
    # Prim's Algorithm
    print_subsection_header("Prim's Algorithm")
    mst_edges, total_weight = prims_mst(weighted_graph)
    print("Minimum Spanning Tree Edges (Prim's):")
    for edge in mst_edges:
        print(f"  {edge[0]} -- {edge[1]} (weight: {edge[2]})")
    print(f"Total MST Weight: {total_weight}")
    
    # Kruskal's Algorithm (without Union-Find)
    print_subsection_header("Kruskal's Algorithm (without Union-Find)")
    mst_edges, total_weight = kruskals_mst(weighted_graph.graph)
    print("Minimum Spanning Tree Edges (Kruskal's):")
    for edge in mst_edges:
        print(f"  {edge[0]} -- {edge[1]} (weight: {edge[2]})")
    print(f"Total MST Weight: {total_weight}")
    
    # Kruskal's Algorithm (with Union-Find)
    print_subsection_header("Kruskal's Algorithm (with Union-Find)")
    mst_edges, total_weight = kruskals_mst_union_find(weighted_graph)
    print("Minimum Spanning Tree Edges (Kruskal's with Union-Find):")
    for edge in mst_edges:
        print(f"  {edge[0]} -- {edge[1]} (weight: {edge[2]})")
    print(f"Total MST Weight: {total_weight}")


def demo_topological_sort():
    """Demonstrate topological sorting algorithms"""
    print_section_header("Topological Sorting Algorithms")
    
    # Create directed acyclic graph
    dag = create_directed_acyclic_graph()
    
    # DFS-based Topological Sort
    print_subsection_header("DFS-based Topological Sort")
    sorted_vertices = topological_sort(dag, list(dag.graph.keys())[0])
    print("Topological order:", sorted_vertices)
    
    # Kahn's Algorithm
    print_subsection_header("Kahn's Algorithm")
    sorted_vertices = kahn_topological_sort(dag)
    print("Topological order (Kahn's):", sorted_vertices)


def demo_advanced_shortest_path():
    """Demonstrate advanced shortest path algorithms (Bellman-Ford and Floyd-Warshall)"""
    print_section_header("Advanced Shortest Path Algorithms")
    
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


def main():
    """Main function to run all demonstrations"""
    print("\n" + "*" * 100)
    print("GRAPH ALGORITHMS DEMONSTRATION".center(100))
    print("*" * 100)
    
    demo_traversal_algorithms()
    demo_cycle_detection()
    demo_shortest_path()
    demo_advanced_shortest_path()
    demo_minimum_spanning_tree()
    demo_topological_sort()
    
    print("\n" + "*" * 100)
    print("END OF DEMONSTRATION".center(100))
    print("*" * 100 + "\n")


if __name__ == "__main__":
    main()