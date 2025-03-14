#!/usr/bin/env python3

"""Graph Traversal Algorithms Demonstration

This module demonstrates BFS and DFS traversal algorithms on various test graphs.
"""

# Import test graphs
from .._test_graph import (
    create_simple_graph,
    create_complex_graph
)

# Import graph algorithms
from ..BFS_list_graph import bfs, bfs_level_order
from ..DFS_list_graph import dfs_recursive, dfs_iterative, dfs_path


def print_subsection_header(title):
    """Print a formatted subsection header"""
    print("\n" + "-" * 60)
    print(f" {title} ".center(60, "-"))
    print("-" * 60)


def demonstrate_traversal_algorithms():
    """Demonstrate BFS and DFS traversal algorithms"""
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