#!/usr/bin/env python3

"""Graph Cycle Detection Algorithms Demonstration

This module demonstrates cycle detection algorithms for both directed and undirected graphs.
"""

# Import test graphs
from .._test_graph import (
    create_simple_graph,
    create_complex_graph,
    create_directed_acyclic_graph,
    create_cyclic_directed_graph
)

# Import graph algorithms
from ..cycle_detection_and_path_undirected_graph import detect_cycle_undirected, find_cycle_path_undirected
from ..cycle_detection_and_path_directed_graph import is_cyclic as is_cyclic_directed, cycle_path as cycle_path_directed
from ..cycle_detection_universal import is_cyclic as is_cyclic_universal, cycle_path as cycle_path_universal


def print_subsection_header(title):
    """Print a formatted subsection header"""
    print("\n" + "-" * 60)
    print(f" {title} ".center(60, "-"))
    print("-" * 60)


def demonstrate_cycle_detection():
    """Demonstrate cycle detection algorithms"""
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