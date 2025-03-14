#only works for undirected graphs
def detect_cycle_undirected(graph):
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor in graph.graph.get(vertex, []):
            if neighbor == parent:
                continue
            if neighbor in visited or dfs(neighbor, vertex):
                return True
        return False

    for vertex in graph.graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True

    return False

def find_cycle_path_undirected(graph):
    visited = set()
    parent = {}

    def dfs(vertex, prev):
        visited.add(vertex)
        parent[vertex] = prev

        for neighbor in graph.graph.get(vertex, []):
            if neighbor == prev:
                continue

            if neighbor in visited:
                cycle = []
                current = vertex
                while current is not None and current != neighbor:
                    cycle.append(current)
                    current = parent.get(current)
                cycle.append(neighbor)
                cycle.append(vertex)
                cycle.reverse()
                return cycle

            path = dfs(neighbor, vertex)
            if path:
                return path

        return None

    for vertex in graph.graph:
        if vertex not in visited:
            cycle = dfs(vertex, None)
            if cycle:
                return cycle

    return None