class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, direction=None):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)

        if not self.directed and vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)

            del self.graph[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if not self.directed and vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if self.directed:
                    edges.append((vertex, neighbor))
                else:
                    if {vertex, neighbor} not in edges:
                        edges.append({vertex, neighbor})
        return edges
