# Kruskal's Algorithm without using Union-Find
def kruskals_mst(adj_list):
    edges = []
    for vertex in adj_list:
        for neighbor, weight in adj_list[vertex]:
            if (neighbor, vertex, weight) not in edges:
                edges.append((vertex, neighbor, weight))
    
    edges.sort(key=lambda x: x[2])
    
    parent = {vertex: vertex for vertex in adj_list}
    
    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]
    
    def union(vertex1, vertex2):
        parent[find(vertex2)] = find(vertex1)
    
    mst_edges = []
    total_weight = 0
    
    for vertex1, vertex2, weight in edges:
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            mst_edges.append((vertex1, vertex2, weight))
            total_weight += weight
    
    return mst_edges, total_weight

# Krushkal's Algorithm using Union-Find
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

def kruskals_mst_union_find(graph):
    if graph.directed:
        raise ValueError("Kruskal's algorithm works only for undirected graphs")
    
    if not graph.graph:
        return [], 0
    
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