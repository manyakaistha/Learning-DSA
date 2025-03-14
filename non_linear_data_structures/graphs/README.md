# Graph Algorithms Bible

## Table of Contents
1. [Introduction to Graphs](#introduction-to-graphs)
   - What is a Graph?
   - Types of Graphs
   - Graph Representations
   - Real-world Applications

2. [Graph Implementation](#graph-implementation)
   - Basic Graph Classes
   - Weighted vs Unweighted Graphs
   - Directed vs Undirected Graphs
   - Implementation Analysis

3. [Graph Traversal Algorithms](#graph-traversal-algorithms)
   - Breadth-First Search (BFS)
   - Depth-First Search (DFS)
   - Comparison and Use Cases

4. [Cycle Detection](#cycle-detection)
   - In Directed Graphs
   - In Undirected Graphs
   - Universal Cycle Detection
   - Applications and Examples

5. [Shortest Path Algorithms](#shortest-path-algorithms)
   - Basic Shortest Path
   - Dijkstra's Algorithm
   - Bellman-Ford Algorithm
   - Floyd-Warshall Algorithm
   - Comparison and When to Use Each

6. [Minimum Spanning Trees](#minimum-spanning-trees)
   - Prim's Algorithm
   - Kruskal's Algorithm
   - Union-Find Data Structure
   - Applications

7. [Topological Sorting](#topological-sorting)
   - DFS-based Approach
   - Kahn's Algorithm
   - Applications in Scheduling

8. [Interview Questions and Practice Problems](#interview-questions)
   - Common Graph Problems
   - Solution Strategies
   - Edge Cases

9. [Glossary](#glossary)
   - Terms and Definitions
   - Common Notations

## Introduction to Graphs

### What is a Graph?

A graph is a fundamental data structure that consists of a set of vertices (also called nodes) and a set of edges that connect these vertices. Think of it as a network of points connected by lines.

```
Example Graph:

A ---- B
|      |
|      |
C ---- D
```

In this simple example:
- Vertices: A, B, C, D
- Edges: (A,B), (A,C), (B,D), (C,D)

### Types of Graphs

1. **Undirected Graph**
   - Edges have no direction
   - If A is connected to B, then B is connected to A
   - Example: Social network friendships

2. **Directed Graph (Digraph)**
   - Edges have direction
   - If A points to B, B might not point to A
   - Example: Web pages and links

3. **Weighted Graph**
   - Edges have weights/costs
   - Example: Road network with distances

4. **Unweighted Graph**
   - All edges have equal importance
   - Example: Social connections

### Graph Representations

1. **Adjacency List**
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

2. **Adjacency Matrix**
```python
#     A  B  C  D
A = [[0, 1, 1, 0],  # A
     [1, 0, 0, 1],  # B
     [1, 0, 0, 1],  # C
     [0, 1, 1, 0]]  # D
```

### Real-world Applications

1. **Social Networks**
   - Vertices: Users
   - Edges: Friendships/Connections

2. **Transportation Networks**
   - Vertices: Cities/Intersections
   - Edges: Roads/Routes
   - Weights: Distances/Travel Times

3. **Computer Networks**
   - Vertices: Devices/Servers
   - Edges: Connections
   - Weights: Bandwidth/Latency

4. **Dependency Management**
   - Vertices: Tasks/Modules
   - Edges: Dependencies
   - Example: Build systems, Package managers

## Graph Implementation

### Basic Graph Classes

In our implementation, we have two main graph classes: `UnweightedGraph` and `WeightedGraph`. Let's understand each in detail.

#### UnweightedGraph Class

The `UnweightedGraph` class represents a graph where edges don't have weights. This is useful for modeling simple connections, like social networks or basic routing problems.

```python
class UnweightedGraph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
```

Key features:
1. Uses adjacency list representation (dictionary of lists)
2. Supports both directed and undirected graphs
3. Simple and memory-efficient for sparse graphs

Core methods:

1. **add_vertex(vertex)**
   - Adds a new vertex to the graph
   - Creates an empty list for its neighbors

2. **add_edge(vertex1, vertex2)**
   - Adds an edge between two vertices
   - For undirected graphs, adds both directions

3. **remove_vertex(vertex)**
   - Removes a vertex and all its edges
   - Updates all affected adjacency lists

4. **remove_edge(vertex1, vertex2)**
   - Removes the edge between two vertices
   - For undirected graphs, removes both directions

#### WeightedGraph Class

The `WeightedGraph` class extends the basic graph concept by adding weights to edges. This is essential for problems involving distances, costs, or capacities.

```python
class WeightedGraph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
```

Key differences from UnweightedGraph:
1. Edges store both destination and weight: `(vertex, weight)`
2. Methods handle the additional weight parameter
3. More suitable for algorithms like Dijkstra's or Prim's

Core methods:

1. **add_edge(vertex1, vertex2, weight)**
   - Adds a weighted edge between vertices
   - Weight represents cost/distance/capacity

2. **get_weight(vertex1, vertex2)**
   - Returns the weight of the edge
   - Returns None if no edge exists

### Implementation Analysis

#### Time Complexity

For a graph with V vertices and E edges:

1. **Adjacency List (Our Implementation)**
   - Add vertex: O(1)
   - Add edge: O(1)
   - Remove vertex: O(V + E)
   - Remove edge: O(degree(v))
   - Find edge: O(degree(v))
   - Space: O(V + E)

2. **Adjacency Matrix (Alternative)**
   - Add vertex: O(V²)
   - Add edge: O(1)
   - Remove vertex: O(V²)
   - Remove edge: O(1)
   - Find edge: O(1)
   - Space: O(V²)

#### When to Use Each Implementation

**Use Adjacency List (Our Implementation) when:**
- The graph is sparse (E << V²)
- You need to iterate over neighbors
- Memory efficiency is important
- You're implementing most graph algorithms

**Use Adjacency Matrix when:**
- The graph is dense (E ≈ V²)
- You need constant-time edge lookups
- The graph is small
- You're doing matrix operations

### Example Usage

```python
# Creating an undirected, unweighted graph
ug = UnweightedGraph()
ug.add_edge('A', 'B')
ug.add_edge('B', 'C')
ug.add_edge('C', 'A')

# Creating a directed, weighted graph
wg = WeightedGraph(directed=True)
wg.add_edge('X', 'Y', 5)
wg.add_edge('Y', 'Z', 3)
wg.add_edge('Z', 'X', 4)
```

### Common Pitfalls

1. **Forgetting Directionality**
   - Always check if the graph is directed
   - Handle both directions for undirected graphs

2. **Edge Weight Handling**
   - Validate weight values (negative weights can break some algorithms)
   - Consider default weights for unweighted conversions

3. **Vertex Existence**
   - Check if vertices exist before operations
   - Handle missing vertex cases gracefully

4. **Memory Management**
   - Be careful with large graphs
   - Consider using more efficient data structures for specific cases

### Interview Practice Questions

1. **Basic Implementation**
   Q: Implement a method to check if a graph is bipartite using the given graph class.
   
2. **Edge Cases**
   Q: How would you modify the WeightedGraph class to support parallel edges?

3. **Optimization**
   Q: Design a memory-efficient representation for a complete graph.

4. **Real-world Application**
   Q: How would you extend the graph classes to support edge attributes beyond weights?

## Graph Traversal Algorithms

### Breadth-First Search (BFS)

BFS is a traversal algorithm that explores a graph level by level, visiting all neighbors of a vertex before moving to the next level.

#### Algorithm Overview

```python
def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    traversal_order = []

    while queue:
        vertex = queue.popleft()
        traversal_order.append(vertex)

        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order
```

#### How BFS Works

1. Start at a given vertex
2. Visit all its neighbors
3. For each neighbor, visit their unvisited neighbors
4. Continue until all reachable vertices are visited

Example:
```
Graph:          BFS from A:
A --- B         Level 0: A
|     |         Level 1: B, C
C --- D         Level 2: D

Traversal Order: A -> B -> C -> D
```

#### Applications

1. **Shortest Path (Unweighted)**
   - Finding shortest path in unweighted graphs
   - Each level represents distance from start

2. **Level Order Traversal**
   - Web crawling (level = clicks from start)
   - Social network connections (friend levels)

3. **Connected Components**
   - Finding all nodes reachable from a start point
   - Network analysis

### Depth-First Search (DFS)

DFS explores a graph by going as deep as possible along each branch before backtracking.

#### Algorithm Overview

```python
def dfs_recursive(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(start_vertex)
    traversal = [start_vertex]

    for neighbor in graph.graph[start_vertex]:
        if neighbor not in visited:
            traversal.extend(dfs_recursive(graph, neighbor, visited))

    return traversal
```

#### How DFS Works

1. Start at a given vertex
2. Recursively visit an unvisited neighbor
3. Backtrack when no unvisited neighbors remain
4. Continue until all reachable vertices are visited

Example:
```
Graph:          DFS from A:
A --- B         Path: A → B → D → C
|     |         
C --- D         Stack: [A] → [A,B] → [A,B,D] → [A,B,D,C]

Traversal Order: A -> B -> D -> C
```

#### Applications

1. **Cycle Detection**
   - Finding cycles in graphs
   - Detecting back edges

2. **Topological Sorting**
   - Dependency resolution
   - Task scheduling

3. **Path Finding**
   - Maze solving
   - Game state exploration

### BFS vs DFS Comparison

#### Time and Space Complexity

Both BFS and DFS:
- Time: O(V + E) where V = vertices, E = edges
- Space: O(V) for visited set and queue/stack

#### When to Use Each

**Use BFS when:**
- Finding shortest paths in unweighted graphs
- Level-by-level exploration is needed
- Target is likely closer to start
- Memory is not a constraint

**Use DFS when:**
- Exploring all possible paths
- Memory is limited (can be implemented with recursion)
- Target is likely far from start
- Topological sorting is needed

### Interview Practice Questions

1. **Path Finding**
   Q: Given a 2D grid with obstacles, find the shortest path from start to end using BFS.

2. **Graph Properties**
   Q: Use DFS to determine if a graph is bipartite.

3. **Optimization**
   Q: Implement an iterative version of DFS without using recursion.

4. **Real-world Application**
   Q: How would you use BFS to find all users within N degrees of connection in a social network?

## Cycle Detection

### Understanding Cycles

A cycle in a graph is a path that starts and ends at the same vertex. Cycle detection is crucial for many applications, from detecting deadlocks to finding redundant dependencies.

### In Directed Graphs

Detecting cycles in directed graphs requires tracking vertices in the current recursion stack.

#### Algorithm Overview

```python
def is_cyclic(graph, start_vertex, visiting=None, visited=None):
    if visiting is None:
        visiting = set()
    if visited is None:
        visited = set()

    visiting.add(start_vertex)

    for neighbor in graph.graph[start_vertex]:
        if neighbor in visiting:
            return True
        if neighbor not in visited:
            if is_cyclic(graph, neighbor, visiting, visited):
                return True

    visiting.remove(start_vertex)
    visited.add(start_vertex)
    return False
```

#### How It Works

1. Maintain two sets:
   - `visiting`: Vertices in current DFS path
   - `visited`: All processed vertices

2. For each vertex:
   - Mark it as 'visiting'
   - Explore its neighbors
   - If we find a 'visiting' neighbor, we found a cycle
   - After processing, mark as 'visited'

Example:
```
Directed Graph:    DFS Path:
1 → 2 → 3         1 → 2 → 3 → 4
    ↑   ↓         Found cycle when
    4 ← 5         reaching 2 again
```

### In Undirected Graphs

Undirected cycle detection is simpler but requires tracking parent vertices to avoid false cycles.

#### Algorithm Overview

```python
def detect_cycle_undirected(graph):
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor in graph.graph[vertex]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True
            if dfs(neighbor, vertex):
                return True
        return False

    for vertex in graph.graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False
```

#### How It Works

1. Use DFS traversal
2. Track parent vertex to avoid false cycles
3. If we find a visited non-parent neighbor, we found a cycle

Example:
```
Undirected Graph:  DFS Path:
A --- B           A → B → C
|     |          Found cycle when
C --- D          reaching A from C
```

### Universal Cycle Detection

Our universal cycle detection works for both directed and undirected graphs.

```python
def is_cyclic_universal(graph, start_vertex, visiting=None, visited=None, parent=None):
    if visiting is None:
        visiting = set()
    if visited is None:
        visited = set()

    visiting.add(start_vertex)

    for neighbor in graph.graph[start_vertex]:
        if not graph.directed and neighbor == parent:
            continue
        if neighbor in visiting:
            return True
        if neighbor not in visited:
            if is_cyclic_universal(graph, neighbor, visiting, visited, start_vertex):
                return True

    visiting.remove(start_vertex)
    visited.add(start_vertex)
    return False
```

### Applications and Examples

1. **Deadlock Detection**
   - Resource allocation graphs
   - Process dependencies

2. **Dependency Analysis**
   - Package dependencies
   - Build systems

3. **Circuit Analysis**
   - Finding feedback loops
   - Electronic circuit verification

### Time and Space Complexity

- Time: O(V + E)
  - We visit each vertex once
  - We explore each edge once

- Space: O(V)
  - For visited and visiting sets
  - Recursion stack in worst case

### Interview Practice Questions

1. **Basic Implementation**
   Q: Implement a function to find and print all cycles in a directed graph.

2. **Edge Cases**
   Q: How would you modify the cycle detection algorithm to work with weighted edges?

3. **Optimization**
   Q: Design an algorithm to find the shortest cycle in an undirected graph.

4. **Real-world Application**
   Q: How would you use cycle detection to find circular dependencies in a software project?

## Shortest Path Algorithms

### Overview

Shortest path algorithms find the minimum cost path between vertices in a graph. Different algorithms handle different scenarios:

- Basic Shortest Path: For unweighted or simple weighted graphs
- Dijkstra's: For non-negative weights
- Bellman-Ford: Handles negative weights
- Floyd-Warshall: All-pairs shortest paths

### Basic Shortest Path

For simple cases, especially with unweighted graphs or when only positive weights are present.

```python
def shortest_path(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph.graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph.graph}

    pq = [(0, start)]
    visited = set()

    while pq:
        current_distance, current_vertex = min(pq)
        pq.remove((current_distance, current_vertex))

        if current_vertex == end:
            break

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                pq.append((distance, neighbor))

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]

    return path[::-1], distances[end]
```

### Dijkstra's Algorithm

The most efficient algorithm for finding shortest paths when all weights are non-negative.

```python
def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph.graph}
    distances[source] = 0
    predecessors = {vertex: None for vertex in graph.graph}

    unvisited = set(graph.graph.keys())

    while unvisited:
        current = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current] == float('inf'):
            break

        unvisited.remove(current)

        for neighbor, weight in graph.graph[current]:
            if neighbor in unvisited:
                distance = distances[current] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current

    return distances, predecessors
```

#### Key Features

1. **Greedy Approach**
   - Always selects the vertex with minimum distance
   - Builds solution incrementally

2. **Optimality**
   - Guarantees shortest paths when weights are non-negative
   - Works with both directed and undirected graphs

### Bellman-Ford Algorithm

Handles graphs with negative weights and detects negative cycles.

```python
def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph.graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph.graph}
    
    V = len(graph.graph)
    edges = graph.get_edges()
    
    for _ in range(V - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
    
    # Check for negative cycles
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None, None, True  # Negative cycle exists
    
    return distances, predecessors, False
```

#### Key Features

1. **Negative Weights**
   - Can handle negative edge weights
   - Detects negative cycles

2. **Relaxation**
   - Performs V-1 iterations of edge relaxation
   - Additional iteration checks for negative cycles

### Floyd-Warshall Algorithm

Finds shortest paths between all pairs of vertices.

```python
def floyd_warshall(graph):
    vertices = graph.get_vertices()
    distances = {}
    predecessors = {}
    
    # Initialize
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
    
    # Floyd-Warshall
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distances[i][k] != float('inf') and distances[k][j] != float('inf'):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
                        predecessors[i][j] = predecessors[k][j]
    
    return distances, predecessors
```

#### Key Features

1. **All-Pairs Shortest Paths**
   - Finds shortest paths between all vertex pairs
   - Works with positive and negative weights

2. **Dynamic Programming**
   - Uses intermediate vertices to find shorter paths
   - O(V³) complexity but simple implementation

### Comparison and When to Use Each

1. **Basic Shortest Path**
   - Use for: Simple graphs, unweighted or positive weights
   - Time: O((V + E) log V) with priority queue
   - Space: O(V)

2. **Dijkstra's Algorithm**
   - Use for: Non-negative weights, single source
   - Time: O((V + E) log V) with priority queue
   - Space: O(V)

3. **Bellman-Ford**
   - Use for: Graphs with negative weights
   - Time: O(VE)
   - Space: O(V)

4. **Floyd-Warshall**
   - Use for: All-pairs shortest paths
   - Time: O(V³)
   - Space: O(V²)

### Interview Practice Questions

1. **Implementation**
   Q: Implement Dijkstra's algorithm using a min-heap priority queue.

2. **Edge Cases**
   Q: Modify Bellman-Ford to return the negative cycle if one exists.

3. **Optimization**
   Q: How would you optimize Floyd-Warshall for sparse graphs?

4. **Real-world Application**
   Q: Design a system to find the fastest route between two points in a city, considering traffic conditions.

## Minimum Spanning Trees

### Overview

A Minimum Spanning Tree (MST) is a subset of edges in a weighted, undirected graph that:
- Connects all vertices
- Has no cycles
- Has minimum total edge weight

### Prim's Algorithm

Builds MST by growing a single tree from a starting vertex.

```python
def prims_mst(graph):
    if not graph.graph:
        return [], 0

    start_vertex = next(iter(graph.graph))
    visited = set()
    mst_edges = []
    total_weight = 0

    pq = [(0, start_vertex, None)]

    while pq and len(visited) < len(graph.graph):
        weight, current, parent = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if parent is not None:
            mst_edges.append((parent, current, weight))
            total_weight += weight

        for neighbor, edge_weight in graph.graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor, current))

    return mst_edges, total_weight
```

#### How Prim's Works

1. Start from any vertex
2. Add the minimum weight edge that connects a visited vertex to an unvisited vertex
3. Repeat until all vertices are visited

Example:
```
Graph:           MST Construction:
A --2-- B       Step 1: A --2-- B
|      |        Step 2: A --2-- B
4      3        |             
|      |        4             
C --1-- D       |             
                C --1-- D
```

### Kruskal's Algorithm

Builds MST by selecting edges in order of increasing weight.

```python
def kruskals_mst_union_find(graph):
    edges = []
    for vertex in graph.graph:
        for neighbor, weight in graph.graph[vertex]:
            if (neighbor, vertex, weight) not in edges:
                edges.append((vertex, neighbor, weight))
    
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(graph.graph.keys())
    
    mst_edges = []
    total_weight = 0
    
    for vertex1, vertex2, weight in edges:
        if uf.find(vertex1) != uf.find(vertex2):
            uf.union(vertex1, vertex2)
            mst_edges.append((vertex1, vertex2, weight))
            total_weight += weight
    
    return mst_edges, total_weight
```

#### Union-Find Data Structure

Kruskal's algorithm uses Union-Find for efficient cycle detection:

```python
class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}
    
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                root1, root2 = root2, root1
            self.parent[root2] = root1
            if self.rank[root1] == self.rank[root2]:
                self.rank[root1] += 1
```

### Comparison

1. **Time Complexity**
   - Prim's: O(E log V) with binary heap
   - Kruskal's: O(E log E) for sorting edges

2. **Space Complexity**
   - Prim's: O(V) for visited set and heap
   - Kruskal's: O(V) for Union-Find structure

3. **When to Use Each**
   - Prim's: Dense graphs (E ≈ V²)
   - Kruskal's: Sparse graphs (E << V²)

### Applications

1. **Network Design**
   - Computer networks
   - Electrical grids
   - Pipeline systems

2. **Clustering**
   - Hierarchical clustering
   - Image segmentation

3. **Approximation Algorithms**
   - Traveling Salesman Problem
   - Steiner Tree Problem

### Interview Practice Questions

1. **Implementation**
   Q: Implement Prim's algorithm using an adjacency matrix.

2. **Edge Cases**
   Q: How would you modify Kruskal's to find the maximum spanning tree?

3. **Optimization**
   Q: Design an algorithm to update MST when an edge weight changes.

4. **Real-world Application**
   Q: How would you use MST algorithms to design an optimal network infrastructure?

## Topological Sorting

### Overview

Topological sorting arranges vertices in a directed acyclic graph (DAG) such that for every directed edge (u,v), vertex u comes before v in the ordering. It's crucial for dependency resolution and scheduling.

### DFS-based Approach

Uses depth-first search to build the topological order.

```python
def topological_sort(graph, start_vertex, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(start_vertex)

    for neighbor in graph.graph[start_vertex]:
        if neighbor not in visited:
           topological_sort(graph, neighbor, visited, result)

    result.append(start_vertex)

    if len(result) == len(graph.graph):
        result.reverse()

    return result
```

#### How DFS Topological Sort Works

1. Use DFS to explore the graph
2. Add vertices to result list after exploring all neighbors
3. Reverse the final list to get topological order

Example:
```
DAG:             DFS Path:
A → B → D        A → B → D
↓   ↓           A → B → C
C → E

Topological Order: A, B, C, D, E
```

### Kahn's Algorithm

Uses in-degree calculation and queue-based approach.

```python
def kahn_topological_sort(graph):
    in_degree = {vertex: 0 for vertex in graph.graph}
    for vertex in graph.graph:
        for neighbor in graph.graph[vertex]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    queue = deque([vertex for vertex, degree in in_degree.items() if degree == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph.graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result
```

#### How Kahn's Algorithm Works

1. Calculate in-degree for all vertices
2. Start with vertices having 0 in-degree
3. Remove vertices and update in-degrees
4. Repeat until all vertices are processed

### Applications in Scheduling

1. **Build Systems**
   - Compiling source files in correct order
   - Resolving library dependencies

2. **Task Scheduling**
   - Project management
   - Course prerequisites

3. **Data Processing**
   - ETL workflows
   - Data pipeline dependencies

### Time and Space Complexity

1. **DFS-based Approach**
   - Time: O(V + E)
   - Space: O(V) for visited set and recursion stack

2. **Kahn's Algorithm**
   - Time: O(V + E)
   - Space: O(V) for queue and in-degree map

### When to Use Each

**Use DFS-based when:**
- Memory efficiency is crucial
- Recursive solution is acceptable
- Need to detect cycles

**Use Kahn's Algorithm when:**
- Need to track progress
- Prefer iterative approach
- Want simpler implementation

### Interview Practice Questions

1. **Implementation**
   Q: Modify the topological sort to detect if the graph has a cycle.

2. **Edge Cases**
   Q: How would you handle multiple valid topological orderings?

3. **Optimization**
   Q: Design an algorithm to find the lexicographically smallest topological order.

4. **Real-world Application**
   Q: How would you use topological sort to schedule tasks with dependencies and deadlines?

## Glossary

### Terms and Definitions

1. **Basic Graph Terms**
   - Vertex/Node: A point in a graph
   - Edge: A connection between vertices
   - Path: A sequence of vertices connected by edges
   - Cycle: A path that starts and ends at the same vertex

2. **Graph Types**
   - Directed Graph: Edges have direction
   - Undirected Graph: Edges have no direction
   - Weighted Graph: Edges have weights
   - DAG: Directed Acyclic Graph

3. **Graph Properties**
   - Connected: All vertices are reachable
   - Sparse: E << V²
   - Dense: E ≈ V²
   - Bipartite: Vertices can be split into two sets

4. **Algorithm Terms**
   - BFS: Breadth-First Search
   - DFS: Depth-First Search
   - MST: Minimum Spanning Tree
   - SPT: Shortest Path Tree

### Common Notations

1. **Variables**
   - V: Number of vertices
   - E: Number of edges
   - u, v: Vertices
   - w: Edge weight

2. **Complexity**
   - O(V): Linear in vertices
   - O(E): Linear in edges
   - O(V + E): Linear in graph size
   - O(V²): Quadratic in vertices

3. **Data Structures**
   - Adjacency List: Graph[v] = [neighbors]
   - Adjacency Matrix: Graph[u][v] = weight
   - Priority Queue: For greedy algorithms
   - Union-Find: For disjoint sets

4. **Special Values**
   - ∞ (float('inf')): Unreachable
   - NULL/None: No path/parent
   - -1: Invalid/not found