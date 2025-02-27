class WeightedGraph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        for i, (v, w) in enumerate(self.graph[vertex1]):
            if v == vertex2:
                self.graph[vertex1][i] = (vertex2, weight)
                break
        else:
            self.graph[vertex1].append((vertex2, weight))

        if not self.directed:
            for i, (v, w) in enumerate(self.graph[vertex2]):
                if v == vertex1:
                    self.graph[vertex2][i] = (vertex1, weight)
                    break
            else:
                self.graph[vertex2].append((vertex1, weight))

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for v in self.graph:
                self.graph[v] = [(n, w) for n, w in self.graph[v] if n != vertex]
            del self.graph[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1] = [(v, w) for v, w in self.graph[vertex1] if v != vertex2]
            if not self.directed:
                self.graph[vertex2] = [(v, w) for v, w in self.graph[vertex2] if v != vertex1]

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex]:
                if self.directed:
                    edges.append((vertex, neighbor, weight))
                else:
                    edge = tuple(sorted([vertex, neighbor]) + [weight])
                    if edge not in edges:
                        edges.append(edge)
        return edges

    def get_weight(self, vertex1, vertex2):
        if vertex1 in self.graph:
            for neighbor, weight in self.graph[vertex1]:
                if neighbor == vertex2:
                    return weight
        return None

# the code below works for unweighted graphs
class UnweightedGraph:
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
