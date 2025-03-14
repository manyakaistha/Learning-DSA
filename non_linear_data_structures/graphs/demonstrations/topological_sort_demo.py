#!/usr/bin/env python3

"""Graph Topological Sort Algorithms Demonstration

This module demonstrates topological sorting algorithms including DFS-based and Kahn's algorithm.
"""

# Import test graphs
from .._test_graph import create_directed_acyclic_graph

# Import graph algorithms
from ..topological_sort import topological_sort
from ..topological_sort_kahns_algorithm import kahn_topological_sort


def print_subsection_header(title):
    """Print a formatted subsection header"""
    print("\n" + "-" * 60)
    print(f" {title} ".center(60, "-"))
    print("-" * 60)


def demonstrate_topological_sort():
    """Demonstrate topological sorting algorithms"""
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