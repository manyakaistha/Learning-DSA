#!/usr/bin/env python3

"""Graph Minimum Spanning Tree Algorithms Demonstration

This module demonstrates minimum spanning tree algorithms including Prim's and Kruskal's algorithms.
"""

# Import test graphs
from .._test_graph import create_weighted_graph
from ..list_basic_graph_implementation import WeightedGraph

# Import graph algorithms
from ..minimum_spanning_tree_prims_algorithm import prims_mst
from ..minimum_cost_spanning_tree_kruskals_algorithm import kruskals_mst, kruskals_mst_union_find


def print_subsection_header(title):
    """Print a formatted subsection header"""
    print("\n" + "-" * 60)
    print(f" {title} ".center(60, "-"))
    print("-" * 60)


def demonstrate_minimum_spanning_tree():
    """Demonstrate minimum spanning tree algorithms"""
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